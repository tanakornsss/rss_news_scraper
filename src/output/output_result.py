import csv

from openpyxl.workbook import Workbook
from root_dir import BASE_DIR


def output_result_xlsx():
    wb = Workbook()
    ws = wb.active
    ws.title = "Analytics Report"

    ws['A1'] = "test"

    wb.save(f"{BASE_DIR}/report.xlsx")

def output_result_csv(result: list[dict]) -> bool:
    fieldnames = [
        "article_id",
        "title",
        "url",
        "content_hash",
        "pub_date",
        "scraped_date",
        "source"
    ]

    sorted_data = sorted(result, key=lambda row: row["article_id"])

    try:
        with open("results.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames)
            writer.writeheader()
            writer.writerows(sorted_data)

        return True
    except PermissionError:
        print("Permission denied")
        return False
    except OSError as e:
        print(f"OS Exception {e}")
        return False
