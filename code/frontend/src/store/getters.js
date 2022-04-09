const getters = {
  sidebar: state => state.app.sidebar,
  device: state => state.app.device,
  token: state => state.user.token,
  avatar: state => state.user.avatar,
  eml: state => state.user.eml,
  sex: state => state.user.sex,
  type: state => state.user.type,
  name: state => state.user.name
}
export default getters
