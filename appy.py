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
