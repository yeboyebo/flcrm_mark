# @class_declaration interna_crm_destinacampana #
import importlib

from YBUTILS.viewREST import helpers

from models.flcrm_mark import models as modelos


class interna_crm_destinacampana(modelos.mtd_crm_destinacampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcrm_mark_crm_destinacampana #
class flcrm_mark_crm_destinacampana(interna_crm_destinacampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration crm_destinacampana #
class crm_destinacampana(flcrm_mark_crm_destinacampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcrm_mark.crm_destinacampana_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
