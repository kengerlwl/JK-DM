<template>
  <div>
    <!-- back to top -->
    <div>
      <a-back-top />
      <strong style="color: rgba(64, 64, 64, 0.6)"></strong>
    </div>
    <span style="font-size: 4rem; nargin: 3rem auto 3rem auto;">Favorite</span>
    <div style="max-width: 70rem; margin: 1rem auto 1rem auto;">
      <a-list itemLayout="vertical" size="large" :pagination="pagination" :dataSource="list">
        <!-- <div slot="footer">
            <b>ant design vue</b> footer part
        </div>-->
        <a-card
          id="card"
          slot="renderItem"
          slot-scope="item, index"
          key="item.title"
          hoverable
          @click="toPlay(item[0], item[2])"
        >
          <a-list-item-meta :description="item[0]">
            <span slot="title" style="font-size: 3rem;">{{item[2]}}</span>
            <img slot="avatar" width="130" alt="logo" :src="item[1]" />
          </a-list-item-meta>
          <a-button
            v-on:click.stop="del($event, item[2])"
            type="danger"
            style="font-size: 1rem; float: right"
          >删除</a-button>
        </a-card>
      </a-list>
    </div>
  </div>
</template>
<script>
import $ from "jquery";
import axios from "axios";

export default {
  created: function() {
    console.log(this.list);
  },
  data() {
    return {
      pagination: {
        onChange: page => {
          console.log(page);
        },
        pageSize: 10
      },
      list2: [],
      list: [
        [
          "http://www.imomoe.io/view/1805.html",
          "http://pic.xiaomingming.org/FileUpload/5079.jpg",
          "\u5076\u50cf\u6d3b\u52a8\u7b2c\u4e09\u5b63"
        ],
        [
          "http://www.imomoe.io/view/7695.html",
          "http://p.xiaomingming.org/FileUpload/201910121123782417.jpg",
          "\u98df\u621f\u4e4b\u7075\u7b2c\u56db\u5b63"
        ],
        [
          "http://www.imomoe.io/view/7729.html",
          "http://p.xiaomingming.org/FileUpload/201992019264977910.jpg",
          "\u6d66\u5c9b\u5742\u7530\u8239\u7684\u65e5\u5e38"
        ],
        [
          "http://www.imomoe.io/view/7570.html",
          "http://p.xiaomingming.org/FileUpload/2019103421543513.jpg",
          "\u653e\u5b66\u540e\u684c\u6e38\u4ff1\u4e50\u90e8"
        ],
        [
          "http://www.imomoe.io/view/1804.html",
          "http://pic.xiaomingming.org/FileUpload/5098.jpg",
          "\u7cbe\u7075\u4f7f\u7684\u5251\u821eOVA"
        ],
        [
          "http://www.imomoe.io/view/1804.html",
          "http://pic.xiaomingming.org/FileUpload/5098.jpg",
          "\u7cbe\u7075\u4f7f\u7684\u5251\u821eOVA"
        ],
        [
          "http://www.imomoe.io/view/1801.html",
          "http://pic.xiaomingming.org/FileUpload/5099.jpg",
          "JOJO\u7684\u5947\u5999\u5192\u9669"
        ],
        [
          "http://www.imomoe.io/view/7711.html",
          "http://p.xiaomingming.org/FileUpload/201981820175113928.jpg",
          "\u53a8\u75c5\u6fc0\u53d1\u7537\u5b69"
        ],
        [
          "http://www.imomoe.io/view/7753.html",
          "http://p.xiaomingming.org/FileUpload/201911120444661595.jpg",
          "UCHITAMA?!\uff5e\u732b\u72d7\u5ba0\u7269\u8857\uff5e"
        ],
        [
          "http://www.imomoe.io/view/7384.html",
          "http://p.xiaomingming.org/FileUpload/20199422163113870.jpg",
          "\u6211\u4e0d\u662f\u8bf4\u4e86\u80fd\u529b\u8981\u5e73\u5747\u503c\u4e48"
        ],
        [
          "http://www.imomoe.io/view/1806.html",
          "http://pic.xiaomingming.org/FileUpload/5088.jpg",
          "\u9b41\u62d43\u6218\u795e\u5d1b\u8d77"
        ],
        [
          "http://www.imomoe.io/view/7381.html",
          "http://p.xiaomingming.org/FileUpload/20199112222236033.jpg",
          "\u82b1\u724c\u60c5\u7f18\u7b2c\u4e09\u5b63"
        ]
      ]
    };
  },
  methods: {
    callback(val) {
      console.log(val);
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
    del: function(event, playName) {
      var el = event.currentTarget.parentNode.parentNode;
      console.log(el);
      el.parentNode.removeChild(el);
      // $('#card').hide(1000)
      this.$notification.open({
        message: playName,
        description: "Delete",
        onClick: () => {
          console.log("Notification Clicked!");
        },
        duration: 2
      });
    }
  }
};
</script>