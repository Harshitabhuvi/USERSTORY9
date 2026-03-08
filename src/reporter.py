import csv
import json

def generate_inventory_report(data):

    with open("inventory_reconciliation.csv", "w", newline="") as f:

        fields = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fields)

        writer.writeheader()
        writer.writerows(data)


def generate_category_summary(data):

    summary = {}

    for row in data:

        cat = row["category"]

        if cat not in summary:
            summary[cat] = 0

        summary[cat] += row["total_sales_value"]

    with open("category_summary.csv", "w", newline="") as f:

        writer = csv.writer(f)
        writer.writerow(["category", "total_sales_value"])

        for k, v in summary.items():
            writer.writerow([k, v])


def generate_quality_report(quality):

    with open("data_quality_report.json", "w") as f:
        json.dump(quality, f, indent=4)
def generate_sales_summary(results, processed):
    total_products = len(results)
    total_sales_value = sum(r["total_sales_value"] for r in results)

    low_stock = sum(1 for r in results if r["stock_status"] == "LOW_STOCK")
    out_stock = sum(1 for r in results if r["stock_status"] == "OUT_OF_STOCK")

    summary = {
        "total_products": total_products,
        "total_transactions_processed": processed,
        "total_sales_value": total_sales_value,
        "low_stock_products": low_stock,
        "out_of_stock_products": out_stock
    }