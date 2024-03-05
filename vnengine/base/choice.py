from typing import List

__all__: List[str] = []

class _Choice:
    """
    Represents the possible choice on a Scene

    Attributes:
        choice_text (str): The text explaining the choice.
    """

    def __init__(self, choice_text: str) -> None:
        """
        Initializes a new instance of the Choice class.

        Args:
            choice_text (str): The text explaining the choice.
        """
        self.choice_text: str = choice_text