def showcols(df):
    cols = df.columns.tolist()
    cols = cols + (10 - len(cols) % 10) % 10 * ['None']
    cols = np.array(cols).reshape(-1, 10)
    return pd.DataFrame(data=cols, columns=range(1, 11))
