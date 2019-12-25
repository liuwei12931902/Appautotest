import xlrd


# ***************************
# 读取Excel 用法
# DoExcel = ReadExcel('testdata.xlsx','sheetName')
# DoExcel.read_excel(rowNum,colNum)
# ***************************

class ReadExcel(object):
    def __init__(self, filename, sheetName):
        self.workbook = xlrd.open_workbook(filename)
        self.sheetName = self.workbook.sheet_by_name(sheetName)

    def read_excel(self, rowNum, colNum):
        value = self.sheetName.cell(rowNum, colNum).value
        return value
