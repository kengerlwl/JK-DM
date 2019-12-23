<template>
  <div>
    <!-- back to top -->
    <div>
      <a-back-top />
      <strong style="color: rgba(64, 64, 64, 0.6)"></strong>
    </div>
    <span style="font-size: 4rem; nargin: 3rem auto 3rem auto;">Classification</span>
    <div>
      <div v-for="item in varData" :key="item[0]" style="display: inline; text-align: left;">
        <a-button type="primary" style="margin: 0.5rem;" @click="clickClass(item[1])">{{ item[1] }}</a-button>
      </div>
    </div>
    <div>
      <!-- <a-radio-group v-model="tabPosition" style="margin:8px">
      <a-radio-button value="top">top</a-radio-button>
      <a-radio-button value="bottom">bottom</a-radio-button>
      <a-radio-button value="left">left</a-radio-button>
      <a-radio-button value="right">right</a-radio-button>
      </a-radio-group>-->

      <div style="max-width: 70rem; margin: 1rem auto 1rem auto;">
        <a-list itemLayout="vertical" size="large" :pagination="pagination" :dataSource="animeList">
          <!-- <div slot="footer">
            <b>ant design vue</b> footer part
          </div>-->
          <a-card
            slot="renderItem"
            slot-scope="item, index"
            key="item[0]"
            hoverable
            @click="toPlay(item[0], item[2])"
          >
            <a-list-item-meta :description="des">
              <span slot="title" style="font-size: 3rem;">{{item[2]}}</span>
              <img slot="avatar" width="130" alt="logo" :src="item[1]" />
            </a-list-item-meta>
          </a-card>
        </a-list>
      </div>
    </div>
  </div>
</template>
<style>
.hello {
  text-align: left;
}
</style>
<script>
import $ from "jquery";
import axios from "axios";

export default {
  created: function() {
    console.log("created");
    this.clickClass("搞笑");
  },
  data() {
    return {
      des:
        "桐人、尤吉欧、爱丽丝。距离两名修剑士和一名整合骑士打败了最高祭司阿多米尼斯多雷特已过去了半年。结束了战斗，爱丽丝在故乡卢利特村生活。在她的身旁，是失去了挚友，自己也失去了手臂和心的桐人。献身般支撑着他的爱丽丝",
      tabPosition: "top",
      varData: [
        ["1", "搞笑"],
        ["2", "格斗"],
        ["3", "教育"],
        ["4", "竞技"],
        ["5", "剧情"],
        ["6", "科幻"],
        ["7", "历史"],
        ["8", "励志"],
        ["9", "魔法"],
        ["10", "青春"],
        ["11", "热血"],
        ["12", "社会"],
        ["13", "神魔"],
        ["14", "童话"],
        ["15", "校园"],
        ["16", "战争"],
        ["17", "真人"],
        ["18", "LOLI"]
      ],
      animeList: [],
      pagination: {
        onChange: page => {
          console.log(page);
        },
        pageSize: 15
      }
    };
  },
  methods: {
    callback(val) {
      console.log(val);
      搞笑;
    },
    toPlay(playTitle, playName) {
      this.$notification.open({
        message: playName,
        description: playTitle,
        onClick: () => {
          console.log("Notification Clicked!");
        },
        duration: 2
      });
      this.$emit("playList", playTitle);
    },
    clickClass(key) {
      axios.get("http://127.0.0.1:8000/va?varity=" + key).then(response => {
        console.log("send get");
        console.log(response.data);
        console.log(response.data.data);
        this.animeList = response.data.data;
        this.$message.success("Loading finished", 1);
      });
    }
  }
};
</script>