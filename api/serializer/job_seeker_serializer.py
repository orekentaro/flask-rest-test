from typing import Any, Union

from models.job_ads import get_job_ads
from models.job_master import get_job_master
from models.job_seeker import JobSeeker
from serializer.base_serializer import BaseSerializer


def _make_data(job_seeker: JobSeeker) -> dict[str, Any]:
    ads = get_job_ads(job_seeker.ads_id)
    job_master = get_job_master(ads.get("job_master_id", {}))
    ads["job_master"] = job_master
    job_seeker_data = job_seeker.__dict__
    job_seeker_data.pop("_sa_instance_state")
    job_seeker_data["ads"] = ads
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
