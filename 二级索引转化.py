smears = df.groupby(['Raw file', 'Modified sequence'])['Retention time'].apply(np.ptp)
smear_pair_inds = smears.index.to_frame()['Raw file'].values
