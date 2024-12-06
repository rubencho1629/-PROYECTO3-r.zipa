# Proyecto Flask con SQLAlchemy y Vercel

Este proyecto es una aplicación web construida con Flask y SQLAlchemy, desplegada en Vercel.

## Requisitos

- Python 3.8+
- pip

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2. Crea un entorno virtual y actívalo:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Crea un archivo `.env` en la raíz del proyecto y define las variables de entorno necesarias:
    ```env
    SECRET_KEY=Colombia123
    USER_DB=<tu_usuario_db>
    PASS_DB=<tu_contraseña_db>
    URL_DB=<url_de_tu_db>
    NAME_DB=<nombre_de_tu_db>
    ```

## Uso

1. Ejecuta la aplicación localmente:
    ```sh
    python app.py
    ```

2. La aplicación estará disponible en `http://127.0.0.1:5000`.

## Despliegue en Vercel

1. Asegúrate de tener el archivo `vercel.json` configurado correctamente.
2. Despliega la aplicación usando Vercel:
    ```sh
    vercel
    ```

## Configuración

La configuración de la aplicación se encuentra en `app/config.py`. Puedes modificar las configuraciones según tus necesidades.

## Pruebas

Para ejecutar las pruebas, usa el siguiente comando:
```sh
pytest├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   └── ...
├── app.py
├── requirements.txt
├── vercel.json
└── README.md