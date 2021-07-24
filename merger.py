import PyPDF2
import sys

inputs = sys.argv[1:]

def merger(my_pdfs):
	merged = PyPDF2.PdfFileMerger()
	for pdf in my_pdfs:
	 print(pdf)
	 merged.append(pdf)
	merged.write("Merged.pdf")
	merged.close()
merger(inputs)