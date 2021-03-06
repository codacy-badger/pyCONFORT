"""
* In this file, the variables used by the different python scripts are collected.
* You must make sure that all the variables are correct before launching db_gen.py.
"""

" INPUT FILE "
input ='smi.smi' # input files
path ='' # path to guassian folder when we do analysis
prefix = False # if prefix = True, set a generic name for the different molecules (i.e. comp_1, comp_2, etc)

" TYPE OF DBGEN JOBS "
verbose = True

" (1) CONFORMERS AND COM FILES GENERATION "
# 3 options:
# Compute = True and write_gauss = True --> generates conformers in SDF files and writes COM files
# Compute = True and write_gauss = False --> generates conformers in SDF files only
# Compute = False and write_gauss = True --> reads SDF files from the main DBGEN folder (all SDF files)
compute = False
write_gauss = True # writting Gaussian COM files after, look options of write_gauss below

" (2) ANALYSIS OF LOG FILES"
# if analysis is True, check all LOG files inside "generated_gaussian_files".
# The folder might multiple subfolders with levels of theory (i.e. coming from the conformer generation).
# This generates new COM files from LOG files with imaginary freqs or errors
analysis = False
sp = False # write COM files after analysis
input_for_sp = '' # add the input line with keywords. For adjusting number of processors and memory, go belo (to gauss_write options)
dup = False # if dup = True, analysis will also separate duplicate LOG files
boltz = False # if boltz = True, analysis will calculate Bolztmann probabilities of each conformer
combine = False # if boltz = True and combine = True, all the data from the CSV files created with boltz will be condensed in 3 CSV files

" COMMONLY CHANGED PARAMETERS"

" (1) CHARGE FOR XTB OPTIMIZATION AND COM FILES "
charge = 0 # final charge of the molecule (used in xTB optimization and input in the final COM input files)
		# If metal_complex = True, the script will recalculate the charge

" (2) TYPE OF OPTIMIZATION "
# Options: xTB, ANI1ccx (if True is selected).  Default : RDKit optimizaiton
ANI1ccx = False
xtb = True

" (3) RDKit AND xTB PARAMETERS "
ewin = 1000 #energy window in kcal/mol to use conformers for RDKit and xTB (conformers with E higher than ewin will be discarded)
sample = 100 # number of conformers to sample to get non-torsional differences (default 100)
solvent_xtb = '' # includes energies in the xTB energies after optimization in gas-phase

" (4) OPTIONS FOR COM FILE GENERATION (write_gauss = True) "
# By default, you include optimization in the COM files.
# Optional:
frequencies = True # include frequency calculation
single_point = False # do not include optimization

" (4.1) ONLY LOWEST ENERGY CONFORMERS REQUIRED"
lowest_only = False
lowest_n  = False # for a given threshold of energy_threshold_for_gaussian
energy_threshold_for_gaussian = 100  #in kcal/mol, from all the conformers generated after xTB optimization
                                    # lowest_n must be True to apply this energy threshold

" (4.2) DEFINITION OF A SECOND CATEGORY OF ATOMS SEPARATED IN GENECP OR GEN"
genecp_atoms = ['Ir']
gen_atoms = ['']

" (4.3) DEFINTION OF BASIS SET AND LEVEL OF THEORY AND SOLVENT "
basis_set = ['6-31+g(d,p)']
basis_set_genecp_atoms = ['def2svp']
level_of_theory = ['wb97xd']
max_cycle_opt = 100 #eefault is 300

" (4.4) DISPERSION CORRECTION FOR COM FILES "
dispersion_correction = False
empirical_dispersion = 'GD3BJ'

" (4.5) SOLVATION MODEL. Options: gas_phase or any solvation model (i.e. SMD, IEFPCM, CPCM)"
solvent_model = 'IEFPCM'
solvent_name = 'Chloroform'

" (4.6) DEFAULT PARAMTERS FOR GAUSSIAN OPTIMIZATION "
chk = False
nprocs = 36
mem='60GB'

" (5) PERFORMANCE OF THE CODE "
time = True #request run time

" (6) EXP RULES "
exp_rules = False # apply some experimental rules to discard some outputs
angle_off = 30 # margin of error to determine angles (i.e. if angle_off is 30, and the angle is 180, angles from
		# 150 to 210 degrees will be discarded)

" (7) OPTIONS FOR METALS, ATOMS WITH UNCOMMON HYBRIDIZATIONS AND NCI COMPLEXES "
# IF A METAL OR AN ATOM WITH UNCOMMON HYBRIDIZATION (i.e. pentacoordinated phosphorus) IS USED
metal_complex= True # specify True to activate this option
metal = 'Ir' # specify the metal(s) or atom(s) with uncommon hybridization, in the format 'A','B','C'...
complex_coord = 6 # specify the coordination number of the atom
complex_type = '' # specify the following: square planar, square pyrimidal (otheriwse defaults to octahedral, Td)
m_oxi = 3 # oxidation number of the atom (it is used to calculate the charge of the molecule)
complex_spin = 3 # final spin of the molecule (the code does not calculate spin, it must be defined by the user)

" (8) IF A NONCOVALENT COMPLEX IS USED "
nci_complex = False # specify  true if NCI complex

" (9) OPTIONS FOR THE AUTOMATED WORKFLOW "
qsub = False # turn on automated submission and analysis of jobs
submission_command = 'qsub_summit' # name of the file containing the submission script


" PRE-OPTIMIZED PARAMETERS - ONLY CHANGE THIS PART IF YOU KNOW WHAT YOU ARE DOING! "

" OUTPUT FILE NAMES "
rdkit_output = '_RDKit.sdf'
xtb_output = '_xTB.sdf'
ani1_output = '_ANI1ccx.sdf'
exp_rules_output_ext = '_rules.sdf'

" FOR UNIQUE CONFORMER SELECTION FOR RDKIT, XTB AND ANI1 "
rms_threshold = 0.25 #cutoff for considering sampled conformers the same (default 0.25) for RDKit and xTB duplicate filters
energy_threshold = 0.2 # energy difference in kcal/mol between unique conformers for RDKit and xTB duplicate filters
initial_energy_threshold = 0.01 # energy difference for the first RDKit filter based on E only
max_matches_RMSD = 1000000 # max iterations to find optimal RMSD in RDKit duplicate filter
                            # The higher the number the longer the duplicate filter takes but
                            # the more duplicates are filtered off
heavyonly = False # If True, H from OH, NH, etc. will not be used to generate conformers (recommended: False with molecules that contain OH groups)

" FILTERS FOR RDKIT OPTIMIZATION "
max_torsions = 20 # Skip any molecules with more than this many torsions (default 5)
num_rot_bonds = 20 # Skip any molecules with more than this many rotatable bonds (default 5)
max_MolWt = 10000 # Skip any molecules with molecular weights higher than this number

" DIHEDRAL PROTOCOL FOR RDKIT OPTIMIZATION (SLOW SINCE IT SCANS MANY DIHEDRALS) "
nodihedrals = True # turn to True if no dihedral scan is needed
degree = 30 # Amount, in degrees, to enumerate torsions if nodihedrals is False

" PARAMETERS FOR RDKIT OPTIMIZATION "
ff = "MMFF" # force field used in the RDKit optimization. Options: MMFF or UFF
etkdg = False # use new ETKDG knowledge-based method instead of distance geometry also needs to be present in RDKIT ENV
seed = int("062609") #random seed (default 062609) for ETKDG
opt_steps_RDKit = 1000

" DEFAULT PARAMETERS FOR ANI1 and xTB OPTIMIZATION "
opt_steps = 1000 # max number of cycles during optimization
opt_fmax = 0.05 # fmax value to achieve optimization

" DEFAULT PARAMETERS ONLY FOR ANI1 OPTIMIZATION "
constraints = None

" DEFAULT PARAMETERS ONLY FOR xTB OPTIMIZATION "
large_sys = True
STACKSIZE = '1G' #set for large system

" MOLECULES now, for eg., molecule list, for later can use as total no. of molecules it is need in the boltz part to read in specific molecules"
maxnumber = 100000 # max number of molecules to use

" CHARGE DEFAULT IF CANNOT BE CALCULATED"
charge_default = 0
