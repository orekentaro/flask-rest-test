import { ElMessage } from "element-plus";

const showMassage = (
  message: string,
  type?: "success" | "info" | "warning" | "error"
) => {
  ElMessage({
    message: message,
    type: type,
  });
};

export default showMassage;