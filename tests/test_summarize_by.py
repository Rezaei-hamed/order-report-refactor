
import pytest 
import pandas as pd
from order_report import summarize_by, validate_columns


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



def test_summarize_by_work_with_region():
    data =pd.DataFrame({
        "order_id":["01", "02"],
        "region": ["North", "South"],
        "discounted_value": [100, 200],
        "returned": [False, False],
    })

    result =summarize_by(data, "region")

    assert len(result) ==2




def test_validate_columns_raises_when_missing():
    data =pd.DataFrame({
        "order_id":["01"],
        "region": ["North"],

    })
    required ={"order_id", "region", "discount"}

    with pytest.raises(ValueError):
        validate_columns(data,required)