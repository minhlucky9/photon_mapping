import os
import pandas as pd
from modules.Energy.CorrectEnergy import read_spectrum_file

#Objectif of this module is read the optical properties (material) of each object 
#Calculate the average value of the spectrum range
#Data is located in this directory: ./PO

def setup_dataset_materials(w_start: int, w_end: int, po_dir: str):
    """
    Fills the materialsR and materialsT dictionaries with information from the provided data for the materials of
    the simulation.
    Parameters
    ----------
    w_start: int
        The first wavelength of band.
    w_end: int
        The last wavelength of band.

    Returns
    -------

    """
    materialsT = {}
    materialsS = {}
    materialsR = {}

    for element in ("Plant", "Env"):  # Reflectances
        files = []
        dir_pathReflect = (
            po_dir + "/" + element + "/ReflectancesMean/"
        )
        for path in os.listdir(dir_pathReflect):
            if os.path.isfile(os.path.join(dir_pathReflect, path)):
                if not path.startswith("."):
                    files.append(path)
        for file in files:
            matName = file.split(".")[0]
            contentReflect, stepReflect, startReflect = read_spectrum_file(
                os.path.join(dir_pathReflect, file)
            )
            
            refl = get_average_of_props_optic(range(w_start, w_end, 1), contentReflect)
            
            materialsR[matName] = (
                float(refl)
                if float(refl) > 0
                else 0.0
            )

    for element in ("Plant", "Env"):  # Transmittances
        files = []
        dir_pathTransmit = (
            po_dir + "/" + element + "/TransmittancesMean/"
        )
        for path in os.listdir(dir_pathTransmit):
            if os.path.isfile(os.path.join(dir_pathTransmit, path)):
                if not path.startswith("."):
                    files.append(path)
        for file in files:
            matName = file.split(".")[0]
            contentTransmit, stepTransmit, startTransmit = read_spectrum_file(
                os.path.join(dir_pathTransmit, file)
            )

            trans = get_average_of_props_optic(range(w_start, w_end, 1), contentTransmit)
            
            materialsT[matName] = (
                float(trans)
                if float(trans) > 0
                else 0.0
            )

    #Specularities
    dir_pathSpec = (po_dir + "/Specularities.xlsx")
    contentSpec = (pd.ExcelFile(dir_pathSpec)).parse(0)
    mat_names = contentSpec["Materiau"]
    mat_spec = contentSpec["Valeur estimee visuellement"]
    
    for i in range(len(mat_spec)):
        materialsS[mat_names[i]] = (
            float(mat_spec[i])
            if float(mat_spec[i]) > 0
            else 0.0
        )


    return materialsR, materialsS, materialsT

def get_average_of_props_optic(band: range, props: dict) -> float:
    res = 0.0
    count = 0
    for i in band:
        if i in props:
            res += props[i]
            count += 1

    if count != 0:
        res /= count
    
    return res