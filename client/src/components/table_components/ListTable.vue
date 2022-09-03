<template #defalt="props">
  <div>
    <TableHeaderTitle :title="title" />
    <el-table :data="tableData" style="width: 100%" :max-height="maxHeight">
      <el-table-column
        v-for="(item, key) in tableColumn"
        sortable
        :label="item"
        :prop="key"
      />
      <el-table-column align="right">
        <template #default="scope">
          <el-button size="small" @click="handleDetail(scope.row)">詳細</el-button>
          <el-button size="small" type="danger" @click="handleDelete(scope.row)"
            >削除</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script lang="ts" setup>
import TableHeaderTitle from "./TableHeaderTitle.vue";

interface Props {
  title: string;
  tableColumn: {};
  tableData: {}[];
  maxHeight?: number | undefined;
}
withDefaults(defineProps<Props>(), {
  maxHeight: 500,
});
interface Emits {
  (e: "submitDetail", value: {}): void;
  (e: "submitDelete", value: {}): void;
}
const emit = defineEmits<Emits>();

const handleDetail = (row: {}) => {
  emit("submitDetail", row);
};
const handleDelete = (row: {}) => {
  emit("submitDelete", row);
};
</script>
