<template>
  <div>
    <!-- back to top -->
    <div>
      <a-back-top />
      <strong style="color: rgba(64, 64, 64, 0.6)"></strong>
    </div>
    <span style="font-size: 4rem; nargin: 3rem auto 3rem auto;">History</span>
    <div style="max-width: 70rem; margin: 1rem auto 1rem auto;">
      <a-list itemLayout="vertical" size="large" :pagination="pagination" :dataSource="list">
        <!-- <div slot="footer">
            <b>ant design vue</b> footer part
        </div>-->
        <a-card
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
      list: [
        [
          "http://www.imomoe.io/view/1802.html",
          "http://pic.xiaomingming.org/FileUpload/5080.jpg",
          "\u963fU\u7b2c\u4e09\u5b63"
        ],
        [
          "http://www.imomoe.io/view/1798.html",
          "http://pic.xiaomingming.org/FileUpload/5101.jpg",
          "\u5047\u9762\u9a91\u58ebDrive"
        ],
        [
          "http://www.imomoe.io/view/7750.html",
          "http://p.xiaomingming.org/FileUpload/2019111122442461901.jpg",
          "\u5f02\u79cd\u65cf\u98ce\u4fd7\u5a18\u8bc4\u9274\u6307\u5357"
        ],
        [
          "http://www.imomoe.io/view/7720.html",
          "http://p.xiaomingming.org/FileUpload/20199922215692206.jpg",
          "\u795e\u7530\u5dddJET GIRLS"
        ],
        [
          "http://www.imomoe.io/view/7718.html",
          "http://p.xiaomingming.org/FileUpload/20199920393374703.jpg",
          "\u6211\u4eec\u65e0\u6cd5\u4e00\u8d77\u5b66\u4e60\u7b2c\u4e8c\u5b63"
        ],
        [
          "http://www.imomoe.io/view/1798.html",
          "http://pic.xiaomingming.org/FileUpload/5101.jpg",
          "\u5047\u9762\u9a91\u58ebDrive"
        ],
        [
          "http://www.imomoe.io/view/1801.html",
          "http://pic.xiaomingming.org/FileUpload/5099.jpg",
          "JOJO\u7684\u5947\u5999\u5192\u9669"
        ],
        [
          "http://www.imomoe.io/view/1803.html",
          "http://pic.xiaomingming.org/FileUpload/5089.jpg",
          "\u795e\u9e64\u4e39\u4e39"
        ],
        [
          "http://www.imomoe.io/view/7749.html",
          "http://p.xiaomingming.org/FileUpload/201911112238876017.jpg",
          "\u522b\u5bf9\u6620\u50cf\u7814\u51fa\u624b\uff01"
        ],
        [
          "http://www.imomoe.io/view/7766.html",
          "http://p.xiaomingming.org/FileUpload/201911182236733439.jpg",
          "\u6392\u7403\u5c11\u5e74\u7b2c\u56db\u5b63"
        ],
        [
          "http://www.imomoe.io/view/7557.html",
          "http://p.xiaomingming.org/FileUpload/20188211958955513.jpg",
          "\u661f\u5408\u4e4b\u7a7a"
        ],
        [
          "http://www.imomoe.io/view/7746.html",
          "http://p.xiaomingming.org/FileUpload/201911918442699906.jpg",
          "\u7ec7\u7530\u8089\u6842\u4fe1\u957f"
        ],
        [
          "http://www.imomoe.io/view/1800.html",
          "http://pic.xiaomingming.org/FileUpload/5090.jpg",
          "\u8336\u554a\u4e8c\u4e2d"
        ],
        [
          "http://www.imomoe.io/view/7762.html",
          "http://p.xiaomingming.org/FileUpload/201911186583395587.jpg",
          "Megalo Box\u7b2c\u4e8c\u5b63"
        ],
        [
          "http://www.imomoe.io/view/7663.html",
          "http://p.xiaomingming.org/FileUpload/201932119594599424.jpg",
          "\u9ad8\u5206\u5c11\u5973\u7b2c\u4e8c\u5b63"
        ],
        [
          "http://www.imomoe.io/view/7715.html",
          "http://p.xiaomingming.org/FileUpload/201994227660185.jpg",
          "\u5165\u95f4\u540c\u5b66\u5165\u9b54\u4e86\uff01"
        ],
        [
          "http://www.imomoe.io/view/7747.html",
          "http://p.xiaomingming.org/FileUpload/201911918482064452.jpg",
          "\u5730\u7f1a\u5c11\u5e74\u82b1\u5b50\u541b"
        ],
        [
          "http://www.imomoe.io/view/7388.html",
          "http://p.xiaomingming.org/FileUpload/20199422294586636.jpg",
          "\u7bee\u7403\u5c11\u5e74\u738b"
        ],
        [
          "http://www.imomoe.io/view/1796.html",
          "http://pic.xiaomingming.org/FileUpload/5111.jpg",
          "\u866b\u5e08\u7eed\u7ae0\u7b2c\u4e8c\u5b63"
        ],
        [
          "http://www.imomoe.io/view/1797.html",
          "http://pic.xiaomingming.org/FileUpload/5102.jpg",
          "\u795e\u9a6c\u9547\u7684\u6d6e\u4e91\u8857"
        ],
        [
          "http://www.imomoe.io/view/189.html",
          "http://pic.xiaomingming.org/FileUpload/2050.jpg",
          "\u6d77\u8d3c\u738b"
        ],
        [
          "http://www.imomoe.io/view/1796.html",
          "http://pic.xiaomingming.org/FileUpload/5111.jpg",
          "\u866b\u5e08\u7eed\u7ae0\u7b2c\u4e8c\u5b63"
        ],
        [
          "http://www.imomoe.io/view/7721.html",
          "http://p.xiaomingming.org/FileUpload/2019910106078789.jpg",
          "\u673a\u7532\u82f1\u96c4 \u673a\u6597\u52c7\u8005"
        ],
        [
          "http://www.imomoe.io/view/1797.html",
          "http://pic.xiaomingming.org/FileUpload/5102.jpg",
          "\u795e\u9a6c\u9547\u7684\u6d6e\u4e91\u8857"
        ],
        [
          "http://www.imomoe.io/view/1806.html",
          "http://pic.xiaomingming.org/FileUpload/5088.jpg",
          "\u9b41\u62d43\u6218\u795e\u5d1b\u8d77"
        ],
        [
          "http://www.imomoe.io/view/7728.html",
          "http://p.xiaomingming.org/FileUpload/201992019244496383.jpg",
          "\u7f8e\u5999\u5c04\u51fb\u90e8"
        ],
        [
          "http://www.imomoe.io/view/1803.html",
          "http://pic.xiaomingming.org/FileUpload/5089.jpg",
          "\u795e\u9e64\u4e39\u4e39"
        ],
        [
          "http://www.imomoe.io/view/7709.html",
          "http://p.xiaomingming.org/FileUpload/20197315274233668.jpg",
          "TRY KNIGHTS"
        ],
        [
          "http://www.imomoe.io/view/1805.html",
          "http://pic.xiaomingming.org/FileUpload/5079.jpg",
          "\u5076\u50cf\u6d3b\u52a8\u7b2c\u4e09\u5b63"
        ],
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
        ],
        [
          "http://www.imomoe.io/view/7761.html",
          "http://p.xiaomingming.org/FileUpload/20191118651089098.jpg",
          "number24"
        ],
        [
          "http://www.imomoe.io/view/1800.html",
          "http://pic.xiaomingming.org/FileUpload/5090.jpg",
          "\u8336\u554a\u4e8c\u4e2d"
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