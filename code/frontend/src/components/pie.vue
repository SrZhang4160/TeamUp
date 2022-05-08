<template>
  <div class="container">
    <div id="tests" style="height: 200px"></div>
    <div id="testss" style="height: 400px"></div>
  </div>
</template>
<script>
import HighCharts from "highcharts";
import highcharts3d from "highcharts/highcharts-3d";
import { piechart, cylinderchart } from "@/api/message";
export default {
  props: {
    id: {
      type: String,
    },
    option: {
      type: Object,
    },
  },
  data() {
    return {
      randomcolor: "",
      optionss: {
          credits: {  //去掉highcharts.com
          enabled:false
        },
        exporting: {  //导出，不显示false
            enabled:true,
        },
        chart: {
          type: "pie",
         
          options3d: {
            enabled: true,
            alpha: 45,
            beta: 0,
          },
        },
        title: {
          text: "Project languages",
        },
        tooltip: {
          pointFormat: "{series.name}: <b>{point.percentage:.1f}%</b>",
        },
        plotOptions: {
          pie: {
            allowPointSelect: true,
            cursor: "pointer",
            depth: 35,
            dataLabels: {
              enabled: true,
              format: "{point.name}",
            },
          },
        },
        series: [
          {
            type: "pie",
            name: "proportion",
            data: [
              ["Firefox", 45.0],
              ["IE", 26.8],
              ["Chrome", 12.8],

              ["Safari", 8.5],
              ["Opera", 6.2],
              ["Others", 0.7],
            ],
          },
        ],
      },
      options: {
         
            credits: {  //去掉highcharts.com
          enabled:false
        },
        exporting: {  //导出，不显示false
            enabled:true,
        },
        
        chart: {
          type: "column",
          margin: 75,
          options3d: {
            enabled: true,
            alpha: 35,
            beta: -10,
            depth: 0,
          },
        },
        title: {
          text: "Student interested fields", //图表的标题文字
        },
        subtitle: {
          text: "", //副标题文字
        },
        xAxis: {
          categories: [
            "星期一",
            "星期二",
            "星期三",
            "星期四",
            "星期五",
            "星期六",
            "星期日",
          ],
          crosshair: true,
          labels: {
                      rotation: -50,
            formatter: function () {
              var labelVal = this.value;
              var reallyVal = "";
              var lvl = labelVal.length;
              if (lvl > 1) {
                for (var i = 1; i <= lvl; i++) {
                  reallyVal += labelVal.substr(i - 1, 1) + "<br/>";
                }
              }
              return reallyVal.substring(0, reallyVal.length - 5);
            },
          },
        },
        plotOptions: {
          column: {
            depth: 25,
          },
          // series: {},
        },
        series: [
        
          {
              name: 'sum',
            data: [
              { color: "#AA4643", y: 11 },
              { color: "#89A54E", y: 12 },
              { color: "#80699B", y: 13 },
              { color: "#3D96AE", y: 14 },
              { color: "#DB843D", y: 15 },
              { color: "#92A8CD", y: 16 },
              { color: "#A47D7C", y: 17 },
            ],
          },
        ],
      },
    };
  },
  mounted() {
    piechart().then((res) => {
      let arr = [];
      // percentage
      for (let i = 0; i < res.projectsLanguages.length; i++) {
        var obj = [
          res.projectsLanguages[i].name,
          res.projectsLanguages[i].percentage,
        ];
        arr.push(obj);
      }
      this.optionss.series[0].data = arr;
      // console.log(this.optionss.series[0].data=arr, "ereeeeeeeeeeeeeeeeeeeeeeeeeeeee");
      HighCharts.chart("tests", this.optionss);
      // console.log(arr,"饼形图")
    });

    cylinderchart().then((res) => {
      let week = [];
      let scroll = [];
      for (let i = 0; i < res.interestedFields.length; i++) {
        this.getColor();
        week.push(res.interestedFields[i].name);
        var objs = {
          color: this.randomcolor,
          y: res.interestedFields[i].num,
        };
        // console.log(11 + i);
        scroll.push(objs);
      }
      this.options.xAxis.categories = week;
      this.options.series[0].data = scroll;
      // console.log(scroll, "变换的y");
      // console.log(this.options.xAxis.categories, "sfe8888trwe");
      HighCharts.chart("testss", this.options);
    });
  },
  methods: {
    getColor() {
      //定义字符串变量colorValue存放可以构成十六进制颜色值的值
      var colorValue = "0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f";
      //以","为分隔符，将colorValue字符串分割为字符数组["0","1",...,"f"]
      var colorArray = colorValue.split(",");
      var color = "#"; //定义一个存放十六进制颜色值的字符串变量，先将#存放进去
      //使用for循环语句生成剩余的六位十六进制值
      for (var i = 0; i < 6; i++) {
        //colorArray[Math.floor(Math.random()*16)]随机取出
        // 由16个元素组成的colorArray的某一个值，然后将其加在color中，
        //字符串相加后，得出的仍是字符串
        color += colorArray[Math.floor(Math.random() * 16)];
      }
      this.randomcolor = color;
    },
  },
};
</script>
<style lang="scss" scoped>
.container {
  width: 100%;
  height: 550px;
  //   border:1px solid red;
  //   overflow-y: scroll
  #testss {
    margin-top: 10px;
  }

}
.highcharts-axis-labels{
  height: 200px !important;
  border: 1px solid red;
}

</style>
