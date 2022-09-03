import { createApp } from 'vue';
import App from './App.vue';
import './index.css';
import router from './router';
import axios from 'axios';
import { store, key } from "./store";
import Cookies from 'js-cookie';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css'
import 'element-plus/theme-chalk/display.css'

const app = createApp(App)
app.use(router, axios, store, key, Cookies, ElementPlus)
app.mount('#app')