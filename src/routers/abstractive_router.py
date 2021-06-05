from fastapi import APIRouter
from fastapi.responses import JSONResponse
from model.models import *
from model.abstractive_summarizer import *
from utils.serializer import *
from utils.model import *

abs_bart = get_abs_bart_model()
abs_T5 = get_abs_T5_model()

router = APIRouter(
    prefix="/abstractive",
    tags=["Abstractive Summary"]
)

@router.post("/")
async def abstractive_all(text_:Text):
        summary_bart = abs_summary(text = text_.article, model = abs_bart)
        summary_t5 = abs_summary(text = text_.article, model = abs_T5)
        res_bart = await summary_bart.get_summary()
        res_t5 = await summary_t5.get_summary()
        return JSONResponse(content = await get_all_abs_summary_response(res_bart, res_t5))

@router.post("/bart")
async def abstractive_bart(text_:Text):
        summary = abs_summary(text = text_.article, model = abs_bart)
        res = await summary.get_summary()
        return JSONResponse(content = await get_single_summary_response(res))

@router.post("/T5")
async def abstractive_T5(text_:Text):
        summary = abs_summary(text = text_.article, model = abs_T5)
        res = await summary.get_summary()
        return JSONResponse(content = await get_single_summary_response(res))
