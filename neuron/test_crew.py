# from crewai import LLM, Agent, Crew, Task, Process
# from pydantic import BaseModel
# import litellm


# litellm._turn_on_debug()


# class RapSong(BaseModel):
#     lyrics: str
#     title: str
#     techniques_used: list[str]


# agent = Agent(
#     role="Rapper",
#     goal="Write technically superb and people liking rap songs",
#     backstory=(
#         "You are a rapper who is highly technical and uses complex skills like assonance. "
#         "You are primarily a hindi rapper who uses a lot of english words in your rap."
#     ),
#     tools=[],
#     verbose=True,
#     allow_delegation=False,
# )


# task = Task(
#     description="""
#         Write a Hindi rap song (you have the freedom to use english words as well) on the topic `{topic}`
#     """,
#     expected_output="""
#         Structured output representing the rap.
#     """,
#     agent=agent,
#     tools=[],
#     output_pydantic=RapSong,
#     output_file="task_out.md",
# )


# ollama_llm = LLM(model="ollama/gemma3:4b", base_url="http://localhost:11434", api_key="")


# crew = Crew(
#     agents=[agent],
#     tasks=[task],
#     verbose=True,
#     process=Process.sequential,
#     chat_llm=ollama_llm,
#     manager_llm=ollama_llm,
#     planning_llm=ollama_llm,
#     function_calling_llm=ollama_llm,
# )

# res = crew.kickoff(inputs={"topic": "life of techie in Bangalore who is applying for jobs but finding it super hard."})
# print(res.raw)
