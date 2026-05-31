# Caso de Consultoria - Optimizacion del Negocio

Proyecto de portafolio orientado a demostrar pensamiento estrategico aplicado a negocio mediante analitica de datos, simulacion economica y propuesta de solucion digital.

El caso se plantea como una consultoria para una empresa industrial peruana del sector cemento, inspirada en problematicas reales de empresas como UNACEM y adaptable a entornos industriales como Minsur o UNACEM. La narrativa tambien conecta con perfiles de consultoria y transformacion digital como Brainstorm.

## Objetivo

Convertir datos de ventas, inventario, costos y desempeno operativo en decisiones empresariales accionables.

## Enfoque del proyecto

El proyecto combina dos capas:

- Fuentes publicas reales para contexto sectorial, financiero y operativo.
- Datos operativos simulados y realistas para ventas, inventario, compras, produccion, costos y metas, porque las empresas no publican informacion transaccional interna a nivel producto-almacen-cliente.

Esta decision permite construir un caso profesional sin inventar que los datos simulados son oficiales.

## Entregables esperados

- Dataset analitico documentado.
- Analisis en Python y/o Excel.
- Dashboard de referencia en Power BI.
- Informe ejecutivo en PPT.
- Version exportable a PDF.
- Documentacion para GitHub.
- Guion de explicacion para entrevistas.

## Estructura del repositorio

```text
data/
  raw/          # fuentes originales o insumos sin transformar
  processed/    # datasets listos para analisis y Power BI
notebooks/      # exploracion y analisis
src/            # scripts reutilizables
powerbi/        # archivo .pbix y recursos del dashboard
reports/
  ppt/          # informe principal
  pdf/          # version exportada
docs/           # documentacion del proyecto
assets/         # imagenes, capturas y recursos visuales
```

## Estado actual

Fase 0: definicion del proyecto, investigacion inicial de fuentes y estructura base del repositorio.

## Documentacion principal

- [Documento maestro](docs/documento_maestro.md)
- [Fuentes de datos](docs/fuentes_datos.md)
