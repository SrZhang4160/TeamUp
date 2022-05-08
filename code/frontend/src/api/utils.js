function isInnerEmail (rule, str, callback) {
    console.log(str.match(/@(\S*)/)[1]);
    let show=false
    if (str === '' || str === null) {
      callback(new Error('must eml'))
    } else if (str.match(/@(\S*)/)[1]=='jhu.edu') {
      console.log(str.match(/@(\S*)/));
      show=true
    } else{
      callback(new Error('Must be used to JHU Email'))
    }
    if(show){
      callback()
    }
  }
  export{
    isInnerEmail
  }