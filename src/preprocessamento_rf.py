from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


def carregar_dados(caminho_arquivo):
    caminho_arquivo = Path(caminho_arquivo)
    df = pd.read_csv(caminho_arquivo)

    cat_cols = [
        "customer_id",
        "customer_region",
        "order_id",
    ]

    int_cols = [
        "customer_age",
        "customer_tenure_months",
        "items_quantity",
        "payment_installments",
        "delivery_time_days",
        "delivery_delay_days",
        "delivery_attempts",
        "customer_service_contacts",
        "resolution_time_days",
        "nps_score",
        "repeat_purchase_30d",
        "complaints_count",
    ]

    float_cols = [
        "order_value",
        "discount_value",
        "freight_value",
        "csat_internal_score",
    ]

    df[cat_cols] = df[cat_cols].astype("object")
    df[int_cols] = df[int_cols].astype("int64")
    df[float_cols] = df[float_cols].astype("float64")

    df["nps_classification"] = df["nps_score"].apply(
        lambda x: "Detractor" if x <= 6 else "Passive" if x <= 8 else "Promoter"
    )

    X = df.drop(
        columns=[
            "customer_id",
            "order_id",
            "nps_score",
            "nps_classification",
            "csat_internal_score",
        ]
    )

    variaveis_categoricas = ["customer_region"]

    preprocesso = ColumnTransformer(
        transformers=[
            ("categorico", OneHotEncoder(handle_unknown="ignore"), variaveis_categoricas)
        ],
        remainder="passthrough",
    )

    X_pre = preprocesso.fit_transform(X)

    return df, X_pre, preprocesso
