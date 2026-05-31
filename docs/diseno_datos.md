# Diseno de Datos

## 1. Periodo de analisis

El caso analizara el periodo:

```text
Enero 2023 - Diciembre 2025
```

Este periodo permite comparar tres anos, detectar tendencias, observar estacionalidad y simular mejoras con suficiente contexto.

## 2. Estrategia general

El modelo de datos combinara:

- Datos publicos reales para contexto sectorial y financiero.
- Datos simulados realistas para la operacion interna.

Los datos simulados representaran una empresa cementera peruana ficticia llamada **Cementos Andinos del Sur S.A.C.**

## 3. Modelo analitico propuesto

El modelo seguira un esquema tipo estrella para facilitar su uso en Power BI.

### Tablas de dimensiones

| Tabla | Descripcion |
| --- | --- |
| `dim_fecha` | Calendario diario y mensual para analisis temporal |
| `dim_producto` | Catalogo de productos, categoria, unidad y estado comercial |
| `dim_cliente` | Clientes o segmentos comerciales |
| `dim_canal` | Canal de venta: distribuidores, constructoras, retail, directo |
| `dim_zona` | Zona geografica de venta y despacho |
| `dim_planta` | Plantas productivas |
| `dim_almacen` | Almacenes y centros de distribucion |
| `dim_proveedor` | Proveedores de insumos o materiales |

### Tablas de hechos

| Tabla | Descripcion |
| --- | --- |
| `fact_ventas` | Ventas por fecha, producto, cliente, canal y zona |
| `fact_inventario` | Stock mensual por producto y almacen |
| `fact_compras` | Compras por proveedor, producto o insumo |
| `fact_produccion` | Produccion mensual por planta y producto |
| `fact_metas` | Metas comerciales y operativas por periodo |

### Tablas de contexto

| Tabla | Descripcion |
| --- | --- |
| `sector_cemento_mensual` | Series sectoriales de produccion y despacho de cemento |
| `supuestos_simulacion` | Parametros usados para construir escenarios |
| `diccionario_kpis` | Definiciones de indicadores y formulas |

## 4. Campos propuestos

### `dim_producto`

| Campo | Tipo | Descripcion |
| --- | --- | --- |
| `producto_id` | Texto | Identificador unico |
| `producto` | Texto | Nombre comercial |
| `categoria` | Texto | Cemento, concreto, agregados, embolsado, granel |
| `unidad_medida` | Texto | Bolsa, tonelada, m3 |
| `precio_lista` | Decimal | Precio referencial |
| `costo_estandar` | Decimal | Costo unitario estimado |
| `estado_catalogo` | Texto | Activo, observar, descontinuar |

### `fact_ventas`

| Campo | Tipo | Descripcion |
| --- | --- | --- |
| `venta_id` | Texto | Identificador de transaccion |
| `fecha` | Fecha | Fecha de venta |
| `producto_id` | Texto | Producto vendido |
| `cliente_id` | Texto | Cliente o segmento |
| `canal_id` | Texto | Canal comercial |
| `zona_id` | Texto | Zona geografica |
| `cantidad` | Decimal | Cantidad vendida |
| `precio_unitario` | Decimal | Precio unitario real |
| `ingreso_bruto` | Decimal | Cantidad por precio unitario |
| `descuento` | Decimal | Descuento comercial |
| `ingreso_neto` | Decimal | Ingreso despues de descuento |
| `costo_total` | Decimal | Costo asociado a la venta |
| `margen_bruto` | Decimal | Ingreso neto menos costo total |

### `fact_inventario`

| Campo | Tipo | Descripcion |
| --- | --- | --- |
| `fecha_corte` | Fecha | Fecha de cierre mensual |
| `producto_id` | Texto | Producto inventariado |
| `almacen_id` | Texto | Almacen |
| `stock_unidades` | Decimal | Stock disponible |
| `stock_valorizado` | Decimal | Valor estimado del inventario |
| `stock_seguridad` | Decimal | Nivel minimo recomendado |
| `stock_maximo` | Decimal | Nivel maximo recomendado |

### `fact_compras`

| Campo | Tipo | Descripcion |
| --- | --- | --- |
| `compra_id` | Texto | Orden de compra |
| `fecha` | Fecha | Fecha de compra |
| `proveedor_id` | Texto | Proveedor |
| `producto_id` | Texto | Insumo o producto |
| `cantidad` | Decimal | Cantidad comprada |
| `costo_unitario` | Decimal | Costo unitario |
| `costo_total` | Decimal | Cantidad por costo unitario |
| `lead_time_dias` | Entero | Tiempo de entrega |

### `fact_produccion`

| Campo | Tipo | Descripcion |
| --- | --- | --- |
| `fecha_mes` | Fecha | Mes de produccion |
| `planta_id` | Texto | Planta |
| `producto_id` | Texto | Producto producido |
| `produccion_real` | Decimal | Produccion real |
| `capacidad_instalada` | Decimal | Capacidad estimada |
| `costo_produccion` | Decimal | Costo total de produccion |
| `merma` | Decimal | Perdida o merma estimada |

### `fact_metas`

| Campo | Tipo | Descripcion |
| --- | --- | --- |
| `fecha_mes` | Fecha | Mes de meta |
| `producto_id` | Texto | Producto |
| `canal_id` | Texto | Canal |
| `meta_ventas` | Decimal | Meta de ventas |
| `meta_margen` | Decimal | Meta de margen |
| `meta_produccion` | Decimal | Meta de produccion |

## 5. KPIs calculados

| KPI | Formula base | Uso |
| --- | --- | --- |
| Ventas netas | `sum(ingreso_neto)` | Medir desempeno comercial |
| Margen bruto | `sum(margen_bruto)` | Medir rentabilidad |
| % Margen bruto | `margen_bruto / ingreso_neto` | Comparar rentabilidad relativa |
| Rotacion de inventario | `costo_ventas / inventario_promedio` | Medir eficiencia de inventario |
| Dias de inventario | `365 / rotacion` | Medir cobertura |
| Sobrestock | `max(stock_unidades - stock_maximo, 0)` | Detectar exceso |
| Stock critico | `stock_unidades < stock_seguridad` | Detectar riesgo de quiebre |
| Cumplimiento ventas | `ventas / meta_ventas` | Medir meta comercial |
| Cumplimiento produccion | `produccion_real / meta_produccion` | Medir meta operativa |
| Ahorro potencial | `sobrestock_valorizado * tasa_reduccion_objetivo` | Simular impacto economico |

## 6. Reglas iniciales de simulacion

- La demanda tendra estacionalidad mensual, con mayor actividad en meses de mayor dinamica constructiva.
- Los productos principales tendran mayor volumen y menor variabilidad.
- Los productos de baja rotacion tendran menor venta, mayor cobertura y riesgo de inmovilizacion.
- Los canales distribuidores y constructoras concentraran mayor volumen.
- Algunas zonas tendran mayor demanda por crecimiento urbano o infraestructura.
- Los costos unitarios variaran por producto, categoria y presion de costos.
- El inventario no siempre estara alineado con la demanda, para permitir detectar oportunidades reales.

## 7. Decisiones pendientes

- Definir cantidad exacta de productos.
- Definir zonas comerciales del Peru.
- Definir cantidad de clientes o segmentos.
- Definir si los productos complementarios incluiran agregados y concreto.
- Definir nivel de detalle diario o mensual para ventas.

## 8. Recomendacion inicial

Para un proyecto de portafolio defendible, se recomienda:

- 25 a 40 productos.
- 4 canales comerciales.
- 6 a 8 zonas.
- 3 plantas.
- 5 almacenes.
- Ventas a nivel diario.
- Inventario, produccion y metas a nivel mensual.
