from fastapi import APIRouter
from fastapi_cache.decorator import cache
import time

router = APIRouter(
    prefix='/operations',
    tags=['Operation']
)

@router.get('/')
async def get_operation():
    return

@router.get('/long_operation')
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return 'Много много данных, которые вычисляются сто лет'