from agents.search_space_updater import search_space_updater
from tasks.update_search_space import update_search_space_task
from crews.refiner import search_axes_refiner
from axes import Axes
import litellm


# print(Axes.schema())


litellm._turn_on_debug()

search_axes_refiner.kickoff(
    inputs={
        "query": "Something cute for brunch",
        "search_space": Axes().model_dump_json(),
        "schema": Axes.model_json_schema(),
    }
)
