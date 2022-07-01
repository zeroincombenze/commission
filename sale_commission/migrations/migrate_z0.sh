#/bin/bash
DB=$(psql -Uodoo10 -Atl|grep "|odoo10|"|awk -F"|" '{print $1}'|sort|tr "\n" " ")
for db in $DB; do
    echo psql -Uodoo10 $db -c "update ir_module_module set latest_version='10.0.2.0.0' where name='sale_commission';"
    psql -Uodoo10 $db -c "update ir_module_module set latest_version='10.0.2.0.0' where name='sale_commission';"
done
