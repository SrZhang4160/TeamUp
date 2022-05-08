import request from '@/utils/request'

// 获取分组结果数据
export function getList(data) {
  return request({
   url: 'criteria_group_show_page_api',
     // url: '/vue-admin-template/preview/list',
    method: 'post',
    data
  })
}
// 获取分组结果数据 预览
export function getListView(data) {
  return request({
     url: 'criteria_group_page_api',
    //url: '/vue-admin-template/preview/list',
    method: 'post',
    data
  })
}

// 获取配置
export function editList(data) {
  return request({
     url: 'criteria_page_api',
    //url: '/vue-admin-template/editpreview/list',
    method: 'post',
    data
  })
}
// 提交1、2
export function preserve(data) {
  return request({
     url: 'update_criteria_page_api',
    //url: '/vue-admin-template/preview/save',
    method: 'post',
    data
  })
}
export function preserve2(data) {
  return request({
     url: 'update_criteria_page_left_api',
    //url: '/vue-admin-template/preview/save',
    method: 'post',
    data
  })
}

//确认保存预览结果
export function savePreview(data) {
  return request({
    url: 'criteria_group_save_page_api',
    // url: '/vue-admin-template/preview/save',
    method: 'post',
    data
  })
}
