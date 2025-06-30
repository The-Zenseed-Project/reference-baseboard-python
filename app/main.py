from fastapi import FastAPI
from app.routes import meta, modules, i18n, accessibility
from app.core import logging as app_logging
from app.core.request_id_middleware import RequestIDMiddleware

app = FastAPI(title="Zenseed Baseboard")

# Register middleware
app.add_middleware(RequestIDMiddleware)

# Include routers
app.include_router(meta.router, prefix="/meta")
app.include_router(modules.router, prefix="/modules")
app.include_router(i18n.router, prefix="/i18n")
app.include_router(accessibility.router, prefix="/accessibility")

@app.get("/")
def root():
    return {"message": "Welcome to the Zenseed Baseboard"}
