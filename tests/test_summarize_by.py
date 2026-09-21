import pandas as pd
from order_report import summarize_by


def test_summarize_by_calculates_totals():
    data = pd.DataFrame({
        "order_id": ["O1", "O2", "O3"],
        "product_category": ["Books", "Books", "Electronics"],
        "discounted_value": [100, 200, 300],
        "returned": [False, True, False],
    })

    result = summarize_by(data, "product_category")

    books_row = result[result["product_category"] == "Books"].iloc[0]
    assert books_row["total_sales"] == 300
    assert books_row["return_rate"] == 0.5