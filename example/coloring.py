from vnengine import story
story = story.Story()

story.set_initial_language('pt')

story.set_languages(['pt', 'en', 'es'])

story.set_resolution('hd')

story.add_starting_background('assets/menu.jpg')

story.add_scene('Formas Vazias', 'Olá, você quer começar a pintar?\n Qual figura pintar primeiro?', 'assets/01.jpg')

story.add_choice('Formas Vazias', 'Quadrado', '02')

story.add_choice('Formas Vazias', 'Triangulo', '03')

story.add_choice('Formas Vazias', 'Circulo', '04')

story.add_scene('02', 'O Quadrado está pintado, e agora?', 'assets/02.jpg')

story.add_choice('02', 'Triangulo', '06')

story.add_choice('02', 'Circulo', '05')

story.add_scene('03', 'O Triangulo está pintado, e agora?', 'assets/03.jpg')

story.add_choice('03', 'Quadrado', '06')

story.add_choice('03', 'Circulo', '07')

story.add_scene('04', 'O Circulo está pintado, e agora?', 'assets/04.jpg')

story.add_choice('04', 'Quadrado', '05')

story.add_choice('04', 'Triangulo', '07')

story.add_scene('05', 'O Quadrado e o Circulo estão pintados, e agora?', 'assets/05.jpg')

story.add_choice('05', 'Triangulo', '08')

story.add_scene('06', 'O Quadrado e o Triangulo estão pintados, e agora?', 'assets/06.jpg')

story.add_choice('06', 'Circulo', '08')

story.add_scene('07', 'O Circulo e o Triangulo estão pintados, e agora?', 'assets/07.jpg')

story.add_choice('07', 'Quadrado', '08')

story.add_scene('08', 'Fim?', 'assets/08.jpg')

story.run()