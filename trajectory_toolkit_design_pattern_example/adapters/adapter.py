# from abc import ABC, abstractmethod
import mdtraj as md
import MDAnalysis as mda
import numpy as np
from .factory import register
from .trajectoryadapter import TrajectoryAdapter
        
class MDTrajAdapter(TrajectoryAdapter):
    def __init__(self, filename):
        self.filename = filename
        self._trajectory = md.load_pdb(filename)
        print('MDTraj')
        
    
    def compute_center_of_mass(self):
        return 10*md.compute_center_of_mass(self._trajectory)
    
    def compute_radius_of_gyration(self):
        return 10*md.compute_rg(self._trajectory)

class MDAnalysisAdapter(TrajectoryAdapter):
    def __init__(self, filename):
        self.filename = filename
        self._universe = mda.Universe(filename)
        print('MDAnalysis')
    
    def compute_center_of_mass(self):
        mass_by_frame = np.ndarray(shape=(len(self._universe.trajectory), 3))
        for ts in self._universe.trajectory:
            mass_by_frame[ts.frame] = self._universe.atoms.center_of_mass(compound='segments')
        return mass_by_frame
        
    def compute_radius_of_gyration(self):
        rg_by_frame = np.empty(len(self._universe.trajectory))
        for ts in self._universe.trajectory:
            rg_by_frame[ts.frame] = self._universe.atoms.radius_of_gyration()
        return rg_by_frame
    
    
    
register('MDTraj', MDTrajAdapter)
register('MDAnalysis', MDAnalysisAdapter)








