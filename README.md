# 🤖 !BigBot

Big bot bigs up the [W3BBIE Server](https://discord.gg/ZYKGW892)

## 🧩 Attributions
* [Bot Concept](https://discordapp.com/users/bigtrav.eth#4250)
* [Bot Collaborator, Refactor, Additional Design](https://discordapp.com/users/jackjackjack#7167)
* [Bot Keeper](https://discordapp.com/users/Kyn#3709)

## 🛠 Installation

### 🐍 Python3
* Do I have Python3?
	- Open your terminal window / ide
	-  `python3 --version`
* I do not have Python3
	- *Install Python3, See next section*

### 🤔 Where Do I Get Python3?

* **🔗 https://realpython.com/installing-python/**
* **🔗https://opensource.com/article/19/5/python-3-default-mac**
* [Python for Windows](https://www.python.org/downloads/windows/)

*Note: there are other links, methods as well. just run a quick itnernet search, or ask ChatGPT)*

### ✅ Requirements

* Install via the `requirements.txt` file
	-  `pip install -r requirements.txt`
* Install via Poetry Package Manager
	- `poetry install`

### 🔓 🌍 The Environement File
* Find the `env_example` file, it is in the `/big_bot/` sub-directoryroot directory of the project
	- `cd ~ big_bot/big_bot`
	- `open env_example` (in an IDE or Text Editor)
* Follow the instructions locatated withing the file to update with proper credentials, and on how to save the file as a hidden file. 

### 🚀 Launching The Bot
* Run the script in the `big_bot/big_bot` directory
	- `cd ~ big_bot/big_bot`
	- `poetry shell`
		+ not neccessary if you installed via `requirements.txt`
	- `python3 app.py`
