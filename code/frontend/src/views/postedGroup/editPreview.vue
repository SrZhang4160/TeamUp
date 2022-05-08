<template>
  <div class="editpreview_wrap">
    <div class="preview_data_title">Group Criteria</div>
    <div class="preview_content">
      <div class="editpreview_list">
        <div
          class="editpreview_listitem"
          v-for="(item, index) in userList"
          :key="index"
        >
          <div class="editpreviewNama">
            <span>{{item.criteriaName}}</span>
          </div>
          <div>Unimportant</div>
          <div>
            <el-slider v-model="item.criteriaNum"></el-slider>
          </div>
          <div>Important</div>
          <div>
            <el-select v-model="item.criteriaPption" @change="change(index)"  placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </div>
        </div>
      </div>
    </div>
    <div class="back_grouping">
      <div>
        <el-button type="primary" plain
        @click="confirm"
          >Group oll students with One click</el-button
        >
      </div>
      <div>
        <el-button type="primary" plain
        @click="confirm"
          >Group students without groups with One click</el-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import { editList,preserve} from "@/api/preview";
export default {
  data() {
    return {
      value2: 15,
      options: [
        {
          value: "Similar",
          label: "Similar",
        },
        {
          value: "Different",
          label: "Different",
        },
       
      ],
      value: "",
      userList:[]
    };
  },
  mounted() {
    let { isTemp } = this.$route.query;
    editList({ isTemp }).then((res) => {
       if (res.code == 1) {
           this.userList=res.criteriaList
      } else {
        this.$message.error(res.msg);
      }
    });
  },
  methods:{
      change(index){
          //console.log(this.userList[index])
      },
      confirm(){
        //  点击保存接口
        preserve({criteriaList:JSON.stringify(this.userList)}).then(res=>{

            if(res.code==1){
                // this.$router.push("/postedGroup/postedGroup")
                // preview
                  const routerJump = this.$router.resolve({
        path: "/preview/preview"
      });
      window.open(routerJump.href, "_blank");
                //console.log("成功")
            }
        })
      }
  }
};
</script>

<style scoped lang="scss">
.editpreview_wrap {
  // max-width: 1000px;
  .preview_data_title {
    width: 100%;
    display: flex;
    justify-content: center;
    height: 80px;
    // border: 1px solid black;
    font-size: 40px;
    align-items: center;
  }
  .preview_content {
    height: 500px;
    // border:1px solid black;
    box-sizing: border-box;
    padding: 0 20px;
    .editpreview_list {
      width: 100%;
      height: 100%;
      border: 3px solid #3ab5ff;
      overflow-y: scroll;
      box-sizing: border-box;
      padding: 10px 10px 10px 10px;
      .editpreview_listitem {
        // border: 1px solid red;
        margin-top: 15px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-sizing: border-box;
        padding: 0 40px 0 10px;
        .editpreviewNama:hover {
          background: #86c5ec;
          color: #fff;
        }
        .editpreviewNama {
          width: 100px;
          border: 3px solid #3ab5ff;
          word-wrap: break-word;
          padding: 2px 0;
          color: #3ab5ff;
          // box-sizing: border-box;

          text-align: center;
          //     // align-items: center;
          //     display: flex;
          //     flex-wrap: wrap;
        }
        :nth-child(3) {
          width: 50%;
        }
      }
    }
  }
  .back_grouping {
    width: 100%;
    display: flex;
    justify-content: center;
    margin-top: 10px;
    :nth-child(2) {
      margin-left: 10px;
    }
  }
}
</style>
