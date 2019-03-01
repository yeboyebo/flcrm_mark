# @class_declaration interna_crm_listasmark #
import importlib

from YBUTILS.viewREST import helpers

from models.flcrm_mark import models as modelos


class interna_crm_listasmark(modelos.mtd_crm_listasmark, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcrm_mark_crm_listasmark #
class flcrm_mark_crm_listasmark(interna_crm_listasmark, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration crm_listasmark #
class crm_listasmark(flcrm_mark_crm_listasmark, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcrm_mark.crm_listasmark_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
