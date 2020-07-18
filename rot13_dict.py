#!/usr/bin/env python3
"This python script generates a dictionary for rotation of ASCII text."

rot_dict_phase_1 = {chr(letter) : chr(letter+13) for letter in range(65, 78)}
rot_dict_phase_2 = {k : v for v, k in rot_dict_phase_1.items()}

cap_rot_dict = {**rot_dict_phase_1, **rot_dict_phase_2}
small_rot_dict = {k.lower() : v.lower() for k, v in cap_rot_dict.items()}

rot_dict = {**cap_rot_dict, **small_rot_dict}
