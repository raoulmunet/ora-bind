# ora-bind

[![tests](https://github.com/raoulmunet/ora-bind/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/ora-bind/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Convert common hard-coded Oracle SQL literals into bind variables and emit a parameter map.

> **Oracle compatibility**
>
> | Oracle version | Support |
> |---|---|
> | Oracle Database 19c | ✅ Supported |
> | Oracle Database 23ai | ✅ Supported |
> | Oracle AI Database 26ai | ✅ Supported |
>
> The current release works offline on SQL text and uses bind syntax that is valid across these releases. Version-specific literal syntax that is not recognized is left unchanged.

## Why use it?

Bind variables can reduce hard parsing, improve cursor reuse and make application SQL safer to parameterize. This tool is a **conversion assistant**, not an automatic deployment rewrite.

## Installation

```bash
python -m pip install "git+https://github.com/raoulmunet/ora-bind.git"
```

## Usage

```bash
ora-bind examples/customer_query.sql
ora-bind examples/customer_query.sql --format json
cat query.sql | ora-bind -
```

Input:

```sql
SELECT *
FROM customers
WHERE customer_id = 123
  AND status = 'ACTIVE'
  AND created_date >= DATE '2026-01-01';
```

Output:

```sql
SELECT *
FROM customers
WHERE customer_id = :b1
  AND status = :b2
  AND created_date >= :b3;
```

Parameter map:

```text
:b1 = 123
:b2 = 'ACTIVE'
:b3 = DATE '2026-01-01'
```

## Scope and limitations

The tool intentionally avoids rewriting literals inside comments and quoted identifiers. It handles common string, numeric and ANSI DATE literals. It does not infer application-language datatypes, execute SQL, or decide whether every literal should be bound.

## Oracle Dev Tools family

This repository is part of the **Oracle Dev Tools** suite: small, composable developer utilities designed around Oracle Database 19c, 23ai and 26ai.

| Area | Tools |
|---|---|
| Foundation | [ora-core](https://github.com/raoulmunet/ora-core) |
| SQL analysis | [ora-impact](https://github.com/raoulmunet/ora-impact) · [ora-plan](https://github.com/raoulmunet/ora-plan) · [ora-lineage](https://github.com/raoulmunet/ora-lineage) · [ora-lint](https://github.com/raoulmunet/ora-lint) · [ora-sql-diff](https://github.com/raoulmunet/ora-sql-diff) · [ora-sql-complexity](https://github.com/raoulmunet/ora-sql-complexity) · [ora-join-viz](https://github.com/raoulmunet/ora-join-viz) · [ora-bind](https://github.com/raoulmunet/ora-bind) |
| Data & operations | [ora-doc](https://github.com/raoulmunet/ora-doc) · [ora-data-quality](https://github.com/raoulmunet/ora-data-quality) · [ora-csv-loader](https://github.com/raoulmunet/ora-csv-loader) · [ora-etl-log](https://github.com/raoulmunet/ora-etl-log) · [ora-migration-check](https://github.com/raoulmunet/ora-migration-check) · [ora-errors](https://github.com/raoulmunet/ora-errors) · [ora-schema-explorer](https://github.com/raoulmunet/ora-schema-explorer) |
| PL/SQL analysis | [ora-exception-flow](https://github.com/raoulmunet/ora-exception-flow) · [ora-call-graph](https://github.com/raoulmunet/ora-call-graph) · [ora-dead-code](https://github.com/raoulmunet/ora-dead-code) |

## License

MIT.
