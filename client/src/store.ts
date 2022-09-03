import Cookies  from 'js-cookie';
import { InjectionKey } from 'vue'
import { createStore, useStore as baseUseStore, Store } from 'vuex'

export interface User {
  token: any
}

export const key: InjectionKey<Store<User>> = Symbol()

// Storeを作成する
export const store = createStore<User>({
  state: {
    token: Cookies.get("login")
  },
  getters: {
    getToken: (state) => {
      return state.token
    }
  },
  actions: {
    update ({ commit, state }, token: User) {
      commit('update', token)
    }
  },
  mutations: {
    update (state, token) {
      state.token = token
    }
  }
})

// 独自のuserStoreメソッドを定義する
export function useStore () {
  // InjectionKeyをuserStoreメソッドに渡す
  return baseUseStore(key)
}