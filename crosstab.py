df = pd.crosstab(data.gene1,data.gene2)
idx = df.columns.union(df.index)
df = df.reindex(index = idx,columns=idx,fill_value=0)
