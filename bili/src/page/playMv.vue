<template>
  <div>
    <h1>{{ msg }}</h1>
    <button class="btn" v-on:click="getData">搜索</button>

    <video
      id="video"
      class="video-js vjs-default-skin"
      controls
      preload="none"
      width="1200"
      poster="http://pic.xiaomingming.org/FileUpload/2679.jpg"
      data-setup="{}"
      v-bind:src="mvUrl"
    >
      <source type="video/mp4" />
    </video>

    <div id="app">
      <ul>
        <li v-for="(temp, index) in list">
          {{ temp }}
          <b v-bind:href="list[index][1]" v-on:click="select($event)">
            {{ temp[0] }}</b
          >
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import $ from "jquery";
import axios from "axios";

export default {
  name: "playMv",
  data() {
    return {
      mvUrl:
        "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_96dfd26e806dd71dedfcb07a0f76a82d.mp4",
      list: {},
      dmurl: ""
    };
  },
  created() {
    this.getData();
  },

  methods: {
    select: function(event) {
      this.dmurl = this.$route.query.url;
      console.log(this.dmurl);
      console.log("select");
      var el = event.currentTarget;
      this.mvUrl = el.getAttribute("href");
      console.log(this.mvUrl);
    },

    getData: function() {
      this.dmurl = this.$route.query.url;

      console.log("getdata"),
        (this.list = [
          [
            "\\u7B2C01\\u96C6",
            "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_9a062ef59a70061f39bab674a3f15c10.mp4"
          ],
          [
            "\\u7B2C02\\u96C6",
            "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_319878966ecdf3e2e9ba2e9cfff7dd45.mp4"
          ],
          [
            "\\u7B2C03\\u96C6",
            "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_b67957543c14128677cdc09b877bec59.mp4"
          ],
          [
            "\\u7B2C04\\u96C6",
            "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_3928bbf09b9ccac28aa4893c626e6a94.mp4"
          ],
          [
            "\\u7B2C05\\u96C6",
            "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_41be0492da8391c1c57da034ed71b55c.mp4"
          ],
          [
            "\\u7B2C06\\u96C6",
            "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_21639ff3b5eca018eb3565667813fc60.mp4"
          ],
          [
            "\\u7B2C07\\u96C6",
            "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_a07a7b9605d784659c003708f6e91f73.mp4"
          ],
          [
            "\\u7B2C08\\u96C6",
            "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_e5ca7cf2c81126ad7a085b8898a795b4.mp4"
          ],
          [
            "\\u7B2C09\\u96C6",
            "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_58cb64da70698447f738f944e3d06566.mp4"
          ],
          [
            "\\u7B2C10\\u96C6",
            "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_da6bb7775de90262d4ac569463edb004.mp4"
          ],
          [
            "\\u7B2C11\\u96C6",
            "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_613dfa604c7bb38e82716ff23e99dd05.mp4"
          ],
          [
            "\\u7B2C12\\u96C6",
            "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_1934c99438d4b994e47971f22879ecd0.mp4"
          ],
          [
            "\\u7B2C01\\u96C6",
            "http://quan.qq.com/video/1098_887dd55ebdeb64b46cddf8453cd8e2c3"
          ],
          [
            "\\u7B2C02\\u96C6",
            "http://quan.qq.com/video/1098_4337887b7dd1ed090d0b859d7c60de83"
          ],
          [
            "\\u7B2C03\\u96C6",
            "http://quan.qq.com/video/1098_ca56e11fb98a2eb87c3e0abe9517f14b"
          ],
          [
            "\\u7B2C04\\u96C6",
            "http://quan.qq.com/video/1098_ee6041fe5f4d4a92060f7d1bbecca7d1"
          ],
          [
            "\\u7B2C05\\u96C6",
            "http://quan.qq.com/video/1098_02a629dd757d68c31d867ee67af16b0e"
          ],
          [
            "\\u7B2C06\\u96C6",
            "http://quan.qq.com/video/1098_7935ddc82f0052152fead8ec7d0410d0"
          ],
          [
            "\\u7B2C07\\u96C6",
            "http://quan.qq.com/video/1098_8c8ba774d344865cf90996ba6eed7c5e"
          ],
          [
            "\\u7B2C08\\u96C6",
            "http://quan.qq.com/video/1098_3729c9ad21ff9f55f49c445e545ce3c4"
          ],
          [
            "\\u7B2C09\\u96C6",
            "http://quan.qq.com/video/1098_236153354b16ac51c6b68fc912f5ee14"
          ],
          [
            "\\u7B2C10\\u96C6",
            "http://quan.qq.com/video/1098_ac7428734cad854f2f100aa33c6b1136"
          ],
          [
            "\\u7B2C11\\u96C6",
            "http://quan.qq.com/video/1098_57b5325773b47113f9f44e4e5012f516"
          ],
          [
            "\\u7B2C12\\u96C6",
            "http://quan.qq.com/video/1098_b19c1edf89369391e0aee5c49da090a8"
          ]
        ]);
      // axios
      //   .get("http://192.168.1.102:8000/viewDm?keyW=" + this.dmurl)
      //   .then(response => {
      //     //如果在手机上访问需要更改域名
      //     console.log(response.data);
      //     console.log(response.data.data);
      //     this.list = response.data.data;
      //   });
    }
  }
};
</script>
