class XPBoardsPlan:

    def __init__(self, user_dict):
        self._is_plan_expired=user_dict['customer']['is_plan_expired']
        self._avaiable_datasets=user_dict['customer']['plan']['dataset_qty'] - user_dict['customer']['datasets_count']
        self._avaiable_devices=user_dict['customer']['plan']['device_qty'] - user_dict['customer']['devices_count']
        self._avaiable_dashboards=user_dict['customer']['plan']['dashboard_qty'] - user_dict['customer']['dashboards_count']

    @property
    def is_plan_expired(self):
        return self._is_plan_expired

    @property
    def avaiable_datasets(self):
        return self._avaiable_datasets

    @property
    def avaiable_devices(self):
        return self._avaiable_devices

    @property
    def avaiable_dashboards(self):
        return self._avaiable_dashboards
