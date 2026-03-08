import plotly.graph_objects as go
from plotly.subplots import make_subplots


def generate_dashboard(results):

    # -------- Sales by Category --------
    category_sales = {}
    for row in results:
        cat = row["category"]
        category_sales[cat] = category_sales.get(cat, 0) + row["total_sales_value"]

    cat_names = list(category_sales.keys())
    cat_values = list(category_sales.values())

    # -------- Stock Status Distribution --------
    stock_status = {}
    for row in results:
        status = row["stock_status"]
        stock_status[status] = stock_status.get(status, 0) + 1

    status_names = list(stock_status.keys())
    status_values = list(stock_status.values())

    # -------- Top Selling Products --------
    top_products = sorted(
        results,
        key=lambda x: x["total_sales_value"],
        reverse=True
    )[:5]

    product_names = [p["product_name"] for p in top_products]
    product_values = [p["total_sales_value"] for p in top_products]

    # -------- Dashboard Layout --------
    fig = make_subplots(
        rows=3,
        cols=1,
        specs=[
            [{"type": "xy"}],
            [{"type": "domain"}],
            [{"type": "xy"}]
        ],
        subplot_titles=(
            "Sales by Category",
            "Stock Status Distribution",
            "Top Selling Products"
        ),
        row_heights=[0.33, 0.55, 0.37],
        vertical_spacing=0.12
    )

    # -------- Sales by Category --------
    fig.add_trace(
        go.Bar(
            x=cat_names,
            y=cat_values,
            marker_color="royalblue",
            text=cat_values,
            textposition="auto"
        ),
        row=1,
        col=1
    )

    # -------- Stock Status --------
    fig.add_trace(
        go.Pie(
            labels=status_names,
            values=status_values,
            hole=0.45,
            textinfo="label+percent",
            textfont=dict(size=18)
        ),
        row=2,
        col=1
    )

    # -------- Top Selling Products --------
    fig.add_trace(
        go.Bar(
            x=product_names,
            y=product_values,
            marker_color="seagreen",
            text=product_values,
            textposition="auto"
        ),
        row=3,
        col=1
    )

    # -------- Axis Labels --------
    fig.update_xaxes(title="Category", row=1, col=1)
    fig.update_yaxes(title="Sales Value", row=1, col=1)

    fig.update_xaxes(title="Product", row=3, col=1)
    fig.update_yaxes(title="Sales Value", row=3, col=1)

    # -------- Layout Styling --------
    fig.update_layout(
        title={
            "text": "Sales & Inventory Dashboard",
            "x": 0.5,
            "xanchor": "center",
            "font": {"size": 36}
        },

        template="plotly_white",

        height=2000,
        width=None,  # allows full width

        font=dict(size=16),

        margin=dict(
            l=40,
            r=40,
            t=80,
            b=40
        ),

        showlegend=False
    )

    # -------- Save Dashboard --------
    fig.write_html(
        "sales_dashboard.html",
        config={"responsive": True}
    )