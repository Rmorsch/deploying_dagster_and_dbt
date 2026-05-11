from dagster import Definitions, load_assets_from_modules

from dagster_and_dbt.defs.assets import dbt, metrics, requests, trips
from dagster_and_dbt.defs.resources import database_resource, dbt_resource
from dagster_and_dbt.defs.schedules import trip_update_schedule, weekly_update_schedule
from dagster_and_dbt.defs.jobs import trip_update_job, weekly_update_job, adhoc_request_job
from dagster_and_dbt.defs.sensors import adhoc_request_sensor

all_assets = load_assets_from_modules([dbt, metrics, requests, trips])

defs = Definitions(
    assets=all_assets,
    resources={
        "database": database_resource,
        "dbt": dbt_resource,
    },
    schedules=[trip_update_schedule, weekly_update_schedule],
    jobs=[trip_update_job, weekly_update_job, adhoc_request_job],
    sensors=[adhoc_request_sensor],
)
