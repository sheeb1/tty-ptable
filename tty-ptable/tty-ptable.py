import argparse os

ASCII_ART_DIR = os.path.join(os.path.dirname(__file__), 'ascii_art')

elements = {
  'H': {
    'name': 'Hydrogen',
    'atomic_number': 1,
    'atomic_mass': '1.008 u',
    'series': 'Reactive nonmetals',
    'common_isotopoes': 'Hydrogen-1 (99.972%), Hydrogen-2 (0.001%)',
    'radioactive_isotopes': 'Hydrogen-3 (trace) (β− decay), Hydrogen-4, Hydrogen-5, Hydrogen-6, Hydrogen-7 (neutron emmission)',
    'electronegativity': '2.20',
    'electron_configuration': '1s1'
  },
  'He': {
    'name': 'Helium',
    'atomic_number': 2,
    'atomic_mass': '4.0026 u',
    'series': 'Noble gases',
    'common_isotopoes': 'Helium-3 (0.0002%), Helium-4 (99.9998%)',
    'radioactive_isotopes': 'Helium-2 (proton emmission), Helium-5, Helium-7, Helium-9, Helium-10 (neutron emmission), Helium-6, Helium-8 (β− decay)',
    'electronegativity': 'N/A',
    'electron_configuration': '1s2'
  },
  'Li': {
    'name': 'Lithium',
    'atomic_number': 3,
    'atomic_mass': '6.94 u',
    'series': 'Alkali metals',
    'common_isotopoes': 'Lithium-6 (7.59%), Lithium-7 (92.41%)',
    'radioactive_isotopes': 'Lithium-3, Lithium-4, Lithium-5 (proton emmission) Lithium-8, Lithium-9, Lithium-11 (β− decay), Lithium-10, Lithium-12 (neutron emmission)',
    'electronegativity': '0.98',
    'electron_configuration': '1s2 2s1'
  },
  'Be': {
    'name': 'Beryllium',
    'atomic_number': 4,
    'atomic_mass': '9.0122 u',
    'series': 'Alkaline earth metals',
    'common_isotopes': 'Beryllium-9 (100%)',
    'radioactive_isotopes': 'Beryllium-5, Beryllium-6 (proton emission), Beryllium-7 (electron capture), Beryllium-8 (α decay), Beryllium-10, Beryllium-11, Beryllium-12, Beryllium-14 (β− decay), Beryllium-13, Beryllium-15, Beryllium-16 (neutron emission)',
    'electronegativity': '1.57',
    'electron_configuration': '1s2 2s2'
  },
  'B': {
    'name': 'Boron',
    'atomic_number': 5,
    'atomic_mass': '10.81 u',
    'series': 'Mettaloids',
    'common_isotopes': 'Boron-10 (19.8%), Boron-11 (80.2%)',
    'radioactive_isotopes': 'Boron-6, Boron-7, Boron-9 (proton emission), Boron-8 (β+ emission), Boron-12, Boron-13, Boron-14, Boron-15, Boron-17, Boron-19 (β− decay), Boron-16, Boron-18 (neutron emission)',
    'electronegativity': '2.04',
    'electron_configuration': '1s2 2s2 2p1'
  },
  'C': {
    'name': 'Carbon',
    'atomic_number': 6,
    'atomic_mass': '12.011 u',
    'series': 'Reactive nonmetals',
    'common_isotopes': 'Carbon-12 (98.89%), Carbon-13 (1.11%)',
    'radioactive_isotopes': 'Carbon-8 (proton emission), Carbon-9, Carbon-10, Carbon-11 (β+ emission), Carbon-14, Carbon-15, Carbon-16, Carbon-17, Carbon-18 (β− decay) Carbon-21 (neutron emission) Carbon-19, Carbon-20, Carbon-22 (variable, β−, β−n, β−2n)',
    'electronegativity': '2.55',
    'electron_configuration': '1s2 2s2 2p2'
  },
  'N': {
    'name': 'Nitrogen',
    'atomic_number': 7,
    'atomic_mass': '14.007 u',
    'series': 'Reactive nonmetals',
    'common_isotopes': 'Nitrogen-14 (99.634%), Nitrogen-15 (0.366%)',
    'radioactive_isotopes': 'Nitrogen-10, Nitrogen-11 (proton emission), Nitrogen-12, Nitrogen-13 (β+ emission) Nitrogen-16, Nitrogen-18, Nitrogen-22, Nitrogen-25 (β− decay), Nitrogen-24 (neutron emission), Nitrogen-17, Nitrogen-19, Nitrogen-20, Nitrogen-21, Nitrogen-23 (',
}

def load_ascii_art(symbol):
  art_file = os.path.join(ASCII_ART_DIR, f"{symbol}.txt")
  try:
    with open(art_file, 'r') as file:
      return file.readlines()
  except FileNotFoundError:
    return ["[ASCII art not available]\n"]

def show_element_info(symbol):
  element = elements.get(symbol)
  if element:
    ascii_art = load_ascii_art(symbol)
    element_info = [
      f"Element name: {element['name']}",
      f"Element symbol: {symbol}",
      f"Atomic Number: {element['atomic_number']}",
      f"Atomic mass: {element['atomic_mass']}",
      f"Series: {element['series']}",
      f"Common isotopes: {element['common_isotopes']}",
      f"Radioactive isotopes: {element['radioactive_isotopes']}",
      f"Electronegativity: {element['electronegativity']}",
      f"Electron configuration: {element['electron_configuration']}",
    ]
    
    max_lines = max(len(ascii_art), len(element_info))

    for i in range(max_lines):
      art_line = ascii_art[i].rstrip() if i < len(ascii_art) else ''
      info_line = element_info[i] if i < len(element_info) else ''
      print(f"{art_line:<40} {info_line}")
  else:
    print(f"Error: Element with symbol '{symbol}' not found")

def show_ascii_periodic_table():
  periodic_table_file = os.path.join(ASCII_ART_DIR, 'periodic_table.txt')
  try:
    with open(periodic_table_file, 'r') as file:
      print(file.read())

except FileNotFoundError:
  print("[Periodic Table not available]")

def main():
  parser = argparse.ArgumentParser(description="A Periodic table for the Linux terminal.")
  for symbol, element in elements.items():
    long_flag = f"--{element['name']}"
    short_flag = f"-{symbol}"

  args = parser.parse_args()

  for symbol, element in elements.items():
    if getattr(args, element['name']) or getattr(args, symbol):
      show_element_info(symbol)
      return
  show_ascii_periodic_table()
