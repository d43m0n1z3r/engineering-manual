# Generation Report

- Input: `../manual.md`
- Output: `../engineering-manual-1.1.0`
- Original preserved at: `source/manual.md`
- Provenance: `source/manual.md` is the frozen original generation input
  (`sha256:673b42f99b70319c8a1366c2178b39606d8302025eaac4f4443c19201acd0143`),
  not a live mirror of this repository. Post-generation changes are tracked in
  `CHANGELOG.md`; recovery from `source/manual.md` restores the generation
  baseline only.
- Task and role cards are derived copies of source tables.

## Counts

- Skill category files: 23
- Unique task IDs detected: 108
- Task cards generated: 108
- Role cards generated: 12

## Warnings

- No structural warnings detected. This is not a guarantee that every generated file is semantically complete.

## Required review before use

1. Compare the generated files with `source/manual.md`.
2. Review task cards alongside their source phase and security sections.
3. Check any large files and split them if needed.
4. Review preserved original cross-references using `XREF.md`.
5. Resolve policy conflicts with the appropriate human authority.
6. Do not treat generation as proof that tests or controls were run.

## Known limitations

- The parser expects the heading and table style of the original manual.
- Task cards are generated only from recognizable task table rows.
- The original task rows remain in source section files; task cards are derived convenience views and must be regenerated or updated when their source changes.
- Original prose references such as `Part 8` and `§2.3` are preserved, not rewritten.
- Character count is only a rough size signal, not a token count.
- The program does not verify whether the manual's technical claims, standard editions, or security policies are current.
