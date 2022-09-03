<template>
  <div>
    <el-alert :title="title" :type="type" :description="description" show-icon>
    </el-alert>
  </div>
</template>
<script lang="ts" setup>
interface Props {
  title: string;
  type?: "success" | "info" | "warning" | "error";
  description: string;
}
const props = withDefaults(defineProps<Props>(), {
  title: "",
  type: "success",
  description: "",
});
</script>
<style>
.el-alert {
  margin: 20px 0 0;
}
.el-alert:first-child {
  margin: 0;
}
</style>
