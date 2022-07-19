import click
import frappe

frappe.init(site="erpnext")
frappe.connect()

@click.command('get-perm')
@click.argument('doctype')
@click.argument('fieldType', required=False)
def get_perm(doctype, **kwargs):
    # SQL query to pull the doc type
    try:
        fieldType = kwargs["fieldType"]
    except:
        fieldType = None
    if doctype and fieldType:
        print(f"Executing get-perm sql query with parameters: doctype:{doctype}, fieldType:{fieldType}")
        print(
            frappe.db.sql(f'''
        SELECT fieldname, label, permlevel
        FROM tabDocField tdf
        WHERE tdf.parent='{doctype}' AND tdf.fieldtype='{fieldType}'
        ''')
        )
        print("Sucessfully executed get-perm sql query")
        return
    if doctype:
        print(f"Executing get-perm sql query with parameters: doctype:{doctype}")
        print(
            frappe.db.sql(f'''
        SELECT fieldname, label, permlevel
        FROM tabDocField tdf
        WHERE tdf.parent='{doctype}'
        ''')
        )
        print("Sucessfully executed get-perm sql query")


@click.command('set-perm')
@click.argument('doctype')
@click.argument('fieldType')
@click.argument('permLevel')
def set_perm(doctype, **kwargs):
    # Validate inputs
    try:
        permLevel = int(kwargs["permLevel"])
        if permLevel < 0 or permLevel > 9:
            raise Exception
    except:
        print("permLevel must be an integer between 0-9")
        return
    try:
        fieldType = kwargs["fieldType"]
    except:
        raise Exception(f"FieldType must be set! fieldType:{fieldType}")

    if doctype and fieldType and permLevel:
        print(f"Executing set-perm sql query with parameters: doctype:{doctype}, fieldType:{fieldType}, permLevel:{permLevel}")
        print(
            frappe.db.sql(f'''
        UPDATE tabDocField tdf
        SET permlevel = {permLevel}
        WHERE tdf.parent='{doctype}' AND tdf.fieldtype='{fieldType}'
        ''')
        )
        print("Sucessfully executed set-perm sql query")

commands = [
    get_perm, set_perm
]
