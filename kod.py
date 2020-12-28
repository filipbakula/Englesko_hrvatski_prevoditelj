from googletrans import Translator
import docx2txt

trans = Translator()
#čitanje teksta
tekst=docx2txt.process("prevedi me.docx")
prevedeno = trans.translate(tekst, src="en", dest="hr")

#Moramo dodati encoding jer ako ga maknemo, poremeti se čitanje i program pukne kad treba upisati taj krivo pročitani znak.
novadatoteka = open("prevedime.txt", "w", encoding='utf-8')

novadatoteka.write(prevedeno.text)
novadatoteka.close()

print(f'Source: {prevedeno.src}')
print(f'Destination: {prevedeno.dest}')
