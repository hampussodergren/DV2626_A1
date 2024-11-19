from ucimlrepo import fetch_ucirepo
import pandas as pd

# fetch dataset
wine_quality = fetch_ucirepo(id=186)

# data (as pandas dataframes)
X = wine_quality.data.features
y = wine_quality.data.targets

# metadata
#print(wine_quality.metadata)

# variable information
#print(wine_quality.variables)

data = pd.concat([X, y], axis = 1)

print(data.head())