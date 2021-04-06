import pyttsx3
import PyPDF2

book= open('poem.pdf', 'rb')
pdfReader =PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
sound = speaker.getProperty('voices')
speaker.setProperty('voice', sound[1].id)
speaker.setProperty('rate', 123)
for num in range(33 , pages):
    page = pdfReader.getPage(num)
    Text = page.extractText()
    speaker.say(Text)
    speaker.runAndWait()
