<template>
  <el-row :gutter="20">
    <span class="ml-3 w-35 text-gray-600 inline-flex items-center">{{
      props.label
    }}</span>
    <el-input v-model="form.name" />
  </el-row>
</template>

<script lang="ts" setup>
import { ref, reactive } from "vue";
interface Props {
  label: string;
}

interface Emits {
  (e: "input", name: any): void;
}

const props = defineProps<Props>();
const form = reactive({ name: "" });
</script>
