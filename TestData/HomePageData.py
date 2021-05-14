import openpyexcel


class HomePageData:
    test_home_page_data = [{"Name": "Gourav", "Email": "xyz@gmail.com", "Password": "pass1", "Gender": "Male"}] #,
                           # {"Name": "Tanu", "Email": "abc@gmail.com", "Password": "pass2", "Gender": "Female"}

    @staticmethod
    def getTestdata(test_case_name):
        dict1 = {}
        book = openpyexcel.load_workbook("D:\\Soni Data\\myfiles\\gacc\\New folder\\pyth\\vido\\pdfs\\datainexcel.xlsx")
        sheet = book.active

        for r in range(1, sheet.max_row + 1):
            if sheet.cell(row=r, column=1).value == test_case_name:
                for c in range(2, sheet.max_column + 1):
                    dict1[sheet.cell(row=1, column=c).value] = sheet.cell(row=r, column=c).value

        return [dict1]
