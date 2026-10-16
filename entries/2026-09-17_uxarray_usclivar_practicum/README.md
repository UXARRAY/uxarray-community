---
title: UXarray's USCLIVAR Practicum
type: tutorial            # demo | question | workshop | tutorial | other
authors: [erogluorhan, Sevans711]
description: UXarray's half day practicum for USCLIVAR's Broadening Earth System Research Across Scales with High-Resolution Modeling Workshop
uxarray_version: "2026.9.1"
status: active        # active | superseded
related: https://usclivar.org/meetings/high-resolution-modeling
tags: [cesm, usclivar, mesaclip]
---

## Purpose

This entry is for UXarray's half day practicum event for USCLIVAR's Broadening 
Earth System Research Across Scales with High-Resolution Modeling Workshop
on 9/17/2026. The MESACLIP dataset is used for this event. The intent is for 
the notebooks to be executed on HPC resources because of how large the dataset 
is. While possible local configuration through online GDEX data access is added 
into the notebooks, running them locally might require changes to the code,
data usage, etc.

## How to run

The conda environment entitled `uxarray-usclivar`was made visible to NCAR's HPC 
users at the time of the event and contained everything needed (it might no 
longer be available depending on when you're reading this). However, this entry
provides its own `enviornment.yml` file just in case users want to create an
environment from scratch.