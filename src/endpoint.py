# --*-- coding:utf-8 --*--
# Author: heliuhong2
# Time: 2022/8/18 下午8:00
from typing import Any, Dict
from fastapi import APIRouter, Body
from src.storage.mysql_storage import MySQLStorage
import jieba
import jieba.analyse

eventDetectRouter = APIRouter()
mysql_storage = MySQLStorage()


@eventDetectRouter.post("/text_extract", response_model=Dict)
async def text_extract(
    feature_inputs = Body(
        ...,
        title="Customer Define Feature Data Input",
        description="Feature Data",
        example= {"text":"今天深圳的天气真好呀"}
        ),
    ) ->Dict[str, Any]:
    """text extract"""
    text = feature_inputs.get("text","")
    kw = jieba.analyse.extract_tags(text, topK=10,
                                    withWeight=True,
                                    allowPOS=('n', 'ns'))
    result_list = []
    for item in kw:
        result_list.append(item[0])
    mysql_storage.extract_result_insert_to_db(result_list)

    return {"result":result_list}


