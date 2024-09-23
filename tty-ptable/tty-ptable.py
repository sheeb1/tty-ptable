import argparse os

ASCII_ART_DIR = os.path.join(os.path.dirname(__file__), 'ascii_art')

elements = {
  'H' = {
    'name': 'Hydrogen',
    'atomic_number': 1,
    'atomic_mass': '1.008 u',
    'series': 'Reactive nonmetals',
    'common_isotopoes': 'Hydrogen-1 (99.972%), Hydrogen-2 (0.001%)',
    'radioactive_isotopes': 'Hydrogen-3 (trace) (β− decay), Hydrogen-4, Hydrogen-5, Hydrogen-6, Hydrogen-7 (neutron emmission)',
    'electronegativity': '2.20',
    'electron_configuration': '1s1'
  }
  'He' = {
    'name': 'Helium',
    'atomic_number': 2,
    'atomic_mass': '4.0026 u',
    'series': 'Noble gases',
    'common_isotopoes': 'Helium-3 (0.0002%), Helium-4 (99.9998%)',
    'radioactive_isotopes': 'Helium-2 (proton emmission), Helium-5, Helium-7, Helium-9, Helium-10 (neutron emmission), Helium-6, Helium-8 (β− decay)',
    'electronegativity': 'N/A',
    'electron_configuration': '1s2'
  }
  'Li' = {
    'name': 'Lithium',
    'atomic_number': 3,
    'atomic_mass': '6.94 u',
    'series': 'Alkali metals',
    'common_isotopoes': 'Lithium-6 (7.59%), Lithium-7 (92.41%)',
    'radioactive_isotopes': 'Lithium-3, Lithium-4, Lithium-5 (proton emmission) Lithium-8, Lithium-9, Lithium-11 (β− decay), Lithium-10, Lithium-12 (neutron emmission)',
    'electronegativity': '0.98',
    'electron_configuration': '1s2 2s1'
  }
  'Be' = {
    
    
  }
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
