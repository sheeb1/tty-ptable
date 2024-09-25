import argparse
import os

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
    'radioactive_isotopes': 'Nitrogen-10, Nitrogen-11 (proton emission), Nitrogen-12, Nitrogen-13 (β+ emission) Nitrogen-16, Nitrogen-18, Nitrogen-22, Nitrogen-25 (β− decay), Nitrogen-24 (neutron emission), Nitrogen-17, Nitrogen-19, Nitrogen-20, Nitrogen-21, Nitrogen-23 (β− decay)',
    'electronegativity': '3.04',
    'electron configuration': '1s2 2s2 2p3'
  },
  'O': {
    'name': 'Oxygen',
    'atomic_number': 8,
    'atomic_mass': '15.999 u',
    'series': 'Reactive nonmetals',
    'common_isotopes': 'Oxygen-16 (99.76%), Oxygen-17 (0.04%), Oxygen-18 (0.20%)',
    'radioactive_isotopes': 'Oxygen-13 (β+ emission), Oxygen-14 (β+ emission), Oxygen-15 (β+ emission), Oxygen-19 (β− decay), Oxygen-20 (β− decay), Oxygen-21 (β− decay), Oxygen-22 (neutron emission)',
    'electronegativity': '3.44',
    'electron_configuration': '1s2 2s2 2p4'
  },
  'F': {
    'name': 'Fluorine',
    'atomic_number': 9,
    'atomic_mass': '18.998 u',
    'series': 'Reactive nonmetals',
    'common_isotopes': 'Fluorine-19 (100%)',
    'radioactive_isotopes': 'Fluorine-17 (β+ emission), Fluorine-18 (β+ emission), Fluorine-20 (β− decay), Fluorine-21 (β− decay), Fluorine-22 (neutron emission), Fluorine-23 (neutron emission)',
    'electronegativity': '3.98',
    'electron_configuration': '1s2 2s2 2p5'
  },
  'Ne': {
    'name': 'Neon',
    'atomic_number': 10,
    'atomic_mass': '20.180 u',
    'series': 'Noble gases',
    'common_isotopes': 'Neon-20 (90.48%), Neon-21 (0.27%), Neon-22 (9.25%)',
    'radioactive_isotopes': 'Neon-16 (β+ emission), Neon-17 (β+ emission), Neon-18 (β+ emission), Neon-19 (β+ emission), Neon-23 (β− decay), Neon-24 (β− decay), Neon-25 (neutron emission), Neon-26 (neutron emission)',
    'electronegativity': 'N/A',
    'electron_configuration': '1s2 2s2 2p6'
  },
  'Na': {
    'name': 'Sodium',
    'atomic_number': 11,
    'atomic_mass': '22.990 u',
    'series': 'Alkali metals',
    'common_isotopes': 'Sodium-23 (100%)',
    'radioactive_isotopes': 'Sodium-18 (β+ emission), Sodium-19 (β+ emission), Sodium-20 (β+ emission), Sodium-21 (β+ emission), Sodium-22 (β+ emission), Sodium-24 (β− decay), Sodium-25 (β− decay), Sodium-26 (neutron emission)',
    'electronegativity': '0.93',
    'electron_configuration': '1s2 2s2 2p6 3s1'
  },
  'Mg': {
    'name': 'Magnesium',
    'atomic_number': 12,
    'atomic_mass': '24.305 u',
    'series': 'Alkaline earth metals',
    'common_isotopes': 'Magnesium-24 (78.99%), Magnesium-25 (10.00%), Magnesium-26 (11.01%)',
    'radioactive_isotopes': 'Magnesium-20 (β+ emission), Magnesium-21 (β+ emission), Magnesium-22 (β+ emission), Magnesium-23 (β+ emission), Magnesium-27 (β− decay), Magnesium-28 (neutron emission), Magnesium-29 (neutron emission), Magnesium-30 (neutron emission)',
    'electronegativity': '1.31',
    'electron_configuration': '1s2 2s2 2p6 3s2'
  },
  'Al': {
    'name': 'Aluminium',
    'atomic_number': 13,
    'atomic_mass': '26.981 u',
    'series': 'Post-transition metals',
    'common_isotopes': 'Aluminium-27 (100%)',
    'radioactive_isotopes': 'Aluminium-23 (β+ emission), Aluminium-24 (β+ emission), Aluminium-25 (β+ emission), Aluminium-28 (β− decay), Aluminium-29 (β− decay), Aluminium-30 (neutron emission)',
    'electronegativity': '1.61',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p1'
  },
  'Si': {
    'name': 'Silicon',
    'atomic_number': 14,
    'atomic_mass': '28.085 u',
    'series': 'Metalloids',
    'common_isotopes': 'Silicon-28 (92.23%), Silicon-29 (4.67%), Silicon-30 (3.10%)',
    'radioactive_isotopes': 'Silicon-22 (β+ emission), Silicon-23 (β+ emission), Silicon-24 (β+ emission), Silicon-31 (β− decay), Silicon-32 (β− decay), Silicon-33 (neutron emission), Silicon-34 (neutron emission)',
    'electronegativity': '1.90',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p2'
  },
  'P': {
    'name': 'Phosphorus',
    'atomic_number': 15,
    'atomic_mass': '30.974 u',
    'series': 'Reactive nonmetals',
    'common_isotopes': 'Phosphorus-31 (100%)',
    'radioactive_isotopes': 'Phosphorus-26 (β+ emission), Phosphorus-27 (β+ emission), Phosphorus-28 (β+ emission), Phosphorus-32 (β− decay), Phosphorus-33 (β− decay), Phosphorus-34 (neutron emission), Phosphorus-35 (neutron emission)',
    'electronegativity': '2.19',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p3'
  },
  'S': {
    'name': 'Sulfur',
    'atomic_number': 16,
    'atomic_mass': '32.06 u',
    'series': 'Reactive nonmetals',
    'common_isotopes': 'Sulfur-32 (94.99%), Sulfur-33 (0.75%), Sulfur-34 (4.25%), Sulfur-36 (0.01%)',
    'radioactive_isotopes': 'Sulfur-27 (β+ emission), Sulfur-28 (β+ emission), Sulfur-29 (β+ emission), Sulfur-35 (β− decay), Sulfur-37 (β− decay), Sulfur-38 (neutron emission), Sulfur-39 (neutron emission)',
    'electronegativity': '2.58',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p4'
  },
  'Cl': {
    'name': 'Chlorine',
    'atomic_number': 17,
    'atomic_mass': '35.45 u',
    'series': 'Reactive nonmetals',
    'common_isotopes': 'Chlorine-35 (75.76%), Chlorine-37 (24.24%)',
    'radioactive_isotopes': 'Chlorine-28 (β+ emission), Chlorine-29 (β+ emission), Chlorine-30 (β+ emission), Chlorine-36 (β− decay), Chlorine-38 (β− decay), Chlorine-39 (neutron emission), Chlorine-40 (neutron emission)',
    'electronegativity': '3.16',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p5'
  },
  'Ar': {
    'name': 'Argon',
    'atomic_number': 18,
    'atomic_mass': '39.948 u',
    'series': 'Noble gases',
    'common_isotopes': 'Argon-36 (0.34%), Argon-38 (0.06%), Argon-40 (99.60%)',
    'radioactive_isotopes': 'Argon-29 (β+ emission), Argon-30 (β+ emission), Argon-31 (β+ emission), Argon-39 (β− decay), Argon-42 (neutron emission), Argon-43 (neutron emission)',
    'electronegativity': 'N/A',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6'
  },
  'K': {
    'name': 'Potassium',
    'atomic_number': 19,
    'atomic_mass': '39.098 u',
    'series': 'Alkali metals',
    'common_isotopes': 'Potassium-39 (93.26%), Potassium-40 (0.0117%), Potassium-41 (6.73%)',
    'radioactive_isotopes': 'Potassium-35 (β+ emission), Potassium-36 (β+ emission), Potassium-37 (β+ emission), Potassium-42 (β− decay), Potassium-43 (β− decay), Potassium-44 (neutron emission), Potassium-45 (neutron emission)',
    'electronegativity': '0.82',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s1'
  },
  'Ca': {
    'name': 'Calcium',
    'atomic_number': 20,
    'atomic_mass': '40.078 u',
    'series': 'Alkaline earth metals',
    'common_isotopes': 'Calcium-40 (96.94%), Calcium-42 (0.65%), Calcium-43 (0.13%), Calcium-44 (2.06%), Calcium-46 (0.004%), Calcium-48 (0.187%)',
    'radioactive_isotopes': 'Calcium-34 (β+ emission), Calcium-35 (β+ emission), Calcium-36 (β+ emission), Calcium-45 (β− decay), Calcium-47 (β− decay), Calcium-49 (neutron emission), Calcium-50 (neutron emission)',
    'electronegativity': '1.00',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2'
  },
  'Sc': {
    'name': 'Scandium',
    'atomic_number': 21,
    'atomic_mass': '44.956 u',
    'series': 'Transition metals',
    'common_isotopes': 'Scandium-45 (100%)',
    'radioactive_isotopes': 'Scandium-40 (β+ emission), Scandium-41 (β+ emission), Scandium-42 (β+ emission), Scandium-46 (β− decay), Scandium-47 (β− decay), Scandium-48 (neutron emission), Scandium-49 (neutron emission)',
    'electronegativity': '1.36',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d1 4s2'
  },
  'Ti': {
    'name': 'Titanium',
    'atomic_number': 22,
    'atomic_mass': '47.867 u',
    'series': 'Transition metals',
    'common_isotopes': 'Titanium-46 (8.25%), Titanium-47 (7.44%), Titanium-48 (73.72%), Titanium-49 (5.41%), Titanium-50 (5.18%)',
    'radioactive_isotopes': 'Titanium-38 (β+ emission), Titanium-39 (β+ emission), Titanium-40 (β+ emission), Titanium-45 (β− decay), Titanium-51 (neutron emission), Titanium-52 (neutron emission)',
    'electronegativity': '1.54',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d2 4s2'
  },
  'V': {
    'name': 'Vanadium',
    'atomic_number': 23,
    'atomic_mass': '50.942 u',
    'series': 'Transition metals',
    'common_isotopes': 'Vanadium-50 (0.24%), Vanadium-51 (99.76%)',
    'radioactive_isotopes': 'Vanadium-43 (β+ emission), Vanadium-44 (β+ emission), Vanadium-45 (β+ emission), Vanadium-52 (β− decay), Vanadium-53 (neutron emission), Vanadium-54 (neutron emission)',
    'electronegativity': '1.63',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d3 4s2'
  },
  'Cr': {
    'name': 'Chromium',
    'atomic_number': 24,
    'atomic_mass': '51.996 u',
    'series': 'Transition metals',
    'common_isotopes': 'Chromium-50 (4.35%), Chromium-52 (83.79%), Chromium-53 (9.50%), Chromium-54 (2.36%)',
    'radioactive_isotopes': 'Chromium-42 (β+ emission), Chromium-43 (β+ emission), Chromium-44 (β+ emission), Chromium-51 (β− decay), Chromium-55 (neutron emission), Chromium-56 (neutron emission)',
    'electronegativity': '1.66',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d5 4s1'
  },
  'Mn': {
    'name': 'Manganese',
    'atomic_number': 25,
    'atomic_mass': '54.938 u',
    'series': 'Transition metals',
    'common_isotopes': 'Manganese-55 (100%)',
    'radioactive_isotopes': 'Manganese-46 (β+ emission), Manganese-47 (β+ emission), Manganese-48 (β+ emission), Manganese-56 (β− decay), Manganese-57 (β− decay), Manganese-58 (neutron emission)',
    'electronegativity': '1.55',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d5 4s2'
  },
  'Fe': {
    'name': 'Iron',
    'atomic_number': 26,
    'atomic_mass': '55.845 u',
    'series': 'Transition metals',
    'common_isotopes': 'Iron-54 (5.85%), Iron-56 (91.75%), Iron-57 (2.12%), Iron-58 (0.28%)',
    'radioactive_isotopes': 'Iron-45 (β+ emission), Iron-46 (β+ emission), Iron-47 (β+ emission), Iron-59 (β− decay), Iron-60 (neutron emission), Iron-61 (neutron emission)',
    'electronegativity': '1.83',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d6 4s2'
  },
  'Co': {
    'name': 'Cobalt',
    'atomic_number': 27,
    'atomic_mass': '58.933 u',
    'series': 'Transition metals',
    'common_isotopes': 'Cobalt-59 (100%)',
    'radioactive_isotopes': 'Cobalt-47 (β+ emission), Cobalt-48 (β+ emission), Cobalt-49 (β+ emission), Cobalt-60 (β− decay), Cobalt-61 (β− decay), Cobalt-62 (neutron emission), Cobalt-63 (neutron emission)',
    'electronegativity': '1.88',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d7 4s2'
  },
  'Ni': {
    'name': 'Nickel',
    'atomic_number': 28,
    'atomic_mass': '58.693 u',
    'series': 'Transition metals',
    'common_isotopes': 'Nickel-58 (68.27%), Nickel-60 (26.10%), Nickel-61 (1.13%), Nickel-62 (3.63%), Nickel-64 (0.92%)',
    'radioactive_isotopes': 'Nickel-48 (β+ emission), Nickel-49 (β+ emission), Nickel-50 (β+ emission), Nickel-63 (β− decay), Nickel-65 (β− decay), Nickel-66 (neutron emission)',
    'electronegativity': '1.91',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d8 4s2'
  },
  'Cu': {
    'name': 'Copper',
    'atomic_number': 29,
    'atomic_mass': '63.546 u',
    'series': 'Transition metals',
    'common_isotopes': 'Copper-63 (69.15%), Copper-65 (30.85%)',
    'radioactive_isotopes': 'Copper-56 (β+ emission), Copper-57 (β+ emission), Copper-58 (β+ emission), Copper-66 (β− decay), Copper-67 (β− decay), Copper-68 (neutron emission)',
    'electronegativity': '1.90',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s1'
  },
  'Zn': {
    'name': 'Zinc',
    'atomic_number': 30,
    'atomic_mass': '65.38 u',
    'series': 'Transition metals',
    'common_isotopes': 'Zinc-64 (48.63%), Zinc-66 (27.90%), Zinc-67 (4.10%), Zinc-68 (18.75%), Zinc-70 (0.62%)',
    'radioactive_isotopes': 'Zinc-57 (β+ emission), Zinc-58 (β+ emission), Zinc-59 (β+ emission), Zinc-69 (β− decay), Zinc-71 (neutron emission)',
    'electronegativity': '1.65',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2'
  },
  'Ga': {
    'name': 'Gallium',
    'atomic_number': 31,
    'atomic_mass': '69.723 u',
    'series': 'Post-transition metals',
    'common_isotopes': 'Gallium-69 (60.11%), Gallium-71 (39.89%)',
    'radioactive_isotopes': 'Gallium-62 (β+ emission), Gallium-63 (β+ emission), Gallium-64 (β+ emission), Gallium-72 (β− decay), Gallium-73 (neutron emission)',
    'electronegativity': '1.81',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p1'
  },
  'Ge': {
    'name': 'Germanium',
    'atomic_number': 32,
    'atomic_mass': '72.63 u',
    'series': 'Metalloids',
    'common_isotopes': 'Germanium-70 (20.52%), Germanium-72 (27.45%), Germanium-73 (7.76%), Germanium-74 (36.52%), Germanium-76 (7.75%)',
    'radioactive_isotopes': 'Germanium-60 (β+ emission), Germanium-61 (β+ emission), Germanium-62 (β+ emission), Germanium-77 (β− decay), Germanium-78 (neutron emission)',
    'electronegativity': '2.01',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p2'
  },
  'As': {
    'name': 'Arsenic',
    'atomic_number': 33,
    'atomic_mass': '74.9216 u',
    'series': 'Metalloids',
    'common_isotopes': 'Arsenic-75 (100%)',
    'radioactive_isotopes': 'Arsenic-66 (β+ emission), Arsenic-67 (β+ emission), Arsenic-68 (β+ emission), Arsenic-77 (β− decay), Arsenic-78 (neutron emission)',
    'electronegativity': '2.18',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p3'
  },
  'Se': {
    'name': 'Selenium',
    'atomic_number': 34,
    'atomic_mass': '78.96 u',
    'series': 'Reactive nonmetals',
    'common_isotopes': 'Selenium-74 (0.89%), Selenium-76 (9.37%), Selenium-77 (7.63%), Selenium-78 (23.77%), Selenium-80 (49.61%), Selenium-82 (8.73%)',
    'radioactive_isotopes': 'Selenium-65 (β+ emission), Selenium-66 (β+ emission), Selenium-67 (β+ emission), Selenium-83 (β− decay), Selenium-84 (neutron emission)',
    'electronegativity': '2.55',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p4'
  },
  'Br': {
    'name': 'Bromine',
    'atomic_number': 35,
    'atomic_mass': '79.904 u',
    'series': 'Reactive nonmetals',
    'common_isotopes': 'Bromine-79 (50.69%), Bromine-81 (49.31%)',
    'radioactive_isotopes': 'Bromine-69 (β+ emission), Bromine-70 (β+ emission), Bromine-71 (β+ emission), Bromine-82 (β− decay), Bromine-83 (neutron emission)',
    'electronegativity': '2.96',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p5'
  },
  'Kr': {
    'name': 'Krypton',
    'atomic_number': 36,
    'atomic_mass': '83.798 u',
    'series': 'Noble gases',
    'common_isotopes': 'Krypton-78 (0.35%), Krypton-80 (2.25%), Krypton-82 (11.59%), Krypton-83 (11.50%), Krypton-84 (57.00%), Krypton-86 (17.30%)',
    'radioactive_isotopes': 'Krypton-74 (β+ emission), Krypton-75 (β+ emission), Krypton-76 (β+ emission), Krypton-87 (β− decay), Krypton-88 (neutron emission)',
    'electronegativity': 'N/A',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6'
  },
  'Rb': {
    'name': 'Rubidium',
    'atomic_number': 37,
    'atomic_mass': '85.4678 u',
    'series': 'Alkali metals',
    'common_isotopes': 'Rubidium-85 (72.17%), Rubidium-87 (27.83%)',
    'radioactive_isotopes': 'Rubidium-74 (β+ emission), Rubidium-75 (β+ emission), Rubidium-76 (β+ emission), Rubidium-88 (β− decay), Rubidium-89 (neutron emission)',
    'electronegativity': '0.82',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 5s1'
  },
  'Sr': {
    'name': 'Strontium',
    'atomic_number': 38,
    'atomic_mass': '87.62 u',
    'series': 'Alkaline earth metals',
    'common_isotopes': 'Strontium-84 (0.56%), Strontium-86 (9.86%), Strontium-87 (7.00%), Strontium-88 (82.58%)',
    'radioactive_isotopes': 'Strontium-79 (β+ emission), Strontium-80 (β+ emission), Strontium-81 (β+ emission), Strontium-89 (β− decay), Strontium-90 (neutron emission)',
    'electronegativity': '0.95',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 5s2'
  },
  'Y': {
    'name': 'Yttrium',
    'atomic_number': 39,
    'atomic_mass': '88.9058 u',
    'series': 'Transition metals',
    'common_isotopes': 'Yttrium-89 (100%)',
    'radioactive_isotopes': 'Yttrium-82 (β+ emission), Yttrium-83 (β+ emission), Yttrium-84 (β+ emission), Yttrium-90 (β− decay), Yttrium-91 (neutron emission)',
    'electronegativity': '1.22',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d1 5s2'
  },
  'Zr': {
    'name': 'Zirconium',
    'atomic_number': 40,
    'atomic_mass': '91.224 u',
    'series': 'Transition metals',
    'common_isotopes': 'Zirconium-90 (51.45%), Zirconium-91 (11.22%), Zirconium-92 (17.15%), Zirconium-94 (17.38%), Zirconium-96 (2.80%)',
    'radioactive_isotopes': 'Zirconium-78 (β+ emission), Zirconium-79 (β+ emission), Zirconium-80 (β+ emission), Zirconium-97 (β− decay), Zirconium-98 (neutron emission)',
    'electronegativity': '1.33',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d2 5s2'
  },
  'Nb': {
    'name': 'Niobium',
    'atomic_number': 41,
    'atomic_mass': '92.9064 u',
    'series': 'Transition metals',
    'common_isotopes': 'Niobium-93 (100%)',
    'radioactive_isotopes': 'Niobium-81 (β+ emission), Niobium-82 (β+ emission), Niobium-83 (β+ emission), Niobium-94 (β− decay), Niobium-95 (neutron emission)',
    'electronegativity': '1.6',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d4 5s1'
  },
  'Mo': {
    'name': 'Molybdenum',
    'atomic_number': 42,
    'atomic_mass': '95.95 u',
    'series': 'Transition metals',
    'common_isotopes': 'Molybdenum-92 (14.84%), Molybdenum-94 (9.25%), Molybdenum-95 (15.92%), Molybdenum-96 (16.68%), Molybdenum-97 (9.55%), Molybdenum-98 (24.13%), Molybdenum-100 (9.63%)',
    'radioactive_isotopes': 'Molybdenum-86 (β+ emission), Molybdenum-87 (β+ emission), Molybdenum-88 (β+ emission), Molybdenum-101 (β− decay), Molybdenum-102 (neutron emission)',
    'electronegativity': '2.16',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s1'
  },
  'Tc': {
    'name': 'Technetium',
    'atomic_number': 43,
    'atomic_mass': '[98] u',
    'series': 'Transition metals',
    'common_isotopes': 'None (all isotopes radioactive)',
    'radioactive_isotopes': 'Technetium-85 (β+ emission), Technetium-86 (β+ emission), Technetium-87 (β+ emission), Technetium-99 (β− decay), Technetium-101 (neutron emission)',
    'electronegativity': '1.9',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s2'
  },
  'Ru': {
    'name': 'Ruthenium',
    'atomic_number': 44,
    'atomic_mass': '101.07 u',
    'series': 'Transition metals',
    'common_isotopes': 'Ruthenium-96 (5.54%), Ruthenium-98 (1.87%), Ruthenium-99 (12.76%), Ruthenium-100 (12.60%), Ruthenium-101 (17.06%), Ruthenium-102 (31.55%), Ruthenium-104 (18.62%)',
    'radioactive_isotopes': 'Ruthenium-89 (β+ emission), Ruthenium-90 (β+ emission), Ruthenium-91 (β+ emission), Ruthenium-105 (β− decay), Ruthenium-106 (neutron emission)',
    'electronegativity': '2.2',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d7 5s1'
  },
  'Rh': {
    'name': 'Rhodium',
    'atomic_number': 45,
    'atomic_mass': '102.9055 u',
    'series': 'Transition metals',
    'common_isotopes': 'Rhodium-103 (100%)',
    'radioactive_isotopes': 'Rhodium-93 (β+ emission), Rhodium-94 (β+ emission), Rhodium-95 (β+ emission), Rhodium-104 (β− decay), Rhodium-105 (neutron emission)',
    'electronegativity': '2.28',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d8 5s1'
  },
  'Pd': {
    'name': 'Palladium',
    'atomic_number': 46,
    'atomic_mass': '106.42 u',
    'series': 'Transition metals',
    'common_isotopes': 'Palladium-102 (1.02%), Palladium-104 (11.14%), Palladium-105 (22.33%), Palladium-106 (27.33%), Palladium-108 (26.46%), Palladium-110 (11.72%)',
    'radioactive_isotopes': 'Palladium-95 (β+ emission), Palladium-96 (β+ emission), Palladium-97 (β+ emission), Palladium-109 (β− decay), Palladium-111 (neutron emission)',
    'electronegativity': '2.20',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10'
  },
  'Ag': {
    'name': 'Silver',
    'atomic_number': 47,
    'atomic_mass': '107.8682 u',
    'series': 'Transition metals',
    'common_isotopes': 'Silver-107 (51.839%), Silver-109 (48.161%)',
    'radioactive_isotopes': 'Silver-94 (β+ emission), Silver-95 (β+ emission), Silver-96 (β+ emission), Silver-110m (β− decay), Silver-111 (neutron emission)',
    'electronegativity': '1.93',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s1'
  },
  'Cd': {
    'name': 'Cadmium',
    'atomic_number': 48,
    'atomic_mass': '112.414 u',
    'series': 'Transition metals',
    'common_isotopes': 'Cadmium-106 (1.25%), Cadmium-108 (0.89%), Cadmium-110 (12.49%), Cadmium-111 (12.80%), Cadmium-112 (24.13%), Cadmium-113 (12.22%), Cadmium-114 (28.73%), Cadmium-116 (7.49%)',
    'radioactive_isotopes': 'Cadmium-95 (β+ emission), Cadmium-96 (β+ emission), Cadmium-97 (β+ emission), Cadmium-115 (β− decay), Cadmium-117 (neutron emission)',
    'electronegativity': '1.69',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2'
  },
  'In': {
    'name': 'Indium',
    'atomic_number': 49,
    'atomic_mass': '114.818 u',
    'series': 'Post-transition metals',
    'common_isotopes': 'Indium-113 (4.29%), Indium-115 (95.71%)',
    'radioactive_isotopes': 'Indium-107 (β+ emission), Indium-108 (β+ emission), Indium-109 (β+ emission), Indium-116 (β− decay), Indium-117 (neutron emission)',
    'electronegativity': '1.78',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p1'
  },
  'Sn': {
    'name': 'Tin',
    'atomic_number': 50,
    'atomic_mass': '118.710 u',
    'series': 'Post-transition metals',
    'common_isotopes': 'Tin-112 (0.97%), Tin-114 (0.66%), Tin-115 (0.34%), Tin-116 (14.54%), Tin-117 (7.68%), Tin-118 (24.22%), Tin-119 (8.59%), Tin-120 (32.58%), Tin-122 (4.63%), Tin-124 (5.79%)',
    'radioactive_isotopes': 'Tin-105 (β+ emission), Tin-106 (β+ emission), Tin-107 (β+ emission), Tin-121m (β− decay), Tin-125 (neutron emission)',
    'electronegativity': '1.96',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p2'
  },
  'Sb': {
    'name': 'Antimony',
    'atomic_number': 51,
    'atomic_mass': '121.760 u',
    'series': 'Metalloids',
    'common_isotopes': 'Antimony-121 (57.21%), Antimony-123 (42.79%)',
    'radioactive_isotopes': 'Antimony-106 (β+ emission), Antimony-107 (β+ emission), Antimony-108 (β+ emission), Antimony-124 (β− decay), Antimony-125 (neutron emission)',
    'electronegativity': '2.05',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p3'
  },
  'Te': {
    'name': 'Tellurium',
    'atomic_number': 52,
    'atomic_mass': '127.60 u',
    'series': 'Metalloids',
    'common_isotopes': 'Tellurium-120 (0.096%), Tellurium-122 (2.603%), Tellurium-123 (0.908%), Tellurium-124 (4.816%), Tellurium-125 (7.139%), Tellurium-126 (18.952%), Tellurium-128 (31.74%), Tellurium-130 (34.08%)',
    'radioactive_isotopes': 'Tellurium-105 (β+ emission), Tellurium-106 (β+ emission), Tellurium-107 (β+ emission), Tellurium-127 (β− decay), Tellurium-129m (neutron emission)',
    'electronegativity': '2.1',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p4'
  },
  'I': {
    'name': 'Iodine',
    'atomic_number': 53,
    'atomic_mass': '126.90447 u',
    'series': 'Reactive nonmetals',
    'common_isotopes': 'Iodine-127 (100%)',
    'radioactive_isotopes': 'Iodine-108 (β+ emission), Iodine-109 (β+ emission), Iodine-110 (β+ emission), Iodine-131 (β− decay), Iodine-132 (neutron emission)',
    'electronegativity': '2.66',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p5'
  },
  'Xe': {
    'name': 'Xenon',
    'atomic_number': 54,
    'atomic_mass': '131.293 u',
    'series': 'Noble gases',
    'common_isotopes': 'Xenon-124 (0.095%), Xenon-126 (0.089%), Xenon-128 (1.919%), Xenon-129 (26.401%), Xenon-130 (4.071%), Xenon-131 (21.232%), Xenon-132 (26.909%), Xenon-134 (10.436%), Xenon-136 (8.857%)',
    'radioactive_isotopes': 'Xenon-108 (β+ emission), Xenon-109 (β+ emission), Xenon-110 (β+ emission), Xenon-135 (β− decay), Xenon-137 (neutron emission)',
    'electronegativity': '2.6',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6'
  },
    'Cs': {
    'name': 'Cesium',
    'atomic_number': 55,
    'atomic_mass': '132.90545 u',
    'series': 'Alkali metals',
    'common_isotopes': 'Cesium-133 (100%)',
    'radioactive_isotopes': 'Cesium-121 (β+ emission), Cesium-122 (β+ emission), Cesium-123 (β+ emission), Cesium-134 (β− decay), Cesium-135 (neutron emission)',
    'electronegativity': '0.79',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 5s1'
  },
  'Ba': {
    'name': 'Barium',
    'atomic_number': 56,
    'atomic_mass': '137.327 u',
    'series': 'Alkaline earth metals',
    'common_isotopes': 'Barium-130 (0.106%), Barium-132 (0.101%), Barium-134 (2.417%), Barium-135 (6.592%), Barium-136 (7.854%), Barium-137 (11.232%), Barium-138 (71.698%)',
    'radioactive_isotopes': 'Barium-114 (β+ emission), Barium-115 (β+ emission), Barium-116 (β+ emission), Barium-139 (β− decay), Barium-140 (neutron emission)',
    'electronegativity': '0.89',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2'
  },
  'La': {
    'name': 'Lanthanum',
    'atomic_number': 57,
    'atomic_mass': '138.90547 u',
    'series': 'Lanthanides',
    'common_isotopes': 'Lanthanum-138 (0.09%), Lanthanum-139 (99.91%)',
    'radioactive_isotopes': 'Lanthanum-121 (β+ emission), Lanthanum-122 (β+ emission), Lanthanum-123 (β+ emission), Lanthanum-140 (β− decay), Lanthanum-141 (neutron emission)',
    'electronegativity': '1.10',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2'
  },
  'Ce': {
    'name': 'Cerium',
    'atomic_number': 58,
    'atomic_mass': '140.116 u',
    'series': 'Lanthanides',
    'common_isotopes': 'Cerium-136 (0.185%), Cerium-138 (0.251%), Cerium-140 (88.450%), Cerium-142 (11.114%)',
    'radioactive_isotopes': 'Cerium-123 (β+ emission), Cerium-124 (β+ emission), Cerium-125 (β+ emission), Cerium-141 (β− decay), Cerium-144 (neutron emission)',
    'electronegativity': '1.12',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4f1 5d1'
  },
  'Pr': {
    'name': 'Praseodymium',
    'atomic_number': 59,
    'atomic_mass': '140.90766 u',
    'series': 'Lanthanides',
    'common_isotopes': 'Praseodymium-141 (100%)',
    'radioactive_isotopes': 'Praseodymium-120 (β+ emission), Praseodymium-121 (β+ emission), Praseodymium-122 (β+ emission), Praseodymium-142 (β− decay), Praseodymium-143 (neutron emission)',
    'electronegativity': '1.13',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4f3 6s2'
  },
  'Nd': {
    'name': 'Neodymium',
    'atomic_number': 60,
    'atomic_mass': '144.242 u',
    'series': 'Lanthanides',
    'common_isotopes': 'Neodymium-142 (27.2%), Neodymium-143 (12.2%), Neodymium-145 (8.3%), Neodymium-146 (27.2%), Neodymium-148 (5.7%), Neodymium-150 (19.8%)',
    'radioactive_isotopes': 'Neodymium-144 (β+ emission), Neodymium-145 (β+ emission), Neodymium-147 (β− decay), Neodymium-148 (neutron emission)',
    'electronegativity': '1.14',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4f4 6s2'
  },
  'Pm': {
    'name': 'Promethium',
    'atomic_number': 61,
    'atomic_mass': '[145] u',
    'series': 'Lanthanides',
    'common_isotopes': 'None (all isotopes radioactive)',
    'radioactive_isotopes': 'Promethium-145 (β− decay), Promethium-147 (β− decay)',
    'electronegativity': '1.13',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4f5 6s2'
  },
  'Sm': {
    'name': 'Samarium',
    'atomic_number': 62,
    'atomic_mass': '150.36 u',
    'series': 'Lanthanides',
    'common_isotopes': 'Samarium-144 (3.10%), Samarium-145 (14.96%), Samarium-147 (15.00%), Samarium-148 (11.24%), Samarium-149 (13.93%), Samarium-150 (26.68%), Samarium-152 (25.99%)',
    'radioactive_isotopes': 'Samarium-151 (β+ emission), Samarium-152 (β+ emission), Samarium-153 (β− decay)',
    'electronegativity': '1.17',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4f6 6s2'
  },
  'Eu': {
    'name': 'Europium',
    'atomic_number': 63,
    'atomic_mass': '151.964 u',
    'series': 'Lanthanides',
    'common_isotopes': 'Europium-151 (47.8%), Europium-153 (52.2%)',
    'radioactive_isotopes': 'Europium-145 (β+ emission), Europium-146 (β+ emission), Europium-150 (β− decay)',
    'electronegativity': '1.2',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4f7 6s2'
  },
  'Gd': {
    'name': 'Gadolinium',
    'atomic_number': 64,
    'atomic_mass': '157.25 u',
    'series': 'Lanthanides',
    'common_isotopes': 'Gadolinium-152 (0.14%), Gadolinium-154 (2.17%), Gadolinium-155 (14.80%), Gadolinium-156 (20.47%), Gadolinium-157 (15.65%), Gadolinium-158 (24.84%), Gadolinium-160 (22.94%)',
    'radioactive_isotopes': 'Gadolinium-148 (β+ emission), Gadolinium-149 (β+ emission), Gadolinium-153 (β− decay)',
    'electronegativity': '1.2',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4f7 5d1'
  },
  'Tb': {
    'name': 'Terbium',
    'atomic_number': 65,
    'atomic_mass': '158.92535 u',
    'series': 'Lanthanides',
    'common_isotopes': 'Terbium-159 (100%)',
    'radioactive_isotopes': 'Terbium-156 (β+ emission), Terbium-157 (β+ emission), Terbium-160 (β− decay)',
    'electronegativity': '1.2',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4f9 6s2'
  },
  'Dy': {
    'name': 'Dysprosium',
    'atomic_number': 66,
    'atomic_mass': '162.500 u',
    'series': 'Lanthanides',
    'common_isotopes': 'Dysprosium-156 (0.06%), Dysprosium-158 (0.10%), Dysprosium-160 (2.34%), Dysprosium-161 (18.89%), Dysprosium-162 (25.49%), Dysprosium-163 (24.90%), Dysprosium-164 (28.17%)',
    'radioactive_isotopes': 'Dysprosium-155 (β+ emission), Dysprosium-159 (β− decay)',
    'electronegativity': '1.22',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4f10 6s2'
  },
  'Ho': {
    'name': 'Holmium',
    'atomic_number': 67,
    'atomic_mass': '164.93033 u',
    'series': 'Lanthanides',
    'common_isotopes': 'Holmium-165 (100%)',
    'radioactive_isotopes': 'Holmium-163 (β+ emission), Holmium-164 (β+ emission), Holmium-166 (β− decay)',
    'electronegativity': '1.23',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4f11 6s2'
  },
  'Er': {
    'name': 'Erbium',
    'atomic_number': 68,
    'atomic_mass': '167.259 u',
    'series': 'Lanthanides',
    'common_isotopes': 'Erbium-162 (0.14%), Erbium-164 (1.58%), Erbium-166 (33.58%), Erbium-167 (22.93%), Erbium-168 (27.39%), Erbium-170 (14.39%)',
    'radioactive_isotopes': 'Erbium-161 (β+ emission), Erbium-163 (β− decay)',
    'electronegativity': '1.24',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4f12 6s2'
  },
  'Tm': {
    'name': 'Thulium',
    'atomic_number': 69,
    'atomic_mass': '168.93422 u',
    'series': 'Lanthanides',
    'common_isotopes': 'Thulium-169 (100%)',
    'radioactive_isotopes': 'Thulium-167 (β+ emission), Thulium-168 (β− decay)',
    'electronegativity': '1.25',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4f13 6s2'
  },
  'Yb': {
    'name': 'Ytterbium',
    'atomic_number': 70,
    'atomic_mass': '173.04 u',
    'series': 'Lanthanides',
    'common_isotopes': 'Ytterbium-168 (0.14%), Ytterbium-170 (3.05%), Ytterbium-171 (14.30%), Ytterbium-172 (21.50%), Ytterbium-173 (16.10%), Ytterbium-174 (31.83%), Ytterbium-176 (13.08%)',
    'radioactive_isotopes': 'Ytterbium-169 (β+ emission), Ytterbium-171 (β− decay)',
    'electronegativity': '1.1',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4f14 6s2'
  },
  'Lu': {
    'name': 'Lutetium',
    'atomic_number': 71,
    'atomic_mass': '174.9668 u',
    'series': 'Lanthanides',
    'common_isotopes': 'Lutetium-175 (97.4%), Lutetium-176 (2.6%)',
    'radioactive_isotopes': 'Lutetium-174 (β+ emission), Lutetium-175 (β− decay)',
    'electronegativity': '1.27',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4f14 5d1'
  },
  'Hf': {
    'name': 'Hafnium',
    'atomic_number': 72,
    'atomic_mass': '178.49 u',
    'series': 'Transition metals',
    'common_isotopes': 'Hafnium-174 (0.16%), Hafnium-176 (5.27%), Hafnium-177 (18.60%), Hafnium-178 (27.28%), Hafnium-179 (13.62%), Hafnium-180 (35.06%)',
    'radioactive_isotopes': 'Hafnium-173 (β+ emission), Hafnium-175 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2'
  },
  'Ta': {
    'name': 'Tantalum',
    'atomic_number': 73,
    'atomic_mass': '180.94788 u',
    'series': 'Transition metals',
    'common_isotopes': 'Tantalum-180 (99.988%)',
    'radioactive_isotopes': 'Tantalum-179 (β+ emission), Tantalum-181 (β− decay)',
    'electronegativity': '1.5',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p3'
  },
  'W': {
    'name': 'Tungsten',
    'atomic_number': 74,
    'atomic_mass': '183.84 u',
    'series': 'Transition metals',
    'common_isotopes': 'Tungsten-182 (26.50%), Tungsten-183 (14.31%), Tungsten-184 (30.64%), Tungsten-186 (28.55%)',
    'radioactive_isotopes': 'Tungsten-178 (β+ emission), Tungsten-180 (β− decay)',
    'electronegativity': '2.36',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p5'
  },
  'Re': {
    'name': 'Rhenium',
    'atomic_number': 75,
    'atomic_mass': '186.207 u',
    'series': 'Transition metals',
    'common_isotopes': 'Rhenium-185 (37.4%), Rhenium-187 (62.6%)',
    'radioactive_isotopes': 'Rhenium-183 (β+ emission), Rhenium-184 (β− decay)',
    'electronegativity': '1.9',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p6'
  },
  'Os': {
    'name': 'Osmium',
    'atomic_number': 76,
    'atomic_mass': '190.23 u',
    'series': 'Transition metals',
    'common_isotopes': 'Osmium-184 (0.02%), Osmium-186 (1.58%), Osmium-187 (1.5%), Osmium-188 (13.2%), Osmium-189 (16.1%), Osmium-190 (25.2%), Osmium-192 (42.8%)',
    'radioactive_isotopes': 'Osmium-188 (β+ emission), Osmium-189 (β− decay)',
    'electronegativity': '2.2',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p4'
  },
  'Ir': {
    'name': 'Iridium',
    'atomic_number': 77,
    'atomic_mass': '192.217 u',
    'series': 'Transition metals',
    'common_isotopes': 'Iridium-191 (37.3%), Iridium-193 (62.7%)',
    'radioactive_isotopes': 'Iridium-190 (β+ emission), Iridium-192 (β− decay)',
    'electronegativity': '2.20',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p4'
  },
  'Pt': {
    'name': 'Platinum',
    'atomic_number': 78,
    'atomic_mass': '195.084 u',
    'series': 'Transition metals',
    'common_isotopes': 'Platinum-194 (32.9%), Platinum-195 (33.8%), Platinum-196 (25.2%), Platinum-198 (8.5%)',
    'radioactive_isotopes': 'Platinum-190 (β+ emission), Platinum-192 (β− decay)',
    'electronegativity': '2.28',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p2'
  },
  'Au': {
    'name': 'Gold',
    'atomic_number': 79,
    'atomic_mass': '196.96657 u',
    'series': 'Transition metals',
    'common_isotopes': 'Gold-197 (100%)',
    'radioactive_isotopes': 'Gold-194 (β+ emission), Gold-195 (β− decay)',
    'electronegativity': '2.54',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p1'
  },
  'Hg': {
    'name': 'Mercury',
    'atomic_number': 80,
    'atomic_mass': '200.592 u',
    'series': 'Transition metals',
    'common_isotopes': 'Mercury-196 (0.15%), Mercury-198 (10%), Mercury-199 (16.87%), Mercury-200 (29.86%), Mercury-201 (13.22%), Mercury-202 (29.09%)',
    'radioactive_isotopes': 'Mercury-194 (β+ emission), Mercury-195 (β− decay)',
    'electronegativity': '2.00',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2'
  },
  'Tl': {
    'name': 'Thallium',
    'atomic_number': 81,
    'atomic_mass': '204.38 u',
    'series': 'Post-transition metals',
    'common_isotopes': 'Thallium-203 (30.6%), Thallium-205 (69.4%)',
    'radioactive_isotopes': 'Thallium-201 (β+ emission), Thallium-202 (β− decay)',
    'electronegativity': '1.62',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p1'
  },
  'Pb': {
    'name': 'Lead',
    'atomic_number': 82,
    'atomic_mass': '207.2 u',
    'series': 'Post-transition metals',
    'common_isotopes': 'Lead-204 (1.4%), Lead-206 (24.1%), Lead-207 (22.1%), Lead-208 (52.4%)',
    'radioactive_isotopes': 'Lead-210 (β− decay)',
    'electronegativity': '1.87',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p1'
  },
  'Bi': {
    'name': 'Bismuth',
    'atomic_number': 83,
    'atomic_mass': '208.98040 u',
    'series': 'Post-transition metals',
    'common_isotopes': 'Bismuth-209 (100%)',
    'radioactive_isotopes': 'Bismuth-210 (β− decay), Bismuth-212 (β− decay)',
    'electronegativity': '2.02',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p1'
  },
  'Po': {
    'name': 'Polonium',
    'atomic_number': 84,
    'atomic_mass': '[209] u',
    'series': 'Metalloids',
    'common_isotopes': 'Polonium-210 (100%)',
    'radioactive_isotopes': 'Polonium-208 (α decay), Polonium-209 (α decay)',
    'electronegativity': '2.0',
    'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p1'
  },
  'At': {
    'name': 'Astatine',
    'atomic_number': 85,
    'atomic_mass': '[210] u',
    'series': 'Halogens',
    'common_isotopes': 'Astatine-210 (100%)',
    'radioactive_isotopes': 'Astatine-211 (α decay), Astatine-212 (α decay)',
    'electronegativity': '2.2',
    'electron_configuration': '[Xe] 4f14 5d10 6s2 6p5'
  },
  'Rn': {
    'name': 'Radon',
    'atomic_number': 86,
    'atomic_mass': '[222] u',
    'series': 'Noble gases',
    'common_isotopes': 'Radon-222 (100%)',
    'radioactive_isotopes': 'Radon-219 (α decay), Radon-220 (α decay)',
    'electronegativity': '0',
    'electron_configuration': '[Xe] 4f14 5d10 6s2 6p6'
  },
  'Fr': {
    'name': 'Francium',
    'atomic_number': 87,
    'atomic_mass': '[223] u',
    'series': 'Alkali metals',
    'common_isotopes': 'Francium-223 (100%)',
    'radioactive_isotopes': 'Francium-221 (β− decay), Francium-222 (β− decay)',
    'electronegativity': '0.7',
    'electron_configuration': '[Rn] 7s1'
  },
  'Ra': {
    'name': 'Radium',
    'atomic_number': 88,
    'atomic_mass': '226.0254 u',
    'series': 'Alkaline earth metals',
    'common_isotopes': 'Radium-226 (100%)',
    'radioactive_isotopes': 'Radium-223 (α decay), Radium-224 (α decay)',
    'electronegativity': '0.9',
    'electron_configuration': '[Rn] 7s2'
  },
  'Ac': {
    'name': 'Actinium',
    'atomic_number': 89,
    'atomic_mass': '227.0278 u',
    'series': 'Actinides',
    'common_isotopes': 'Actinium-227 (100%)',
    'radioactive_isotopes': 'Actinium-228 (β− decay), Actinium-229 (β− decay)',
    'electronegativity': '1.1',
    'electron_configuration': '[Rn] 6d1 7s2'
  },
  'Th': {
    'name': 'Thorium',
    'atomic_number': 90,
    'atomic_mass': '232.0377 u',
    'series': 'Actinides',
    'common_isotopes': 'Thorium-232 (100%)',
    'radioactive_isotopes': 'Thorium-230 (α decay), Thorium-231 (β− decay)',
    'electronegativity': '1.30',
    'electron_configuration': '[Rn] 6d2 7s2'
  },
  'Pa': {
    'name': 'Protactinium',
    'atomic_number': 91,
    'atomic_mass': '231.03588 u',
    'series': 'Actinides',
    'common_isotopes': 'Protactinium-231 (100%)',
    'radioactive_isotopes': 'Protactinium-230 (α decay), Protactinium-232 (β− decay)',
    'electronegativity': '1.5',
    'electron_configuration': '[Rn] 6d1 7s2'
  },
  'U': {
    'name': 'Uranium',
    'atomic_number': 92,
    'atomic_mass': '238.02891 u',
    'series': 'Actinides',
    'common_isotopes': 'Uranium-238 (99.27%), Uranium-235 (0.72%)',
    'radioactive_isotopes': 'Uranium-234 (α decay), Uranium-236 (β− decay)',
    'electronegativity': '1.38',
    'electron_configuration': '[Rn] 6d1 7s2'
  },
  'Np': {
    'name': 'Neptunium',
    'atomic_number': 93,
    'atomic_mass': '237.0482 u',
    'series': 'Actinides',
    'common_isotopes': 'Neptunium-237 (100%)',
    'radioactive_isotopes': 'Neptunium-236 (α decay), Neptunium-238 (β− decay)',
    'electronegativity': '1.36',
    'electron_configuration': '[Rn] 5f4 6d1 7s2'
  },
  'Pu': {
    'name': 'Plutonium',
    'atomic_number': 94,
    'atomic_mass': '244.0642 u',
    'series': 'Actinides',
    'common_isotopes': 'Plutonium-244 (0.1%)',
    'radioactive_isotopes': 'Plutonium-239 (α decay), Plutonium-240 (β− decay)',
    'electronegativity': '1.28',
    'electron_configuration': '[Rn] 5f6 7s2'
  },
  'Am': {
    'name': 'Americium',
    'atomic_number': 95,
    'atomic_mass': '243.0614 u',
    'series': 'Actinides',
    'common_isotopes': 'Americium-241 (100%)',
    'radioactive_isotopes': 'Americium-243 (α decay), Americium-242 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f7 7s2'
  },
  'Cm': {
    'name': 'Curium',
    'atomic_number': 96,
    'atomic_mass': '247.0703 u',
    'series': 'Actinides',
    'common_isotopes': 'Curium-247 (100%)',
    'radioactive_isotopes': 'Curium-245 (α decay), Curium-246 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f7 6d1 7s2'
  },
  'Bk': {
    'name': 'Berkelium',
    'atomic_number': 97,
    'atomic_mass': '247.0703 u',
    'series': 'Actinides',
    'common_isotopes': 'Berkelium-247 (100%)',
    'radioactive_isotopes': 'Berkelium-246 (α decay), Berkelium-245 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f9 7s2'
  },
  'Cf': {
    'name': 'Californium',
    'atomic_number': 98,
    'atomic_mass': '251.0796 u',
    'series': 'Actinides',
    'common_isotopes': 'Californium-251 (100%)',
    'radioactive_isotopes': 'Californium-249 (α decay), Californium-250 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f10 7s2'
  },
  'Es': {
    'name': 'Einsteinium',
    'atomic_number': 99,
    'atomic_mass': '252.0829 u',
    'series': 'Actinides',
    'common_isotopes': 'Einsteinium-253 (100%)',
    'radioactive_isotopes': 'Einsteinium-252 (α decay), Einsteinium-254 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f11 7s2'
  },
  'Fm': {
    'name': 'Fermium',
    'atomic_number': 100,
    'atomic_mass': '257.0951 u',
    'series': 'Actinides',
    'common_isotopes': 'Fermium-257 (100%)',
    'radioactive_isotopes': 'Fermium-256 (α decay), Fermium-255 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f12 7s2'
  },
  'Md': {
    'name': 'Mendelevium',
    'atomic_number': 101,
    'atomic_mass': '258.0984 u',
    'series': 'Actinides',
    'common_isotopes': 'Mendelevium-258 (100%)',
    'radioactive_isotopes': 'Mendelevium-257 (α decay), Mendelevium-256 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f13 7s2'
  },
  'No': {
    'name': 'Nobelium',
    'atomic_number': 102,
    'atomic_mass': '259.101 (u)',
    'series': 'Actinides',
    'common_isotopes': 'Nobelium-259 (100%)',
    'radioactive_isotopes': 'Nobelium-258 (α decay), Nobelium-257 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f14 7s2'
  },
  'Lr': {
    'name': 'Lawrencium',
    'atomic_number': 103,
    'atomic_mass': '266.119 u',
    'series': 'Actinides',
    'common_isotopes': 'Lawrencium-262 (100%)',
    'radioactive_isotopes': 'Lawrencium-260 (α decay), Lawrencium-261 (β− decay)',
    'electronegativity': '1.6',
    'electron_configuration': '[Rn] 5f14 6d1 7s2'
  },
  'Rf': {
    'name': 'Rutherfordium',
    'atomic_number': 104,
    'atomic_mass': '[267] u',
    'series': 'Transition metals',
    'common_isotopes': 'Rutherfordium-267 (100%)',
    'radioactive_isotopes': 'Rutherfordium-266 (α decay), Rutherfordium-265 (β− decay)',
    'electronegativity': '1.6',
    'electron_configuration': '[Rn] 5f14 6d2 7s2'
  },
  'Db': {
    'name': 'Dubnium',
    'atomic_number': 105,
    'atomic_mass': '[268] u',
    'series': 'Transition metals',
    'common_isotopes': 'Dubnium-268 (100%)',
    'radioactive_isotopes': 'Dubnium-267 (α decay), Dubnium-266 (β− decay)',
    'electronegativity': '1.5',
    'electron_configuration': '[Rn] 5f14 6d3 7s2'
  },
  'Sg': {
    'name': 'Seaborgium',
    'atomic_number': 106,
    'atomic_mass': '[271] u',
    'series': 'Transition metals',
    'common_isotopes': 'Seaborgium-271 (100%)',
    'radioactive_isotopes': 'Seaborgium-270 (α decay), Seaborgium-269 (β− decay)',
    'electronegativity': '1.6',
    'electron_configuration': '[Rn] 5f14 6d4 7s2'
  },
  'Bh': {
    'name': 'Bohrium',
    'atomic_number': 107,
    'atomic_mass': '[270] u',
    'series': 'Transition metals',
    'common_isotopes': 'Bohrium-270 (100%)',
    'radioactive_isotopes': 'Bohrium-271 (α decay), Bohrium-269 (β− decay)',
    'electronegativity': '1.6',
    'electron_configuration': '[Rn] 5f14 6d5 7s2'
  },
  'Hs': {
    'name': 'Hassium',
    'atomic_number': 108,
    'atomic_mass': '[277] u',
    'series': 'Transition metals',
    'common_isotopes': 'Hassium-277 (100%)',
    'radioactive_isotopes': 'Hassium-276 (α decay), Hassium-275 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f14 6d6 7s2'
  },
  'Mt': {
    'name': 'Meitnerium',
    'atomic_number': 109,
    'atomic_mass': '[278] u',
    'series': 'Transition metals',
    'common_isotopes': 'Meitnerium-278 (100%)',
    'radioactive_isotopes': 'Meitnerium-276 (α decay), Meitnerium-275 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f14 6d7 7s2'
  },
  'Ds': {
    'name': 'Darmstadtium',
    'atomic_number': 110,
    'atomic_mass': '[281] u',
    'series': 'Transition metals',
    'common_isotopes': 'Darmstadtium-281 (100%)',
    'radioactive_isotopes': 'Darmstadtium-280 (α decay), Darmstadtium-279 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f14 6d8 7s2'
  },
  'Rg': {
    'name': 'Roentgenium',
    'atomic_number': 111,
    'atomic_mass': '[282] u',
    'series': 'Transition metals',
    'common_isotopes': 'Roentgenium-282 (100%)',
    'radioactive_isotopes': 'Roentgenium-281 (α decay), Roentgenium-280 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f14 6d9 7s2'
  },
  'Cn': {
    'name': 'Copernicium',
    'atomic_number': 112,
    'atomic_mass': '[285] u',
    'series': 'Transition metals',
    'common_isotopes': 'Copernicium-285 (100%)',
    'radioactive_isotopes': 'Copernicium-284 (α decay), Copernicium-283 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f14 6d10 7s2'
  },
  'Nh': {
    'name': 'Nihonium',
    'atomic_number': 113,
    'atomic_mass': '[286] u',
    'series': 'Post-transition metals',
    'common_isotopes': 'Nihonium-286 (100%)',
    'radioactive_isotopes': 'Nihonium-285 (α decay), Nihonium-284 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f14 6d10 7s2'
  },
  'Fl': {
    'name': 'Flerovium',
    'atomic_number': 114,
    'atomic_mass': '[289] u',
    'series': 'Post-transition metals',
    'common_isotopes': 'Flerovium-289 (100%)',
    'radioactive_isotopes': 'Flerovium-288 (α decay), Flerovium-287 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f14 6d10 7s2'
  },
  'Mc': {
    'name': 'Moscovium',
    'atomic_number': 115,
    'atomic_mass': '[288] u',
    'series': 'Post-transition metals',
    'common_isotopes': 'Moscovium-288 (100%)',
    'radioactive_isotopes': 'Moscovium-287 (α decay), Moscovium-286 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f14 6d10 7s2'
  },
  'Lv': {
    'name': 'Livermorium',
    'atomic_number': 116,
    'atomic_mass': '[293] u',
    'series': 'Post-transition metals',
    'common_isotopes': 'Livermorium-293 (100%)',
    'radioactive_isotopes': 'Livermorium-292 (α decay), Livermorium-291 (β− decay)',
    'electronegativity': '1.3',
    'electron_configuration': '[Rn] 5f14 6d10 7s2'
  },
  'Ts': {
    'name': 'Tennessine',
    'atomic_number': 117,
    'atomic_mass': '[294] u',
    'series': 'Halogens',
    'common_isotopes': 'Tennessine-294 (100%)',
    'radioactive_isotopes': 'Tennessine-293 (α decay), Tennessine-292 (β− decay)',
    'electronegativity': '1.0',
    'electron_configuration': '[Rn] 5f14 6d10 7s2 7p5'
  },
  'Og': {
    'name': 'Oganesson',
    'atomic_number': 118,
    'atomic_mass': '[294] u',
    'series': 'Noble gases',
    'common_isotopes': 'Oganesson-294 (100%)',
    'radioactive_isotopes': 'Oganesson-293 (α decay), Oganesson-292 (β− decay)',
    'electronegativity': '0',
    'electron_configuration': '[Rn] 5f14 6d10 7s2 7p6'
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
  return "[Periodic Table not available]"

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
