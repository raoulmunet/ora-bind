# ora-bind

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

## License

MIT.
