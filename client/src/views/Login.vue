<template>
  <el-container>
    <el-header>
      <div class="flex justify-center container m-[auto] pt-14">
        <el-card class="box-card"
          ><div class="flex justify-center">
            <h1>採用管理画面</h1>
          </div></el-card
        >
      </div>
    </el-header>
    <el-main>
      <div class="flex justify-center container m-[auto] pt-16">
        <el-card class="box-card">
          <el-form
            ref="ruleFormRef"
            :rules="rules"
            :label-position="labelPosition"
            label-width="30px"
            :model="formData"
            style="max-width: 90%"
          >
            <el-form-item label="Email" prop="email">
              <el-input
                v-model="formData.email"
                placeholder="メールアドレスを入力して下さい"
              ></el-input>
            </el-form-item>
            <el-form-item label="Password" prop="password">
              <el-input
                v-model="formData.password"
                type="password"
                placeholder="パスワードを入力して下さい"
                show-password
              >
              </el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm(ruleFormRef)"
                >ログイン</el-button
              >
            </el-form-item>
          </el-form>
        </el-card>
      </div>
    </el-main>
  </el-container>
</template>
<script lang="ts" setup>
import router from "../router";
import { reactive, ref } from "vue";
import type { ElForm } from "element-plus";
import showMassage from "../utils/message";
import { postApi } from "../utils/api";
import { LoginForm } from "../type";
type FormInstance = InstanceType<typeof ElForm>;
const ruleFormRef = ref<FormInstance>();

const labelPosition = "top";

const rules = reactive({
  email: [
    {
      required: true,
      message: "メールアドレスを入力してください",
      trigger: "blur",
    },
  ],
  password: [
    {
      required: true,
      message: "パスワードを入力してください",
      trigger: "blur",
    },
  ],
});
const formData: LoginForm = reactive({
  email: "",
  password: "",
});
const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.validate((valid) => {
    if (valid) {
      var data = new FormData();
      data.append("email", formData.email);
      data.append("password", formData.password);
      postApi("/api/login", data)
        .then((response) => {
          let res = response.data["result"];
          if (res == "success") {
            router.push("/");
          } else {
            showMassage("ログインに失敗しました", "error");
            return false;
          }
        })
        .catch((e) => {
          showMassage(`ログインに失敗しました:${e}`, "error");
        });
    } else {
      return false;
    }
  });
};
</script>

<style scoped>
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 50%;
}
</style>
