# Реалізуйте програму, яка копіює вміст одного файлу в інший.

file = open("text.txt", 'r', encoding='utf-8')
to_file = open("text_new.txt", 'w', encoding='utf-8')
text = file.read()
to_file.write(text)

file.close()
to_file.close()
