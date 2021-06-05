import asyncio

async def get_single_summary_response(res):
    return {"summary": res}

async def get_all_abs_summary_response(res_bart, res_t5):
    res = {'Bart': res_bart, 'T5': res_t5}
    return {"summary": res}

async def get_all_ext_summary_response(resLex, resLsa, resLuhn, resKL):
    res = {'LexRank': resLex,
           'LSA': resLsa,
           'Luhn': resLuhn,
           'KL-SUM': resKL}
    return {'summary': res}