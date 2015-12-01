from scipy import stats
import pandas as pd
import collections

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

chi, p = stats.chisquare(freq.values())
print("chisquared: " + str(chi) + " with a probability of " + str(p))
