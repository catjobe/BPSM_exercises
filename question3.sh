#!/bin/bash

grep -Ew "^Jan" example_people_data.tsv | wc -l
