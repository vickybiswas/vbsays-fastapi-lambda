import sentry_sdk
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware
# from starlette.middleware.base import BaseHTTPMiddleware
from app.router.main import api_router
from app.core.config import settings
from app.error_handlers import exception_handlers, generic_exception_handler


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
# class DefaultHeaderMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request, call_next):
#         response = await call_next(request)
#         response.headers["X-Custom-Header"] = "Custom Value"
#         response.headers["ngrok-skip-browser-warning"] = True
#         return response
# app.add_middleware(DefaultHeaderMiddleware)  
# Register specific exception handlers
for exc_class, handler in exception_handlers.items():
    app.add_exception_handler(exc_class, handler)

# Register the generic exception handler
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(api_router, prefix=settings.API_V1_STR)

# End of File