# @class_declaration interna_crm_adjuntoscampana #
import importlib

from YBUTILS.viewREST import helpers

from models.flcrm_mark import models as modelos


class interna_crm_adjuntoscampana(modelos.mtd_crm_adjuntoscampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcrm_mark_crm_adjuntoscampana #
class flcrm_mark_crm_adjuntoscampana(interna_crm_adjuntoscampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration crm_adjuntoscampana #
class crm_adjuntoscampana(flcrm_mark_crm_adjuntoscampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcrm_mark.crm_adjuntoscampana_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
