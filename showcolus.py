def showcolus(df):
    return pd.DataFrame(np.array(df.columns.tolist() +
             ['None{}'.format(i) for i in range(1, 11 - len(df.columns) % 10)]).reshape(-1,10),
             columns=range(1, 11))
