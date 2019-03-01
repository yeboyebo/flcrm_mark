# @class_declaration interna_crm_estadoscampana #
import importlib

from YBUTILS.viewREST import helpers

from models.flcrm_mark import models as modelos


class interna_crm_estadoscampana(modelos.mtd_crm_estadoscampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcrm_mark_crm_estadoscampana #
class flcrm_mark_crm_estadoscampana(interna_crm_estadoscampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration crm_estadoscampana #
class crm_estadoscampana(flcrm_mark_crm_estadoscampana, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcrm_mark.crm_estadoscampana_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
