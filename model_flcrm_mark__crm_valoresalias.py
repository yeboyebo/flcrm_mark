# @class_declaration interna_crm_valoresalias #
import importlib

from YBUTILS.viewREST import helpers

from models.flcrm_mark import models as modelos


class interna_crm_valoresalias(modelos.mtd_crm_valoresalias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcrm_mark_crm_valoresalias #
class flcrm_mark_crm_valoresalias(interna_crm_valoresalias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration crm_valoresalias #
class crm_valoresalias(flcrm_mark_crm_valoresalias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcrm_mark.crm_valoresalias_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
