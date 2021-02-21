import PyPDF2
import pyttsx3

def AddingWaterMark():
    minutes_file = open("meetingminutes.pdf", 'rb')
    minutes_reader = PyPDF2.PdfFileReader(minutes_file)
    minutes_firstpage = minutes_reader.getPage(0)
    watermark_file = open("watermark.pdf", 'rb')
    pdf_watermark_reader = PyPDF2.PdfFileReader(watermark_file)
    watermark_firstpage = pdf_watermark_reader.getPage(0)
    minutes_firstpage.mergePage(watermark_firstpage)

    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_writer.addPage(minutes_firstpage)

    for pagenum in range(1, minutes_reader.numPages):
        page_obj = minutes_reader.getPage(pagenum)
        pdf_writer.addPage(page_obj)

    result_pdf = open("watermarkedCover.pdf", 'wb')
    pdf_writer.write(result_pdf)
    
    minutes_file.close()
    watermark_file.close()
    result_pdf.close()


def makeAudioBookFromPDF():
    book = open("meetingminutes.pdf", 'rb')
    pdf_reader = PyPDF2.PdfFileReader(book)
    pages = pdf_reader.numPages

    play = pyttsx3.init()
    print("playing....")
    for num in range(0, pages):
        page = pdf_reader.getPage(num)
        text = page.extractText()
        play.say(text)
        play.runAndWait()

