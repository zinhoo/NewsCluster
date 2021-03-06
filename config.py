'''
@Descripttion: 配置文件
@version: 
@Author: 徐飞飞
@Date: 2019-12-18 07:33:01
@LastEditors  : 徐飞飞
@LastEditTime : 2019-12-31 11:05:46
'''

# 数据库
db_host='192.168.171.49'
db_user='root'
db_port=33306
db_passwd='123456'
db_db='news4primer'


# DataLoader相关参数
# 数据读取sql
dl_read_data_sql = "select news_id, content from newsapi where date_format(publishedAt, '%Y-%m-%d') between '2019-12-17' and '2019-12-18';"


# Text2Vector 相关参数
t2v_tokenizer_path = "./data/tokenizer_result.pkl"

t2v_doc2vec_min_count = 2
t2v_doc2vec_window = 3
t2v_doc2vec_size = 100
t2v_doc2vec_sample = 1e-3
t2v_doc2vec_negative = 5
t2v_doc2vec_workers = 4
t2v_doc2vec_epochs = 20


# Cluster 相关参数
cluster_vec_path = "./data/doc2vec_vectors.pkl"

cluster_dbscan_eps = 4
cluster_dbscan_min_samples = 1


# EventExtractor相关参数
ee_sql = "select label, newsid from cluster;"