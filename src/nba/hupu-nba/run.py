#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-22 17:49:00

import time
from nba.board import Board
from nba.hupuapi import APIClient
from nba.controls import Controller


def main():
    brd = Board()
    api = APIClient()
    ctr = Controller(brd, api)
    try:
        ctr.start()
    except Exception as e:
        pass
    finally:
        brd.exit()


if __name__ == '__main__':
    main()
