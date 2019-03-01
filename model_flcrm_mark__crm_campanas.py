# @class_declaration interna_crm_campanas #
import importlib

from YBUTILS.viewREST import helpers

from models.flcrm_mark import models as modelos


class interna_crm_campanas(modelos.mtd_crm_campanas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcrm_mark_crm_campanas #
class flcrm_mark_crm_campanas(interna_crm_campanas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration crm_campanas #
class crm_campanas(flcrm_mark_crm_campanas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcrm_mark.crm_campanas_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
