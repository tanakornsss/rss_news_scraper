from openpyxl.workbook import Workbook
from root_dir import BASE_DIR


def output_result_xlsx():
    wb = Workbook()
    ws = wb.active
    ws.title = "Analytics Report"

    ws['A1'] = "test"

    wb.save(f"{BASE_DIR}/report.xlsx")

# Test
output_result_xlsx()