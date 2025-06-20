import pandas as pd
import os

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 定义输入和输出文件路径
# input_file = os.path.join(current_dir, 'train.tsv')
# output_file = os.path.join(current_dir, 'train_processed.tsv')
input_file = os.path.join(current_dir, 'dev.tsv')
output_file = os.path.join(current_dir, 'dev_processed.tsv')

# 读取TSV文件
df = pd.read_csv(input_file, sep='\t')

# 随机抽取1%的数据
sampled_df = df.sample(frac=0.01, random_state=42)

# 保存为新的TSV文件
sampled_df.to_csv(output_file, sep='\t', index=False)

print(f"已成功将TSV文件缩小至1%，输出文件为：{output_file}")