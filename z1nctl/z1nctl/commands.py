import click
# import frappe

@click.group()
def z1nctl():
    pass

@z1nctl.command('get-perm')
@click.argument('doctype')
@click.argument('fieldtype', required=False)
def get_perm(doctype, fieldtype):
    # SQL query to pull the doc type
    if doctype:
        print(f"Not implemented, should query DB for permissions from doctype: {doctype}")
        # return frappe.db.sql("")

    if doctype and fieldtype:
        print(f"Not implemented, doctype: {doctype}, fieldtype:{fieldtype}")

@z1nctl.command('set-perm')
@click.argument('doctype')
@click.argument('fieldtype')
def set_perm(doctype, fieldtype):
    if doctype:
        print(f"Not implemented, should query DB for permissions from doctype: {doctype}")
    if doctype and fieldtype:
        print(f"Not implemented, doctype: {doctype}, fieldtype:{fieldtype}")

commands = [
    get_perm, set_perm
]

if __name__ == "__main__":
    z1nctl()