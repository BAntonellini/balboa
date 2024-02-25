from pathlib import Path

from sqlmesh.dbt.loader import sqlmesh_config

config = sqlmesh_config(Path(__file__).parent, default_target_environment='dev')
