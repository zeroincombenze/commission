Le formule sono testi con istruzioni python che devono restituire l'importo della
provvigione nella variabile ``result``.

Le istruzioni possono contente condizioni con struttura <if CONDITION elif CONDITION else>.

La condizione CONDITION può riferirsi ai valori della riga fattura o della riga ordine
Questo è un esempio:

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

Nell'esempio, l'importo della provvigione dipende dal flag ``purchase_ok`` (può essere
acqistato) e dalla categoria prodotto e dal riferimento cliente.
Quindi la formula può contenere qualsiasi riferimento a:

* Testata Ordine / Fattura
* Riga Ordine / Fattura
* Prodotto
* Cliente
* Altro
