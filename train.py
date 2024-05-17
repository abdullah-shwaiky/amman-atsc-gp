import os
import sys

import fire


if "SUMO_HOME" in os.environ:
    tools = os.path.join(os.environ["SUMO_HOME"], "tools")
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")

from linear_rl.true_online_sarsa import TrueOnlineSarsaLambda

from sumo_rl import uni_area


def run(use_gui=False, episodes=10):
    fixed_tl = False
    reward_fns = ["average-speed"]

    for reward in reward_fns:
        env = uni_area(out_csv_name=f"outputs/uni_area/{reward}/{reward}", use_gui=use_gui, yellow_time=2, fixed_ts=fixed_tl,reward_fn=reward)
        env.reset()

        agents = {
            ts_id: TrueOnlineSarsaLambda(
                env.observation_spaces[ts_id],
                env.action_spaces[ts_id],
                alpha=0.0001,
                gamma=0.95,
                epsilon=0.05,
                lamb=0.1,
                fourier_order=1,
            )
            for ts_id in env.agents
        }

        for ep in range(1, episodes + 1):
            print('episode reset - episode',ep)
            obs = env.reset()
            done = {agent: False for agent in env.agents}
            while len(env.agents):
                actions = {ts_id: agents[ts_id].act(obs[0][ts_id]) for ts_id in obs[0].keys()}

                next_obs, r, terminated, truncated, info = env.step(actions=actions)
                for ts_id in next_obs.keys():
                    agents[ts_id].learn(
                        state=obs[0][ts_id], action=actions[ts_id], reward=r[ts_id], next_state=next_obs[ts_id], done=done[ts_id]
                    )
                    obs[0][ts_id] = next_obs[ts_id]
                print(len(env.agents))

        env.close()


if __name__ == "__main__":
    fire.Fire(run)
