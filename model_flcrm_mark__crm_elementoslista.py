# @class_declaration interna_crm_elementoslista #
import importlib

from YBUTILS.viewREST import helpers

from models.flcrm_mark import models as modelos


class interna_crm_elementoslista(modelos.mtd_crm_elementoslista, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcrm_mark_crm_elementoslista #
class flcrm_mark_crm_elementoslista(interna_crm_elementoslista, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration crm_elementoslista #
class crm_elementoslista(flcrm_mark_crm_elementoslista, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcrm_mark.crm_elementoslista_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
