package com.example.jim60.aiv;

import android.annotation.SuppressLint;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.AsyncTask;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Gravity;
import android.view.Menu;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.widget.ImageButton;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;


import org.eclipse.paho.android.service.MqttAndroidClient;
import org.eclipse.paho.client.mqttv3.*;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;


public class MainActivity extends AppCompatActivity {

    private WebView webview;
    ImageButton imgbtnUp,imgbtnDown,imgbtnRight,imgbtnLeft,imgbtnAuto,imgbtnStop;
    public static String wifiModuleIP = "";
    public static int wifiModulePort = 0;
    public static String CMD = "0";
    String addr = "172.20.10.6";
    String address = addr + ":21567";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        webview = (WebView) findViewById(R.id.webview);
        WebSettings webSettings = webview.getSettings();
        webSettings.setJavaScriptEnabled(true);

        //processConnect(addr, "8080");
        //webview.loadUrl("http://" + addr + ":8080/javascript_simple.html");

        imgbtnUp = (ImageButton) findViewById(R.id.imgbtnUp);
        imgbtnDown = (ImageButton) findViewById(R.id.imgbtnDown);
        imgbtnLeft = (ImageButton) findViewById(R.id.imgbtnLeft);
        imgbtnRight = (ImageButton) findViewById(R.id.imgbtnRight);
        imgbtnAuto = (ImageButton) findViewById(R.id.imgbtnAuto);
        imgbtnStop = (ImageButton) findViewById(R.id.imgbtnStop);

        imgbtnUp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                CMD = "f";
                SendToRaspberryPi();
            }
        });
        imgbtnStop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                CMD = "s";
                SendToRaspberryPi();
            }
        });
        imgbtnAuto.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                CMD = "a";
                SendToRaspberryPi();
            }
        });
        imgbtnRight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                CMD = "r";
                SendToRaspberryPi();
            }
        });
        imgbtnLeft.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                CMD = "l";
                SendToRaspberryPi();
            }
        });
        imgbtnDown.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                CMD = "b";
                SendToRaspberryPi();
            }
        });

        //設定介面與主畫面顯示

        View btn = findViewById(R.id.settingbtn);
        View btn2 = findViewById(R.id.ipOkBtn);
        final View frms = findViewById(R.id.settinglayout);
        final View frmm = findViewById(R.id.mainlayout);
        final TextView textView = findViewById(R.id.txtip);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                frms.bringToFront();
            }
        });
        btn2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                addr = textView.getText().toString();
                webview.loadUrl("http://" + addr + ":8080/javascript_simple.html");
                frmm.bringToFront();
            }
        });
    }

    //取得IP及PORT
    public void getIPandPort()
    {
        String IPandPort = address.toString();
        Log.d("MYTEST","IP String : " + IPandPort);
        String temp[] = IPandPort.split(":");
        wifiModuleIP = temp[0];
        wifiModulePort = Integer.valueOf(temp[1]);
        Log.d("MYTEST","IP : " + wifiModuleIP);
        Log.d("MYTEST","Port : " + wifiModulePort);
    }

    //按下按鈕
    public  void SendToRaspberryPi()
    {
        getIPandPort();
        Sock_AsyncTask cmd_control = new Sock_AsyncTask();
        cmd_control.execute();
    }

    //當按下按鈕背景執行發送訊息
    public class Sock_AsyncTask extends AsyncTask<Void,Void,Void>
    {
        Socket socket;

        @Override
        protected Void doInBackground(Void... voids) {
            try
            {
                InetAddress inetAddress = InetAddress.getByName(MainActivity.wifiModuleIP);
                socket = new java.net.Socket(inetAddress,MainActivity.wifiModulePort);
                DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());
                dataOutputStream.writeBytes(CMD);
                dataOutputStream.close();
                socket.close();
            }
            catch (UnknownHostException e){e.printStackTrace();}
            catch (IOException e){e.printStackTrace();}
            return null;
        }
    }
}
