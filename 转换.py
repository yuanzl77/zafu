import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('result.csv')

# 假设 CSV 文件有一列名为 'IP 地址'
ip_addresses = df['IP 地址']

# 提取 IP 地址并格式化
formatted_ips = [f"{ip}:443#官方优选{i+1}" for i, ip in enumerate(ip_addresses)]

# 将结果写入 ip.txt
with open('ip.txt', 'w') as f:
    for ip in formatted_ips:
        f.write(ip + '\n')
