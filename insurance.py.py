import streamlit as st
import pandas as pd
from pickle import load
from sklearn.preprocessing import MinMaxScaler

# App Title
st.title('Predictive Model')
st.write('Attorney Involvement in Claims')

# Sidebar Inputs
st.sidebar.write('Enter Details of Claimants📝')

def Features_in():
    Sex = st.sidebar.radio('Sex ', ['Female', 'Male'])
    Sex_ = 0 if Sex == 'Female' else 1

    Insure = st.sidebar.radio('Does Claimant is Insured or Not ', ['Yes', 'No'])
    insure = 0 if Insure == 'No' else 1

    SBelt = st.sidebar.radio('Wearing seat belt', [0, 1])
    st.sidebar.markdown('0 - No | 1 - Yes')

    age = st.sidebar.number_input('Enter Age of Claimant : ', min_value=0, max_value=100)

    Loss = st.number_input('Loss')

    AS = st.sidebar.radio('Accident severity', [0, 1, 2])
    st.sidebar.markdown('0 - Minor  | 1 - Moderate | 2 - Severe')

    amount_setteled = st.number_input('Settlement amount')

    Policy_type = st.sidebar.radio('Policy type', [0, 1])
    st.sidebar.markdown('0 - Comprehensive | 1 - Third-Party ')

    # Creating data dictionary
    data = {
        'CLMSEX': Sex_,
        'CLMINSUR': insure,
        'SEATBELT': SBelt,
        'CLMAGE': age,
        'LOSS': Loss,
        'Accident_Severity': AS,
        'Settlement_Amount': amount_setteled,
        'Policy_Type': Policy_type
    }

    df = pd.DataFrame(data, index=[0])
    return df

# Get input features
features = Features_in()

if st.button('Submit'):
    st.write("Input Features:")
    st.write(features)

    # Load model
    loaded_model = load(open('insure.pkl', 'rb'))

    # Columns to scale
    cols_to_scale = ['CLMAGE', 'LOSS', 'Settlement_Amount']

    # Apply MinMaxScaler (assume same training scale ranges)
    scaler = MinMaxScaler()
    scaler.fit([[0, 0, 0], [100, 100000, 100000]])  # adjust based on training data

    features[cols_to_scale] = scaler.transform(features[cols_to_scale])

    # Ensure column order
    final_features = ['CLMSEX', 'CLMINSUR', 'SEATBELT', 'CLMAGE',
                      'LOSS', 'Accident_Severity', 'Settlement_Amount', 'Policy_Type']
    features = features[final_features]

    # Predict
    res = loaded_model.predict(features)

    # Output
    if res == 0:
        msg = 'No, Attorney is not involved in the claim.'
        st.warning(msg)
    else:
        msg = 'Yes, Attorney is involved in the claim ⚖️'
        st.success(msg)






