from __future__ import annotations

import calendar
import csv
import random
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path


SEED = 20260530
START_DATE = date(2023, 1, 1)
END_DATE = date(2025, 12, 31)

random.seed(SEED)

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
OUT_DIR = BASE_DIR / "data" / "processed"

MONTH_NAMES = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
]

SEASONALITY = {
    1: 0.78,
    2: 0.86,
    3: 1.05,
    4: 1.09,
    5: 1.13,
    6: 1.06,
    7: 0.96,
    8: 1.01,
    9: 1.10,
    10: 1.16,
    11: 1.08,
    12: 0.90,
}

YEAR_FACTOR = {2023: 1.00, 2024: 1.06, 2025: 1.11}


def ensure_dirs() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def date_range(start: date, end: date):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


def month_range(start: date, end: date):
    current = date(start.year, start.month, 1)
    while current <= end:
        yield current
        if current.month == 12:
            current = date(current.year + 1, 1, 1)
        else:
            current = date(current.year, current.month + 1, 1)


def weighted_choice(items: list[dict], weight_key: str) -> dict:
    total = sum(float(item[weight_key]) for item in items)
    pick = random.uniform(0, total)
    current = 0.0
    for item in items:
        current += float(item[weight_key])
        if current >= pick:
            return item
    return items[-1]


def build_dimensions() -> dict[str, list[dict]]:
    dim_fecha = []
    for day in date_range(START_DATE, END_DATE):
        dim_fecha.append(
            {
                "fecha": day.isoformat(),
                "anio": day.year,
                "mes": day.month,
                "nombre_mes": MONTH_NAMES[day.month - 1],
                "trimestre": (day.month - 1) // 3 + 1,
                "dia": day.day,
                "dia_semana": day.weekday() + 1,
                "es_fin_semana": "Si" if day.weekday() >= 5 else "No",
                "fecha_mes": date(day.year, day.month, 1).isoformat(),
            }
        )

    product_specs = [
        ("Cemento Portland Tipo I 42.5kg", "Cemento embolsado", "Portland", "bolsa_42_5kg", 32.0, 22.4, "Activo", 1.35),
        ("Cemento Portland IP 42.5kg", "Cemento embolsado", "Puzolanico", "bolsa_42_5kg", 30.5, 21.0, "Activo", 1.50),
        ("Cemento Alta Resistencia 42.5kg", "Cemento embolsado", "Especial", "bolsa_42_5kg", 37.0, 25.7, "Activo", 1.05),
        ("Cemento Antisalitre 42.5kg", "Cemento embolsado", "Especial", "bolsa_42_5kg", 36.5, 25.4, "Activo", 0.88),
        ("Cemento Tipo V 42.5kg", "Cemento embolsado", "Especial", "bolsa_42_5kg", 38.0, 27.1, "Activo", 0.70),
        ("Cemento Albanileria 42.5kg", "Cemento embolsado", "Albanileria", "bolsa_42_5kg", 28.0, 19.5, "Activo", 0.92),
        ("Cemento Premium Acabados 42.5kg", "Cemento embolsado", "Acabados", "bolsa_42_5kg", 34.0, 24.8, "Observar", 0.50),
        ("Cemento Economico 42.5kg", "Cemento embolsado", "Economico", "bolsa_42_5kg", 26.5, 21.2, "Observar", 0.72),
        ("Cemento Portland Tipo I Granel", "Cemento granel", "Portland", "tonelada", 355.0, 247.0, "Activo", 1.24),
        ("Cemento Portland IP Granel", "Cemento granel", "Puzolanico", "tonelada", 338.0, 235.0, "Activo", 1.30),
        ("Cemento Alta Resistencia Granel", "Cemento granel", "Especial", "tonelada", 405.0, 285.0, "Activo", 0.76),
        ("Cemento Tipo V Granel", "Cemento granel", "Especial", "tonelada", 418.0, 304.0, "Observar", 0.48),
        ("Concreto f'c 175 kg/cm2", "Concreto premezclado", "Estandar", "m3", 245.0, 178.0, "Activo", 0.82),
        ("Concreto f'c 210 kg/cm2", "Concreto premezclado", "Estandar", "m3", 275.0, 199.0, "Activo", 1.15),
        ("Concreto f'c 280 kg/cm2", "Concreto premezclado", "Estructural", "m3", 318.0, 228.0, "Activo", 1.05),
        ("Concreto f'c 350 kg/cm2", "Concreto premezclado", "Estructural", "m3", 372.0, 272.0, "Activo", 0.72),
        ("Concreto bombeable", "Concreto premezclado", "Especial", "m3", 390.0, 286.0, "Activo", 0.60),
        ("Concreto autocompactante", "Concreto premezclado", "Especial", "m3", 455.0, 355.0, "Observar", 0.30),
        ("Arena gruesa lavada", "Agregados", "Arena", "tonelada", 48.0, 31.0, "Activo", 0.78),
        ("Arena fina zarandeada", "Agregados", "Arena", "tonelada", 43.0, 28.0, "Activo", 0.66),
        ("Piedra chancada 1/2", "Agregados", "Piedra", "tonelada", 62.0, 41.0, "Activo", 0.74),
        ("Piedra chancada 3/4", "Agregados", "Piedra", "tonelada", 59.0, 39.0, "Activo", 0.70),
        ("Hormigon seleccionado", "Agregados", "Hormigon", "tonelada", 51.0, 34.0, "Activo", 0.52),
        ("Base granular afirmada", "Agregados", "Base", "tonelada", 46.0, 33.0, "Observar", 0.38),
        ("Cal industrial hidratada", "Complementarios", "Cal", "bolsa_25kg", 24.0, 17.5, "Activo", 0.36),
        ("Mortero seco embolsado", "Complementarios", "Mortero", "bolsa_40kg", 29.0, 22.0, "Activo", 0.42),
        ("Aditivo plastificante", "Complementarios", "Aditivo", "galon", 42.0, 30.5, "Observar", 0.22),
        ("Aditivo impermeabilizante", "Complementarios", "Aditivo", "galon", 48.0, 36.0, "Observar", 0.18),
        ("Sellador para concreto", "Complementarios", "Acabados", "galon", 55.0, 43.0, "Descontinuar", 0.12),
        ("Curador quimico", "Complementarios", "Acabados", "galon", 52.0, 39.0, "Observar", 0.16),
        ("Microsilice industrial", "Complementarios", "Insumo", "bolsa_20kg", 96.0, 78.0, "Observar", 0.10),
        ("Cemento blanco decorativo", "Cemento embolsado", "Decorativo", "bolsa_25kg", 44.0, 36.0, "Descontinuar", 0.08),
    ]

    dim_producto = []
    for idx, spec in enumerate(product_specs, start=1):
        precio = spec[4]
        costo = spec[5]
        dim_producto.append(
            {
                "producto_id": f"PROD{idx:03d}",
                "producto": spec[0],
                "categoria": spec[1],
                "subcategoria": spec[2],
                "unidad_medida": spec[3],
                "precio_lista": round(precio, 2),
                "costo_estandar": round(costo, 2),
                "margen_objetivo_pct": round((precio - costo) / precio, 4),
                "estado_catalogo": spec[6],
                "peso_demanda": spec[7],
            }
        )

    dim_canal = [
        {"canal_id": "CAN01", "canal": "Distribuidores", "tipo_cliente": "B2B", "peso_demanda": 0.38, "descuento_base_pct": 0.055},
        {"canal_id": "CAN02", "canal": "Constructoras", "tipo_cliente": "B2B", "peso_demanda": 0.30, "descuento_base_pct": 0.040},
        {"canal_id": "CAN03", "canal": "Retail ferretero", "tipo_cliente": "B2B/B2C", "peso_demanda": 0.22, "descuento_base_pct": 0.025},
        {"canal_id": "CAN04", "canal": "Venta directa industrial", "tipo_cliente": "B2B", "peso_demanda": 0.10, "descuento_base_pct": 0.035},
    ]

    dim_zona = [
        {"zona_id": "ZON01", "zona": "Lima Metropolitana", "macroregion": "Centro", "peso_demanda": 1.45},
        {"zona_id": "ZON02", "zona": "Callao", "macroregion": "Centro", "peso_demanda": 0.72},
        {"zona_id": "ZON03", "zona": "Norte", "macroregion": "Norte", "peso_demanda": 0.95},
        {"zona_id": "ZON04", "zona": "Sur", "macroregion": "Sur", "peso_demanda": 0.88},
        {"zona_id": "ZON05", "zona": "Centro Andino", "macroregion": "Centro", "peso_demanda": 0.66},
        {"zona_id": "ZON06", "zona": "Ica", "macroregion": "Sur Chico", "peso_demanda": 0.58},
        {"zona_id": "ZON07", "zona": "Arequipa", "macroregion": "Sur", "peso_demanda": 0.80},
        {"zona_id": "ZON08", "zona": "Cusco y Oriente", "macroregion": "Oriente", "peso_demanda": 0.54},
    ]

    dim_planta = [
        {"planta_id": "PLA01", "planta": "Planta Lima Sur", "zona_id": "ZON01", "capacidad_mensual_ton": 135000},
        {"planta_id": "PLA02", "planta": "Planta Sierra Central", "zona_id": "ZON05", "capacidad_mensual_ton": 88000},
        {"planta_id": "PLA03", "planta": "Planta Costa Norte", "zona_id": "ZON03", "capacidad_mensual_ton": 76000},
    ]

    dim_almacen = [
        {"almacen_id": "ALM01", "almacen": "CD Lima", "zona_id": "ZON01", "capacidad_ton_equiv": 42000},
        {"almacen_id": "ALM02", "almacen": "CD Callao", "zona_id": "ZON02", "capacidad_ton_equiv": 25000},
        {"almacen_id": "ALM03", "almacen": "CD Norte", "zona_id": "ZON03", "capacidad_ton_equiv": 27000},
        {"almacen_id": "ALM04", "almacen": "CD Sur", "zona_id": "ZON04", "capacidad_ton_equiv": 24000},
        {"almacen_id": "ALM05", "almacen": "CD Centro", "zona_id": "ZON05", "capacidad_ton_equiv": 22000},
    ]

    dim_proveedor = [
        {"proveedor_id": f"PROV{idx:03d}", "proveedor": name, "categoria_abastecimiento": category, "pais": country}
        for idx, (name, category, country) in enumerate(
            [
                ("Canteras del Centro", "Clinker y caliza", "Peru"),
                ("Transportes Andinos", "Transporte", "Peru"),
                ("Energia Industrial Sur", "Energia", "Peru"),
                ("Suministros Mineros SAC", "Repuestos", "Peru"),
                ("Aditivos Tecnicos LATAM", "Aditivos", "Chile"),
                ("Envases Industriales Peru", "Bolsas y empaques", "Peru"),
                ("Servicios Portuarios Callao", "Logistica", "Peru"),
                ("Maquinarias y Fajas SAC", "Mantenimiento", "Peru"),
                ("Quimicos del Pacifico", "Insumos quimicos", "Peru"),
                ("Agregados del Sur", "Agregados", "Peru"),
                ("Control y Automatizacion SAC", "Tecnologia industrial", "Peru"),
                ("Importadora Cement Tech", "Repuestos importados", "Mexico"),
            ],
            start=1,
        )
    ]

    dim_cliente = []
    channel_segments = {
        "CAN01": ("Distribuidor regional", 30),
        "CAN02": ("Constructora", 22),
        "CAN03": ("Ferreteria", 20),
        "CAN04": ("Industrial", 8),
    }
    client_id = 1
    for channel_id, (segment, count) in channel_segments.items():
        for n in range(1, count + 1):
            zona = weighted_choice(dim_zona, "peso_demanda")
            dim_cliente.append(
                {
                    "cliente_id": f"CLI{client_id:03d}",
                    "cliente": f"{segment} {n:02d}",
                    "segmento": segment,
                    "canal_preferente_id": channel_id,
                    "zona_id": zona["zona_id"],
                    "tamano_cliente": random.choice(["Grande", "Mediano", "Mediano", "Pequeno"]),
                }
            )
            client_id += 1

    return {
        "dim_fecha": dim_fecha,
        "dim_producto": dim_producto,
        "dim_canal": dim_canal,
        "dim_zona": dim_zona,
        "dim_planta": dim_planta,
        "dim_almacen": dim_almacen,
        "dim_proveedor": dim_proveedor,
        "dim_cliente": dim_cliente,
    }


def relevant_products(products: list[dict], channel: dict) -> list[dict]:
    channel_name = channel["canal"]
    filtered = []
    for product in products:
        category = product["categoria"]
        if channel_name == "Retail ferretero" and category == "Cemento granel":
            continue
        if channel_name == "Retail ferretero" and category == "Concreto premezclado":
            continue
        if channel_name == "Venta directa industrial" and category == "Complementarios":
            continue
        filtered.append(product)
    return filtered


def quantity_for(product: dict, channel: dict, zone: dict, day: date) -> float:
    category = product["categoria"]
    channel_name = channel["canal"]
    zone_factor = float(zone["peso_demanda"])
    season = SEASONALITY[day.month] * YEAR_FACTOR[day.year]

    if category == "Cemento embolsado":
        if channel_name == "Retail ferretero":
            low, high = 25, 220
        elif channel_name == "Distribuidores":
            low, high = 180, 900
        else:
            low, high = 250, 1400
    elif category == "Cemento granel":
        low, high = 20, 260
    elif category == "Concreto premezclado":
        low, high = 8, 115
    elif category == "Agregados":
        low, high = 12, 180
    else:
        low, high = 4, 75

    base = random.uniform(low, high)
    demand_weight = float(product["peso_demanda"])
    quantity = base * season * (0.75 + 0.25 * zone_factor) * (0.85 + 0.20 * demand_weight)
    return round(max(quantity, 1.0), 2)


def build_sales(dimensions: dict[str, list[dict]]) -> tuple[list[dict], dict[tuple[str, str], float], dict[tuple[str, str], float]]:
    products = dimensions["dim_producto"]
    channels = dimensions["dim_canal"]
    zones = dimensions["dim_zona"]
    clients = dimensions["dim_cliente"]

    clients_by_channel = defaultdict(list)
    for client in clients:
        clients_by_channel[client["canal_preferente_id"]].append(client)

    sales = []
    sales_qty_month_product = defaultdict(float)
    sales_cost_month_product = defaultdict(float)
    sale_num = 1

    for day in date_range(START_DATE, END_DATE):
        season = SEASONALITY[day.month] * YEAR_FACTOR[day.year]
        weekday_factor = 0.58 if day.weekday() >= 5 else 1.0
        expected_tx = 46 * season * weekday_factor
        tx_count = max(8, int(random.gauss(expected_tx, 7)))

        for _ in range(tx_count):
            channel = weighted_choice(channels, "peso_demanda")
            zone = weighted_choice(zones, "peso_demanda")
            product = weighted_choice(relevant_products(products, channel), "peso_demanda")
            client_pool = clients_by_channel[channel["canal_id"]]
            client = random.choice(client_pool)

            quantity = quantity_for(product, channel, zone, day)
            list_price = float(product["precio_lista"])
            discount_pct = max(
                0.0,
                min(
                    0.14,
                    float(channel["descuento_base_pct"]) + random.uniform(-0.012, 0.022),
                ),
            )
            price_variation = random.uniform(0.985, 1.035)
            unit_price = round(list_price * price_variation, 2)
            gross_income = round(quantity * unit_price, 2)
            discount = round(gross_income * discount_pct, 2)
            net_income = round(gross_income - discount, 2)
            cost_factor = random.uniform(0.975, 1.065)
            total_cost = round(quantity * float(product["costo_estandar"]) * cost_factor, 2)
            gross_margin = round(net_income - total_cost, 2)

            sale = {
                "venta_id": f"V{sale_num:07d}",
                "fecha": day.isoformat(),
                "fecha_mes": date(day.year, day.month, 1).isoformat(),
                "producto_id": product["producto_id"],
                "cliente_id": client["cliente_id"],
                "canal_id": channel["canal_id"],
                "zona_id": zone["zona_id"],
                "cantidad": quantity,
                "precio_unitario": unit_price,
                "ingreso_bruto": gross_income,
                "descuento": discount,
                "ingreso_neto": net_income,
                "costo_total": total_cost,
                "margen_bruto": gross_margin,
            }
            sales.append(sale)
            month_key = (sale["fecha_mes"], product["producto_id"])
            sales_qty_month_product[month_key] += quantity
            sales_cost_month_product[month_key] += total_cost
            sale_num += 1

    return sales, sales_qty_month_product, sales_cost_month_product


def build_inventory(dimensions: dict[str, list[dict]], sales_qty: dict[tuple[str, str], float]) -> list[dict]:
    products = dimensions["dim_producto"]
    warehouses = dimensions["dim_almacen"]
    inventory = []

    for month in month_range(START_DATE, END_DATE):
        month_key = month.isoformat()
        _, last_day = calendar.monthrange(month.year, month.month)
        cutoff = date(month.year, month.month, last_day).isoformat()
        for product in products:
            monthly_qty = sales_qty.get((month_key, product["producto_id"]), 0.0)
            base_total_stock = monthly_qty * random.uniform(0.45, 1.35)

            if product["estado_catalogo"] == "Observar":
                base_total_stock *= random.uniform(1.25, 1.85)
            elif product["estado_catalogo"] == "Descontinuar":
                base_total_stock *= random.uniform(1.80, 2.75)
            elif random.random() < 0.18:
                base_total_stock *= random.uniform(1.35, 1.95)

            for warehouse in warehouses:
                share = random.uniform(0.12, 0.27)
                stock_units = round(max(base_total_stock * share, random.uniform(8, 45)), 2)
                stock_safety = round(max(monthly_qty * share * 0.28, 5), 2)
                stock_max = round(max(monthly_qty * share * 1.45, stock_safety * 2.0), 2)

                if random.random() < 0.035 and product["estado_catalogo"] == "Activo":
                    stock_units = round(stock_safety * random.uniform(0.45, 0.88), 2)

                overstock = round(max(stock_units - stock_max, 0), 2)
                stock_value = round(stock_units * float(product["costo_estandar"]), 2)
                inventory.append(
                    {
                        "fecha_corte": cutoff,
                        "fecha_mes": month_key,
                        "producto_id": product["producto_id"],
                        "almacen_id": warehouse["almacen_id"],
                        "stock_unidades": stock_units,
                        "stock_valorizado": stock_value,
                        "stock_seguridad": stock_safety,
                        "stock_maximo": stock_max,
                        "sobrestock_unidades": overstock,
                        "sobrestock_valorizado": round(overstock * float(product["costo_estandar"]), 2),
                        "estado_stock": "Critico" if stock_units < stock_safety else ("Sobrestock" if overstock > 0 else "Normal"),
                    }
                )

    return inventory


def build_purchases(dimensions: dict[str, list[dict]], sales_qty: dict[tuple[str, str], float]) -> list[dict]:
    products = dimensions["dim_producto"]
    providers = dimensions["dim_proveedor"]
    purchases = []
    purchase_num = 1

    for month in month_range(START_DATE, END_DATE):
        orders = random.randint(26, 42)
        for _ in range(orders):
            product = weighted_choice(products, "peso_demanda")
            provider = random.choice(providers)
            month_key = month.isoformat()
            qty_ref = sales_qty.get((month_key, product["producto_id"]), random.uniform(100, 700))
            quantity = round(max(qty_ref * random.uniform(0.08, 0.34), 5), 2)
            cost_unit = round(float(product["costo_estandar"]) * random.uniform(0.92, 1.08), 2)
            lead_time = random.randint(4, 28)
            if provider["pais"] != "Peru":
                lead_time += random.randint(18, 45)
            purchases.append(
                {
                    "compra_id": f"OC{purchase_num:06d}",
                    "fecha": date(month.year, month.month, random.randint(1, 24)).isoformat(),
                    "fecha_mes": month_key,
                    "proveedor_id": provider["proveedor_id"],
                    "producto_id": product["producto_id"],
                    "cantidad": quantity,
                    "costo_unitario": cost_unit,
                    "costo_total": round(quantity * cost_unit, 2),
                    "lead_time_dias": lead_time,
                }
            )
            purchase_num += 1

    return purchases


def build_production(dimensions: dict[str, list[dict]], sales_qty: dict[tuple[str, str], float]) -> list[dict]:
    products = [
        product
        for product in dimensions["dim_producto"]
        if product["categoria"] in {"Cemento embolsado", "Cemento granel", "Concreto premezclado", "Agregados"}
    ]
    plants = dimensions["dim_planta"]
    production = []

    for month in month_range(START_DATE, END_DATE):
        month_key = month.isoformat()
        for product in products:
            demand = sales_qty.get((month_key, product["producto_id"]), random.uniform(200, 1500))
            for plant in plants:
                plant_share = float(plant["capacidad_mensual_ton"]) / sum(float(p["capacidad_mensual_ton"]) for p in plants)
                produced = round(demand * plant_share * random.uniform(0.88, 1.18), 2)
                capacity = round(float(plant["capacidad_mensual_ton"]) * float(product["peso_demanda"]) * 0.018, 2)
                unit_cost = float(product["costo_estandar"]) * random.uniform(0.95, 1.08)
                merma = round(produced * random.uniform(0.004, 0.028), 2)
                production.append(
                    {
                        "fecha_mes": month_key,
                        "planta_id": plant["planta_id"],
                        "producto_id": product["producto_id"],
                        "produccion_real": produced,
                        "capacidad_instalada": capacity,
                        "utilizacion_capacidad_pct": round(min(produced / capacity, 1.35), 4) if capacity else 0,
                        "costo_produccion": round(produced * unit_cost, 2),
                        "merma": merma,
                    }
                )

    return production


def build_goals(dimensions: dict[str, list[dict]], sales_qty: dict[tuple[str, str], float]) -> list[dict]:
    products = dimensions["dim_producto"]
    channels = dimensions["dim_canal"]
    goals = []

    for month in month_range(START_DATE, END_DATE):
        month_key = month.isoformat()
        for product in products:
            total_qty = sales_qty.get((month_key, product["producto_id"]), 0.0)
            for channel in channels:
                channel_factor = float(channel["peso_demanda"]) * random.uniform(0.88, 1.14)
                target_qty = round(max(total_qty * channel_factor * random.uniform(0.92, 1.08), 1), 2)
                target_sales = round(target_qty * float(product["precio_lista"]) * (1 - float(channel["descuento_base_pct"])), 2)
                goals.append(
                    {
                        "fecha_mes": month_key,
                        "producto_id": product["producto_id"],
                        "canal_id": channel["canal_id"],
                        "meta_cantidad": target_qty,
                        "meta_ventas": target_sales,
                        "meta_margen": round(target_sales * float(product["margen_objetivo_pct"]), 2),
                        "meta_produccion": round(target_qty * random.uniform(0.95, 1.12), 2),
                    }
                )

    return goals


def build_sector_context() -> list[dict]:
    rows = []
    base_production = 870000
    base_dispatch = 835000
    for month in month_range(START_DATE, END_DATE):
        season = SEASONALITY[month.month] * YEAR_FACTOR[month.year]
        production = base_production * season * random.uniform(0.96, 1.04)
        dispatch = base_dispatch * season * random.uniform(0.95, 1.05)
        rows.append(
            {
                "fecha_mes": month.isoformat(),
                "produccion_cemento_ton_ref": round(production, 2),
                "despacho_nacional_ton_ref": round(dispatch, 2),
                "exportaciones_ton_ref": round(production * random.uniform(0.015, 0.045), 2),
                "indice_demanda_construccion_ref": round(100 * season * random.uniform(0.97, 1.03), 2),
                "origen": "Simulado calibrado con referencias publicas sectoriales",
            }
        )
    return rows


def build_metadata() -> tuple[list[dict], list[dict], list[dict]]:
    sources = [
        {
            "fuente": "UNACEM Peru - Reporte de Sostenibilidad 2024",
            "url": "https://unacem.pe/wp-content/uploads/2025/05/Reporte-UNACEM-Peru-2024-auditoria.pdf",
            "uso": "Contexto operativo y sector cementero",
        },
        {
            "fuente": "Grupo UNACEM - Reporte Integrado 2024",
            "url": "https://grupounacem.com/wp-content/uploads/2025/04/Reporte-Integrado-2024.pdf",
            "uso": "Contexto financiero y magnitudes empresariales",
        },
        {
            "fuente": "ASOCEM - Reportes estadisticos mensuales",
            "url": "https://www.asocem.org.pe/archivo/",
            "uso": "Referencia sectorial de produccion y despacho",
        },
        {
            "fuente": "BCRPData",
            "url": "https://estadisticas.bcrp.gob.pe/estadisticas/series/",
            "uso": "Contexto macroeconomico y sector construccion",
        },
        {
            "fuente": "MINEM - Produccion minera",
            "url": "https://www.gob.pe/institucion/minem/informes-publicaciones/5472883-produccion-minera",
            "uso": "Referencia para narrativa industrial y minera",
        },
    ]

    assumptions = [
        {"supuesto": "Periodo", "valor": "Enero 2023 a diciembre 2025"},
        {"supuesto": "Empresa", "valor": "Cementos Andinos del Sur S.A.C."},
        {"supuesto": "Naturaleza de datos operativos", "valor": "Simulados con reglas de negocio"},
        {"supuesto": "Estacionalidad", "valor": "Mayor demanda relativa entre marzo-junio y septiembre-noviembre"},
        {"supuesto": "Canales", "valor": "Distribuidores, constructoras, retail ferretero y venta directa industrial"},
        {"supuesto": "Inventario", "valor": "Incluye casos normales, criticos y sobrestock para analisis"},
        {"supuesto": "Costos", "valor": "Costos unitarios estimados por categoria y producto"},
        {"supuesto": "Moneda", "valor": "Soles peruanos PEN"},
        {"supuesto": "Semilla aleatoria", "valor": str(SEED)},
    ]

    kpis = [
        {"kpi": "Ventas netas", "formula": "sum(ingreso_neto)", "interpretacion": "Ingresos despues de descuentos"},
        {"kpi": "Margen bruto", "formula": "sum(margen_bruto)", "interpretacion": "Rentabilidad bruta generada"},
        {"kpi": "Margen bruto pct", "formula": "margen_bruto / ingreso_neto", "interpretacion": "Rentabilidad relativa"},
        {"kpi": "Sobrestock valorizado", "formula": "sum(sobrestock_valorizado)", "interpretacion": "Capital inmovilizado por exceso"},
        {"kpi": "Stock critico", "formula": "stock_unidades < stock_seguridad", "interpretacion": "Riesgo de quiebre de stock"},
        {"kpi": "Cumplimiento ventas", "formula": "ventas_reales / meta_ventas", "interpretacion": "Avance contra meta comercial"},
        {"kpi": "Utilizacion capacidad", "formula": "produccion_real / capacidad_instalada", "interpretacion": "Uso de capacidad productiva"},
        {"kpi": "Ahorro potencial", "formula": "sobrestock_valorizado * tasa_reduccion", "interpretacion": "Impacto economico estimado"},
    ]
    return sources, assumptions, kpis


def main() -> None:
    ensure_dirs()
    dimensions = build_dimensions()
    sales, sales_qty, _sales_cost = build_sales(dimensions)
    inventory = build_inventory(dimensions, sales_qty)
    purchases = build_purchases(dimensions, sales_qty)
    production = build_production(dimensions, sales_qty)
    goals = build_goals(dimensions, sales_qty)
    sector_context = build_sector_context()
    sources, assumptions, kpis = build_metadata()

    for table_name, rows in dimensions.items():
        write_csv(OUT_DIR / f"{table_name}.csv", rows)

    write_csv(OUT_DIR / "fact_ventas.csv", sales)
    write_csv(OUT_DIR / "fact_inventario.csv", inventory)
    write_csv(OUT_DIR / "fact_compras.csv", purchases)
    write_csv(OUT_DIR / "fact_produccion.csv", production)
    write_csv(OUT_DIR / "fact_metas.csv", goals)
    write_csv(OUT_DIR / "sector_cemento_mensual.csv", sector_context)
    write_csv(OUT_DIR / "supuestos_simulacion.csv", assumptions)
    write_csv(OUT_DIR / "diccionario_kpis.csv", kpis)
    write_csv(RAW_DIR / "fuentes_publicas_referenciales.csv", sources)

    print("Datos simulados generados correctamente.")
    print(f"Directorio de salida: {OUT_DIR}")
    print(f"Ventas: {len(sales):,} filas")
    print(f"Inventario: {len(inventory):,} filas")
    print(f"Compras: {len(purchases):,} filas")
    print(f"Produccion: {len(production):,} filas")
    print(f"Metas: {len(goals):,} filas")


if __name__ == "__main__":
    main()
