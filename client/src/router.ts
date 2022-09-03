import { createRouter,createWebHistory } from 'vue-router';
import JobSeekerList from "./views/JobSeekerList.vue";
import JobSeeker from "./views/JobSeeker.vue";
import Login from "./views/Login.vue"
import Mainpage from "./views/MainPage.vue"
import Top from './views/Top.vue';
import JobVacancies from './views/JobVacancies.vue';
import JobVacanciesList from './views/JobVacanciesList.vue';
import Recruiter from './views/Recruiter.vue';
import DashBoard from './views/DashBoard.vue';
import RecruitementFlow from './views/RecruitmentFlow.vue';
import Permission from './views/Permission.vue';
import ParameterStor from './views/ParameterStor.vue';
import { store } from "./store"
import Cookies  from 'js-cookie';

const routes = [
  { path: '/', name: '/', component: Mainpage ,
    children: [
      { path: '/', name: 'top', component: Top },
      { path: '/job_seeker', name: 'jobSeeker', component: JobSeeker },
      { path: '/job_seeker_list', name: 'jobSeekerList', component: JobSeekerList },
      { path: '/job_vacancies', name: 'jobVacanciesList', component: JobVacancies },
      { path: '/job_vacancies_list', name: 'jobVacanciesrList', component: JobVacanciesList },
      { path: '/dashboard', name: 'dashBoard', component: DashBoard },
      { path: '/recruiter', name: 'recruiter', component: Recruiter },
      { path: '/recruitement_flow', name: 'recruitementFlow', component: RecruitementFlow },
      { path: '/permisson', name: 'permission', component: Permission },
      { path: '/parameter_stor', name: 'parameterStor', component: ParameterStor },
    ]
},
    { path: '/login', name: 'login', component: Login }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to, from, next) => {
  store.dispatch('update', Cookies.get("login"));
  if (to.name != "login") {
    if (store.state.token){
      next();
    } else {
      next('/login');
    }
  } else {
    next()
  }
});

export default router;