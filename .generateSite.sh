#!/bin/bash

## This is a small script for those interested in generating the
## gh-pages site locally to check if the site works before pushing up
## to the GitHub repo, where the site will then become live (anyone on
## the internet can see it).

## You will need to install jekyll in order to run this command.

## You run this script by typing in the terminal/commandline:

## sh ./.generateSite.sh

jekyll serve --watch

## You cancel this script by pressing Ctrl-C
