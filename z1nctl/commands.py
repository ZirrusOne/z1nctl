import click
import frappe
from psycopg2 import sql


@click.command('get-perm')
@click.argument('doctype')
@click.argument('fieldType', required=False)
def get_perm(doctype, **kwargs):
    # SQL query to pull the doc type
    print(frappe.get_hooks())
    try:
        fieldType = kwargs["fieldType"]
    except:
        fieldType = None
    if doctype and fieldType:
        print(f"Executing get-perm sql query with parameters: doctype:{doctype}, fieldType:{fieldType}")
        frappe.db.sql('''
        SELECT fieldname, label, permlevel
        FROM tabDocField tdf
        WHERE tdf.parent={doctype} AND tdf.fieldtype={fieldType}
        ''').format(
            doctype = sql.Identifier(doctype),
            fieldType = sql.Identifier(fieldType)
        )
        print("Sucessfully executed get-perm sql query")
        return
    if doctype:
        print(f"Executing get-perm sql query with parameters: doctype:{doctype}")
        frappe.db.sql('''
        SELECT fieldname, label, permlevel
        FROM tabDocField tdf
        WHERE tdf.parent='{doctype}'
        ''').format(
            doctype = sql.Identifier(doctype)
        )
        print("Sucessfully executed get-perm sql query")


@click.command('set-perm')
@click.argument('doctype')
@click.argument('fieldType')
@click.argument('permLevel')
def set_perm(doctype, fieldType, permLevel):
    # Validate inputs
    try:
        permLevel = int(permLevel)
        if permLevel < 0 or permLevel > 9:
            raise Exception
    except:
        print("permLevel must be an integer between 0-9")
        return

    if doctype and fieldType and permLevel:
        print(f"Executing set-perm sql query with parameters: doctype:{doctype}, fieldType:{fieldType}, permLevel:{permLevel}")
        frappe.db.sql('''
        UPDATE tabDocField tdf
        SET permlevel = {permLevel}
        WHERE tdf.parent={doctype} AND tdf.fieldtype={fieldType}
        ''').format(
            permLevel = sql.Literal(permLevel),
            doctype = sql.Identifier(doctype),
            fieldType = sql.Identifier(fieldType)
        )
        print("Sucessfully executed set-perm sql query")

commands = [
    get_perm, set_perm
]
