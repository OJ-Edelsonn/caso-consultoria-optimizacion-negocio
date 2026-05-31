# Fuentes de Datos

Este documento registra las fuentes publicas identificadas para calibrar el caso. La regla del proyecto es separar claramente:

- Datos reales publicos: usados como contexto, benchmark o calibracion.
- Datos simulados: usados para analisis transaccional de ventas, inventario, compras y operaciones.

## Matriz inicial de fuentes

| Fuente | Enlace | Tipo de dato | Uso en el proyecto | Estado |
| --- | --- | --- | --- | --- |
| UNACEM Peru - Reporte de Sostenibilidad 2024 | https://unacem.pe/wp-content/uploads/2025/05/Reporte-UNACEM-Peru-2024-auditoria.pdf | Produccion, despachos, canales, capacidad, contexto operativo | Calibrar narrativa cementera e indicadores industriales | Identificada |
| Grupo UNACEM - Reporte Integrado 2024 | https://grupounacem.com/wp-content/uploads/2025/04/Reporte-Integrado-2024.pdf | Ingresos, costos, EBITDA, inversiones y resultados consolidados | Contexto financiero y magnitudes del negocio | Identificada |
| ASOCEM - Reportes estadisticos mensuales | https://www.asocem.org.pe/archivo/ | Produccion, despacho nacional, despacho total y exportaciones de cemento | Series sectoriales mensuales para mercado peruano | Identificada |
| BCRPData | https://estadisticas.bcrp.gob.pe/estadisticas/series/ | Series macroeconomicas y sectoriales | Contexto economico, construccion y demanda agregada | Identificada |
| MINEM - Produccion minera | https://www.gob.pe/institucion/minem/informes-publicaciones/5472883-produccion-minera | Produccion minera por periodo | Referencia para adaptar lenguaje e indicadores hacia mineria | Identificada |
| Minsur - Reportes y estados financieros | https://www.minsur.com/reportes-financieros/ | Reportes corporativos, produccion y resultados | Referencia industrial/minera para narrativa de eficiencia | Identificada |
| Brainstorming - Consultoria en Transformacion Digital | https://brainstorming.la/ | Enfoque de estrategia digital, embudo, metricas y crecimiento | Referencia para narrativa consultiva y digital | Identificada |
| Datos Abiertos Peru | https://www.datosabiertos.gob.pe/ | Posibles datasets publicos complementarios | Busqueda de variables externas si agregan valor | Por evaluar |

## Hallazgos iniciales

### UNACEM

La informacion publica disponible permite construir contexto de alto nivel sobre produccion, despachos, canales, plantas y resultados. Sin embargo, no publica datos internos transaccionales de ventas por cliente, inventario por SKU, costos unitarios por producto ni ordenes de compra detalladas.

Decision: usar UNACEM como referencia contextual, no como fuente transaccional.

### ASOCEM y BCRP

Estas fuentes pueden complementar el modelo con series mensuales del mercado cementero o variables macroeconomicas relacionadas con construccion. Son utiles para calibrar tendencias y estacionalidad.

Decision: revisar si descargaremos series mensuales para alimentar el analisis de tendencia del mercado.

### Minsur y MINEM

Minsur y MINEM sirven para reforzar la adaptabilidad industrial del proyecto. El caso no se convertira en un proyecto minero completo, pero usara indicadores compatibles con industria: produccion, costos, inventario, eficiencia y cumplimiento.

Decision: mantener Minsur como referencia narrativa y de lenguaje industrial.

### Brainstorm / Brainstorming

Brainstorm se abordara desde la narrativa consultiva y de transformacion digital: diagnostico, solucion digital, roadmap, metricas y valor para el negocio. No se espera usar datos internos de Brainstorm.

Decision: incluir Brainstorm como lectura de posicionamiento profesional, no como fuente de datos.

## Decision de datos para el proyecto

Se construira un dataset operativo simulado con realismo empresarial. Este dataset incluira:

- Productos cementeros y complementarios.
- Canales de venta.
- Clientes o segmentos.
- Zonas comerciales.
- Almacenes.
- Plantas.
- Ventas mensuales.
- Inventario mensual.
- Compras.
- Produccion.
- Costos.
- Metas.

Los parametros de volumen, tendencia y escala se calibraran con fuentes publicas. Los datos internos simulados se marcaran como simulados en el diccionario de datos.

## Criterios para aceptar una fuente

- Debe ser publica y verificable.
- Debe aportar contexto, calibracion o variables utiles.
- Debe poder citarse en el informe.
- No debe requerir acceso privado ni credenciales.
- No debe presentarse como dato interno si solo es referencia externa.

## Pendientes

- Descargar o registrar reportes publicos relevantes en `data/raw/` si el tamano y licencia lo permiten.
- Definir si las series de ASOCEM/BCRP se integraran como datos reales en el dashboard.
- Crear diccionario de datos para las tablas simuladas.
- Documentar supuestos de simulacion.
