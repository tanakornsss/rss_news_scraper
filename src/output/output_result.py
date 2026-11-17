import csv

from openpyxl.workbook import Workbook
from root_dir import BASE_DIR


def output_result_xlsx():
    wb = Workbook()
    ws = wb.active
    ws.title = "Analytics Report"

    ws['A1'] = "test"

    wb.save(f"{BASE_DIR}/report.xlsx")

def output_result_csv(result: list[dict]):
    fieldnames = [
        "article_id",
        "title",
        "url",
        "content_hash",
        "pub_date",
        "scraped_date",
        "source"
    ]

    with open("results.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        writer.writerows(result)