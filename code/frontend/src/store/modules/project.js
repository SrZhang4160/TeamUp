

  import {
    getToken,
    setToken,
    removeToken
  } from '@/utils/auth'

  import {
    create_project_api
  } from '@/api/project'


  const getDefaultState = () => {
    return {
      token: getToken(),
      projectName: '',
      projectIntroduction: '',
      teamname: '',
      keywords: '',
      intendedLanguage: '',
      otherLanguage: '',
      type: '',
      skillWanted: ''
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
    // SET_NAME: (state, name) => {
    //   state.name = name
    // },
    // SET_EML: (state, eml) => {
    //   state.eml = eml
    // },
    // SET_SEX: (state, sex) => {
    //   state.sex = sex
    // },
    // SET_TYPE: (state, type) => {
    //   state.type = type
    // },
    // SET_AVATAR: (state, avatar) => {
    //   state.avatar = avatar
    // }
  }

  const actions = {


    // addstinfo
    create_project({ commit }, projectinfo) {
      const { teamname,projectname, projectidea, keywords, language, otherlanguage, apptype, skillwanted} = projectinfo
 
      return new Promise((resolve, reject) => {
        create_project_api({

          projectName: projectname,
          projectIntroduction: projectidea,
          teamName: teamname,
          keywords: keywords,
          intendedLanguage: language,
          otherLanguage: otherlanguage,
          type: apptype,
          skillWanted: skillwanted,
        }).then(response => {

          const data = response
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
    namespaced: false,
    state,
    mutations,
    actions
  }
