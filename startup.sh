#!/bin/bash

nohup python3 -u douyin_remove_watermark.py >& log_douyin_remove_watermark.log &
tail -f -n 100 log_douyin_remove_watermark.log