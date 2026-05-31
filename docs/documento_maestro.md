# Documento Maestro del Proyecto

## 1. Resumen ejecutivo

Este proyecto desarrolla un caso de consultoria para optimizar decisiones de negocio en una empresa industrial peruana, usando analitica de ventas, inventario, costos y desempeno operativo.

El caso principal se ubica en el sector cemento, inspirado en el contexto publico de UNACEM y el mercado peruano de materiales de construccion. A la vez, el enfoque se adapta a empresas industriales como Minsur o UNACEM porque trabaja problemas comunes: eficiencia operativa, control de inventario, costos, rotacion, cumplimiento de metas e indicadores de procesos.

La narrativa de consultoria y transformacion digital conecta con empresas como Brainstorm/Brainstorming: diagnostico del negocio, mapa del problema, propuesta de solucion digital, impacto esperado y roadmap de implementacion.

## 2. Perfil del proyecto

| Elemento | Definicion |
| --- | --- |
| Nombre | Caso de Consultoria - Optimizacion del Negocio |
| Autor | Edelson Anghuelo Orihuela Jara |
| Perfil | Estudiante de Ingenieria Empresarial y Sistemas, 7mo ciclo |
| Proposito | Proyecto de portafolio para postulaciones, practicas pre profesionales y entrevistas |
| Sector base | Industria cementera peruana |
| Empresas de referencia | UNACEM, Minsur, Brainstorm/Brainstorming |
| Entregable principal | Informe ejecutivo en PPT |
| Entregables complementarios | Dashboard Power BI, dataset, analisis Python/Excel, documentacion GitHub |

## 3. Problema de negocio

Una empresa industrial con alto volumen de operaciones puede vender mucho y aun asi perder eficiencia por tres causas principales:

- Productos con bajo margen o baja contribucion al resultado.
- Inventario excesivo, lento o mal distribuido entre almacenes.
- Compras y produccion no alineadas con la demanda real, generando sobrestock, quiebres o costos innecesarios.

El reto es convertir informacion operativa dispersa en decisiones concretas: que productos priorizar, que inventario reducir, como mejorar compras y que impacto economico podria lograrse.

## 4. Objetivo general

Convertir datos de ventas, inventario, costos y desempeno operativo en decisiones empresariales que mejoren rentabilidad, rotacion y eficiencia operativa.

## 5. Objetivos especificos

- Identificar productos rentables y no rentables.
- Detectar inventario ineficiente: sobrestock, baja rotacion y stock inmovilizado.
- Analizar tendencias de ventas por producto, canal, zona y periodo.
- Evaluar costos, margen bruto y contribucion por categoria.
- Medir cumplimiento de metas comerciales y operativas.
- Proponer acciones para reducir stock innecesario, mejorar compras y optimizar catalogo.
- Simular impacto economico estimado de las acciones propuestas.
- Presentar resultados en un dashboard y un informe ejecutivo defendible en entrevista.

## 6. Alcance funcional

### 6.1 Analisis

- Rentabilidad por producto, categoria y canal.
- Margen bruto y margen de contribucion.
- Rotacion de inventario.
- Dias de cobertura.
- Productos de baja venta o baja rentabilidad.
- Tendencia mensual de ventas y demanda.
- Cumplimiento de metas.
- Indicadores de procesos: produccion, despacho, compras y abastecimiento.

### 6.2 Propuestas

- Reducir stock innecesario.
- Mejorar politicas de compra y reposicion.
- Optimizar catalogo comercial.
- Priorizacion de productos segun rentabilidad y rotacion.
- Alertas de inventario critico o exceso.
- Tablero ejecutivo para seguimiento.

### 6.3 Simulacion economica

- Ahorro por reduccion de sobrestock.
- Liberacion de capital de trabajo.
- Mejora estimada de margen por optimizacion de mix.
- Reduccion de costos de almacenamiento.
- Impacto esperado sobre EBITDA o margen operativo, expresado como escenario estimado.

## 7. Narrativa unica del proyecto

El proyecto no se divide en dos versiones. Se construye como un solo caso profesional con dos lecturas complementarias:

| Enfoque | Como aparece en el proyecto |
| --- | --- |
| Consultoria y transformacion digital | Diagnostico, mapa del problema, solucion digital, roadmap, impacto esperado |
| Industria y operaciones | Inventario, costos, rotacion, eficiencia, metas, procesos, indicadores operativos |

Esto permite presentarlo ante empresas de consultoria, transformacion digital, cemento, mineria o industria sin rehacer el proyecto.

## 8. Empresa modelo del caso

Se trabajara con una empresa ficticia realista del sector cemento peruano:

**Cementos Andinos del Sur S.A.C.**

La empresa sera usada como caso de estudio para no atribuir datos internos a UNACEM, Minsur u otra compania. El contexto sectorial se calibrara con reportes publicos reales, especialmente de UNACEM y fuentes sectoriales. Los datos operativos internos seran simulados de forma documentada.

### 8.1 Justificacion del sector cemento

- Tiene operaciones industriales intensivas en costos, inventario y logistica.
- Permite analizar productos, canales, despachos, plantas y almacenes.
- Tiene informacion publica disponible sobre mercado, produccion, despachos y resultados empresariales.
- Se vincula directamente con UNACEM.
- Sus problemas de inventario y eficiencia son transferibles a mineria y manufactura.

### 8.2 Adaptabilidad hacia Minsur

Aunque el caso base sera cementero, los indicadores tambien aplican a una empresa minera:

- Control de inventario de insumos, repuestos o producto terminado.
- Costos por unidad producida.
- Cumplimiento de produccion vs meta.
- Rotacion de inventario.
- Eficiencia operativa.
- Simulacion de ahorro por optimizacion de compras y stock.

## 9. Estrategia de datos

### 9.1 Decision principal

Usaremos una estrategia mixta:

- **Datos publicos reales:** contexto sectorial, financiero y productivo.
- **Datos simulados realistas:** ventas, inventario, compras, produccion, costos y metas a nivel transaccional.

Esta decision es necesaria porque las empresas no publican bases internas completas con detalle de producto, cliente, almacen, costo unitario, stock diario y metas comerciales.

### 9.2 Fuentes publicas iniciales

| Fuente | Uso previsto |
| --- | --- |
| UNACEM Peru - Reporte 2024 | Contexto de produccion, despachos, canales comerciales, capacidad instalada y desempeno |
| Grupo UNACEM - Reporte Integrado 2024 | Contexto financiero consolidado: ingresos, costos, EBITDA e inversiones |
| ASOCEM - Reportes estadisticos mensuales | Mercado cementero peruano: produccion, despacho nacional y exportaciones |
| BCRPData | Series macroeconomicas y sectoriales para construccion/cemento |
| MINEM | Referencias industriales/mineras para adaptar lenguaje de eficiencia operativa |
| Minsur - Reportes publicos | Referencia para narrativa industrial/minera |

La matriz completa esta en [fuentes_datos.md](fuentes_datos.md).

### 9.3 Tablas propuestas

#### Tablas de contexto real

- `sector_cemento_mensual`
- `unacem_resumen_anual`
- `grupo_unacem_financiero_anual`
- `minem_referencia_industrial`
- `fuentes_referenciales`

#### Tablas simuladas operativas

- `dim_producto`
- `dim_categoria`
- `dim_cliente`
- `dim_canal`
- `dim_zona`
- `dim_planta`
- `dim_almacen`
- `fact_ventas`
- `fact_inventario`
- `fact_compras`
- `fact_produccion`
- `fact_metas`

### 9.4 Granularidad sugerida

| Tabla | Granularidad |
| --- | --- |
| Ventas | Producto, cliente, canal, zona, fecha |
| Inventario | Producto, almacen, fecha de corte |
| Compras | Producto/insumo, proveedor, fecha, orden |
| Produccion | Planta, producto, fecha mensual |
| Metas | Producto/categoria, canal, mes |

## 10. Requerimientos funcionales

| ID | Requerimiento |
| --- | --- |
| RF01 | Registrar y documentar fuentes publicas usadas como referencia. |
| RF02 | Generar o consolidar datasets operativos simulados con trazabilidad. |
| RF03 | Calcular KPIs de ventas, margen, costos, inventario y operaciones. |
| RF04 | Identificar productos rentables, no rentables y de baja contribucion. |
| RF05 | Detectar sobrestock, baja rotacion y productos inmovilizados. |
| RF06 | Analizar tendencias mensuales y cumplimiento de metas. |
| RF07 | Clasificar productos mediante analisis ABC/XYZ o matriz valor-rotacion. |
| RF08 | Simular escenarios de ahorro e impacto economico. |
| RF09 | Construir dashboard Power BI con vistas ejecutivas y operativas. |
| RF10 | Elaborar informe PPT con diagnostico, solucion, impacto y roadmap. |
| RF11 | Documentar el proyecto en GitHub de forma comprensible para reclutadores. |
| RF12 | Preparar una explicacion para entrevistas usando lenguaje de negocio y datos. |

## 11. Requerimientos no funcionales

| ID | Requerimiento |
| --- | --- |
| RNF01 | Reproducibilidad: los datasets procesados deben poder regenerarse desde scripts. |
| RNF02 | Transparencia: distinguir datos reales, simulados y supuestos. |
| RNF03 | Mantenibilidad: estructura ordenada por carpetas y codigo legible. |
| RNF04 | Escalabilidad: el modelo debe permitir agregar nuevas categorias, plantas o periodos. |
| RNF05 | Usabilidad: dashboard claro para perfiles ejecutivos y operativos. |
| RNF06 | Rendimiento: archivos optimizados para Power BI y analisis local. |
| RNF07 | Privacidad: no usar ni afirmar datos internos no publicos de empresas reales. |
| RNF08 | Trazabilidad: cada metrica debe tener definicion y formula. |
| RNF09 | Portabilidad: el proyecto debe poder entenderse desde GitHub sin depender del entorno local. |
| RNF10 | Calidad narrativa: el informe debe explicar problema, analisis, solucion e impacto esperado. |

## 12. Tecnologias

| Herramienta | Uso |
| --- | --- |
| Git y GitHub | Control de versiones y portafolio publico |
| Python | Limpieza, generacion de datos, analisis y simulacion |
| pandas / numpy | Manipulacion y calculo de datos |
| matplotlib / seaborn / plotly | Visualizacion exploratoria |
| Excel | Validacion, tablas y analisis complementario |
| Power BI | Dashboard ejecutivo y operativo |
| PowerPoint | Informe principal |
| Markdown | Documentacion tecnica y de negocio |

## 13. KPIs principales

### Comerciales y rentabilidad

- Ventas netas.
- Margen bruto.
- Margen de contribucion.
- Rentabilidad por producto.
- Mix de ventas por categoria.
- Cumplimiento de meta comercial.

### Inventario y compras

- Rotacion de inventario.
- Dias de inventario.
- Stock inmovilizado.
- Sobrestock estimado.
- Quiebres de stock.
- Nivel de cobertura.
- Costo de almacenamiento estimado.

### Operaciones

- Produccion mensual.
- Despacho mensual.
- Cumplimiento de produccion vs meta.
- Costo unitario.
- Eficiencia por planta.
- Cumplimiento de pedidos.

### Impacto economico

- Ahorro potencial.
- Capital liberado.
- Mejora estimada de margen.
- ROI de la solucion digital.
- Payback estimado.

## 14. Metodologia de analisis

1. Definir problema y alcance.
2. Levantar fuentes publicas y supuestos.
3. Disenar modelo de datos.
4. Crear dataset operativo simulado.
5. Realizar analisis exploratorio.
6. Calcular KPIs.
7. Clasificar productos y detectar oportunidades.
8. Simular escenarios de mejora.
9. Construir dashboard.
10. Elaborar informe ejecutivo.
11. Preparar explicacion para entrevistas.

## 15. Dashboard propuesto

| Pagina | Contenido |
| --- | --- |
| Resumen ejecutivo | Ventas, margen, inventario, ahorro potencial, alertas |
| Rentabilidad y catalogo | Productos rentables/no rentables, ABC, mix comercial |
| Inventario y compras | Sobrestock, rotacion, cobertura, compras sugeridas |
| Operaciones | Produccion, despachos, costos y cumplimiento |
| Simulacion | Escenarios de reduccion de stock, mejora de margen y ahorro |
| Roadmap | Iniciativas, prioridad, esfuerzo e impacto |

## 16. Informe PPT propuesto

1. Portada.
2. Contexto del negocio.
3. Problema identificado.
4. Mapa del problema.
5. Objetivo del analisis.
6. Fuentes de datos y supuestos.
7. Hallazgos de ventas y rentabilidad.
8. Hallazgos de inventario.
9. Hallazgos operativos.
10. Oportunidades priorizadas.
11. Propuesta de solucion digital.
12. Simulacion de impacto economico.
13. Roadmap de implementacion.
14. Riesgos y consideraciones.
15. Cierre ejecutivo.

## 17. Roadmap de desarrollo

| Fase | Resultado |
| --- | --- |
| Fase 0 - Definicion | Documento maestro, estructura de repo, fuentes iniciales |
| Fase 1 - Datos | Diseno del modelo, generacion/recoleccion de datos, diccionario |
| Fase 2 - Analisis | KPIs, EDA, rentabilidad, inventario, tendencias |
| Fase 3 - Simulacion | Escenarios de impacto economico y supuestos |
| Fase 4 - Dashboard | Power BI con paginas ejecutivas y operativas |
| Fase 5 - Informe | PPT final con narrativa consultiva e industrial |
| Fase 6 - GitHub | README final, capturas, instrucciones y version publica |
| Fase 7 - Entrevista | Guion de explicacion, preguntas probables y respuestas |

## 18. Flujo colaborativo

El proyecto se desarrollara por iteraciones. En cada fase se buscara que el autor pueda explicar:

- Que problema se resolvio.
- Que datos se usaron.
- Que decision se tomo.
- Que resultado se obtuvo.
- Como defenderia el analisis en entrevista.

La participacion humana no sera solo revisar resultados: tambien se definiran supuestos, se validaran KPIs y se practicara la explicacion.

## 19. Estrategia GitHub

El repositorio local ya esta inicializado. Aun no tiene remoto configurado.

Nombre sugerido para GitHub:

```text
caso-consultoria-optimizacion-negocio
```

Visibilidad recomendada:

```text
Publico
```

Razon: es un proyecto de portafolio. La documentacion debe dejar claro que los datos operativos son simulados y que las fuentes publicas se usan como referencia contextual.

## 20. Riesgos y mitigacion

| Riesgo | Mitigacion |
| --- | --- |
| No encontrar datos transaccionales reales | Usar dataset simulado realista y documentar supuestos |
| Confundir datos simulados con datos oficiales | Etiquetar claramente origen de cada tabla |
| Dashboard demasiado tecnico | Separar vistas ejecutivas y operativas |
| Informe poco defendible | Incluir problema, metodologia, hallazgos, impacto y roadmap |
| Proyecto muy amplio | Trabajar por fases y priorizar entregables |

## 21. Decision inicial

El proyecto se construira como un caso de consultoria industrial basado en una empresa cementera ficticia realista, calibrada con fuentes publicas del mercado peruano y reportes empresariales. Esta ruta es la mas defendible porque permite demostrar habilidades de negocio, datos, procesos, simulacion y transformacion digital sin depender de informacion privada.
