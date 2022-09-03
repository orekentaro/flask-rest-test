<template>
  <el-row class="tac">
    <el-col :span="12">
      <h5 class="mb-2"></h5>
      <el-menu default-active="2" class="el-menu-vertical-demo">
        <el-sub-menu index="1">
          <template #title>
            <el-icon><Avatar /></el-icon>
            <span>採用者管理</span>
          </template>
          <el-menu-item index="1-1"
            ><router-link to="/job_seeker">進行中求職者</router-link></el-menu-item
          >
          <el-menu-item index="1-2"
            ><router-link to="/job_seeker_list">求職者一覧管理</router-link>
          </el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="2">
          <template #title>
            <el-icon><Edit /></el-icon>
            <span>求人管理</span>
          </template>
          <el-menu-item index="2-1">
            <router-link to="/job_vacancies">掲載中求人</router-link>
          </el-menu-item>
          <el-menu-item index="2-2"
            ><router-link to="/job_vacancies_list"
              >求人一覧管理</router-link
            ></el-menu-item
          >
        </el-sub-menu>
        <el-sub-menu index="3">
          <template #title>
            <el-icon><setting /></el-icon>
            <span>設定</span>
          </template>
          <el-sub-menu index="3-1">
            <template #title>採用者管理</template>
            <el-menu-item index="3-1-1">
              <router-link to="/recruiter">採用者一覧</router-link>
            </el-menu-item>
            <el-menu-item index="3-1-2">
              <router-link to="dashboard">ダッシュボード</router-link>
            </el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="3-2">
            <template #title>マスターデータ</template>
            <el-menu-item index="3-2-1">
              <router-link to="/recruitement_flow">採用フロー管理</router-link>
            </el-menu-item>
            <el-menu-item index="3-2-2">
              <router-link to="/permisson">権限管理</router-link>
            </el-menu-item>
            <el-menu-item index="3-2-3">
              <router-link to="/parameter_stor">パラメーターストア</router-link>
            </el-menu-item>
          </el-sub-menu>
        </el-sub-menu>
      </el-menu>
    </el-col>
  </el-row>
</template>
<script lang="ts" setup>
import { Edit, Avatar, Setting } from "@element-plus/icons-vue";
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
</script>
<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  height: 90vh;
}
</style>
