import PyPDF2
import pyttsx3

# functions for adding a water mark
def AddingWaterMark():

    # opening up minutes file
    minutes_file = open("meetingminutes.pdf", 'rb')
    # using the reader to read the binary file
    minutes_reader = PyPDF2.PdfFileReader(minutes_file)
    # getting the first page of the file
    minutes_firstpage = minutes_reader.getPage(0)
    # opening up watermark file
    watermark_file = open("watermark.pdf", 'rb')
    # reading the watermark binary file
    pdf_watermark_reader = PyPDF2.PdfFileReader(watermark_file)
    # getting the first page of the watermark file
    watermark_firstpage = pdf_watermark_reader.getPage(0)
    # merging first page of minutes file and watermark file together
    minutes_firstpage.mergePage(watermark_firstpage)

    # creating a pdf writer object
    pdf_writer = PyPDF2.PdfFileWriter()
    # add the cover page to the writer object
    pdf_writer.addPage(minutes_firstpage)

    # adding the rest of the pages to the writer object
    for pagenum in range(1, minutes_reader.numPages):
        page_obj = minutes_reader.getPage(pagenum)
        pdf_writer.addPage(page_obj)

    result_pdf = open("watermarkedCover.pdf", 'wb')
    pdf_writer.write(result_pdf)

    # close all files to prevent memory loss
    minutes_file.close()
    watermark_file.close()
    result_pdf.close()


# create audio book function
def makeAudioBookFromPDF():
    # opening up the file
    book = open("meetingminutes.pdf", 'rb')
    # reading the binary
    pdf_reader = PyPDF2.PdfFileReader(book)
    # getting the number of pages
    pages = pdf_reader.numPages

    # initialize the speaker object
    play = pyttsx3.init()
    print("playing....")

    for num in range(0, pages):
        # getting current page
        page = pdf_reader.getPage(num)
        # getting the text
        text = page.extractText()
        # say the text out loud
        play.say(text)
        # wait until the entire page has been read
        play.runAndWait()

