from crews.refiner import search_axis_refiner
import json
from neuron.intelligence.utils import extract_json_from_response
from axes import AXIS_REGISTRY, Axes
import asyncio
from collections.abc import Coroutine


async def _refined_axis(query, axis_name, axis_model):
    result = await search_axis_refiner.kickoff_async(
        inputs={
            "query": query,
            "axis_name": axis_name,
            "axis_model": json.dumps(axis_model.model_json_schema(), indent=2),
            "axis_model_schema": json.dumps(axis_model.model_json_schema(), indent=2),
        }
    )
    try:
        model_instance = axis_model(**extract_json_from_response(result.raw))
    except Exception:
        print(f"this was the result for the model {axis_model}\n#####################\n", result.raw)
        raise
    return model_instance


async def _refine_axes(query):
    result_coroutines = []

    for axis_name, axis_model in AXIS_REGISTRY:
        result_coro: Coroutine = _refined_axis(query, axis_name, axis_model)
        result_coroutines.append(result_coro)

    results = await asyncio.gather(*result_coroutines)
    axis_instances = dict(
        (axis_name, result) for (axis_name, axis_model), result in zip(AXIS_REGISTRY, results, strict=True)
    )
    updated_search_space = Axes(**axis_instances)
    print("Update search space ######################\n", updated_search_space)
    return updated_search_space
