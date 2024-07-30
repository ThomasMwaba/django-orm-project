class InventoryAppRouter:
    def db_for_read(self, model, **hints):
        if model.meta.app_label == "orm_app":
            return "inventory_db"
        return None

    def db_for_write(self, model, **hints):
        if model.meta.app_label == "orm_app":
            return "inventory_db"
        return None

    def allow_relation(self, model, obj1, obj2, **hints):
        if obj1._meta.app_label == "orm_app" or obj1._meta.app_label == "orm_app":
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "orm_app":
            return "inventory_db"
        return None
