================================
|Zeroincombenze| commission 10.0
================================

.. contents::



Overview / Panoramica
=====================

|en| All management related with commissions and incentive in Odoo.


|it| Moduli per la gestione delle provvigioni

Avaiable Addons / Moduli disponibili
------------------------------------

+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| Name / Nome                          | Version    | OCA Ver.   | Description / Descrizione                                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| hr_commission                        | |halt|     | |halt|     | HR commissions                                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| sale_agent_profile                   | 10.0.0.1.1 | |no_check| | Set default agent authorization user profile                                     |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| sale_commission                      | 10.0.11.0. | 10.0.2.6.0 | Sales commissions                                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| sale_commission_areamanager          | 10.0.1.0.0 | 10.0.1.1.0 | Add head agent on sale agent                                                     |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| sale_commission_bi                   | 10.0.0.1.0 | |no_check| | Add commission values in invoice BI                                              |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| sale_commission_formula              | 10.0.1.0.2 | 10.0.1.0.1 | Sale commissions computed by formulas                                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| sale_commission_geo_assign           | |no_check| | 10.0.1.0.0 | Assign agents to partners according to their location                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| sale_commission_pricelist            | |no_check| | 10.0.1.0.0 | Sales commissions by pricelist                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| website_sale_commission_lead_geo_ass | |no_check| | 10.0.1.0.0 | Assign agents to leads according to their location                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+




Getting started / Come iniziare
===============================

|Try Me|


Prerequisites / Prerequisiti
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


Installation / Installazione
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


Upgrade / Aggiornamento
-----------------------

::

    deploy_odoo update -r commission -b 10.0 -G zero -p $HOME/10.0
    vem amend $HOME/10.0/venv_odoo
    # Adjust following statements as per your system
    sudo systemctl restart odoo


Support / Supporto
------------------

|Zeroincombenze| This project is mainly supported by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__



Get involved / Ci mettiamo in gioco
===================================

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/zeroincombenze/commission/issues>`_.

In case of trouble, please check there if your issue has already been reported.


Proposals for enhancement
-------------------------

|en| If you have a proposal to change on oh these modules, you may want to send an email to <cc@shs-av.com> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.

|it| Se hai proposte per migliorare uno dei moduli, puoi inviare una mail a <cc@shs-av.com> per un iniziale contatto.


ChangeLog History / Cronologia modifiche
----------------------------------------

sale_commission_formula: 10.0.0.1.2 (2024-03-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Documentation upgrade


sale_commission_bi: 10.0.0.1.1 (2024-03-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP[ Inherit agent_id from sale_commission module
* [QUA] Test coverage 73% (60: 16+44) [0 TestPoints] - quality rating 45 (target 100)



sale_commission_areamanager: 10.0.0.1.0 (2024-03-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Initial implementation / Implementazione iniziale
* [IMP] Inherit head_agent from sale_commission module
* [QUA] Test coverage 33% (48: 32+16) [0 TestPoints] - quality rating 21 (target 100)


sale_commission: 10.0.1.0.7 (2024-03-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] head_agent moved into sale_commission_areamanager module
* [IMP[ agent_id moved into sale_commision_bi module
* [IMP] Aligned to OCA module | Allineaato al modulo OCA
* [IMP] Commission BI | Business Intelligence delle provvigioni
* [IMP] Settlement lines | Menù con righe liquidazioni
* [QUA] Test coverage 83% (458: 80+378) [11 TestPoints] - quality rating 54 (target 100)


sale_commission: 10.0.1.0.6 (2024-02-07)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Sale order cannot update commisions
* [QUA] Test coverage 70% (677: 204+473) [11 TestPoints] - quality rating 45 (target 100)


sale_commission_bi: 10.0.0.1.0 (2024-02-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Initial implementation / Implementazione iniziale
* [QUA] Test coverage 100% (10: 0+10) [0 TestPoints] - quality rating 61 (target 100)


sale_commission: 10.0.1.0.5 (2024-02-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Integration with OCA module
* [IMP] sale_agent_id on invoice header
* [QUA] Test coverage 72% (589: 163+426) [11 TestPoints] - quality rating 47 (target 100)


sale_commission: 10.0.1.0.4 (2023-04-06)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Error in invoice update / Errore in cambio dati fattura


sale_commission: 10.0.1.0.3 (2023-03-06)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash after change shipping or invoice address / Crash al cambio di indirizzo


Credits / Ringraziamenti
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


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


Last Update / Ultimo aggiornamento: 2024-03-10

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
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
