from src.collector.database import Database
from src.output.output_result import output_result_csv

def export_result():

    db = Database()

    result = db.get_articles()
    output_result_csv(result)

    print("Output csv generated")
