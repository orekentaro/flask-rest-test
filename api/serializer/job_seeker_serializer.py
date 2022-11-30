from typing import Any, Union

import utils.constans as const
from models.job_ads import JobAds
from models.job_seeker import JobSeeker
from models.memo import Memo
from models.progress_info import ProgressInfo
from serializer.base_serializer import BaseSerializer
from serializer.job_ads_serializer import JobAdsSerializer
from serializer.progress_info_serializer import ProgressInfoSerializer


class JobSeekerSerializer(BaseSerializer):
    def data(self, job_seeker: Union[JobSeeker, list[JobSeeker]]) -> Union[dict[str, Any], list]:  # type: ignore[override]
        if type(job_seeker) == list:
            return_list = []
            for js in job_seeker:
                job_seeker_data = self._make_list(js)
                return_list.append(job_seeker_data)
            return return_list
        else:
            return self._make_detail(job_seeker)  # type: ignore[arg-type]

    def _make_list(self, job_seeker: JobSeeker) -> dict[str, Any]:
        ads = JobAdsSerializer().data(
            self._get_one(JobAds, job_seeker.ads_id, to_model=True)  # type: ignore[arg-type]
        )
        job_seeker_data = self._model_to_dict(job_seeker)
        job_seeker_data["ads"] = ads
        job_seeker_data.update({"gender": const.GENDER[job_seeker_data["gender"]]})
        job_seeker_data["memo"] = self._get_relation(
            Memo, **{"job_seeker_id": job_seeker.id}
        )
        del job_seeker_data["ads_id"]
        return job_seeker_data

    def _make_detail(self, job_seeker: JobSeeker) -> dict[str, Any]:
        data = self._make_list(job_seeker)
        data["progress_info"] = ProgressInfoSerializer().data(
            self._get_relation(  # type: ignore[arg-type]
                ProgressInfo, to_model=True, **{"job_seeker_id": job_seeker.id}
            )
        )
        return data
