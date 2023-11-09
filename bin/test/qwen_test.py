from transformers import AutoModelForCausalLM,AutoTokenizer
from transformers.generation import GenerationConfig
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),'../..'))
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from config.load_update_config import read_config, update_config
config = read_config()
model_path = config['path']['model_path']
print(model_path)

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_path,
                                             device_map='auto',trust_remote_code=True).eval()
response, history = model.chat(tokenizer,"你好",history=None)
print(response)

response, history = model.chat(tokenizer,input(),history=history)
print(response)
