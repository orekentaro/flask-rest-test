from typing import Any, Union

from models.job_ads import JobAds
from models.job_master import JobMaster
from serializer.base_serializer import BaseSerializer


class JobAdsSerializer(BaseSerializer):
    def data(self, job_ads: Union[JobAds, list[JobAds]]) -> Union[dict[str, Any], list]:  # type: ignore[override]
        if type(job_ads) == list:
            return_list = []
            for ja in job_ads:
                job_ads_data = self._make_data(ja)
                return_list.append(job_ads_data)
            return return_list
        else:
            return self._make_data(job_ads)  # type: ignore[arg-type]

    def _make_data(self, job_ads: JobAds) -> dict[str, Any]:
        job_master = self._get_one(JobMaster, job_ads.id)
        ads = self._model_to_dict(job_ads)
        ads["job_master"] = job_master
        del ads["job_master_id"]
        return ads
