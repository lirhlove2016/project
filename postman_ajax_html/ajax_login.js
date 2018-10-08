var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://ceshi.farmfriend.com.cn/flyHandApp/api/user/loginPassword",
  "method": "POST",
  "headers": {
    "content-type": "application/x-www-form-urlencoded",
  },
  "data": {
    "phone": "18301212965",
    "password": "123",
    "InviteCode": ""
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});