import pandas as pd





def validate_columns(data, requaired_columns):
    missing_columns =requaired_columns.difference(data.columns)
    if missing_columns:
        missing_text =", ".join(sorted(missing_columns))
        raise ValueError(f"Saknade kolumner:{missing_text}")




    
def summarize_by(data, group_column):
    summary = data.groupby(group_column, as_index=False).agg(
        order_count=("order_id", "nunique"),
        total_sales=("discounted_value", "sum"),
        returns=("returned", "sum"),
    )
    summary["total_sales"] = summary["total_sales"].round(2)
    summary["return_rate"] = (summary["returns"] / summary["order_count"]).round(3)
    summary = summary.sort_values("total_sales", ascending=False).reset_index(drop=True)
    return summary





