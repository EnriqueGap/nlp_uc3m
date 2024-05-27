# Regular Expressions
Used in patter search in string characters.

In python we use library `re`
## Pattern definition
Metacharacters: `. ^ $ * + ? { } [ ] \\ | ( )`

Escape characters:

Code |	Mean
-----| ------
\d |	numeric
\D |	non numeric
\s |	white space
\S |	non withe space
\w |	alphanumeric
\W |	non alphanumeric
.  |	any character

Repetitive patterns

Code |  Mean
 --- | ---
`*` | Repeat zero or more, like `{0,}`.
`+` | Repeat one  or more, like `{1,}`.
`?` | Repeat zero o one, like `{0,1}`.
`{n}` |	Repeat exactly n times.
`{n,}` | Repeat at least  n times.
`{n,m}` | Repeat between n, m times.

Delimiters

Code | Mean
 --- | ---
`^` | Text starts
`$` | Text ends
`\b` | At the beggining (end) of the word
`\B` | Is not at the beggining (end) of the word

Exclusion patterns: `[^ ]`
