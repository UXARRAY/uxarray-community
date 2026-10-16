# UXarray Community

A shared space between the [UXarray](https://github.com/UXARRAY/uxarray) team and its
user community. Here you'll find demonstration notebooks from the team, notebooks users put
together to ask questions or report behavior, workshop and tutorial material, and anything
else that comes out of working together.

Everything is organized by date. Browse the full catalog in **[INDEX.md](INDEX.md)**, or read
the notebooks with their rendered outputs on the
**[community site](https://uxarray.github.io/uxarray-community/)**.

## Layout

```
entries/
└── YYYY-MM-DD_short-slug/
    ├── README.md          # metadata + description of the entry
    ├── data.md            # where to get the data used (data is not stored here)
    ├── environment.yml    # pinned environment, including the UXarray version
    └── notebooks/         # *.ipynb notebooks
        └── *.ipynb

```

### Entries

Each dated folder is a self-contained **entry**. The date is when the entry was created
(or when the event it belongs to happened) and doesn't change afterward.

Every entry's `README.md` starts with a small metadata block, and the rest of the README
can contain any more information the authors think would be useful. For example:

```yaml
---
title: Zonal mean on MPAS output
type: demo            # demo | question | workshop | other
authors: [github-username]
description: One sentence on what this entry is for
uxarray_version: "2026.9.1"
status: active        # active | superseded
related: https://github.com/UXARRAY/uxarray/discussions/...
tags: [mpas, zonal-mean]
---

## Purpose

Why this entry exists and who it's for.

<More text as needed...>
```

`INDEX.md` is generated from these blocks automatically, so please don't edit it by hand.

## Running an entry

Each entry pins its own environment, so notebooks stay runnable even as UXarray evolves:

```bash
cd entries/2026-10-12_some-entry
conda env create -f environment.yml
conda activate <env-name-from-file>
jupyter lab
```

Older entries may target older UXarray versions on purpose. Entries marked
`status: superseded` have been replaced by a newer approach, usually linked in their README.

## Contributing

Questions, demos, and fixes are all welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).
For general questions that don't need a notebook, please use
[UXarray Discussions](https://github.com/UXARRAY/uxarray/discussions).

## License

Apache 2.0, the same as UXarray. See [LICENSE](LICENSE).
