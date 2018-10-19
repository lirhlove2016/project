package test.com.okhttp.test;

import com.squareup.okhttp.*;

import java.io.IOException;

/**
 * okhttp,get,post
 */
public class Test_okhttp001
{
    public static final MediaType JSON = MediaType.parse("application/json; charset=utf-8");
    //post
    public String post(OkHttpClient client, String url) throws IOException
    {
        Request request = new Request.Builder()
                .url(url)
                .post(new FormEncodingBuilder()
                        .add("userName", "lirunhua")  //参数1
                        .add("passWord", "12345")  //参数二,
                        .build())
                .build();
        Response response = client.newCall(request).execute();
        return response.body().string();
    }
    //get
    public String get(OkHttpClient client, String url) throws IOException {
        Request request = new Request.Builder().url(url).build();
        Response response = client.newCall(request).execute();
        return response.body().string();
    }

    //main
    public static void main(String[] args)
    {
        //调用get
        System.out.println("--------this is get request-----------------");
        OkHttpClient client = new OkHttpClient();
        try
        {
            String res = new Test_okhttp001().get(client,
                    "http://www.baidu.com");
            System.out.println(res);
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }

        //调用post
        System.out.println("--------this is post request-----------------");
        //OkHttpClient client = new OkHttpClient();
        try
        {
            String res = new Test_okhttp001().post(client,
                    "http://ceshi.farmfriend.com.cn/reapermanager/sys/login");
            System.out.println(res);
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }

    }
}