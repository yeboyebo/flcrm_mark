# @class_declaration interna_crm_configmark #
import importlib

from YBUTILS.viewREST import helpers

from models.flcrm_mark import models as modelos


class interna_crm_configmark(modelos.mtd_crm_configmark, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcrm_mark_crm_configmark #
class flcrm_mark_crm_configmark(interna_crm_configmark, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration crm_configmark #
class crm_configmark(flcrm_mark_crm_configmark, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcrm_mark.crm_configmark_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
