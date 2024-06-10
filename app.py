import os

#os.system("python download_model.py jujimeizuo/EmoLLM_Model")
os.system('streamlit run web_demo-aiwei.py --server.address=0.0.0.0 --server.port 8080')
