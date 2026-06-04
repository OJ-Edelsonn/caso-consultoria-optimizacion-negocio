# Diseño del Dashboard Power BI

## Objetivo del dashboard

En este dashboard voy a convertir el análisis de ventas, rentabilidad, inventario, cumplimiento de metas y simulación económica en una herramienta visual para la toma de decisiones.

El dashboard debe permitirme explicar el proyecto desde una perspectiva ejecutiva y operativa: qué está pasando en el negocio, dónde están las oportunidades y qué impacto económico podría generarse.

## Audiencia objetivo

El dashboard está pensado para tres perfiles:

| Perfil | Necesidad |
| --- | --- |
| Gerencia general | Ver crecimiento, rentabilidad, riesgos e impacto económico |
| Área comercial | Evaluar ventas, margen, productos rentables y cumplimiento de metas |
| Operaciones / logística | Controlar inventario, sobrestock, rotación y acciones de reposición |

## Fuentes que cargaré en Power BI

### Datos principales

| Archivo | Uso |
| --- | --- |
| `data/processed/fact_ventas.csv` | Ventas, margen, productos, canales, zonas y fechas |
| `data/processed/fact_inventario.csv` | Stock, sobrestock, estado de inventario y valorización |
| `data/processed/fact_metas.csv` | Metas comerciales y operativas |
| `data/processed/fact_produccion.csv` | Producción, capacidad y eficiencia operativa |
| `data/processed/dim_producto.csv` | Información de productos, categorías y estado de catálogo |
| `data/processed/dim_fecha.csv` | Calendario para análisis temporal |
| `data/processed/dim_canal.csv` | Canales comerciales |
| `data/processed/dim_zona.csv` | Zonas geográficas |
| `data/processed/dim_almacen.csv` | Almacenes |
| `data/processed/dim_planta.csv` | Plantas productivas |

### Resultados del análisis

| Archivo | Uso |
| --- | --- |
| `reports/hallazgos_exploratorios.csv` | Hallazgos ejecutivos |
| `reports/oportunidades_priorizadas.csv` | Productos priorizados por rentabilidad y sobrestock |
| `reports/escenarios_impacto_economico.csv` | Escenarios conservador, moderado y agresivo |
| `reports/impacto_producto_moderado.csv` | Impacto por producto en escenario moderado |
| `reports/impacto_accion_moderado.csv` | Impacto por tipo de acción sugerida |

## Modelo de datos propuesto

Voy a usar un modelo tipo estrella, donde las dimensiones explican a las tablas de hechos.

### Relaciones principales

| Tabla origen | Campo | Tabla destino | Campo | Tipo |
| --- | --- | --- | --- | --- |
| `dim_producto` | `producto_id` | `fact_ventas` | `producto_id` | 1 a muchos |
| `dim_producto` | `producto_id` | `fact_inventario` | `producto_id` | 1 a muchos |
| `dim_producto` | `producto_id` | `fact_metas` | `producto_id` | 1 a muchos |
| `dim_producto` | `producto_id` | `fact_produccion` | `producto_id` | 1 a muchos |
| `dim_fecha` | `fecha` | `fact_ventas` | `fecha` | 1 a muchos |
| `dim_canal` | `canal_id` | `fact_ventas` | `canal_id` | 1 a muchos |
| `dim_canal` | `canal_id` | `fact_metas` | `canal_id` | 1 a muchos |
| `dim_zona` | `zona_id` | `fact_ventas` | `zona_id` | 1 a muchos |
| `dim_almacen` | `almacen_id` | `fact_inventario` | `almacen_id` | 1 a muchos |
| `dim_planta` | `planta_id` | `fact_produccion` | `planta_id` | 1 a muchos |

## Medidas DAX principales

### Ventas y margen

```DAX
Ventas Netas = SUM(fact_ventas[ingreso_neto])

Costo Total = SUM(fact_ventas[costo_total])

Margen Bruto = SUM(fact_ventas[margen_bruto])

Margen Bruto % = DIVIDE([Margen Bruto], [Ventas Netas])

Cantidad Vendida = SUM(fact_ventas[cantidad])

Transacciones = DISTINCTCOUNT(fact_ventas[venta_id])

Stock Valorizado = SUM(fact_inventario[stock_valorizado])

Sobrestock Valorizado = SUM(fact_inventario[sobrestock_valorizado])

Sobrestock Unidades = SUM(fact_inventario[sobrestock_unidades])

Sobrestock % = DIVIDE([Sobrestock Valorizado], [Stock Valorizado])

Meta Ventas = SUM(fact_metas[meta_ventas])

Cumplimiento Ventas % = DIVIDE([Ventas Netas], [Meta Ventas])

Capital Liberado = SUM(escenarios_impacto_economico[capital_liberado])

Ahorro Operativo Anual = SUM(escenarios_impacto_economico[ahorro_operativo_anual])

Impacto Total Referencial = SUM(escenarios_impacto_economico[impacto_total_referencial])
