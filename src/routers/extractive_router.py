from fastapi import APIRouter
from fastapi.responses import JSONResponse
from model.models import *
from model.extractive_summarizer import *
from utils.serializer import *
from utils.model import *

router = APIRouter(
    prefix="/extractive",
    tags=["Extractive Summary"]
)

@router.post("/")
async def extractive_all(text_:Text, sentences_count:int):
        summaryLex = ext_summary(text = text_.article, model = get_ext_LexRank(), sentences_count=sentences_count)
        resLex = await summaryLex.get_summary()
        summaryLsa = ext_summary(text = text_.article, model = get_ext_Lsa(), sentences_count=sentences_count)
        resLsa = await summaryLsa.get_summary()
        summaryLuhn = ext_summary(text = text_.article, model = get_ext_Luhn(), sentences_count=sentences_count)
        resLuhn = await summaryLuhn.get_summary()
        summaryKL = ext_summary(text = text_.article, model = get_ext_KL(), sentences_count=sentences_count)
        resKL = await summaryKL.get_summary()
        return JSONResponse(content = await get_all_ext_summary_response(resLex, resLsa, resLuhn, resKL))

@router.post("/LexRank")
async def extractive_LexRank(text_:Text, sentences_count:int):
        summary = ext_summary(text = text_.article, model = get_ext_LexRank(), sentences_count=sentences_count)
        res = await summary.get_summary()
        return JSONResponse(content = await get_single_summary_response(res))

@router.post("/LSA")
async def extractive_Lsa(text_:Text, sentences_count:int):
        summary = ext_summary(text = text_.article, model = get_ext_Lsa(), sentences_count=sentences_count)
        res = await summary.get_summary()
        return JSONResponse(content = await get_single_summary_response(res))

@router.post("/Luhn")
async def extractive_Luhn(text_:Text, sentences_count:int):
        summary = ext_summary(text = text_.article, model = get_ext_Luhn(), sentences_count=sentences_count)
        res = await summary.get_summary()
        return JSONResponse(content = await get_single_summary_response(res))

@router.post("/KL-Sum")
async def extractive_KL_Sum(text_:Text, sentences_count:int):
        summary = ext_summary(text = text_.article, model = get_ext_KL(), sentences_count=sentences_count)
        res = await summary.get_summary()
        return JSONResponse(content = await get_single_summary_response(res))