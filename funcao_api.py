import pubchempy as pcp
import time
from googletrans import Translator

class Api: 
    def buscar_molecula(self, input):
        formula = input.replace(" ", "")

        try:
            resultados = pcp.get_compounds(formula, 'formula')
            if not resultados:
                resultados = pcp.get_compounds(formula, 'name')
            if not resultados:
                return {"info": f"Molecule '{formula}' not found.", "image": None}
            molecula = resultados[0]

            time.sleep(2)
            info = (

            f"Name: {molecula.iupac_name}\n"
            f"Molecular Formula: {molecula.molecular_formula}\n"
            f"Molecular Weight: {molecula.molecular_weight} g/mol\n"
            f"CID: {molecula.cid}\n"
            f"Number of Atoms: {molecula.heavy_atom_count}\n"
            f"H-bond Donors: {molecula.h_bond_donor_count}\n"
            f"H-bond Acceptors: {molecula.h_bond_acceptor_count}"

            )
            image = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/{molecula.cid}/PNG"
            return {"info": info, "image": image}
        except Exception:
            return {"info": f"Molecule '{formula}' not found.", "image": None}

    def traduzir(self, texto, idioma_destino):
        translator = Translator()
        resultado = translator.translate(texto, dest=idioma_destino)
        return resultado.text



