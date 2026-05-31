# Guia para Crear el Repositorio en GitHub Manualmente

Esta guia es para crear el repositorio remoto desde tu cuenta `OJ-Edelsonn` y luego conectarlo con la carpeta local del proyecto.

## 1. Crear el repositorio en GitHub

1. Entra a GitHub con tu cuenta `OJ-Edelsonn`.
2. Haz clic en el boton `+` de la parte superior derecha.
3. Selecciona `New repository`.
4. Completa estos campos:

```text
Owner: OJ-Edelsonn
Repository name: caso-consultoria-optimizacion-negocio
Description: Proyecto de consultoria y analitica de datos para optimizar ventas, inventario, costos y eficiencia operativa en una empresa industrial peruana.
Visibility: Public
```

5. No marques estas opciones:

```text
Add a README file
Add .gitignore
Choose a license
```

La razon es que el proyecto local ya tiene `README.md`, `.gitignore` y estructura inicial. Si GitHub crea archivos por su lado, luego tendriamos que resolver diferencias innecesarias.

6. Haz clic en `Create repository`.

## 2. Conectar el repositorio local

Despues de crear el repositorio, GitHub mostrara una URL parecida a esta:

```text
https://github.com/OJ-Edelsonn/caso-consultoria-optimizacion-negocio.git
```

Desde la carpeta local oficial:

```text
C:\Users\EDELSON ORIHUELA\OneDrive\Documentos\PROYECTOS CV\GPT\caso-consultoria-optimizacion-negocio
```

se conectara el remoto con:

```bash
git remote add origin https://github.com/OJ-Edelsonn/caso-consultoria-optimizacion-negocio.git
```

Luego se hara el primer commit y push.

## 3. Recomendacion para portafolio

Mantener el repositorio publico ayuda a que reclutadores y empresas puedan ver:

- Problema de negocio.
- Metodologia.
- Codigo y datos.
- Dashboard.
- Informe ejecutivo.
- Capacidad de documentar y explicar decisiones.

## 4. Nota importante sobre datos

El repositorio debe aclarar siempre que:

- Las fuentes publicas se usan como contexto y calibracion.
- Los datos operativos internos son simulados de forma realista.
- No se afirma tener acceso a informacion confidencial de UNACEM, Minsur ni Brainstorm.
