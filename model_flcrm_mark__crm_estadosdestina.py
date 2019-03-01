# @class_declaration interna_crm_estadosdestina #
import importlib

from YBUTILS.viewREST import helpers

from models.flcrm_mark import models as modelos


class interna_crm_estadosdestina(modelos.mtd_crm_estadosdestina, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcrm_mark_crm_estadosdestina #
class flcrm_mark_crm_estadosdestina(interna_crm_estadosdestina, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration crm_estadosdestina #
class crm_estadosdestina(flcrm_mark_crm_estadosdestina, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcrm_mark.crm_estadosdestina_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
