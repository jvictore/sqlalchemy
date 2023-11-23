# mssql/__init__.py
# Copyright (C) 2005-2023 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: https://www.opensource.org/licenses/mit-license.php
# mypy: ignore-errors

from . import aioodbc  # noqa
from . import base  # noqa
from . import pymssql  # noqa
from . import pyodbc  # noqa
from . import pypyodbc  # noqa
from .base import BIGINT
from .base import BINARY
from .base import BIT
from .base import CHAR
from .base import DATE
from .base import DATETIME
from .base import DATETIME2
from .base import DATETIMEOFFSET
from .base import DECIMAL
from .base import DOUBLE_PRECISION
from .base import FLOAT
from .base import IMAGE
from .base import INTEGER
from .base import JSON
from .base import MONEY
from .base import NCHAR
from .base import NTEXT
from .base import NUMERIC
from .base import NVARCHAR
from .base import REAL
from .base import ROWVERSION
from .base import SMALLDATETIME
from .base import SMALLINT
from .base import SMALLMONEY
from .base import SQL_VARIANT
from .base import TEXT
from .base import TIME
from .base import TIMESTAMP
from .base import TINYINT
from .base import UNIQUEIDENTIFIER
from .base import VARBINARY
from .base import VARCHAR
from .base import XML
from ...sql import try_cast


base.dialect = dialect = pypyodbc.dialect


__all__ = (
    "JSON",
    "INTEGER",
    "BIGINT",
    "SMALLINT",
    "TINYINT",
    "VARCHAR",
    "NVARCHAR",
    "CHAR",
    "NCHAR",
    "TEXT",
    "NTEXT",
    "DECIMAL",
    "NUMERIC",
    "FLOAT",
    "DATETIME",
    "DATETIME2",
    "DATETIMEOFFSET",
    "DATE",
    "DOUBLE_PRECISION",
    "TIME",
    "SMALLDATETIME",
    "BINARY",
    "VARBINARY",
    "BIT",
    "REAL",
    "IMAGE",
    "TIMESTAMP",
    "ROWVERSION",
    "MONEY",
    "SMALLMONEY",
    "UNIQUEIDENTIFIER",
    "SQL_VARIANT",
    "XML",
    "dialect",
    "try_cast",
)
