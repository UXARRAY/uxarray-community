---
title: UXarray Tutorial and Collaboratory
type: demo            # demo | question | workshop | other
authors: [erogluorhan, dylannelson, Sevans711, cmdupuis3]
description: UXarray's tutorial for NCAR's HPC users and collaboratory
uxarray_version: "2026.9.1"
status: active        # active | superseded
related: 
tags: [cesm, mpas]
---

## Purpose

This entry is for UXarray's hybrid tutorial and collaboratory for NCAR's HPC 
users on 10/20/2026. The target audience is scientists and research across NCAR 
labs, partner universities, etc. The intent is for the notebooks to be executed 
on HPC resources, and locally running them might require changes to the code, 
data usage, etc. 

## How to run

The conda environment entitled `uxarray-usclivar` will be reused from UXarray's 
USCLIVAR workshop practicum because it is visible to everyone at the time of the 
event and contains everything (and maybe more) needed. However, this entry 
provides its own `enviornment.yml` file just in case users want to create an 
environment from scratch. 