import csv
import logging
from typing import Dict, List


def load_inventory(file_path: str) -> Dict[str, dict]:
    inventory: Dict[str, dict] = {}

    with open(file_path, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:

            product_id = row.get("product_id")

            # Skip rows without product_id
            if not product_id:
                logging.warning("Missing product_id row skipped")
                continue

            try:
                inventory[product_id] = {
                    "product_name": row.get("product_name"),
                    "current_stock": int(row.get("current_stock", 0)),
                    "unit_price": float(row.get("unit_price", 0)),
                    "category": row.get("category"),
                }

            except ValueError:
                logging.warning(
                    f"Invalid numeric value for product {product_id}, row skipped"
                )
                continue

    return inventory


def load_sales(file_path: str) -> List[dict]:
    sales: List[dict] = []

    with open(file_path, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:

            # Skip rows without product_id
            if not row.get("product_id"):
                logging.warning("Sales row missing product_id skipped")
                continue

            sales.append(row)

    return sales