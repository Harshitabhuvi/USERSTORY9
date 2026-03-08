def reconcile_inventory(inventory, sales_summary):
    results = []

    for product_id, data in inventory.items():

        sold_qty = sales_summary.get(product_id, 0)

        final_stock = data["current_stock"] - sold_qty

        if final_stock < 0:
            final_stock = 0
            stock_status = "STOCK_ERROR"
        elif final_stock == 0:
            stock_status = "OUT_OF_STOCK"
        elif final_stock <= 10:
            stock_status = "LOW_STOCK"
        else:
            stock_status = "AVAILABLE"

        total_sales_value = sold_qty * data["unit_price"]

        results.append({
            "product_id": product_id,
            "product_name": data["product_name"],
            "category": data["category"],
            "current_stock": data["current_stock"],
            "total_sold_quantity": sold_qty,
            "final_stock": final_stock,
            "stock_status": stock_status,
            "total_sales_value": total_sales_value
        })

    return results