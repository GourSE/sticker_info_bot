#-*- Makefile -*-

ifeq ($(OS),Windows_NT) 
	detected_OS := Windows
	CC ?= gcc
else
	detected_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')

ifeq (, $(shell which gcc))
	CC = clang
else ifeq (, $(shell which clang))
	CC = gcc
else ifeq (, $(shell which cc))

all: error

endif

endif

all: bot

ifeq ($(detected_OS), Linux)

bot: src/main.c

	mkdir -p ~/bin
	$(CC) src/main.c src/colour.h -o ~/bin/sticker_info_bot -Wall
	mkdir -p ~/.local/share/sticker_info_bot
	cp -r -u ./*.py ~/.local/share/sticker_info_bot

ifneq ("$(wildcard ~/.local/share/sticker_info_bot/config.cfg)", "")
	@echo "\n\n\e[32mConfig file exits, will not replace\e[0m"
	@echo "To replace old config, try \e[92mmake replace\e[0m\n\n"
else
	cp -r -u ./config.cfg ~/.local/share/sticker_info_bot
endif


ifeq (, $(shell which pip3))
	pip install -r requirements.txt -U
else
	pip3 install -r requirements.txt -U
endif

	@echo "\ndone"
	@echo "Looking forward to compile into this directory, run \e[92mmake current\e[0m"
	@echo "For removing the program, run \e[92mmake clean\e[0m\n\n"
	@echo "To modify config.cfg, run \e[92msticker_info_bot -c\e[0m or \e[92msticker_info_bot --config\e[0m"

replace: src/main.c

	mkdir -p ~/bin
	$(CC) src/main.c src/colour.h -o ~/bin/sticker_info_bot -Wall
	mkdir -p ~/.local/share/sticker_info_bot
	cp -r -u ./*.py ./config.cfg ~/.local/share/sticker_info_bot

ifeq (, $(shell which pip3))
	pip install -r requirements.txt -U
else
	pip3 install -r requirements.txt -U
endif

	@echo "\ndone"
	@echo "Looking forward to compile into this directory, run \e[92mmake current\e[0m"
	@echo "For removing the program, run \e[92mmake clean\e[0m\n\n"
	@echo "To modify config.cfg, run \e[92msticker_info_bot -c\e[0m or \e[92msticker_info_bot --config\e[0m\n\n"

current: src/main.c
	$(CC) src/main.c src/colour.h -o sticker_info_bot -Wall

	@echo "\ndone"

clean:
	rm -f ~/bin/sticker_info_bot
	rm -f -r ~/.local/share/sticker_info_bot
	rm -f sticker_info_bot

	@echo "\ndone"

endif