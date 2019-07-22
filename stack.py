mapping1 = mapping.drop('isoform_id', axis=1).join(
    mapping['isoform_id'].str.split(',', expand=True).stack().reset_index(level=1, drop=True).rename('isoform_id')).reset_index(drop=True)
   
isoform_count = mapping1['gene_id'].value_counts().reset_index().rename(columns={'index': 'gene_id', 'gene_id': 'count'})

mapping = pd.concat([mapping, mapping['gene_id'].str.split('|', expand=True).rename(columns={0: 'gene_name', 1: 'entrz_id'})], axis=1)
