#!/usr/bin/env python3
"This python script generates a dictionary for rotation of ASCII text."

rot_dict_phase_1 = {
    'A':'N',
    'B':'O',
    'C':'P',
    'D':'Q',
    'E':'R',
    'F':'S',
    'G':'T',
    'H':'U',
    'I':'V',
    'J':'W',
    'K':'X',
    'L':'Y',
    'M':'Z'
}
rot_dict_phase_2 = {k : v for v, k in rot_dict_phase_1.items()}

cap_rot_dict = {**rot_dict_phase_1, **rot_dict_phase_2}
small_rot_dict = {k.lower() : v.lower() for k, v in cap_rot_dict.items()}

rot_dict = {**cap_rot_dict, **small_rot_dict}
