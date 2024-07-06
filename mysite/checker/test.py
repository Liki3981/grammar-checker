import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
def grammar(s):
    matches = tool.check(s)
    return matches
