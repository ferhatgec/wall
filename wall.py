#!/usr/bin/env python3
#
# MIT License
#
# Copyright (c) 2021 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
#
# wall - get & set pseudo-randomly selected wallpapers from unsplash (executable)
#
# github.com/ferhatgec/wall


from os import environ, system
from sys import argv
from pathlib import Path

from requests import get

unsplash = 'https://source.unsplash.com/random/{res}/?'


class Wall:
    def __init__(self):
        self.screen_res = '2048x1152'
        self.home_path = f'{Path.home()}/wall/'

    def get_image(self):
        if not Path(self.home_path).exists():
            Path(self.home_path).mkdir(exist_ok=True)

        with open(f'{self.home_path}wallpaper.jpeg', 'wb') as f:
            f.write(get(unsplash.format(res=self.screen_res)).content)

        if Path(f'{self.home_path}wallpaper.jpeg').exists():
            self.set_wallpaper()

    def set_wallpaper(self):
        desktop_session = environ.get("DESKTOP_SESSION").lower()

        if desktop_session in ['pop', 'gnome', 'cinnamon', 'mate']:
            system(f'gsettings set org.gnome.desktop.background picture-uri \'file://{self.home_path}wallpaper.jpeg\'')
        else:
            print('Uuh! There\'s another desktop env.')


if len(argv) >= 2:
    if argv[1] == 'help':
        print('Wall - Wall, set wallpaper that pseudo-randomly selected from Unsplash',
              '---',
              f'{argv[0]} category another_category', sep='\n')

        exit(1)

    for index, arg in enumerate(argv):
        if index == 0:
            continue

        unsplash += f'{arg},'

init = Wall()
init.get_image()
