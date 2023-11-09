from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceBgeEmbeddings
from langchain.vectorstores import chroma
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from config.load_update_config import read_config, update_config
config = read_config()
text2vec_path = config['path']['text2vec_path']
print(text2vec_path)

def load_documents(directory = '../data/documents'):
    loader = DirectoryLoader(directory)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size = 512, chuck_overlap = 0)
    split_docs = text_splitter.split_documents(documents)
    return split_docs

def load_embedding_model():
    encode_kwargs = {"normalize_embedding":False}
    model_kwargs = {"devide": "cuda:0"}
    return HuggingFaceBgeEmbeddings(
        model_name = text2vec_path,
        model_kwargs = model_kwargs,
        encode_kwargs = encode_kwargs
    )

def store_chroma(docs, embeddings, persist_directory = "../data/vec"):
    db = chroma.from_documents(docs, embeddings, persist_directory = persist_directory)
    db.persist()
    return db


embeddings = load_embedding_model()

if not os.path.exists("../data/vec"):
    documents = load_documents()
    db = store_chroma(documents,embeddings)
else:
    chroma(persist_directory="../data/vec",embedding_function=embeddings)



