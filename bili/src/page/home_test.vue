<template>
  <div class="container-fluid" id="home">
    <div class="row-fluid">
      <div class="span12">
        <form class="form-search">
          <input class="input-medium search-query" type="text" v-model="url" />
          <button class="btn" v-on:click="click">搜索</button>
        </form>

        <div id="app">
          <ul>
            <li v-for="(temp, index) in list">
              {{ temp }}nput-medium search-query
              <b v-bind:href="list[index][0]" v-on:click="select($event)">
                {{ temp[1] }}</b
              >
            </li>
          </ul>
        </div>
      </div>
    </div>
    <a v-bind:href="url">{{ url }}</a>
  </div>
</template>

<script>
// import axios from "axios";
import $ from "jquery";

export default {
  name: "home",
  data() {
    return {
      url: "Welcome to ",
      list: {}
    };
  },
  methods: {
    select: function(event) {
      console.log("select");
      var el = event.currentTarget;
      alert("当前对象的内容：" + el.getAttribute("href"));
      this.$router.push({
        path: "/play",
        query: {
          url: el.getAttribute("href")
        }
      });
    },

    click: function() {
      console.log("click"),
        (this.list = [
          [
            "http://www.imomoe.io/view/2634.html",
            "\u660e\u6cbb\u4e1c\u4eac\u604b\u4f3d",
            "http://pic.xiaomingming.org/FileUpload/4218.jpg"
          ],
          [
            "http://www.imomoe.io/view/7546.html",
            "\u95ea\u4e71\u795e\u4e50\u7b2c\u4e8c\u5b63",
            "http://p.xiaomingming.org/FileUpload/20181013033149583.jpg"
          ],
          [
            "http://www.imomoe.io/view/7501.html",
            "\u4e1c\u4eac\u98df\u5c38\u9b3c\u7b2c\u56db\u5b63",
            "http://p.xiaomingming.org/FileUpload/201810418234388208.jpg"
          ],
          [
            "http://www.imomoe.io/view/7208.html",
            "\u4e1c\u4eac\u98df\u5c38\u9b3c\u7b2c\u4e09\u5b63",
            "http://p.xiaomingming.org/FileUpload/20184218582980056.jpg"
          ],
          [
            "http://www.imomoe.io/view/7299.html",
            "\u4e1c\u4eac\u98df\u5c38\u9b3c \u771f\u4eba\u7248",
            "http://p.xiaomingming.org/FileUpload/2017122318321765575.jpg"
          ],
          [
            "http://www.imomoe.io/view/1716.html",
            "\u4e1c\u4eac\u98df\u5c38\u9b3c\u7b2c\u4e8c\u5b63",
            "http://pic.xiaomingming.org/FileUpload/5177.jpg"
          ],
          [
            "http://www.imomoe.io/view/2149.html",
            "\u4e1c\u4eac\u98df\u5c38\u9b3c",
            "http://pic.xiaomingming.org/FileUpload/4741.jpg"
          ],
          [
            "http://www.imomoe.io/view/2325.html",
            "\u6050\u6016\u6b8b\u54cd",
            "http://pic.xiaomingming.org/FileUpload/4536.jpg"
          ],
          [
            "http://www.imomoe.io/view/6034.html",
            "\u4e1c\u4eac\u5730\u97078.0",
            "http://pic.xiaomingming.org/FileUpload/674.jpg"
          ],
          [
            "http://www.imomoe.io/view/5385.html",
            "\u4e1c\u4eac\u9b54\u4eba\u5b66\u56ed\u5251\u98ce\u5e16 \u7b2c\u4e00\u5b63",
            "http://pic.xiaomingming.org/FileUpload/1344.jpg"
          ]
        ]);
      // axios
      //   .get("http://192.168.1.102:8000/search?keyW=" + this.url)
      //   .then(response => {
      //     console.log(response.data);
      //     console.log(response.data.data);
      //     this.list = response.data.data;
      //   });
    }
  }
};
</script>
<!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
