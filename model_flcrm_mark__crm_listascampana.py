# @class_declaration interna_crm_listascampana #
import importlib

from YBUTILS.viewREST import helpers

from models.flcrm_mark import models as modelos


class interna_crm_listascampana(modelos.mtd_crm_listascampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcrm_mark_crm_listascampana #
class flcrm_mark_crm_listascampana(interna_crm_listascampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration crm_listascampana #
class crm_listascampana(flcrm_mark_crm_listascampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcrm_mark.crm_listascampana_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
