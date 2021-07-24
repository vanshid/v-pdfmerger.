import PyPDF2
with open("dummy.pdf","rb") as f:
#print(dir(PyPDF2))
 reading = PyPDF2.PdfFileReader(f)
 print(reading.numPages)
 print(reading.getPage(0))
 page = reading .getPage(0)
 print(page.rotateCounterClockwise(900))

writer = PyPDF2.PdfFileWriter()
writer.addPage(page)
with open("crooked.pdf","wb") as binaryfile:
    writer.write(binaryfile)

	