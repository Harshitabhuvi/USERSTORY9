import matplotlib.pyplot as plt


def plot_sales_by_category(results):

    category_sales = {}

    for row in results:
        cat = row["category"]
        value = row["total_sales_value"]

        category_sales[cat] = category_sales.get(cat, 0) + value

    categories = list(category_sales.keys())
    sales = list(category_sales.values())

    plt.figure()

    plt.bar(categories, sales)

    plt.title("Sales Value by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales Value")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.savefig("sales_by_category.png")