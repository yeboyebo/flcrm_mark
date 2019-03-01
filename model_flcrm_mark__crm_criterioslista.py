# @class_declaration interna_crm_criterioslista #
import importlib

from YBUTILS.viewREST import helpers

from models.flcrm_mark import models as modelos


class interna_crm_criterioslista(modelos.mtd_crm_criterioslista, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcrm_mark_crm_criterioslista #
class flcrm_mark_crm_criterioslista(interna_crm_criterioslista, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration crm_criterioslista #
class crm_criterioslista(flcrm_mark_crm_criterioslista, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcrm_mark.crm_criterioslista_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
