import os

from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.utilities.zapier import ZapierNLAWrapper

slack_channel_name = "#slack_channel_name"

# get from https://platform.openai.com/
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "sk-...")

# get from https://nla.zapier.com/demo/provider/debug (under User Information, after logging in):
os.environ["ZAPIER_NLA_API_KEY"] = os.environ.get("ZAPIER_NLA_API_KEY", "sk-...")

llm = OpenAI(temperature=0)
zapier = ZapierNLAWrapper(zapier_nla_api_key=os.environ["ZAPIER_NLA_API_KEY"])
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
agent = initialize_agent(toolkit.get_tools(), llm, agent="zero-shot-react-description", verbose=True)

# agent.run("Summarize the last email I received regarding Silicon Valley Bank. Send the summary to the #test-zapier channel in slack.")
# agent.run(f"Summarize the last email in my gmail regarding 'Zapier API'. Send the summary to the {slack_channel_name} channel in slack.")
# agent.run(f"xxxxxに関して、私のgmailに最後に届いたメールを100字程度に要約する、そしてslackの{slack_channel_name}チャンネルに要約を送信する。")
