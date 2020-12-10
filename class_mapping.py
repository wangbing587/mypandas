# 构建标签
import pandas as pd

class_mapping = {label:idx for idx,label in enumerate(sorted(set(train_label)))}
df['classlabel'] = df['classlabel'].map(class_mapping)
# 反转
inv_class_mapping = {v: k for k, v in class_mapping.items()}
df['classlabel'] = df['classlabel'].map(inv_class_mapping)

from sklearn.preprocessing import LabelEncoder
class_le = LabelEncoder()
y = class_le.fit_transform(df['classlabel'].values)


# One-hot
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features=[0])
ohe.fit_transform(X).toarray()

pd.get_dummies(df[['price', 'color', 'size']])
