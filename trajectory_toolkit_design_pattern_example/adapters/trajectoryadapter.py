from abc import ABC, abstractmethod
class TrajectoryAdapter(ABC):
    
    @abstractmethod
    def compute_center_of_mass(self):
        pass
        
    @abstractmethod
    def compute_radius_of_gyration(self):
        pass
        
    def print_filename(self):
        print (self.filename)