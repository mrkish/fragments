import PyPDF2
import csv
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

#
# Created to generate batches of Water Service Applications
# to the STL Water Division. Script will fill in the
# addresses and ZIP codes.
#
# Input dependencies: 
# 1) A .csv file with whatever information required entered.
#       NOTE: First column MUST be populated.
# 
# 2) A premade Water Service Application filled out with 
# relevant owner information (script assumes it will all be the
# the same owner).
#

def main():

    with open('propertyList.csv', newline='') as f:
        f.readline()
        reader = csv.reader(f)
        your_list = list(reader)

    for property in your_list:
        packet = newByteIO()
        c = canvas.Canvas(packet, pagesize=letter)
        c.drawString(75,539, property[0]) # Property Address
        c.drawString(438,539, property[1]) # Property ZIP
        c.drawString(284,183, property[2]) # Num of Units
        c.drawString(75,571, property[3]) # Property Owner
        c.drawString(75,409, property[4]) # Owner FEIN/SSN
        c.drawString(430,87, property[5]) # Current Date
        c.drawString(75,510, property[6]) # Owner Address
        c.drawString(75,481, property[7]) # Owner City
        c.drawString(260,481, property[8]) # Owner State
        c.drawString(438,481, property[9]) # Owner ZIP
        c.drawString(75,87, property[10]) # Owner Phone
        c.drawString(75,324, property[11]) # MGMT Name
        c.drawString(260,324, property[12]) # MGMT Address
        c.drawString(75,295, property[13]) # MGMT City
        c.drawString(260,295, property[14]) # MGMT State
        c.drawString(438,295, property[15]) # MGMT ZIP
        c.showPage()
        c.save()

        packet.seek(0)
        new_pdf = PyPDF2.PdfFileReader(packet)

        applicationPdf = PyPDF2.PdfFileReader(open('Water Service Application.pdf', 'rb'))
        pageToCopy = applicationPdf.getPage(0)
        pageToCopy.mergePage(new_pdf.getPage(0))

        outputStream = open(property[0] + ' Water Service Application.pdf', 'wb')

        output = PyPDF2.PdfFileWriter() 
        output.addPage(pageToCopy)
        output.write(outputStream)
        outputStream.close()

def newByteIO():
    return io.BytesIO()
    
if __name__ == "__main__":
    main()