import pandas as pd 
import numpy as np
 
def calc_rsi(data,column, window=14):

    # Establish gains and losses for each day
    data['Variation'] = data[column].diff()
    data = data[1:]
    data['Gain'] = np.where(data['Variation'] > 0, data['Variation'], 0)
    data['Loss'] = np.where(data['Variation'] < 0, data['Variation'], 0)

    # Calculate simple averages so we can initialize the classic averages
    simple_avg_gain = data['Gain'].rolling(window).mean()
    simple_avg_loss = data['Loss'].abs().rolling(window).mean()
    classic_avg_gain = simple_avg_gain.copy()
    classic_avg_loss = simple_avg_loss.copy()

    for i in range(window, len(classic_avg_gain)):
        classic_avg_gain[i] = (classic_avg_gain[i - 1] * (window - 1) + data['Gain'].iloc[i]) / window
        classic_avg_loss[i] = (classic_avg_loss[i - 1] * (window - 1) + data['Loss'].abs().iloc[i]) / window
    
    # Calculate the RSI
    RS = classic_avg_gain / classic_avg_loss
    RSI = 100 - (100 / (1 + RS))

    return RSI