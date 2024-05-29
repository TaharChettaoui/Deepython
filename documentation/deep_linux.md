### Linux commands 
| Command |  Description |
|---|---|
| nvidia-smi   |  Current occupation of all available gpus | 
| ps up -pid  |  Information about a process by its id | 
| taskset -c 0,1,2,3,4 python3 | restrict the number of used cores  | 


### Conda envs
| Command |  Description |
|---|---|
| conda create --name ENV_NAME python=3.7  | Create a new environment | 
| conda activate project-env  | Activate your new environment | 
| conda env remove -n ENV_NAME | Removing Conda environment | 
| conda env list | List all existing environments |
| conda list  | display all packages in this environment | 


conda activate project-env

### Tmux
Allows multiple terminal sessions to be accessed simultaneously in a single window. It can also be used to detach processes from their controlling terminals,
allowing SSH sessions to remain active without being visible.  

| Command |  Description |
|---|---|
| tmux new -s mysession |	Start a new session with the name mysession |
| tmux kill-ses -t mysession |	kill/delete session mysession |
| tmux a -t mysession |	Attach to a session with the name mysession |
| tmux ls |	Show all sessions |

https://tmuxcheatsheet.com/  
