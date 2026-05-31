# Diccionario de Datos

Este diccionario describe las tablas que se generaran para el caso de consultoria. Las tablas operativas son simuladas y representan la operacion interna de **Cementos Andinos del Sur S.A.C.**

## Convencion de origen

| Tipo | Significado |
| --- | --- |
| Publico | Fuente externa verificable usada como contexto |
| Simulado | Dato generado para representar procesos internos |
| Derivado | Dato calculado desde tablas base |

## Tablas principales

| Tabla | Origen | Nivel de detalle | Uso |
| --- | --- | --- | --- |
| `dim_fecha` | Simulado | Dia | Analisis temporal |
| `dim_producto` | Simulado | Producto | Catalogo y rentabilidad |
| `dim_cliente` | Simulado | Cliente/segmento | Analisis comercial |
| `dim_canal` | Simulado | Canal | Comparacion por canal |
| `dim_zona` | Simulado | Zona | Analisis geografico |
| `dim_planta` | Simulado | Planta | Produccion y capacidad |
| `dim_almacen` | Simulado | Almacen | Inventario y cobertura |
| `dim_proveedor` | Simulado | Proveedor | Compras y abastecimiento |
| `fact_ventas` | Simulado | Transaccion diaria | Ventas, margen y tendencia |
| `fact_inventario` | Simulado | Producto-almacen-mes | Rotacion, cobertura y sobrestock |
| `fact_compras` | Simulado | Orden de compra | Compras, costos y lead time |
| `fact_produccion` | Simulado | Producto-planta-mes | Produccion, capacidad y merma |
| `fact_metas` | Simulado | Producto-canal-mes | Cumplimiento comercial y operativo |
| `sector_cemento_mensual` | Simulado calibrado | Mes | Contexto sectorial referencial |
| `supuestos_simulacion` | Derivado | Supuesto | Trazabilidad del escenario |
| `diccionario_kpis` | Derivado | KPI | Definicion de indicadores |

## KPIs clave

| KPI | Tabla base | Definicion |
| --- | --- | --- |
| Ventas netas | `fact_ventas` | Suma de ingresos despues de descuentos |
| Margen bruto | `fact_ventas` | Ingreso neto menos costo total |
| Porcentaje de margen | `fact_ventas` | Margen bruto dividido entre ingreso neto |
| Rotacion de inventario | `fact_ventas`, `fact_inventario` | Costo de ventas dividido entre inventario promedio |
| Dias de inventario | `fact_inventario` | 365 dividido entre rotacion anualizada |
| Sobrestock | `fact_inventario` | Stock por encima del maximo recomendado |
| Stock critico | `fact_inventario` | Stock por debajo del stock de seguridad |
| Cumplimiento de ventas | `fact_ventas`, `fact_metas` | Ventas reales divididas entre meta |
| Cumplimiento de produccion | `fact_produccion`, `fact_metas` | Produccion real dividida entre meta |
| Ahorro potencial | `fact_inventario` | Valor de sobrestock reducible por escenario |

## Uso en Power BI

El modelo recomendado es tipo estrella:

- Las dimensiones se conectan a las tablas de hechos por sus llaves.
- `dim_fecha` debe conectarse con ventas por `fecha` y con hechos mensuales usando una columna de mes.
- `fact_ventas` es la tabla central para rentabilidad.
- `fact_inventario` es la tabla central para eficiencia de stock.
- `fact_produccion` y `fact_compras` complementan el analisis industrial.
