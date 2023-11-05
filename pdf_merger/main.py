import PyPDF2

pdf_files =["Domicile Certificate.pdf","10th Marksheet.pdf","12th Marksheet.pdf","Graduation Marksheet.pdf","MS CIT Certificate.pdf","School Leaving Certificate.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdf_files:
    pdfFile = open(filename, mode='rb') 
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)

pdfFile.close()
merger.write("Merged_Documents.pdf")
