# import mdtraj as md
#from adapter import MDTrajAdapter, MDAnalysisAdapter
#import MDAnalysis as mda
from adapters import *
# import adapters
#import numpy as np
import sys

toolkit = sys.argv[1]

# if toolkit == 'MDTraj':
    # trajectory = md.load_pdb('protein.pdb')

    # print('MDTraj')
    # print(10*md.compute_center_of_mass(trajectory))
    # print(10*md.compute_rg(trajectory))
    # traj_analysis = MDTrajAdapter('protein.pdb')
    
    # print(traj_analysis.compute_center_of_mass())
    # print(traj_analysis.compute_radius_of_gyration())
    # traj_analysis.print_filename()
#else:
    # universe = mda.Universe('protein.pdb')

    # print('MDAnalysis')
    # mass_by_frame = np.ndarray(shape=(len(universe.trajectory), 3))
    # for ts in universe.trajectory:
        # mass_by_frame[ts.frame] = universe.atoms.center_of_mass(compound='segments')
    
    # rg_by_frame = np.empty(len(universe.trajectory))
    # for ts in universe.trajectory:
        # rg_by_frame[ts.frame] = universe.atoms.radius_of_gyration()
    
    # print(mass_by_frame)
    # print(rg_by_frame)
    
# if toolkit == 'MDTraj':
    # traj_analysis = MDTrajAdapter('protein.pdb')
# else:
    # traj_analysis = MDAnalysisAdapter('protein.pdb')
traj_analysis = factory.trajectory_factory(toolkit, filename='protein.pdb')
print(traj_analysis.compute_center_of_mass())
print(traj_analysis.compute_radius_of_gyration())
traj_analysis.print_filename()
    
    
    
    
    
    
    
    
    
    