from crewai import Task
from agents import blog_researcher, content_writer
# from tools import yt_tool

# Task: Get summaries of the videos
research_task = Task(
    description="Identify the video {topic} and get detailed information from the channel",
    expected_output="A comprehensive 3 paragraph long report based on the information from the video",
    tools=[],
    agent=blog_researcher
)

# Writing task
writing_task = Task(
    description="Write a blog post on {topic}",
    expected_output="A 1000 word blog post on the topic {topic}",
    tools=[],
    agent=content_writer,
    async_execution=False,
    output="blog_post.txt"
)
