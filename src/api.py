# --*-- coding:utf-8 --*--
# Author: heliuhong2
# Time: 2022/8/18 下午7:42
# -*- coding: utf-8 -*-
"""Main API."""

from typing import Any, Dict
from fastapi import FastAPI
from src.endpoint import eventDetectRouter

def get_application() -> FastAPI:
    """Initialize fastapi app."""
    application = FastAPI(
        title="text_extract",
        description="do a simple entity extraction on the text body",
        version="1.0.0"
    )

    application.include_router(eventDetectRouter)

    return application


app = get_application()


@app.get("/", include_in_schema=False)
def read_root() -> Dict[str, Any]:
    """Test root path."""
    return {"message": "Hello World"}


import uvicorn
if __name__ == "__main__":
    uvicorn.run(app = "api:app",host = "0.0.0.0",
                port = 8000,debug=True,reload = True)
