from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Integer,
    Numeric,
    Sequence,
    SmallInteger,
    String,
    create_engine,
)
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import QueuePool

load_dotenv()

engine = create engine(
    os.getenv('DB_URL'),
    echo = True,
    poolclass = QueuePool,
    pool_size = 5
    max_overflow = 1,
    pool_recycle = 3600,
    pool_pre_ping = True,
    connect_args={
        "connect-timeout": 60 
        "keepalives": 1,
        "keepalives_idle": 30,
        "keepalives_interval": 10,
        "keepalives_count": 5,
    },
)

Session = sessionmaker(bind=engine)
