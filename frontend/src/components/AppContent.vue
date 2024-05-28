<template>
  <div class="container-md mt-5">
    <div class="row">
      <div class="col-sm-6 mb-3 mb-sm-0">
        <figure class="figure">
          <img
            :src="rawImageUrl || defaultImageUrl"
            class="figure-img img-fluid rounded"
            alt="Raw Picture"
          />
          <div class="row">
            <div class="col">
              <input
                type="file"
                ref="upload"
                @change="update"
                style="display: none"
              />
              <button
                type="button"
                class="btn btn-outline-warning"
                @click="trueUpload"
              >
                Choose Img
              </button>
            </div>
            <div class="col">
              <figcaption class="figure-caption text-end">
                Raw Picture
              </figcaption>
            </div>
          </div>
        </figure>
      </div>

      <div class="col-sm-6">
        <figure class="figure">
          <img
            :src="detectedImageUrl || defualtDetectedImageUrl"
            class="figure-img img-fluid rounded"
            alt="..."
          />
          <figcaption class="figure-caption text-end">
            Detected Picture
          </figcaption>
        </figure>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "AppContent",
  data() {
    return {
      rawImageUrl: "",
      detectedImageUrl: "",
      defaultImageUrl: require("E:/yolo/Detection-yolov5/frontend/src/assets/000000000025.jpg"),
      defualtDetectedImageUrl: require("E:/yolo/Detection-yolov5/frontend/src/assets/0000000000251.jpg"),
    };
  },
  methods: {
    trueUpload() {
      this.$refs.upload.click();
    },
    getObjectURL(file) {
      let url = null;
      if (window.createObjectURL != undefined) {
        url = window.createObjectURL(file);
      } else if (window.URL != undefined) {
        url = window.URL.createObjectURL(file);
      } else if (window.webkitURL != undefined) {
        url = window.webkitURL.createObjectURL(file);
      }
      return url;
    },
    update(event) {
      let file = event.target.files[0];
      if (file) {
        this.rawImageUrl = this.getObjectURL(file);
        let formData = new FormData();
        formData.append("file", file);

        axios
          .post("http://127.0.0.1:5003/upload", formData, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          })
          .then((response) => {
            if (response.data.status === 1) {
              this.detectedImageUrl = response.data.draw_url;
            } else {
              alert("File upload failed");
            }
          })
          .catch((error) => {
            console.error("There was an error!", error);
          });
      }
    },
  },
};
</script>
<style scoped></style>
