# @class_declaration interna_crm_aliascampana #
import importlib

from YBUTILS.viewREST import helpers

from models.flcrm_mark import models as modelos


class interna_crm_aliascampana(modelos.mtd_crm_aliascampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcrm_mark_crm_aliascampana #
class flcrm_mark_crm_aliascampana(interna_crm_aliascampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration crm_aliascampana #
class crm_aliascampana(flcrm_mark_crm_aliascampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcrm_mark.crm_aliascampana_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
