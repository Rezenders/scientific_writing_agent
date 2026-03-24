---
name: find-annotations
description: Use when you need an inventory of all open inline annotations in the manuscript — todos, revision markers, and author comments — before a writing session or submission.
---

# Find Annotations

Scans all `.tex` files for inline annotation commands and reports them grouped by type, with file and line number.

## Standard Annotation Commands

| Command | Meaning |
|---|---|
| `\todo{...}` | Open task / reminder |
| `\revise{...}` | Content needing revision |
| `\red{...}` | Highlighted warning |

<!-- ADD YOUR AUTHORS
     If your project defines per-author annotation commands (e.g. \alice{...}, \bob{...}),
     add them to the table above and to the grep command below.
     Example:
       \alice{...}  — Alice's inline comments
       \bob{...}    — Bob's inline comments
-->

## Workflow

Run the following search across all `.tex` files in the repository root:

```bash
grep -rn --include="*.tex" \
  -e '\\todo{' \
  -e '\\revise{' \
  -e '\\red{' \
  . | sort
# ADD YOUR AUTHORS: append -e '\\authorname{' for each author command
```

Then present results grouped by annotation type, showing:
- File name and line number
- Full annotation content (extract the `{...}` argument)

## Output Format

```
### \todo  (N open)
- introduction.tex:42  — "add citation for claim about X"
- approach.tex:118     — "clarify the role of the resolution model here"

### \revise  (N open)
- evaluation.tex:73    — "this paragraph is too vague"

### \red  (N open)
- approach.tex:55  — "CHECK: is this still accurate after last refactor?"

### Author comments  (N open)
- [author-command].tex:204  — "..."

---
Total: N annotations across M files.
```

If no annotations are found, report: **No open annotations — manuscript is clean.**

## Notes

- Archive / scratch files that are not `\input`'d in the main document should be flagged separately.
- Staging files for temporarily removed content should be included in the scan, as they may return to the main flow.
