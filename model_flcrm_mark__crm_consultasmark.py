# @class_declaration interna_crm_consultasmark #
import importlib

from YBUTILS.viewREST import helpers

from models.flcrm_mark import models as modelos


class interna_crm_consultasmark(modelos.mtd_crm_consultasmark, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcrm_mark_crm_consultasmark #
class flcrm_mark_crm_consultasmark(interna_crm_consultasmark, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration crm_consultasmark #
class crm_consultasmark(flcrm_mark_crm_consultasmark, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcrm_mark.crm_consultasmark_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
