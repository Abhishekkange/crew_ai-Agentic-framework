from crewai import Agent
# from tools import yt_tool
from langchain_google_genai import ChatGoogleGenerativeAI



#llm create 

llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro',verbose=True,temperature=0.5,google_api_key='AIzaSyAPuGZdoWkHw8N49NyN2tjp3lpRV_pI-2M')





#blog researcher Agent

blog_researcher =  Agent(role="blog researcher for youtube videos",
                         goal='get the relevant videos for the topic {topic}',
                         verbose=True,
                         Memory = True,
                         backstory=("This blog researcher is an expert in understanding concepts of  AI, Machine Learning  and Data science"),
                         tools=[],
                         llm=llm,
                         allow_delegation=True  
                         )

#content writer agent

content_writer  = Agent(
                        role='content writer ',
                        goal='write a blog post on {topic}',
                        verbose=True,
                        llm=llm,
                        Memory=True,
                        backstory=("This content writer is an expert in writing blogs on AI, Machine Learning and Data Science"),
                        tools=[],
                        allow_delegation=False
)