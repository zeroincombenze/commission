The formulas are python text statements which have to return the commission amount
in ``result`` variable.

Statement can contains <if CONDITION elif CONDITION else> structure.

The CONDITION refers to invoice line or sale order line values.
This is a formula example:

::

    if line.product_id.purchase_ok:
        result = line.price_subtotal * 10.0 / 100
    elif line.product_id.categ_id.name == "Special":
        result = line.price_subtotal * 5.0 / 100
    elif (
        (line._name == 'account.invoice.line' and line.partner_id.ref == "Special") or
        (line._name == 'sale.order.line' and line.order_id.partner_id.ref == "Special")
    ):
        result = line.price_subtotal * 15.0 / 100
    else:
        result = line.price_subtotal * 20.0 / 100

In above example, commission amount depends on product flag ``purchase_ok`` (can be
purchased) and product category value and customer reference.
So formula can test any value of:

* Sale Order / Account Invoice header
* Sale Order / Account Invoice line
* Product
* Customer
* Others

Here you can find the most common field:

+-----------------------+---------------------------------+-------------------------------+
| Description           | Invoice technical name          | Sale order  technical name    |
+-----------------------+---------------------------------+-------------------------------+
| Total Amount          | line.invoice_id.amount_total    | line.order_id.amount_total    |
+-----------------------+---------------------------------+-------------------------------+
| Customer Name         | line.invoice_id.partner_id.name | line.order_id.partner_id.name |
+-----------------------+---------------------------------+-------------------------------+
| Payment Terms         | line.invoice_id.payment_term_id | line.order_id.payment_term_id |
+-----------------------+---------------------------------+-------------------------------+
| Salesman              | line.invoice_id.user_id         | line.order_id.user_id         |
+-----------------------+---------------------------------+-------------------------------+
| Discount (%)          | line.discount                   | line.discount                 |
+-----------------------+---------------------------------+-------------------------------+
| Line total            | line.price_subtotal             | line.price_subtotal           |
+-----------------------+---------------------------------+-------------------------------+
| Product Name          | line.product_id.name            | line.product_id.name          |
+-----------------------+---------------------------------+-------------------------------+
| Product Category Name | line.product_id.categ_id.name   | line.product_id.categ_id.name |
+-----------------------+---------------------------------+-------------------------------+
| Quantiy               | line.quantity                   | line.product_uom_qty          |
+-----------------------+---------------------------------+-------------------------------+
