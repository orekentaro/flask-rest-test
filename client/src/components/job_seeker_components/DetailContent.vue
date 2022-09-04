<template #default="props">
  <div class="label">{{ label }}</div>
  <div class="content">
    {{ content }}
  </div>
</template>
<script lang="ts" setup>
interface Props {
  label: string;
  content: string;
}
withDefaults(defineProps<Props>(), {
  label: "",
  content: "",
});
</script>
<style scoped>
.label {
  font-weight: 150;
  font-size: 2rem;
}
.content {
  font-weight: 100;
  font-size: 1.5rem;
  padding-top: 0.3rem;
  margin-left: 2rem;
}
</style>
