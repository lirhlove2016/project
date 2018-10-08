//<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://dev01.bdhlan.com:8080/bdhsystem/farmplantend/farmlands/725e0f5e66fe4a17b64114e0474b86e3",
  "method": "PUT",
  "headers": {
    "content-type": "application/json",
    "bdhauthorization": "B94ftK1WY6JSUe7hBTfmgOsGckPFbW8dRASuVNQ52ag5f9pS//4V5E66NZNgQq9tnw2GwdcnZgG7Nz6SEv/klZB+VHjS3DzMCKDb92L",
    "cache-control": "no-cache",
    "postman-token": "27e6fa0a-1092-9745-0aff-5ae0817d404b"
  },
  "processData": false,
  "data": "{ \"farmlandName\": \"3号地块\", \"farmlandArea\": \"10\", \"type\": 1, \"farmlandLevel\": 2, \"farmlandSoilQuality\": 2, \"pictures\": [ \"http://farmlandbucketstest.oss-cn-beijing.aliyuncs.com/21B7F1920D734078898AD63088736D55\" ], \"userId\": \"1\", \"otherInstructions\": \"\" }"
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
