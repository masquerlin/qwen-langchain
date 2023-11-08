from langchain.llms import chatglm
from config.load_update_config import read_config, update_config
config = read_config()
model_path = config['path']['model_path']
local_url = config['url']['local_api_url']


llm = chatglm(endpoint_url = local_url,
              max_token = 80000,
              top_p = 0.9)
