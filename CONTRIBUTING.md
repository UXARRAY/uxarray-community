# Contributing to UXarray Community

## Asking a question with a notebook

1. If your question is general, start a thread in
   [UXarray Discussions](https://github.com/UXARRAY/uxarray/discussions).
2. If a notebook helps show the problem, either open an issue here using the
   **Question with notebook** template, or add an entry yourself (below) with `type: question`.

## Adding an entry

1. Fork this repository and create a branch.
2. Copy the template into a new dated folder:

   ```bash
   cp -r templates/entry entries/2026/2026-10-14_my-short-slug
   ```

   Folder names must be `YYYY-MM-DD_slug`, where the slug is lowercase letters, digits,
   and hyphens, and the folder sits under the matching year.
3. Fill in the metadata block at the top of `README.md`. Required fields are
   `title`, `type`, `authors`, and `uxarray_version` (quote the version, e.g. `"2026.9.1"`).
4. Pin your environment in `environment.yml`, especially the UXarray version you used.
5. Describe where the data comes from in `data.md`.
6. Install the hooks once, then commit and open a pull request:

   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Guidelines

- **No large data.** Files over 1 MB are rejected by a pre-commit check, and common data
  formats (`*.nc`, `*.grib`, `*.zarr`) are git-ignored. Point to the data instead (a DOI,
  a public URL, an NCAR GDEX or Campaign Storage path, or a small download script). For a
  genuinely tiny sample file, use `git add -f`.
- **Notebook outputs are stripped** on commit by `nbstripout` to keep diffs reviewable.
  If an entry is a polished showcase that should display outputs on GitHub, add its path
  to the `exclude` pattern of the nbstripout hook in `.pre-commit-config.yaml`.
- **Don't edit `INDEX.md`.** It's regenerated automatically after merges.
- **Don't rewrite old entries to new APIs.** Add a new entry and set `status: superseded`
  on the old one, linking to its replacement.

You can validate your entry locally:

```bash
pip install pyyaml
python scripts/build_index.py --check
```
