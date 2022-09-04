export interface JobSeeker {
  corr_person: string;
  gender: string;
  birthday: string;
  career: string;
  job_ads: string;
  job_id: string;
  memo: Memo[];
  name: string;
  phase: Phase;
  progress: Progress[];
  status: Result;
  title: string;
  create_time: string;
}

export interface Memo {
  create_time: BigInteger;
  memo: string;
  changer: string;
}

export interface Progress {
  corr_person: string;
  info: string;
  phase: Phase;
  result: Result;
  schedule: BigInteger;
}

export type Phase = "応募" | "一次面接" | "二次面接" | "内定" | "内定承諾"| "入社"| "辞退" | undefined
export type Result = "選考中" | "日程調整中" | "予定" | "実施" | "キャンセル"| "通過"| "不合格" | undefined

export interface LoginForm {
  email: string;
  password: string;
};