function isInnerEmail (rule, str, callback) {
    console.log(str.match(/@(\S*)/)[1]);
    let show=false
    if (str === '' || str === null) {
      callback(new Error('邮箱必须'))
    } else if (str.match(/@(\S*)/)[1]=='jhu.edu') {
      console.log(str.match(/@(\S*)/));
      show=true
    }else{
      callback(new Error('必须用以jhu.edu结尾的邮箱'))
    }
    if(show){
      callback()
    }
  }
  export{
    isInnerEmail
  }