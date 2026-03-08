from datetime import datetime
import logging


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        logging.warning(f"Invalid date skipped: {date_str}")
        return None


def parse_quantity(qty_str):
    try:
        return int(qty_str)
    except ValueError:
        logging.warning(f"Invalid quantity format: {qty_str}")
        return None


def aggregate_sales(sales, inventory, month=4, year=2024):

    result = {}
    processed = 0

    quality = {
        "invalid_dates": 0,
        "negative_quantities": 0,
        "unknown_products": 0,
        "valid_transactions": 0
    }

    for row in sales:

        product_id = row.get("product_id")
        date_str = row.get("transaction_date")
        qty_str = row.get("quantity_sold")

        # Validate quantity
        qty = parse_quantity(qty_str)
        if qty is None:
            quality["negative_quantities"] += 1
            continue

        if qty < 0:
            logging.warning(f"Negative quantity ignored for product {product_id}")
            quality["negative_quantities"] += 1
            continue

        # Validate date
        date = parse_date(date_str)
        if date is None:
            quality["invalid_dates"] += 1
            continue

        # Filter month/year
        if date.month != month or date.year != year:
            continue

        # Check product exists
        if product_id not in inventory:
            logging.warning(f"Unknown product id: {product_id}")
            quality["unknown_products"] += 1
            continue

        # Valid transaction
        quality["valid_transactions"] += 1
        processed += 1

        result[product_id] = result.get(product_id, 0) + qty

    logging.info(f"Sales aggregation completed. Processed {processed} valid transactions.")

    return result, processed, quality