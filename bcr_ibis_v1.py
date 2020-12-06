#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:30:12 2020
Breast Cancer Risk Factors - Conversion to Text File for Export to IBIS 

@author: Sophie Vincoff
"""
#import numpy as np
ibis = "v8 \n 1 \n"

#%% Table 1: Personal Information Fields

# Everything after the = sign will obviously be reevaluated once the website is made 
name = ""                               # 1: text comprised of numbers, letters. No special characters or blanks.
age = ""                                # 2: in years, set to -99 if missing
age_menarche =  ""                      # 3: in years (integer), -99 if missing
live_births = ""                        # 4: 0 = nulliparous, 1 = parous, 2 = unknown 
age_birth1 = ""                         # 5: years (int). -99 if parous but age unknown, 0 if nulliparous
men_stat = ""                           # 6: years(int). -99 if pre-menopausal, unknown, or post-menopausal with unknown age at menopause
men_age = ""                            # 7: years(int). -99 if pre-menopausal, unknown, or post-menopausal with unknown age at menopause
height = ""                             # 8: height(in meters, to nearest cm ie 1.65), -99 if missing
weight = ""                             # 9: weight(in kg). Set to -99 if missing
hyperplasia = ""                        # 10: 1 if history of hyperplasia, 0 otherwise
atyp_hyperplasia = ""                   # 11: 1 if history of atypical hyperplasia, 0 otherwise
lcis = ""                               # 12: 1 if history of LCIS, 0 otherwise 
NIU = 0                                 # 13: MUST BE 0
ovarian = ""                            # 14: 1 if woman has had ovarian cancer, 0 otherwise
age_ovarian = ""                        # 15: years(int). -99 if missing
ashkenazi = ""                          # 16: 1 if Ashkenazi Jew. 0 if missing or unknown.
hrt_use = ""                            # 17: 0 = never, 1 = previous (> 5y ago), 2 = previous (<5y ago), 3 = current user
hrt_type = ""                           # 18: 0 = oestrogen, 1 = combined, hrt_use == 0, or hrt_type == 1
hrt_time = ""                           # 19: number of years (to 1 decimal place if needed), 0 if not relevant/missing/unknown
hrt_future = ""                         # 20: num years (1dp if needed), 0 if not relevant/missing/unknown
hrt_lastuse = ""                        # 21: num years (1dp if needed) 0 if nr/missing/unknown
genetic = ""                            # 22: 0 = never or unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2
gen_father = ""                         # 23: same as 22

# code 


# Final Table 1 String
table1 = name + " " + age + " " + age_menarche + " " + live_births + " " + age_birth1 + " " + men_stat + " " + men_age + " " + height + " "
table1 = table1 + weight + " " + hyperplasia + " " + atyp_hyperplasia + " " + lcis + " " + NIU + " " + ovarian + " " + age_ovarian + " " + ashkenazi + " "
table1 = table1 + hrt_use + " " + hrt_type + " " + hrt_time + " " + hrt_future + " " + hrt_lastuse + " " + genetic + " " + gen_father 

#%% Table 2: Compulsory Family History Members' Information

# Mother
mom_bc = ""                             # 24: 0 = no/missing/unknown, 1 = yes
mom_bilateral = ""                      # 25: 0 = no/missing/unknown, 1 = yes
mom_ovarian = ""                        # 26: 0 = no/nr/unknown, 1 = yes
mom_bc_age = ""                         # 27: age in years (int). -99 if nr/missing/unknown
mom_bilateral_age = ""                  # 28: age in years (int). -99 if nr/missing/unknown
mom_ovarian_age = ""                    # 29: age in years (int). -99 if nr/missing/unknown
mom_gen = ""                            # 30: 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2

# Sisters
num_sisters = 0                         # 31: Number (int). Then, each sister is a string of 7 numbers.
sisters = list()                        # each index will hold a string 
for i in range(0, num_sisters + 1):
    sis_bc = ""                         # 32, 39, 46,: 0 = no/missing/unknown, 1 = yes
    sis_bilateral = ""                  # 33: 0 = no/missing/unknown, 1 = yes
    sis_ovarian = ""                    # 34: 0 = no/nr/unknown, 1 = yes
    sis_bc_age = ""                     # 35: age in years (int). -99 if nr/missing/unknown
    sis_bilateral_age = ""              # 36: age in years (int). -99 if nr/missing/unknown
    sis_ovarian_age = ""                # 37: age in years (int). -99 if nr/missing/unknown
    sis_gen = ""                        # 38: 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2
    
    sisters.append("" + sis_bc + " " + sis_bilateral + " " + sis_ovarian + " " + sis_bc_age + " " + sis_bilateral_age + " " + sis_ovarian_age + " " + sis_gen)

sister_string = "" 
for s in sisters:
    sister_string = sister_string + s
    
# Paternal Grandmother
pgran_bc = ""                           # last sister +2: 0 = no/missing/unknown, 1 = yes
pgran_bilateral = ""                    # last sister +3: 0 = no/missing/unknown, 1 = yes
pgran_ovarian = ""                      # last sister +4: 0 = no/nr/unknown, 1 = yes
pgran_bc_age = ""                       # last sister +5: age in years (int). -99 if nr/missing/unknown
pgran_bilateral_age = ""                # last sister +6: age in years (int). -99 if nr/missing/unknown
pgran_ovarian_age = ""                  # last sister +7: age in years (int). -99 if nr/missing/unknown
pgran_gen = ""                          # last sister +8: 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2   

# Maternal Grandmother
mgran_bc = ""                           # last sister +9: 0 = no/missing/unknown, 1 = yes
mgran_bilateral = ""                    # last sister +10: 0 = no/missing/unknown, 1 = yes
mgran_ovarian = ""                      # last sister +11: 0 = no/nr/unknown, 1 = yes
mgran_bc_age = ""                       # last sister +12: age in years (int). -99 if nr/missing/unknown
mgran_bilateral_age = ""                # last sister +13: age in years (int). -99 if nr/missing/unknown
mgran_ovarian_age = ""                  # last sister +14: age in years (int). -99 if nr/missing/unknown
mgran_gen = ""                          # last sister +15: 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2

#Paternal aunts
num_paternal_aunts = 0                  # last sister +16: age in years (max for visual display is 5, but others will be included in calculation)
p_aunts = list()                        # each index will hold a string 
for i in range(0, num_paternal_aunts + 1):
    paunt_bc = ""                       # last sister +17, 24, etc.: 0 = no/missing/unknown, 1 = yes
    paunt_bilateral = ""                # last sister +18, 25: 0 = no/missing/unknown, 1 = yes
    paunt_ovarian = ""                  # last sister +19,: 0 = no/nr/unknown, 1 = yes
    paunt_bc_age = ""                   # last sister +20,: age in years (int). -99 if nr/missing/unknown
    paunt_bilateral_age = ""            # last sister +21,: age in years (int). -99 if nr/missing/unknown
    paunt_ovarian_age = ""              # last sister +22,: age in years (int). -99 if nr/missing/unknown
    paunt_gen = ""                      # last sister +23,: 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2
    
    p_aunts.append("" + paunt_bc + " " + paunt_bilateral + " " + paunt_ovarian + " " + paunt_bc_age + " " + paunt_bilateral_age + " " + paunt_ovarian_age + " " + paunt_gen)

paunt_string = "" 
for s in p_aunts:
    paunt_string = paunt_string + s

#Maternal aunts
num_maternal_aunts = 0                  # last paunt +1: age in years (max for visual display is 5, but others will be included in calculation)
m_aunts = list()                        # each index will hold a string 
for i in range(0, num_maternal_aunts + 1):
    maunt_bc = ""                       # last paunt +2,9,: 0 = no/missing/unknown, 1 = yes
    maunt_bilateral = ""                # last paunt +3,: 0 = no/missing/unknown, 1 = yes
    maunt_ovarian = ""                  # last paunt +4,: 0 = no/nr/unknown, 1 = yes
    maunt_bc_age = ""                   # last paunt +5,: age in years (int). -99 if nr/missing/unknown
    maunt_bilateral_age = ""            # last paunt +6,: age in years (int). -99 if nr/missing/unknown
    maunt_ovarian_age = ""              # last paunt +7,: age in years (int). -99 if nr/missing/unknown
    maunt_gen = ""                      # last paunt +8,: 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2
    
    m_aunts.append("" + maunt_bc + " " + maunt_bilateral + " " + maunt_ovarian + " " + maunt_bc_age + " " + maunt_bilateral_age + " " + maunt_ovarian_age + " " + maunt_gen)

maunt_string = "" 
for s in m_aunts:
    maunt_string = maunt_string + s

# Daughters
num_daughters = 0                       # last maunt +1: age in years (max for visual display is 5, but others will be included in calculation)
daughters = list()                      # each index will hold a string 
for i in range(0, num_daughters + 1):
    daughter_bc = ""                    # last maunt +2,9,: 0 = no/missing/unknown, 1 = yes
    daughter_bilateral = ""             # last maunt +3,: 0 = no/missing/unknown, 1 = yes
    daughter_ovarian = ""               # last maunt +4,: 0 = no/nr/unknown, 1 = yes
    daughter_bc_age = ""                # last maunt +5,: age in years (int). -99 if nr/missing/unknown
    daughter_bilateral_age = ""         # last maunt +6,: age in years (int). -99 if nr/missing/unknown
    daughter_ovarian_age = ""           # last maunt +7,: age in years (int). -99 if nr/missing/unknown
    daughter_gen = ""                   # last maunt +8,: 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2
    
    daughters.append("" + daughter_bc + " " + daughter_bilateral + " " + daughter_ovarian + " " + daughter_bc_age + " " + daughter_bilateral_age + " " + daughter_ovarian_age + " " + daughter_gen)

daughter_string = "" 
for s in daughters:
    daughter_string = daughter_string + s

#Final Table 2 String
table2 = "" + mom_bc + " " + mom_bilateral + " " + mom_ovarian + " " + mom_bc_age + " " + mom_bilateral_age + " " + mom_ovarian_age + " " + mom_gen
table2 = table2 + " " + num_sisters + " " + sister_string
table2 = table2 + " " + pgran_bc + " " + pgran_bilateral + " " + pgran_ovarian + " " + pgran_bc_age + " " + pgran_bilateral_age + " " + pgran_ovarian_age + " " + pgran_gen
table2 = table2 + " " + mgran_bc + " " + mgran_bilateral + " " + mgran_ovarian + " " + mgran_bc_age + " " + mgran_bilateral_age + " " + mgran_ovarian_age + " " + mgran_gen
table2 = table2 + " " + num_paternal_aunts + " " + paunt_string + " " + num_maternal_aunts + " " + maunt_string + " " + num_daughters + " " + daughter_string
    
#%% Table 3: Optional Family History Members

# Neices
no_neices = 0                                # no_sisters +1 if any brothers have neice w breast cancer, no_sisters if not, 0 if no info 
# Sisters
sisters_daughters = list()
for i in range(0, num_sisters + 1):
    num_sdaughters = 0                       # num(int) of this sister's daughters WITH BREAST CANCER, 0 if no info
    for i in range(0, num_sdaughters + 1):
        sdaughter_bc = ""                    # 0 = no/missing/unknown, 1 = yes
        sdaughter_bilateral = ""             # 0 = no/missing/unknown, 1 = yes
        sdaughter_ovarian = ""               # 0 = no/nr/unknown, 1 = yes
        sdaughter_bc_age = ""                # age in years (int). -99 if nr/missing/unknown
        sdaughter_bilateral_age = ""         # age in years (int). -99 if nr/missing/unknown
        sdaughter_ovarian_age = ""           # age in years (int). -99 if nr/missing/unknown
        sdaughter_gen = ""                   # 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2
        
        sisters_daughters.append("" + num_sdaughters + " " + sdaughter_bc + " " + sdaughter_bilateral + " " + sdaughter_ovarian + " " + sdaughter_bc_age + " " + sdaughter_bilateral_age + " " + sdaughter_ovarian_age + " " + daughter_gen)

sdaughter_string = "" 
for s in sisters_daughters:
    sdaughter_string = sdaughter_string + s


# Sisters
brothers_daughters = list()
num_bdaughters = 0                           # number of brothers daughters, counting all brothers
for i in range(0, num_bdaughters + 1):
    bdaughter_bc = ""                        # 0 = no/missing/unknown, 1 = yes
    bdaughter_bilateral = ""                 # 0 = no/missing/unknown, 1 = yes
    bdaughter_ovarian = ""                   # 0 = no/nr/unknown, 1 = yes
    bdaughter_bc_age = ""                    # age in years (int). -99 if nr/missing/unknown
    bdaughter_bilateral_age = ""             # age in years (int). -99 if nr/missing/unknown
    bdaughter_ovarian_age = ""               # age in years (int). -99 if nr/missing/unknown
    bdaughter_gen = ""                       # 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2
        
    brothers_daughters.append("" + bdaughter_bc + " " + bdaughter_bilateral + " " + bdaughter_ovarian + " " + bdaughter_bc_age + " " + bdaughter_bilateral_age + " " + bdaughter_ovarian_age + " " + bdaughter_gen)

bdaughter_string = "" 
for s in brothers_daughters:
    bdaughter_string = bdaughter_string + s
    
# Paternal half sisters
phsisters = list()                           # list of paternal half sisters 
num_phsisters = 0                            # integer. 0 if no info
for i in range(0, num_phsisters + 1):
    phsister_bc = ""                         # 0 = no/missing/unknown, 1 = yes
    phsister_bilateral = ""                  # 0 = no/missing/unknown, 1 = yes
    phsister_ovarian = ""                    # 0 = no/nr/unknown, 1 = yes
    phsister_bc_age = ""                     # age in years (int). -99 if nr/missing/unknown
    phsister_bilateral_age = ""              # age in years (int). -99 if nr/missing/unknown
    phsister_ovarian_age = ""                # age in years (int). -99 if nr/missing/unknown
    phsister_gen = ""                        # 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2
        
    phsisters.append("" + phsister_bc + " " + phsister_bilateral + " " + phsister_ovarian + " " + phsister_bc_age + " " + phsister_bilateral_age + " " + phsister_ovarian_age + " " + phsister_gen)
    
phsister_string = "" 
for s in phsisters:
    phsister_string = phsister_string + s
   
# Maternal half sisters
mhsisters = list()                           # list of maternal half sisters 
num_mhsisters = 0                            # integer. 0 if no info
for i in range(0, num_mhsisters + 1):
    mhsister_bc = ""                         # 0 = no/missing/unknown, 1 = yes
    mhsister_bilateral = ""                  # 0 = no/missing/unknown, 1 = yes
    mhsister_ovarian = ""                    # 0 = no/nr/unknown, 1 = yes
    mhsister_bc_age = ""                     # age in years (int). -99 if nr/missing/unknown
    mhsister_bilateral_age = ""              # age in years (int). -99 if nr/missing/unknown
    mhsister_ovarian_age = ""                # age in years (int). -99 if nr/missing/unknown
    mhsister_gen = ""                        # 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2
        
    mhsisters.append("" + mhsister_bc + " " + mhsister_bilateral + " " + mhsister_ovarian + " " + mhsister_bc_age + " " + mhsister_bilateral_age + " " + mhsister_ovarian_age + " " + mhsister_gen)
    
mhsister_string = "" 
for s in mhsisters:
    mhsister_string = mhsister_string + s
    
# Daughters of Paternal Aunts
p_aunts_daughts = list()                        # each index will hold a string 
for i in range(0, num_paternal_aunts + 1):
    num_paunt_daughts = 0                       # number of daughters of paternal aunt
    for i in range(0, num_paunt_daughts + 1):
        pauntd_bc = ""                          # 0 = no/missing/unknown, 1 = yes
        pauntd_bilateral = ""                   # 0 = no/missing/unknown, 1 = yes
        pauntd_ovarian = ""                     # 0 = no/nr/unknown, 1 = yes
        pauntd_bc_age = ""                      # age in years (int). -99 if nr/missing/unknown
        pauntd_bilateral_age = ""               # age in years (int). -99 if nr/missing/unknown
        pauntd_ovarian_age = ""                 # age in years (int). -99 if nr/missing/unknown
        pauntd_gen = ""                         # 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2
        
        p_aunts_daughts.append("" + num_paunt_daughts + " " + pauntd_bc + " " + pauntd_bilateral + " " + pauntd_ovarian + " " + pauntd_bc_age + " " + pauntd_bilateral_age + " " + pauntd_ovarian_age + " " + pauntd_gen)

pauntd_string = "" 
for s in p_aunts_daughts:
    pauntd_string = pauntd_string + s

# Daughters of Maternal Aunts
m_aunts_daughts = list()                        # each index will hold a string 
for i in range(0, num_maternal_aunts + 1):
    num_maunt_daughts = 0                       # number of daughters of paternal aunt
    for i in range(0, num_maunt_daughts + 1):
        mauntd_bc = ""                          # 0 = no/missing/unknown, 1 = yes
        mauntd_bilateral = ""                   # 0 = no/missing/unknown, 1 = yes
        mauntd_ovarian = ""                     # 0 = no/nr/unknown, 1 = yes
        mauntd_bc_age = ""                      # age in years (int). -99 if nr/missing/unknown
        mauntd_bilateral_age = ""               # age in years (int). -99 if nr/missing/unknown
        mauntd_ovarian_age = ""                 # age in years (int). -99 if nr/missing/unknown
        mauntd_gen = ""                         # 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2
        
        m_aunts_daughts.append("" + num_maunt_daughts + " " + mauntd_bc + " " + mauntd_bilateral + " " + mauntd_ovarian + " " + mauntd_bc_age + " " + mauntd_bilateral_age + " " + mauntd_ovarian_age + " " + mauntd_gen)

mauntd_string = "" 
for s in m_aunts_daughts:
    mauntd_string = mauntd_string + s

# Daughters of Paternal Uncles
puncledaught = 0                                # 0 if no pat uncle daughters, 1 if any
puncle_daughters = list()                              # list of maternal half sisters 
num_puncled = 0                                 # integer. 0 if no info
for i in range(0, num_puncled + 1):
    puncled_bc = ""                             # 0 = no/missing/unknown, 1 = yes
    puncled_bilateral = ""                      # 0 = no/missing/unknown, 1 = yes
    puncled_ovarian = ""                        # 0 = no/nr/unknown, 1 = yes
    puncled_bc_age = ""                         # age in years (int). -99 if nr/missing/unknown
    puncled_bilateral_age = ""                  # age in years (int). -99 if nr/missing/unknown
    puncled_ovarian_age = ""                    # age in years (int). -99 if nr/missing/unknown
    puncled_gen = ""                            # 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2
        
    puncle_daughters.append("" + puncled_bc + " " + puncled_bilateral + " " + puncled_ovarian + " " + puncled_bc_age + " " + puncled_bilateral_age + " " + puncled_ovarian_age + " " + puncled_gen)
    
puncled_string = "" 
for s in puncle_daughters:
    puncled_string = puncled_string + s
    
# Daughters of Maternal Uncles
muncledaught = 0                                # 0 if no pat uncle daughters, 1 if any
muncle_daughters = list()                              # list of maternal half sisters 
num_muncled = 0                                 # integer. 0 if no info
for i in range(0, num_muncled + 1):
    muncled_bc = ""                             # 0 = no/missing/unknown, 1 = yes
    muncled_bilateral = ""                      # 0 = no/missing/unknown, 1 = yes
    muncled_ovarian = ""                        # 0 = no/nr/unknown, 1 = yes
    muncled_bc_age = ""                         # age in years (int). -99 if nr/missing/unknown
    muncled_bilateral_age = ""                  # age in years (int). -99 if nr/missing/unknown
    muncled_ovarian_age = ""                    # age in years (int). -99 if nr/missing/unknown
    muncled_gen = ""                            # 0 = never/unknown, 1 = negative, 2 = BRCA1, 3 = BRCA2
        
    muncle_daughters.append("" + muncled_bc + " " + muncled_bilateral + " " + muncled_ovarian + " " + muncled_bc_age + " " + muncled_bilateral_age + " " + muncled_ovarian_age + " " + muncled_gen)
    
muncled_string = "" 
for s in muncle_daughters:
    muncled_string = muncled_string + s
    
# Final Table 3 string
table3 = "" + no_neices + " " + sdaughter_string + " " + num_bdaughters + " " + bdaughter_string + " " + num_phsisters + " " + phsister_string
table3 = table3 + " " + num_mhsisters + " " + mhsister_string + " " + num_paternal_aunts + " " + pauntd_string + " " + num_maternal_aunts + " " + mauntd_string
table3 = table3 + " " + puncledaught + " " + num_puncled + " " + puncled_string + " " + muncledaught + " " + num_muncled + " " + muncled_string

#%% Table 4: New Information
father_bc = ""                              # position table 3 + 1: 0 = no/unknown, 1 = yes
brother_bc = ""                             # table 3 + 2: 0 = no/unknown, 1 = yes
density_measure = ""                        # 0 = Volpara Volumetric Density(%) or unknown, 1 = VAS Percentage Density, 2 = BI-RADS ATLAS Density
density_val = ""                            # 0.00-100.00 from Volpara or VAS, OR for BI-RADS: 1 (<25%), 2 (25-50%), 3 (50-75%), 4 (>75%), -99 if unavailable
poly_SNP = ""                               # log relative risk, decimal; 0 if missing/unknown

# Final table 4 string
table4 =  "" + father_bc + " " + brother_bc + " " + density_measure + " " + density_val + " " + poly_SNP

#%% Final String!
ibis = ibis + table1 + " " + table2 + " " + table3 + " " + table4



















































