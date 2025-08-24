import pubchempy as pcp
print(pcp.get_compounds('H2O', 'formula'))  # Provavelmente []
print(pcp.get_compounds('H2O', 'name'))     # Provavelmente []
print(pcp.get_compounds('water', 'name'))   # Deve retornar resultado!