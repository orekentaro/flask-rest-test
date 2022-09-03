import axios from "axios";

export const fetchApi = (
  url: string
): Promise<AxiosResponse<any, any>> => {
  return axios.get(url, { withCredentials: true })
}

export const postApi = (
  url: string,
  data: FormData
): Promise<AxiosResponse<any, any>> => {
  return axios.post(url, data, { withCredentials: true })
}
