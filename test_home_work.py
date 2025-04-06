import csv
import io
from zipfile import ZipFile
from openpyxl import load_workbook
from conftest import CMD_DIR, ARCH_ZIP
from pypdf import PdfReader


def test_zip_created_and_read(create_folder):
    with ZipFile(ARCH_ZIP, "w") as testzip:
        testzip.write(CMD_DIR + "/test_zip.csv", "test_zip.csv")
        testzip.write(CMD_DIR + "/test_zip.xlsx", "test_zip.xlsx")
        testzip.write(CMD_DIR + "/test_zip.pdf", "test_zip.pdf")

    with ZipFile(ARCH_ZIP, "r") as zip_file:
        file_list = zip_file.namelist()
        print('-----')
        print("Содержимое архива:", file_list)

        with zip_file.open("test_zip.pdf") as pdf_file:
            pdf_read = PdfReader(pdf_file)
            pdf_text = pdf_read.pages[0].extract_text()
            assert pdf_text == "Тестовый PDF-документ  Здравствуйте! Это документ в формате PDF, который был создан для тестирования загрузки файлов. Никакой полезной информации он не несёт. "
            print('Успешно pdf')

        with zip_file.open("test_zip.xlsx") as xlsx_file:
            xlsx_read = load_workbook(xlsx_file)
            xlsx_text = xlsx_read.active
            third_row = [cell.value for cell in xlsx_text[3]]
            assert third_row[:3] == ['CN002', 'Сергеев', 'Константин']
            print('Успешно xlsx')

        with zip_file.open("test_zip.csv") as csv_file:
            with io.TextIOWrapper(csv_file) as text_file:
                csv_reader = csv.reader(text_file)
                first_row = next(csv_reader)
                csv_text = ' '.join(first_row).split()
                assert csv_text[:3] == ['Index', 'Customer', 'Id']
                print('Успешно csv')
