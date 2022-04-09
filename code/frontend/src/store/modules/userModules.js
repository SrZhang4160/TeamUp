import {
  login,
  logout,
  getInfo
} from '@/api/userapi'
import {
  getToken,
  setToken,
  removeToken
} from '@/utils/auth'
import {
  resetRouter
} from '@/router'
import {
  addstinfo_api,
  getstinfo_api,
  updatestinfo_api,
  create_student_api
} from '@/api/stinfoapi'

const getDefaultState = () => {
  return {
    token: getToken(),
    name: '',
    eml: '',
    sex: '',
    type: '',
    avatar: ''
  }
}

const state = getDefaultState()

const mutations = {
  RESET_STATE: (state) => {
    Object.assign(state, getDefaultState())
  },
  SET_TOKEN: (state, token) => {
    state.token = token
  },
  SET_NAME: (state, name) => {
    state.name = name
  },
  SET_EML: (state, eml) => {
    state.eml = eml
  },
  SET_SEX: (state, sex) => {
    state.sex = sex
  },
  SET_TYPE: (state, type) => {
    state.type = type
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar
  }
}

const actions = {
  // create_student
  create_student({ commit }, forminfo) {
    const { name, email, password, avatar } = forminfo
    return new Promise((resolve, reject) => {
      create_student_api({
        name: name,
        email: email,
        password: password,
        avatar: avatar,
        type: 0
      }).then(response => {
        // eslint-disable-next-line
        const data = response
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // addstinfo
  addstinfo({ commit }, stinfo) {
   const { name, skillLevel, major, leadInt, grade, fieldInt, prod, exep, mbti, prefer, preferNot } = stinfo
    return new Promise((resolve, reject) => {
      addstinfo_api({
        name: name,
        skillLevel: skillLevel,
        major: major,
        leadInt: leadInt,
        grade: grade,
        fieldInt: fieldInt,
        prod: prod,
        exep: exep,
        mbti: mbti,
        prefer: prefer,
        preferNot: preferNot
      }).then(response => {
        // eslint-disable-next-line
        const data = response
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // updatestinfo
  updatestinfo({ commit}, stinfo ) {

    const { name, skillLevel, major, leadInt, grade, fieldInt, prod, exep, mbti, prefer, preferNot } = stinfo
    const input = {
      userDetails:{
        name: name,
        skillLevel: skillLevel,
        major: major,
        leadInt: leadInt,
        grade: grade,
        fieldInt: fieldInt,
        prod: prod,
        exep: exep,
        mbti: mbti,
        prefer: prefer,
        preferNot: preferNot
      }         
    }
    return new Promise((resolve, reject) => {
      updatestinfo_api(input).then(response => {
        const data = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // getstinfo
  getstinfo({ commit, state }) {
    return new Promise((resolve, reject) => {
      getstinfo_api(state.token).then(response => {
        const data = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user login
  loginMod({ commit }, userInfo) {
    const { username, password } = userInfo
    return new Promise((resolve, reject) => {
      login({
        email: username.trim(),
        username: username.trim(),
        password: password
      }).then(response => {
        const data = response
        commit('SET_TOKEN', data.token)
        setToken(data.token)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // 获取用户信息 方法调用处理
  getInfo({ commit, state }) {
    return new Promise((resolve, reject) => {
      getInfo(state.token).then(response => {
        const data = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const { name, eml, type, avatar } = data
        commit('SET_EML', eml)
        commit('SET_TYPE', type)
        commit('SET_SEX', 0)
        commit('SET_NAME', name)
        commit('SET_AVATAR', avatar)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout
  logout({ commit, state }) {
    return new Promise((resolve, reject) => {
      logout(state.token).then(() => {
        removeToken() // must remove  token  first
        resetRouter()
        commit('RESET_STATE')
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // remove token
  resetToken({ commit }) {
    return new Promise(resolve => {
      removeToken() // must remove  token  first
      commit('RESET_STATE')
      resolve()
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
