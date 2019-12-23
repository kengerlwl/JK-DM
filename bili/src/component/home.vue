<template>
  <div>
    <!-- back to top -->
    <div>
      <a-back-top />
      <strong style="color: rgba(64, 64, 64, 0.6)"></strong>
    </div>
    <!-- carousel -->
    <a-carousel style="max-width: 80rem; margin: 1rem auto 1rem auto" autoplay>
      <div v-for="item in image" :key="item.imgUrl">
        <img class="scrollImg" :src="item.imgUrl" />
      </div>
    </a-carousel>
    <p style="font-size: 4rem; text-align: start; padding-left: 10rem;">Recommend</p>
    <div style="margin: auto auto 10rem 10rem; border-left: 5px solid red;">
      <div style="max-width: 70rem; margin: 1rem auto 1rem auto;">
        <a-list itemLayout="vertical" size="large" :pagination="pagination" :dataSource="List">
          <!-- <div slot="footer">
            <b>ant design vue</b> footer part
          </div>-->
          <a-card
            slot="renderItem"
            slot-scope="item, index"
            key="item[0]"
            hoverable
            @click="toPlay(item[0], item[1])"
          >
            <a-list-item-meta :description="item[0]">
              <span slot="title" style="font-size: 3rem;">{{item[1]}}</span>
              <img slot="avatar" width="130" alt="logo" :src="item[2]" />
            </a-list-item-meta>
          </a-card>
        </a-list>
      </div>
    </div>
  </div>
</template>
<style scoped>
/* For demo */
.ant-carousel >>> .slick-slide {
  text-align: center;
  max-height: 30rem;
  line-height: 30rem;
  background: #364d79;
  overflow: hidden;
}

/* .ant-carousel >>> .slick-slide h3 {
  color: #fff;
} */

.scrollImg {
  display: block;
  margin: auto;
  max-width: 130%;
}
</style>
<script>
export default {
  data() {
    return {
      image: [
        { imgUrl: "../../static/img/1.jpg" },
        { imgUrl: "../../static/img/2.jpg" },
        { imgUrl: "../../static/img/3.jpg" },
        { imgUrl: "../../static/img/4.jpg" },
        { imgUrl: "../../static/img/5.jpg" }
      ],
      List: [
        [
          "http://www.imomoe.io/view/7226.html",
          "\u78a7\u84dd\u5e7b\u60f3\u7b2c\u4e8c\u5b63",
          "http://p.xiaomingming.org/FileUpload/201910421331123591.jpg"
        ],
        [
          "http://www.imomoe.io/view/7383.html",
          "GrandBlue",
          "http://p.xiaomingming.org/FileUpload/20182281333154023.jpg"
        ],
        [
          "http://www.imomoe.io/view/6297.html",
          "\u866b\u5b7d",
          "http://pic.xiaomingming.org/FileUpload/406.jpg"
        ],
        [
          "http://www.imomoe.io/view/6195.html",
          "\u82cd\u4e4b\u6d41\u661fSPT\u96f7\u5179\u7eb3",
          "http://pic.xiaomingming.org/FileUpload/508.jpg"
        ],
        [
          "http://www.imomoe.io/view/6073.html",
          "\u84dd\u5b9d\u77f3\u4e4b\u8c1c \u91cd\u5236\u7248",
          "http://pic.xiaomingming.org/FileUpload/627.jpg"
        ],
        [
          "http://www.imomoe.io/view/5968.html",
          "\u84dd\u82b1",
          "http://pic.xiaomingming.org/FileUpload/747.jpg"
        ],
        [
          "http://www.imomoe.io/view/5804.html",
          "\u672a\u9ebb\u7684\u90e8\u5c4b",
          "http://pic.xiaomingming.org/FileUpload/906.jpg"
        ],
        [
          "http://www.imomoe.io/view/5466.html",
          "\u5149\u4e0e\u6c34\u7684\u5973\u795e",
          "http://pic.xiaomingming.org/FileUpload/1252.jpg"
        ],
        [
          "http://www.imomoe.io/view/5394.html",
          "\u82cd\u5929\u4e4b\u62f3",
          "http://pic.xiaomingming.org/FileUpload/1341.jpg"
        ],
        [
          "http://www.imomoe.io/view/5155.html",
          "\u5047\u9762\u9a91\u58eb\u8d85\u7ea7\u7535\u738b\u7535\u5f71\u4e09\u90e8\u66f2\uff1a\u84dd\u4e4b\u7ae0",
          "http://pic.xiaomingming.org/FileUpload/1572.jpg"
        ]
      ],
      pagination: {
        onChange: page => {
          console.log(page);
        },
        pageSize: 5
      }
    };
  },
  methods: {
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
    }
  },
  props: ["animeList"]
};
</script>
