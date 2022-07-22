# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Муха села набв ваабвренье - вот и все стихотвабворенье'
new_text = ' '.join(list(filter(lambda x: 'абв' not in x, text.split())))
print(new_text)