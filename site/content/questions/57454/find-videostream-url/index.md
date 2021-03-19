+++
type = "question"
title = "Find Videostream URl"
description = '''HI I have a chinese ip cam with no software or manual I can view the stream and make changes to settings from ie browser (only) by typing the ip address of the cam. I want to setup the camera to a surveillance program like ispy or genius vision. But i dont know the url of the stream. Can anybody hel...'''
date = "2016-11-18T11:48:00Z"
lastmod = "2016-11-22T10:06:00Z"
weight = 57454
keywords = [ "url", "video", "stream", "ipcan", "address" ]
aliases = [ "/questions/57454" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Find Videostream URl](/questions/57454/find-videostream-url)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57454-score" class="post-score" title="current number of votes">0</div><span id="post-57454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI I have a chinese ip cam with no software or manual I can view the stream and make changes to settings from ie browser (only) by typing the ip address of the cam. I want to setup the camera to a surveillance program like ispy or genius vision. But i dont know the url of the stream. Can anybody help in identifying the Video stream url for the camera? I dont know which protocol is being used.It is supposed to use onvif and http protocols, but not sure. Only i can say is that the compression type is H.264</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-video" rel="tag" title="see questions tagged &#39;video&#39;">video</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-ipcan" rel="tag" title="see questions tagged &#39;ipcan&#39;">ipcan</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '16, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/c9625ca503ebfa2dc13ff34d373747e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="suhail500&#39;s gravatar image" /><p><span>suhail500</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="suhail500 has no accepted answers">0%</span></p></div></div><div id="comments-container-57454" class="comments-container"></div><div id="comment-tools-57454" class="comment-tools"></div><div class="clear"></div><div id="comment-57454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57460"></span>

<div id="answer-container-57460" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57460-score" class="post-score" title="current number of votes">0</div><span id="post-57460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By typing only the camera's IP (ca.me.ra.ip) into the browser window, you tell the browser to send a HTTP GET to url "http://ca.me.ra.ip:80". The camera then provides a html document which contains some text and layout and also the url of the video stream as I assume that it opens as a moving picture on the page. So you can either ask your browser to show you the original html received from the camera (in Mozilla Firefox, use <code>Ctrl+U</code> to open it in a new tab) and then look for the url of the video stream in it, or you can use Wireshark to capture your PC's communication with the camera, open the camera's main page again, and see what further http requests your PC sends after the first GET, or to what port(s) it establishes another TCP session (to see the latter, apply a display filter <code>ip.dst == ca.me.ra.ip and tcp.flags.syn == 1 and tcp.flags.ack == 0</code>). The camera may make analysis of http requests using Wireshark complex if it uses https and/or if it uses an exotic port for the video server, so I'd definitely start by analysing the html of the main page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '16, 00:36</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-57460" class="comments-container"><span id="57552"></span><div id="comment-57552" class="comment"><div id="post-57552-score" class="comment-score"></div><div class="comment-text"><p>Hi Sandy Tkhs 4 the message. Tried the mozilla method , dont know what to make from it. Pasting the code that i got from cntrl+U page. Pls giv ur comments</p><pre><code>&lt;html xmlns=&quot;http://www.w3.org/1999/xhtml&quot;&gt;
&lt;head&gt;
&lt;title&gt;Login&lt;/title&gt;
&lt;script type=&quot;text/javascript&quot; src=&quot;m.jsp&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/javascript&quot; src=&quot;config.js&quot;&gt;&lt;/script&gt;

   &lt;script type=&quot;text/javascript&quot;&gt;
   var gHashCookie = new Hash.Cookie(&#39;NetSuveillanceWebCookie&#39;,{duration: 30});
var settings = {
    username:&#39;&#39;
    }
    function savesetting() 
{

    gHashCookie.extend(settings);

}
var iLanguage=100;
function resizeL(){        

                    $(&#39;username&#39;).setStyle(&#39;width&#39;,InputName.width);
                   $(&#39;username&#39;).setStyle(&#39;height&#39;,InputName.height);   
                   $(&#39;username&#39;).setStyle(&#39;margin-top&#39;,InputName.marginTop);                                          
                   $(&#39;username&#39;).setStyle(&#39;margin-right&#39;,InputName.marginRight);
                   $(&#39;userNameInput&#39;).setStyle(&#39;margin-top&#39;,SpanLoginName.marginTop);       
                   $(&#39;password&#39;).setStyle(&#39;width&#39;,InputPassword.width);
                   $(&#39;password&#39;).setStyle(&#39;height&#39;,InputPassword.height);
                   $(&#39;password&#39;).setStyle(&#39;margin-top&#39;,InputPassword.marginTop);
                   $(&#39;password&#39;).setStyle(&#39;margin-right&#39;,InputPassword.marginRight);                   
                   $(&#39;loginBT&#39;).setStyle(&#39;width&#39;,LoginButton.width);
                   $(&#39;loginBT&#39;).setStyle(&#39;height&#39;,LoginButton.height);                    

                   if(1==LogoNumbers)
                   {
                       $(&quot;logo1&quot;).setStyle(&#39;background&#39;,&#39;none&#39;);
                   }  

                    wwidth =document.documentElement.clientWidth;
                    wheight=document.documentElement.clientHeight;
                    $(&#39;login&#39;).setStyle(&#39;width&#39;,wwidth);

                   $(&#39;lm&#39;).setStyle(&#39;width&#39;,wwidth);

                    if(wwidth&lt;=417)
                    {
                        $(&#39;lmll&#39;).style.width=0;
                        $(&#39;lmrr&#39;).style.width=0;
                        $(&#39;lml&#39;).style.width=0;
                        $(&#39;lmr&#39;).style.widht=0;
                        $(&#39;lmm&#39;).setStyle(&#39;width&#39;,wwidth);

                        $(&#39;ldl&#39;).setStyle(&#39;width&#39;,0)
                        $(&#39;ldm&#39;).setStyle(&#39;width&#39;,wwidth);
                        $(&#39;ldr&#39;).setStyle(&#39;width&#39;,0)
                    }
                    else if(wwidth&lt;=1127)
                   {
                        $(&#39;lmll&#39;).style.width=0;
                        $(&#39;lmrr&#39;).style.width=0;                          
                        $(&#39;lml&#39;).setStyle(&#39;width&#39;,(wwidth-417)/2+(355-(wwidth-417)/2));
                        $(&#39;lml&#39;).setStyle(&#39;margin-left&#39;,-(355-(wwidth-417)/2));
                        $(&#39;lmr&#39;).setStyle(&#39;width&#39;,(wwidth-417)/2);
                        $(&#39;lmm&#39;).setStyle(&#39;width&#39;,417);

                        $(&#39;ldl&#39;).setStyle(&#39;width&#39;,((wwidth-417)/2)-1)
                        $(&#39;ldm&#39;).setStyle(&#39;width&#39;,417);
                        $(&#39;ldr&#39;).setStyle(&#39;width&#39;,(wwidth-(417+(wwidth-417)/2-1)));

                    }
                    else
                    {        

                       $(&#39;lml&#39;).setStyle(&#39;margin-left&#39;,0);

                       $(&#39;lml&#39;).setStyle(&#39;width&#39;,355);                       
                       $(&#39;lmr&#39;).setStyle(&#39;width&#39;,355);
                       $(&#39;lmm&#39;).setStyle(&#39;width&#39;,417);                       

                       $(&#39;ldm&#39;).setStyle(&#39;width&#39;,417);
                       var w=(wwidth-(417+355+355))/2;
                       $(&#39;ldl&#39;).setStyle(&#39;width&#39;,w+355);
                       $(&#39;ldr&#39;).setStyle(&#39;width&#39;,(wwidth-(417+355+w)));                   

                        $(&#39;lmll&#39;).setStyle(&#39;width&#39;,w);  
                        $(&#39;lmrr&#39;).setStyle(&#39;width&#39;,w);                             
                    }

}
window.addEvent(&#39;resize&#39;,function(){
    resizeL();
});
window.addEvent(&#39;domready&#39;,function(){  
 $(&#39;userNameInput&#39;).setText(Translate.usr); 
 $(&#39;passWordInput&#39;).setText(Translate.pswd);
 $(&#39;loginBT&#39;).setText(Translate.login); 
 getsetting();
});

function getsetting(){
            if (gHashCookie.get(&#39;username&#39;)) {
        settings[&#39;username&#39;] = gHashCookie.get(&#39;username&#39;);
    } else {
        settings[&#39;username&#39;] = &#39;&#39;;
    }

    $(&#39;username&#39;).setProperty(&#39;value&#39;, settings[&#39;username&#39;]); 

}

function savename() {
    var username = $(&quot;username&quot;).value;
    settings[&#39;username&#39;] = username;    
    savesetting();

}
   &lt;/script&gt;
&lt;style type=&quot;text/css&quot;&gt;
    *{font-size:12px;margin: 0;padding: 0; color:#fff; font-family:Arial, &quot;ËÎÌå&quot;}
#login {top:0px;position:absolute;width:100%;height:100%;margin:0;padding:0;left:0px;}
    #lx{width:478px;height:186px;margin:auto; margin-top:196px}
    #lb{width:53px;height:186px;background:url(lbbg.jpg);float:left}
    #lc{width:45px;height:186px;background:url(lcbg.jpg);float:left}
    #la{width:380px;height:186px;background:url(labg.jpg);float:left}
        #lal{width:8px; height:186px;float:left;background:url(lal.jpg)}
        #lar{width:24px;height:186px;float:right; background:url(lar.jpg)}
        #lalogo{width:251px;height:37px;position:relative;top:20px;left:11px;background:url(lalogo.jpg)}
        #lainput{width:253px;height:70px;float:left;margin:35px 0 0 5px;}
            #lainput div{width:250px;float:left;margin:5px 0 0 0;text-align:right}
            #lainput span{margin:0 6px 0 0}
            #lainput input{width:130px; height:18px;padding:3px 0 0 0}
            #lainput select{width:133px; height:18px;}
        #labt {width:10px;height:10px;float:left;margin:72px 0 0 0}     
&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
               
            
            
            

        
            
            
            
            
            

                 
                 
                  
                    

                       
                        
                        
                        &lt;form action=&quot;&quot; id=&quot;pass-login-form&quot; name=&quot;pass-login-form&quot; method=&quot;post&quot;&gt;
                          &lt;input type=&quot;hidden&quot; name=&quot;command&quot; value=&quot;login&quot;/&gt;
                        
                        &lt;input id=&quot;username&quot; name=&quot;username&quot; type=&quot;text&quot; style=&quot;color: #000; font-size: 15px; 
                                margin: 0 120px 0 0; padding: 0px 0 0 0px; width: 133px; height: 25px;float:right;&quot; onkeydown=&quot;javascript:if (event.keyCode==13) event.keyCode=9;&quot;/&gt;
                            

                        
                        
                        &lt;input id=&quot;password&quot; name=&quot;password&quot; type=&quot;password&quot; style=&quot;color: #000; font-size: 15px; 
                                margin: 0 120px 0 0; padding: 0px 0 0 0px; width: 133px; height: 25px;float:right;&quot; onkeydown=&quot;javascript:if (event.keyCode==13) savename();&quot;/&gt;
                            
                            

                        
                        
                            &lt;button id=&quot;loginBT&quot; type=&quot;submit&quot; onclick=&quot;savename()&quot; style=&quot;cursor: pointer;margin:25px 0 0 0;color: #000; width: 88px; height: 28px;
                                padding: 4px 0 0 0; border: 0; background: url(bt.gif)&quot;&gt;
                            &lt;/button&gt;
                        
                        &lt;/form&gt;
                      
                                   
                
                  
                

            
            
            
            
            
        
        
            
            
            
            
            
            
            
            
                
    

    &lt;script type=&quot;text/javascript&quot;&gt;
            resizeL();
//             var lang=(navigator.userLanguage||navigator.language).toLowerCase(); 
//             if(lang==&quot;zh-cn&quot;)
//             {
// 
//              $(&quot;userNameInput&quot;).setText(&quot;ÓÃ»§Ãû&quot;);
//              $(&quot;passWordInput&quot;).setText(&quot;ÃÜÂë&quot;);
//              $(&quot;loginBT&quot;).setText(&quot;µÇÂ¼&quot;);
// 
//             }
            switch(iLanguage)
        {
            case 100:
            {
                document.write(&quot;&lt;script src=&quot;English.js&quot;&gt;&lt;\/script&gt;&quot;);
                break;
            }
            case 101:
            {

                document.write(&quot;&lt;script src=&quot;SimpChinese.js&quot;&gt;&lt;\/script&gt;&quot;);
                break;
            }
            default:
            {        
                document.write(&quot;&lt;script src=&quot;English.js&quot;&gt;&lt;\/script&gt;&quot;);
            }

        }            

    &lt;/script&gt;
    &lt;/body&gt;
    &lt;/html&gt;</code></pre></div><div id="comment-57552-info" class="comment-info"><span class="comment-age">(22 Nov '16, 10:06)</span> <span class="comment-user userinfo">suhail500</span></div></div></div><div id="comment-tools-57460" class="comment-tools"></div><div class="clear"></div><div id="comment-57460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

