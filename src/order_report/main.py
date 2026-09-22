import logging
from pathlib import Path

import pandas as pd

from .config import ReportConfig
from .transform import summarize_by, validate_columns

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(name)s | %(message)s",
)

config = ReportConfig(
    input_path=Path("data/orders.csv"),
    output_dir=Path("output"),
)

config.output_dir.mkdir(parents=True, exist_ok=True)

def main():
    logger.info("Startar orderrapport")
    try:
        data = pd.read_csv(config.input_path)

        required = {
            "order_id", "order_date", "customer_id", "region",
            "product_category", "quantity", "unit_price", "discount", "returned",
        }

        validate_columns(data, required)

        logger.info("Läser in %d rader", len(data))

        data["region"] = data["region"].fillna("Unknown").astype(str).str.strip().str.title()
        data["product_category"] = (
            data["product_category"]
            .fillna("Unknown")
            .astype(str)
            .str.strip()
            .str.title()
        )

        data["quantity"] = pd.to_numeric(data["quantity"], errors="coerce")
        invalid_count = data["quantity"].isna().sum()
        if invalid_count > 0:
            logger.warning("Hittade %d ogiltiga värden i quantity, ersätter med 1", invalid_count)
        data["quantity"] = data["quantity"].fillna(1)

        data["unit_price"] = pd.to_numeric(data["unit_price"], errors="coerce")
        invalid_count = data["unit_price"].isna().sum()
        if invalid_count > 0:
            logger.warning("Hittade %d ogiltiga värden i unit_price, ersätter med median", invalid_count)
        data["unit_price"] = data["unit_price"].fillna(data["unit_price"].median())

        data["discount"] = pd.to_numeric(data["discount"], errors="coerce").fillna(0)

        data["returned"] = (
            data["returned"]
            .fillna("false")
            .astype(str)
            .str.strip()
            .str.lower()
            .isin(["true", "yes", "1", "ja"])
        )

        data["order_value"] = data["quantity"] * data["unit_price"]
        data["discounted_value"] = data["order_value"] * (1 - data["discount"])

        total_sales = round(data["discounted_value"].sum(), 2)
        number_of_orders = data["order_id"].nunique()
        number_of_returns = int(data["returned"].sum())

        overview = pd.DataFrame(
            {
                "metric": ["total_sales", "order_count", "return_count"],
                "value": [total_sales, number_of_orders, number_of_returns],
            }
        )
        overview.to_csv(config.output_dir / "overview.csv", index=False)
        logger.info("Sparade %s", "overview.csv")

        result1 = summarize_by(data, "product_category")
        result1.to_csv(config.output_dir / "sales_by_category.csv", index=False)
        logger.info("Sparade %s", "sales_by_category.csv")

        result2 = summarize_by(data, "region")
        result2.to_csv(config.output_dir / "sales_by_region.csv", index=False)
        logger.info("Sparade %s", "sales_by_region.csv")

        returns_by_category = summarize_by(data, "product_category")
        returns_by_category = returns_by_category[
            ["product_category", "order_count", "returns", "return_rate"]
        ]
        returns_by_category = returns_by_category.sort_values(
            "return_rate", ascending=False
        ).reset_index(drop=True)
        returns_by_category.to_csv(config.output_dir / "returns_by_category.csv", index=False)
        logger.info("Sparade %s", "returns_by_category.csv")

    except Exception as error:
        logger.error("Något gick fel: %s", error)


if __name__ == "__main__":
    main()