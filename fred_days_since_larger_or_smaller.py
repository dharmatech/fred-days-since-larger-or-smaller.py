import numpy as np
import pandas as pd
import fred_pandas
# ----------------------------------------------------------------------
def calc_days_since(df):

    df['value'] = pd.to_numeric(df['value'])

    df['date'] = pd.to_datetime(df['date'])

    df['value_diff'] = df['value'].diff()

    df['days_since'] = np.nan

    df['days_since'] = df['days_since'].astype('Int64')

    for i in range(1, len(df)):

        if df['value_diff'].iloc[i] < 0:

            lower_values = df[df['value'] < df['value'].iloc[i]]

            previous_lower_values = lower_values[lower_values['date'] < df['date'].iloc[i]]

            if not previous_lower_values.empty:
                df['days_since'].iloc[i] = (df['date'].iloc[i] - previous_lower_values['date'].iloc[-1]).days

        elif df['value_diff'].iloc[i] > 0:
                
            higher_values = df[df['value'] > df['value'].iloc[i]]

            previous_higher_values = higher_values[higher_values['date'] < df['date'].iloc[i]]

            if not previous_higher_values.empty:
                df['days_since'].iloc[i] = (df['date'].iloc[i] - previous_higher_values['date'].iloc[-1]).days

        else:

            same_values = df[df['value'] == df['value'].iloc[i]]

            previous_same_values = same_values[same_values['date'] < df['date'].iloc[i]]

            if not previous_same_values.empty:
                df['days_since'].iloc[i] = (df['date'].iloc[i] - previous_same_values['date'].iloc[-1]).days
# ----------------------------------------------------------------------

def calc_days_since_alt(df):

    df['value'] = pd.to_numeric(df['value'])

    df['date'] = pd.to_datetime(df['date'])

    df['value_diff'] = df['value'].diff()

    df['days_since'] = np.nan

    df['days_since'] = df['days_since'].astype('Int64')


    df['value_diff_days_since'] = np.nan

    df['value_diff_days_since'] = df['value_diff_days_since'].astype('Int64')

    # ----------------------------------------------------------------------
    for i in range(1, len(df)):

        if df['value_diff'].iloc[i] < 0:

            lower_values = df[df['value'] < df['value'].iloc[i]]

            previous_lower_values = lower_values[lower_values['date'] < df['date'].iloc[i]]

            if not previous_lower_values.empty:
                df['days_since'].iloc[i] = (df['date'].iloc[i] - previous_lower_values['date'].iloc[-1]).days

        elif df['value_diff'].iloc[i] > 0:
                
            higher_values = df[df['value'] > df['value'].iloc[i]]

            previous_higher_values = higher_values[higher_values['date'] < df['date'].iloc[i]]

            if not previous_higher_values.empty:
                df['days_since'].iloc[i] = (df['date'].iloc[i] - previous_higher_values['date'].iloc[-1]).days

        else:

            same_values = df[df['value'] == df['value'].iloc[i]]

            previous_same_values = same_values[same_values['date'] < df['date'].iloc[i]]

            if not previous_same_values.empty:
                df['days_since'].iloc[i] = (df['date'].iloc[i] - previous_same_values['date'].iloc[-1]).days
    # ----------------------------------------------------------------------
    for i in range(1, len(df)):

        if df['value_diff'].iloc[i] < 0:

            lower_values = df[df['value_diff'] < df['value_diff'].iloc[i]]

            previous_lower_values = lower_values[lower_values['date'] < df['date'].iloc[i]]

            if not previous_lower_values.empty:
                df['value_diff_days_since'].iloc[i] = (df['date'].iloc[i] - previous_lower_values['date'].iloc[-1]).days

        elif df['value_diff'].iloc[i] > 0:
                
            higher_values = df[df['value_diff'] > df['value_diff'].iloc[i]]

            previous_higher_values = higher_values[higher_values['date'] < df['date'].iloc[i]]

            if not previous_higher_values.empty:
                df['value_diff_days_since'].iloc[i] = (df['date'].iloc[i] - previous_higher_values['date'].iloc[-1]).days

        else:

            same_values = df[df['value_diff'] == df['value_diff'].iloc[i]]

            previous_same_values = same_values[same_values['date'] < df['date'].iloc[i]]

            if not previous_same_values.empty:
                df['value_diff_days_since'].iloc[i] = (df['date'].iloc[i] - previous_same_values['date'].iloc[-1]).days
    

# ----------------------------------------------------------------------
def update(series_names):

    ls = []

    for name in series_names:
        print(f'Updating {name}')
        df = fred_pandas.update_records(name)        
        ls.append((name, df))

    for name, df in ls:
        print(f'{name:<20} {len(df)}')
        # calc_days_since(df)
        calc_days_since_alt(df)

    items = [
        df.iloc[-1].to_frame().transpose().assign(series=name)
        for name, df in ls
    ]

    table = pd.concat(items, ignore_index=True)

    return table
# ----------------------------------------------------------------------

# df_sub = ls[0][1]

# df_sub

# change_days_since

# value_days_since
# value_diff_days_since