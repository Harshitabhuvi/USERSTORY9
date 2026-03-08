import argparse
import time
import logging
from visualizer import plot_sales_by_category
from loader import load_inventory, load_sales
from config_loader import load_config
from sales_aggregator import aggregate_sales
from inventory_engine import reconcile_inventory
from dashboard import generate_dashboard
from reporter import (
    generate_inventory_report,
    generate_category_summary,
    generate_quality_report
)

# Load configuration
config = load_config()

# Configure logging using config
logging.basicConfig(
    filename=config["log_file"],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"
)


def main():
    """Main entry point for the Inventory Reconciliation Engine"""

    # Start execution timer
    start_time = time.time()

    # ---------------- CLI ARGUMENTS ----------------
    parser = argparse.ArgumentParser(
        description="Inventory Reconciliation & Sales Analysis Engine"
    )

    parser.add_argument(
        "--month",
        type=int,
        default=4,
        help="Month to process (default: 4)"
    )

    parser.add_argument(
        "--year",
        type=int,
        default=2024,
        help="Year to process (default: 2024)"
    )

    args = parser.parse_args()

    print("\nStarting Inventory Processing Engine")
    print("-------------------------------------")

    # ---------------- LOAD DATA ----------------
    inventory = load_inventory(config["inventory_file"])
    sales = load_sales(config["sales_file"])

    # ---------------- SALES AGGREGATION ----------------
    aggregated, processed, quality = aggregate_sales(
        sales,
        inventory,
        args.month,
        args.year
    )

    # ---------------- INVENTORY RECONCILIATION ----------------
    results = reconcile_inventory(inventory, aggregated)

    # ---------------- REPORT GENERATION ----------------
    generate_inventory_report(results)
    generate_category_summary(results)
    generate_quality_report(quality)

    print("\nProcessing completed successfully!")
    print(f"Processed Period: {args.month}/{args.year}")
    print("Valid Transactions Processed:", processed)
    plot_sales_by_category(results)
    generate_dashboard(results)
    # ---------------- PERFORMANCE METRICS ----------------
    total_rows = len(sales)

    invalid_rows = (
        quality["invalid_dates"]
        + quality["negative_quantities"]
        + quality["unknown_products"]
    )

    print("\nPerformance Metrics")
    print("-------------------")
    print("Total Rows Read:", total_rows)
    print("Valid Transactions:", processed)
    print("Invalid Rows:", invalid_rows)

    # End execution timer
    end_time = time.time()
    execution_time = round(end_time - start_time, 2)

    print("Execution Time:", execution_time, "seconds\n")


if __name__ == "__main__":
    main()