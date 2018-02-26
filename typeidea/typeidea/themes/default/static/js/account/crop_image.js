$(function() {
    $("#id_avatar").change(function () {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $("#image").attr("src", e.target.result);
                $("#modalCrop").modal("show");
            }
            reader.readAsDataURL(this.files[0]);
        }
    });

    var $image = $("#image");
    var cropBoxData;
    var canvasData;
    $("#modalCrop").on("shown.bs.modal", function () {
        $image.cropper({
            viewModel: 1,
            aspectRatio: 1/1,
            minCropBoxWidth: 200,
            minCropBoxHeight: 200,
        });
    }).on("hidden.bs.modal", function() {
        $image.cropper("destroy");
    }); 

    $(".js-crop-and-upload").click(function () {
        var cropData = $image.cropper("getData");
        var form = $("#formUpload");
        $("#id_x").val(cropData["x"]);
        $("#id_y").val(cropData["y"]);
        $("#id_height").val(cropData["height"]);
        $("#id_width").val(cropData["width"]);

        $.ajax({
            url: form.attr("crop-image-url"),
            type: "POST",
            data:  new FormData(form[0]),
            cache: false,
            contentType: false,
            processData:false,
            success: function (data) {
                $(".rounded-circle").attr('src', data.image_url + "?t=" + data.random);
                $("#modalCrop").modal('hide');
            },
            error: function()   {
                alert('图片上传出现一些问题，请选择其他图片上传,可能的问题\n 1. 图片太大\n 2. 文件文太长');
                $("#modalCrop").modal('hide');
            }
        });

        return false
    });

});
