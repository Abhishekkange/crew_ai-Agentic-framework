from crewai import Crew,Process
from agents import blog_researcher, content_writer
from tasks import research_task,writing_task


# Create a crew
crew = Crew(agents=[blog_researcher, content_writer], tasks=[research_task, writing_task],process=Process.sequential,memory=True,cache=True,max_rpm=100,share_crew=True)


result = crew.kickoff(inputs=('topic:"AI VS ML VS DL VS Data Science'))
print(result)