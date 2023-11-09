from langchain.llms import chatglm
from langchain.chains import RetrievalQA
import sys,os
root_path = os.path.join(os.path.dirname(__file__),'..')
sys.path.append(root_path)
from config.load_update_config import read_config, update_config
from data_embedding import processing_data

#读取配置文件获取参数列表
config = read_config(os.path.join(root_path,'config/config.yaml'))
model_path = config['path']['model_path']
text2vec_model_path = config['path']['text2vec_path']
local_url = config['url']['local_api_url']
load_data_directory = os.path.join(os.path.dirname(__file__),'../data/documents')
save_data_directory = os.path.join(os.path.dirname(__file__),'../data/vec')

data_process = processing_data(text2vec_model_path,load_data_directory,save_data_directory)
db = data_process.running()

llm = chatglm(endpoint_url = local_url,
              max_token = 80000,
              top_p = 0.9)

retriever = db.as_retriever()
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever = retriever
)

def chat(question, history):
    response = qa.run(question)
    return response

history = []
while True:
    response = chat(input("question:"), history)
    print("answer:", response)
