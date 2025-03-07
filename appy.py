import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from stmol import showmol
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors
from padelpy import from_smiles
# from PaDEL_pywrapper import PaDEL
# from PaDEL_pywrapper import descriptors
import numpy as np
import pickle
import joblib

st.title("Predictor de docking score de ligando-receptor Mpro")

compound_smiles=st.text_input('Ingresa tu código SMILES','CC1CCC2C13CCC(=C)C(C3)C2(C)C ')
mm = Chem.MolFromSmiles(compound_smiles)

Draw.MolToFile(mm,'mol.png')
st.image('mol.png')

#######
RDKit_select_descriptors = joblib.load('archivos/RDKit_select_descriptors.pickle')
PaDEL_select_descriptors = joblib.load('./archivos/PaDEL_select_descriptors.pickle')
robust_scaler = joblib.load('./archivos/robust_scaler.pickle')
minmax_scaler = joblib.load('./archivos/minmax_scaler.pickle')
#selector_lgbm = joblib.load('./archivos/selector_LGBM.pickle')
#lgbm_model = joblib.load('./archivos/krr_best_model.pickle')
selector_lgbm = joblib.load('./archivos/selector_LGBM.joblib')
lgbm_model = joblib.load('./archivos/hgb_best_model.joblib')

