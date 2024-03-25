import argparse
import re
import warnings
import os
import subprocess
import shutil
from typing import List

def modify_script(input: str, start_language: str, languages: str, resolution: str) -> str:
    """
    Used to modify the original script of the user. It creates a new script with the additional info passed as arguments.
    
    Args:
        input (str): The input file to be modified.
        start_language (str): The default language that the game starts.
        languages (str): The languages available to be chosen.
        resolution (str): The resolution of the game.
        
    Returns:
        str: The modified script with the additional info.
    """
    # Open the script file
    try:
        with open(input, 'r') as file:
            original_content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File {input} not found.")
    except IOError:
        raise IOError(f"Error reading file {input}.")
        
    # remove these commands to be replaced by the ones passed as arguments from the CLI
    modified_content = re.sub(r'.*?(set_initial_language|set_languages|set_resolution|run).*', '', original_content)

    # get the file name
    story_var_name = re.search(r'\b(\w+)\s*=\s*story\.Story\(\)', modified_content)
    
    if story_var_name:
        story_var_name = story_var_name.group(1)
    else:
        warnings.warn("Couldn't find assignment of story.Story()")
        
    # creates the additional code based on the CLI arguments
    additional_code = f"""
{story_var_name}.set_initial_language('{start_language}')
{story_var_name}.set_languages('{languages}')
{story_var_name}.set_resolution('{resolution}')
{story_var_name}.run()
    """    
    modified_content += additional_code
    
    # return the new script code
    return modified_content

def build(resolutions: List[str], languages: str, start_language: str, input: str, output: str) -> None:
    """
    Used to build the executable.
    
    Args:
        resolutions (List[str]): The resolutions of the project.
        languages (str): The languages available to be chosen.
        start_language (str): The default language that the game starts.
        input (str): The input file to be executed.
        output (str): The folder destination of the executable.
        
    Returns:
        None
    """
    for resolution in resolutions:
        # get extra info 
        file_name = os.path.splitext(os.path.basename(input))[0]
        temp_file_path = f"{output}/temp_{resolution}.py"
        output_folder = f"{output}/{file_name}_{resolution}"
        
        # Create script with additional infos
        final_script = modify_script(input, start_language, languages, resolution)   
        
        # Create temp file
        try:
            with open(temp_file_path, 'w') as file:
                file.write(final_script)
        except IOError:
            raise IOError(f"Error writing to file {temp_file_path}")
            
        # Build executable from temp file
        os.mkdir(output_folder)
        command = ["pyinstaller", "--onefile", "--distpath", output_folder,"--name", file_name, temp_file_path]
        try:
            subprocess.run(command, check=True)
            print("Executable created with success!")
        except subprocess.CalledProcessError as e:
            print("Error generating executable: ", e)
            
        # copy assets folder to destiny folder
        assets_folder = f"{os.path.dirname(input)}/assets"
        shutil.copytree(assets_folder, output_folder+"/assets")
        
        # remove temp file
        os.remove(temp_file_path)

def main() -> None:
    """
    The main entry point for the command line interface (CLI) of the VNEngine project.

    This function sets up the argument parser and handles the provided command line arguments.

    Subcommands:
        build: Build the project.

    Arguments:
        --resolutions: Resolutions of the Project. Possible values: hd, fullhd, 4k. This argument is required.
        --initial_lang: Default language that the game starts. This argument is required.
        --languages: Languages available to be chosen. Possible values: 'de' (German), 'en' (English), 'es' (Spanish), 'fr' (French), and 'pt' (Portuguese). This argument is required.
        --input: Name of the input file to be executed. This argument is required.
        --output: Folder destination of the executable. This argument is required.

    If no subcommand is provided, the function will print a message indicating that no action was given and suggest using -h to see the available actions.

    If the 'build' subcommand is provided, the function will call the build function with the provided arguments.

    If an unknown subcommand is provided, the function will print a message indicating that the action is unknown.
    """
    parser = argparse.ArgumentParser(description="Build the VNEngine project")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    build_parser = subparsers.add_parser("build", help="Build the project")
    build_parser.add_argument("--resolutions", help="Resolutions of the Project. Possible values: hd, fullhd, 4k", required=True)
    build_parser.add_argument("--initial_lang", help="Default language that the game starts", required=True) #todo
    build_parser.add_argument("--languages", help="Languages available to be chosen. Possible values: 'de' (German), 'en' (English), 'es' (Spanish), 'fr' (French), and 'pt' (Portuguese).", required=True) #todo
    build_parser.add_argument("--input", help="Name of the input file to be executed", required=True)
    build_parser.add_argument("--output", help="Folder destination of the executable", required=True)
    args = parser.parse_args()

    if args.subcommand is None:
        print("No action given. Use -h to see the available actions.")
    
    if args.subcommand == "build":
        build(str(args.resolutions).split(','), str(args.languages), str(args.initial_lang), str(args.input), str(args.output))
    else:
        print("Unknown action:", args.action)

if __name__ == "__main__":
    main()
        