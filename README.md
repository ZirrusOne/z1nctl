## Z1Nctl

Z1N Command Line Tools for all things ERPNext

### Usage

`bench --site {sitename} get-perm {doctype} {fieldtype(optional)}`

get-perm returns back the permissions for a given `doctype`, and optionally the specific `fieldtype` within that `doctype`.

`bench --site {sitename} set-perm {doctype} {fieldtype} {permlevel}`

set-perm sets the permissions for a given `doctype`, `fieldtype` within that doctype, to the integer `permlevel`.

#### License

MIT
