from pathlib import Path

import pandas as pd


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

    variaveis_selecionadas = [
        "delivery_delay_days",
        "complaints_count",
        "customer_service_contacts",
        "resolution_time_days",
        "repeat_purchase_30d",
        "freight_value",
        "order_value",
    ]

    X = df[variaveis_selecionadas]

    return df, X
