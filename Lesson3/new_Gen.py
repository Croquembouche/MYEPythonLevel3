# Python libraries
from fpdf import FPDF
from create_case_maps import plot_usa_case_map, plot_global_case_map

WIDTH = 210
HEIGHT = 297
TEST_DATE = "10/20/20"
def create_title(day, pdf):
    pdf.set_font('Arial', '', 24)
    pdf.ln(60)
    pdf.write(5, f"Covid Analytics Report")
    pdf.ln(10)
    pdf.set_font('Arial', '', 16)
    pdf.write(4, f'{day}')
    pdf.ln(5)
def create_report(filename="test.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.image("./resources/letterhead_cropped.png",0,0,WIDTH)
    create_title(TEST_DATE, pdf)
    plot_usa_case_map("usa_cases.png", day=TEST_DATE)
    pdf.image("usa_cases.png",5,90,WIDTH-20)
    pdf.add_page()
    pdf.output(filename, 'F')
    print("Finished")
create_report()