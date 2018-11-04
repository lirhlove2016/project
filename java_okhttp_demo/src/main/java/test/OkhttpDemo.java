package test;

import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;

import java.io.IOException;
import java.util.concurrent.TimeUnit;

public class OkhttpDemo {

    public String run(OkHttpClient client, String url) throws IOException {
        Request request = new Request.Builder().url(url).build();

        Response response = client.newCall(request).execute();
        return response.body().string();
    }
    public static void main( String[] args )
    {
        OkHttpClient client = new OkHttpClient();
        try
        {
            String res = new OkhttpDemo().run(client, "http://www.baidu.com");
            System.out.println(res);
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }

    }

}
