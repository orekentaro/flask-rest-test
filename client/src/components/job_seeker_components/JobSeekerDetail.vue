<template #default="props">
  <TableHeaderTitle :title="data?.name" />
  <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
    <el-tab-pane label="面談履歴" name="first">面談履歴</el-tab-pane>
    <el-tab-pane label="基本情報" name="second"
      ><el-card class="box-card">
        <template #header>
          <div class="card-header">
            <span class="pr-5">{{ data?.create_time }}</span>
            <span
              ><strong>{{ data?.job_ads }}</strong
              >からの応募</span
            >
          </div>
        </template>
        <DetailContent label="生年月日" :content="data?.birthday" />
        <DetailContent label="経歴" :content="data?.career" />
      </el-card>
    </el-tab-pane>
    <el-tab-pane label="メモ" name="third">メモ</el-tab-pane>
  </el-tabs>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import type { TabsPaneContext } from "element-plus";
import { JobSeeker } from "../../type";
import TableHeaderTitle from "../table_components/TableHeaderTitle.vue";

interface Props {
  data: JobSeeker | undefined;
}
const props = defineProps<Props>();

const activeName = ref("first");

const handleClick = (tab: TabsPaneContext, event: Event) => {
  console.log(tab, event);
};
</script>
<style scoped>
.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}

.card-header {
  display: flex;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}
</style>
