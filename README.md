## Installation

1. Create Virtual environment
```sh
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies
```sh
pip3 install -r requirements.txt
```

## Use

See options with: `python3 -m src.prompt.cli --help`

Client thats wait pin inputs: `python3 -m src.prompt.init_wiz_controller`

## Configure environment

***Config crontab task to init wiz controller on startup so***

1. Enter to `crontab -e`

```sh
@reboot /home/[local-user]/command/wiz-controller-init.sh 2>&1 | while IFS= read -r line; do echo "[$(date '+\%Y-\%m-\%d \%H:\%M:\%S')] $line"; done >> /home/[local-user]/data/wiz_controller.log
```

2. Create a command

```sh
touch /home/[local-user]/command/wiz-controller-init.sh
```

3. Put this content to execute init

```sh
#!/bin/bash

# Wait for intenet conectivity
for i in {1..30}; do
    if ping -c1 8.8.8.8 &>/dev/null; then
        echo "Connected to internet"
        break
    else
        echo "Waiting for internet connection..."
        sleep 1
    fi
done

# Navigate to the project
cd ~/projects/wiz-controller || exit 1

# Activate the virtual environment
source .venv/bin/activate

# Print date and time before running
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Initializing wiz controller..."

# Execute the command
python3 -m src.prompt.init_wiz_controller
```

***Config crontab task to execute discovery each 15 minutes***

1. Enter to `crontab -e`

```sh
*/15 * * * * /home/[local-user]/command/wiz-controller-discovery.sh 2>&1 | while IFS= read -r line; do echo "[$(date '+\%Y-\%m-\%d \%H:\%M:\%S')] $line"; done >> /home/[local-user]/data/wiz_controller.log
```

2. Create a command

```sh
touch /home/[local-user]/command/wiz-controller-discovery.sh
```

3. Put this content to execute discovery

```sh
#!/bin/bash

# Navigate to the project
cd ~/projects/wiz-controller || exit 1

# Activate the virtual environment
source .venv/bin/activate

# Print date and time before running
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Running discovery..."

# Execute the command
python3 -m src.prompt.cli discovery --broadcast_space 192.168.0.255
```

***Set shutdown permission***

1. Connect to raspberry by SSH and execute:

```sh
sudo visudo
```

2. Go to end line of the file and put the next command

```
pi ALL=NOPASSWD: /usr/sbin/shutdown
```