"""
This script is used to evaluate your submission to the competition.
It assumes the script where you implemented your ActorModule is in the same folder and is named "tuto_competition.py".
It also assumes your ActorModule implementation is named "MyActorModule".
When using this script, don't forget to set "SLEEP_TIME_AT_RESET" to 0.0 in config.json.
"""

from copy import deepcopy

from tmrl.networking import RolloutWorker
from tmrl.util import partial
from tmrl.envs import GenericGymEnv
import tmrl.config.config_objects as cfg_obj

from .tuto_competition import MyActorModule  # change this to match your ActorModule name


# rtgym environment class (full TrackMania Gym environment):
env_cls = partial(GenericGymEnv, id="real-time-gym-v0", gym_kwargs={"config": cfg_obj.CONFIG_DICT})

# Device used for inference on workers (change if you like but keep in mind that the competition evaluation is on CPU)
device_worker = 'cpu'

try:
    from .tuto_competition import obs_preprocessor
except Exception as e:
    obs_preprocessor = cfg_obj.OBS_PREPROCESSOR


if __name__ == "__main__":
    rw = RolloutWorker(env_cls=env_cls,
                       actor_module_cls=MyActorModule,
                       device=device_worker,
                       obs_preprocessor=obs_preprocessor,
                       standalone=True)
    rw.run()
