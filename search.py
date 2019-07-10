import numpy as np
import pandas as pd
data = pd.DataFrame(data=np.arange(12).reshape(4, 3), columns=list('abc'))

data[data['a'] == 9]
data[data['a'].isin([0, 9])]
