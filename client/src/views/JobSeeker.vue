<template>
  <el-card class="box-card">
    <CloseButton v-if="detail_flag" @close="detail_flag = false" />
    <template v-if="!detail_flag">
      <ListTable
        :title="table_title"
        :table-data="tableData"
        :table-column="table_column"
        @submitDetail="handleDetail"
        @submitDelete="handleDelete"
      />
    </template>
    <template v-else>
      <JobSeekerDetail :data="detail_job_seeker" />
    </template>
  </el-card>
</template>

<script lang="ts" setup>
import { ref, onBeforeMount, reactive } from "vue";
import showMassage from "../utils/message";
import { fetchApi } from "../utils/api";
import { JobSeeker } from "../type";
import CloseButton from "../components/CloseButton.vue";
import JobSeekerDetail from "../components/job_seeker_components/JobSeekerDetail.vue";

const table_title = "進行中求職者";
const table_column = {
  name: "名前",
  phase: "フェーズ",
  status: "現状ステータス",
  corr_person: "担当者",
};

let detail_flag = ref<boolean>(false);
let detail_job_seeker = ref<JobSeeker | undefined>();
const tableData: JobSeeker[] = reactive([]);

const handleDetail = (value: JobSeeker) => {
  detail_flag.value = true;
  detail_job_seeker.value = value;
};

const handleDelete = (value: JobSeeker) => {
  console.log("削除", value);
};

onBeforeMount(() => {
  fetchApi("api/job_seeker?active_flag=0")
    .then((response) => {
      let res = response.data;
      if (res["result"] == "success") {
        res["data"].forEach((element: JobSeeker) => {
          tableData.push(element);
        });
        showMassage("進行中求職者の取得に成功しました", "success");
      } else {
        showMassage("進行中求職者の取得に失敗しました", "error");
        return false;
      }
    })
    .catch((e) => {
      showMassage(`進行中求職者の取得に失敗しました:${e}`, "error");
    });
});
</script>

<style>
.close-button {
  float: right;
}
.close-button:hover {
  cursor: pointer;
}
</style>
