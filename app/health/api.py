import psutil
from fastapi import APIRouter
from . import schemas
import time

router = APIRouter()

@router.get('')
def get_health() -> schemas.Health:
    process = psutil.Process()
    
    cpu_usage = process.cpu_percent(interval=1)

    memory_info = process.memory_info()
    ram_usage_gb = memory_info.rss / 1_000_000_000
    
    virtual_memory = psutil.virtual_memory()
    total_memory = virtual_memory.total / 1_000_000_000
    available_memory = virtual_memory.available / 1_000_000_000

    thread_count = process.num_threads()

    open_files = len(process.open_files())
    process_uptime = time.time() - process.create_time()

    return schemas.Health(
        ram_usage=ram_usage_gb,
        cpu_usage=cpu_usage,
        total_memory=total_memory,
        available_memory=available_memory,
        thread_count=thread_count,
        open_files=open_files,
        process_uptime=process_uptime
    )
