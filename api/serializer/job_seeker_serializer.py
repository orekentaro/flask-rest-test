from typing import Any, Union

import utils.constans as const
from models.job_ads import JobAds
from models.job_master import JobMaster
from models.job_seeker import JobSeeker
from models.memo import Memo
from serializer.base_serializer import BaseSerializer
from utils.get_data import get_one, get_relation, model_to_dict


def _make_data(job_seeker: JobSeeker) -> dict[str, Any]:
    ads = get_one(JobAds, job_seeker.ads_id)
    job_master = get_one(JobMaster, ads.get("job_master_id", {}))
    ads["job_master"] = job_master
    del ads["job_master_id"]
    job_seeker_data = model_to_dict(job_seeker)
    job_seeker_data["ads"] = ads
    del job_seeker_data["ads_id"]
    job_seeker_data.update({"gender": const.GENDER[job_seeker_data["gender"]]})
    job_seeker_data["memo"] = get_relation(Memo, {"job_seeker_id": job_seeker.id})
    return job_seeker_data


class JobSeekerSerializer(BaseSerializer):
    @classmethod
    def serialize(cls, job_seeker: Union[JobSeeker, list[JobSeeker]]) -> Union[dict[str, Any], list]:  # type: ignore[override]
        if type(job_seeker) == list:
            return_list = []
            for js in job_seeker:
                job_seeker_data = _make_data(js)
                return_list.append(job_seeker_data)
            return return_list
        else:
            return _make_data(job_seeker)  # type: ignore[arg-type]
