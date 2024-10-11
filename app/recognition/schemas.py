from pydantic import BaseModel

class Health(BaseModel):
    ram_usage: float  # RAM usage in GB
    cpu_usage: float  # CPU usage as a percentage
    total_memory: float  # Total memory in the system (GB)
    available_memory: float  # Available memory in the system (GB)
    thread_count: int  # Number of threads
    open_files: int  # Number of open files
    process_uptime: float  # Uptime of the process in seconds
