import baidubce.protocol
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials
from baidubce.services.tsdb.tsdb_client import TsdbClient
# when use https as the protocol, you may find certificate expire problem, this can be resovled by adding the following lines
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context 
 
HOST = 'yfhcaiji.tsdb-1tampz9bqczm.tsdb.iot.gz.baidubce.com'
AK = 'ALTAKaAOU2rlcLbNbiN3lEki4n'     # 用户的百度智能云 Access Key ID
SK = '98a43801870f4f4492c431db131b59eb'     # 用户的百度智能云 Secret Access Key
 
###########可选配置#############
#使用HTTP协议
protocol=baidubce.protocol.HTTP
#使用HTTPS协议
# protocol= baidubce.protocol.HTTPS
connection_timeout_in_mills=None  #连接超时时间
send_buf_size=None                #发送缓冲区大小
recv_buf_size=None                #接收缓冲区大小
retry_policy=None                 #重试策略
 
#生成config对象
config = BceClientConfiguration(
        credentials=BceCredentials(AK, SK),
        endpoint=HOST,
        protocol=protocol,
        connection_timeout_in_mills=connection_timeout_in_mills,
        send_buf_size=send_buf_size,
        recv_buf_size=recv_buf_size,
        retry_policy=retry_policy)
 
#创建TsdbCient
tsdb_client = TsdbClient(config)
# 获取metric列表
result = tsdb_client.get_metrics()
print( result.metrics)
''''
sql = "select * from wind"
result = tsdb_client.get_rows_with_sql(sql)
print (result)'''