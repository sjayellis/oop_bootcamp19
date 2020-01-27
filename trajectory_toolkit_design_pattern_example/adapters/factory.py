# from adapter import MDTrajAdapter, MDAnalysisAdapter
from .trajectoryadapter import TrajectoryAdapter

_toolkits = {}

def register(toolkit_name, toolkit_class):
    if not issubclass(toolkit_class, TrajectoryAdapter):
        raise TypeError('{0} is not a TrajectoryAdapter'.format(toolkit_class))
    _toolkits[toolkit_name] = toolkit_class

def trajectory_factory(trajectory_toolkit, **kwargs):
    # if trajectory_toolkit == 'MDTraj':
        # traj_analysis = MDTrajAdapter(kwargs['filename'])
    # elif trajectory_toolkit == 'MDAnalysis':
        # traj_analysis = MDAnalysisAdapter(kwargs['filename'])
    # else:
        # raise TypeError('Toolkit not found')
    # traj_toolkits = {'MDTraj': MDTrajAdapter, 'MDAnalysis': MDAnalysisAdapter}
    
    if trajectory_toolkit not in _toolkits.keys():
       raise TypeError('Toolkit not found')
    
    
    traj_analysis = _toolkits[trajectory_toolkit](kwargs['filename'])
    
    return traj_analysis
    
    
    
    
    
    
    
    
    
    
    
    
    