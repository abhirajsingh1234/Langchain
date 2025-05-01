#duckduckgo search tool

from langchain_community.tools import DuckDuckGoSearchRun

searcher = DuckDuckGoSearchRun()

# print(searcher.invoke("who is bhishmahpitamah"))


#shell tool   (run command tool on command line)

from langchain_community.tools import ShellTool

shell = ShellTool()

# print(shell.invoke("whoami"))

