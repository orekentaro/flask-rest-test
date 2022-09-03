<template>
  <el-row :gutter="20">
    <el-col :span="4" class="font-mono text-2xl text-neutral-100 pt-3">
      <router-link to="/">採用管理画面</router-link>
    </el-col>
    <el-col :span="17"></el-col>
    <el-col :span="2" class="pt-4 pl-10"
      ><el-link type="info">ログアウト</el-link></el-col
    >
  </el-row>
</template>
<script lang="ts" setup></script>
<style>
.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
