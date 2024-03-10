================================================
|icon| Sales commissions/Provvigioni 10.0.11.0.6
================================================

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/commission/10.0/sale_commission/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| This module allows to define sales agents with their commissions and assign
them in customers and sales orders.

You can then make the settlements of these commissions, and generate the
corresponding supplier invoices to pay their commissions fees.

You can define which base amount is going to be taken into account: net amount
(based on margin) or gross amount (line subtotal amount)


|it| Modulo per gestione provvigioni agenti

Si può assegnare un agente in anagrafica cliente per permettere di calcolare
la provvigione nelle righe degli ordini di vendita e di conseguenza nelle
relative fatture.

I dati sono modificabili per ogni riga del documento.

Si possono generare le liquidazioni agenti per il pagamento delle stesse.
La liquidazione può essere calcolata sulla vendita oppure sul pagato.

I provvigioni sono calcolate al prezzo o al margine del prodotto.


|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/commission/10.0/sale_commission/static/description/description.png


Features | Caratteristiche
--------------------------

+------------------------------------------------+---------------------+-------------------------------+-------------------------------------+
| Description | Descrizione                      | OCA                 | Z0incombenze(R)               | Note(s)                             |
+------------------------------------------------+---------------------+-------------------------------+-------------------------------------+
| Commission type | Tipi provvigione             | Fixed or by section | Fissa o per fasce             | More with *sale_commission_formula* |
+------------------------------------------------+---------------------+-------------------------------+-------------------------------------+
| Invoice state | Stato fattura                  | Open or paid        | Fatturato o pagato            |                                     |
+------------------------------------------------+---------------------+-------------------------------+-------------------------------------+
| Amount type | Tipo importo                     | Gross or net        | Margine o prezzo              |                                     |
+------------------------------------------------+---------------------+-------------------------------+-------------------------------------+
| Settlement date to | Data liquidazione         | Day to excluded     | Incluso sino a                | Comportamento diverso               |
+------------------------------------------------+---------------------+-------------------------------+-------------------------------------+
| Recalculate commission | Ricalcolo provvigioni | Draft document      | Documenti in bozza o validati | Comportamento diverso               |
+------------------------------------------------+---------------------+-------------------------------+-------------------------------------+
| Commission type menu | Menù tipo provvigione   | unprotect           | Solo manager                  | Comportamento diverso               |
+------------------------------------------------+---------------------+-------------------------------+-------------------------------------+
| Settlements analisys | Analisi liquidazioni    | Account report      | Account BI                    | Comportamento diverso               |
+------------------------------------------------+---------------------+-------------------------------+-------------------------------------+



Configuration | Configurazione
------------------------------

☰ Sales > Commission Management > Commission types

☰ Sales > Commission Management > Agents

☰ Sales > Customers > Customers > Assign customers to agents



Usage | Utilizzo
----------------

☰ Invoicing > Customer Invoices

☰ Sales > Commission Management > Settle Commission

Reporting

☰ Sales > Commission Management > Settlements

☰ Invoicing > Reports > Businsess Intelligence > Commission analysis



Getting started | Primi passi
=============================

|Try Me|


Prerequisites | Prerequisiti
----------------------------

* python 2.7+ (best 2.7.5+)
* postgresql 9.2+ (best 9.5)

::

    cd $HOME
    # Follow statements activate deployment, installation and upgrade tools
    cd $HOME
    [[ ! -d ./tools ]] && git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -pUT
    source $HOME/devel/activate_tools



Installation | Installazione
----------------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instructions are just an  | Istruzioni di esempio valide solo per    |
| example; use on Linux CentOS 7+ | distribuzioni Linux CentOS 7+,           |
| Ubuntu 14+ and Debian 8+        | Ubuntu 14+ e Debian 8+                   |
|                                 |                                          |
| Installation is built with:     | L'installazione è costruita con:         |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://zeroincombenze-tools.readthedocs.io/>`__ |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| $HOME/10.0 |
+----------------------------------------------------------------------------+

::

    # Odoo repository installation; OCB repository must be installed
    deploy_odoo clone -r commission -b 10.0 -G zero -p $HOME/10.0
    # Upgrade virtual environment
    vem amend $HOME/10.0/venv_odoo



Upgrade | Aggiornamento
-----------------------

::

    deploy_odoo update -r commission -b 10.0 -G zero -p $HOME/10.0
    vem amend $HOME/10.0/venv_odoo
    # Adjust following statements as per your system
    sudo systemctl restart odoo



Support | Supporto
------------------

|Zeroincombenze| This module is supported by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__



Get involved | Ci mettiamo in gioco
===================================

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/zeroincombenze/commission/issues>`_.

In case of trouble, please check there if your issue has already been reported.



Proposals for enhancement
-------------------------

|en| If you have a proposal to change this module, you may want to send an email to <cc@shs-av.com> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.

|it| Se hai proposte per migliorare questo modulo, puoi inviare una mail a <cc@shs-av.com> per un iniziale contatto.



ChangeLog History | Cronologia modifiche
----------------------------------------

10.0.1.0.7 (2024-03-10)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] head_agent moved into sale_commission_areamanager module
* [IMP[ agent_id moved into sale_commision_bi module
* [IMP] Aligned to OCA module | Allineaato al modulo OCA
* [IMP] Commission BI | Business Intelligence delle provvigioni
* [IMP] Settlement lines | Menù con righe liquidazioni
* [QUA] Test coverage 83% (458: 80+378) [11 TestPoints] - quality rating 54 (target 100)

10.0.1.0.6 (2024-02-07)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Sale order cannot update commisions
* [QUA] Test coverage 70% (677: 204+473) [11 TestPoints] - quality rating 45 (target 100)

10.0.1.0.5 (2024-02-05)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Integration with OCA module
* [IMP] sale_agent_id on invoice header
* [QUA] Test coverage 72% (589: 163+426) [11 TestPoints] - quality rating 47 (target 100)

10.0.1.0.4 (2023-04-06)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Error in invoice update / Errore in cambio dati fattura

10.0.1.0.3 (2023-03-06)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash after change shipping or invoice address / Crash al cambio di indirizzo



Credits | Ringraziamenti
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


Authors | Autori
----------------

* `Odoo Community Association (OCA) <https://odoo-community.org>`__
* `Tecnativa S. L. <https://www.tecnativa.com>`__
* `Avanzosc <https://https:>`__
* `Agile Business Group sagl <https://www.agilebg.com>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it>`__



Contributors | Partecipanti
---------------------------

* `Davide Corio <davide.corio@domsense.com>`__
* `Joao Alfredo Gama Batista <joao.gama@savoirfairelinux.com>`__
* `Sandy Carter <sandy.carter@savoirfairelinux.com>`__
* `Giorgio Borelli <giorgio.borelli@abstract.it>`__
* `Daniel Campos <danielcampos@avanzosc.es>`__
* `Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>`__
* `Oihane Crucelaegui <oihanecruce@gmail.com>`__
* `Nicola Malcontenti <nicola.malcontenti@agilebg.com>`__
* `Aitor Bouzas <aitor.bouzas@adaptivecity.com>`__
* `Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>`__



Maintainer | Manutenzione
-------------------------

* `Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>`__



----------------

|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://www.zeroincombenze.it/>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato da `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sulla propria infrastuttura.
La distribuzione `Zeroincombenze® <https://www.zeroincombenze.it/>`__ è progettata per le esigenze del mercato italiano.


|
|

This module is part of commission project.

Last Update / Ultimo aggiornamento: 2024-03-10

.. |Maturity| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: 
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg
    :target: https://erp10.zeroincombenze.it
    :alt: Try Me
.. |Zeroincombenze| image:: https://avatars0.githubusercontent.com/u/6972555?s=460&v=4
   :target: https://www.zeroincombenze.it/
   :alt: Zeroincombenze
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |same| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/same.png
.. |late| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/late.png
.. |halt| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/halt.png
.. |info| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/info.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/Desktoptelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md
