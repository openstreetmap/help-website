+++
type = "question"
title = "Problem with our Web site"
description = '''Thank you. I have a small Web site that makes a Ajax &quot;GET&quot; request every 200ms to a Web server. The Web site wait for a small document (750 bytes) from the server, it displays the document data before to send a new request to the server.  The document is updated periodically every 200ms by another p...'''
date = "2013-01-18T06:41:00Z"
lastmod = "2013-01-30T01:10:00Z"
weight = 17776
keywords = [ "http" ]
aliases = [ "/questions/17776" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Problem with our Web site](/questions/17776/problem-with-our-web-site)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17776-score" class="post-score" title="current number of votes">0</div><span id="post-17776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Thank you. I have a small Web site that makes a Ajax "GET" request every 200ms to a Web server. The Web site wait for a small document (750 bytes) from the server, it displays the document data before to send a new request to the server. The document is updated periodically every 200ms by another process (priority superior than web server'one). There is no synchronization between two processes. So, the reading task (web server) may be interrupted from time to time by the writing task, but not for long time. The data in the document could be error some times, but it is not a big problem, because the data is only for display, in addition we check data and display only if data is good. The problem is that our application is stopped after some hours of run, and always after reception of a "Continuation or non-HTTP traffic" packet. And the web site doesn't know to detect this case. As the packet "says" the data is not finished, it is keeped to wait some packets more that never arrive, so it is blocked. I think it is an error coming from the server side, but is it possible to fix it in the web site or not ? Case OK from Wireshark (during some hours) :</p><pre><code>HTTP/1.1 200 OK (application/octet-stream)</code></pre><p>case not OK from Whireshark :</p><pre><code>HTTP/1.1 200 OK (application/octet-stream)
Continuation or non-HTTP traffic.</code></pre><p>Following is the source code of the web site :</p><pre><code>&lt;!DOCTYPE html PUBLIC &quot;-//W3C//DTD XHTML 1.0 Transitional//EN&quot; &quot;http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd&quot;&gt;
&lt;html xmlns=&quot;http://www.w3.org/1999/xhtml&quot; xml:lang=&quot;en&quot; lang=&quot;en&quot;&gt;
&lt;head&gt;
&lt;title&gt;XPS-Q8 - Test AJAX&lt;/title&gt;
&lt;meta http-equiv=&quot;Content-Type&quot; content=&quot;text/html;charset=ISO-8859-1&quot; /&gt;
&lt;script type=&quot;text/javascript&quot;&gt;

var req=null;
var timeout=null;
function requestGetAJAX()
{
document.FP_MoveFormRefresh.test2.value = &quot;-1  -1&quot;;
timeout=null;
var url = &quot;/lnkXpsdata.json?nocache=&quot; + Math.random();
req=createRequest();
req.onreadystatechange=stateChange;
req.open(&quot;GET&quot;, url, true);
req.send(null);
timeout=setTimeout(&quot;treatmentTimeout()&quot;, 5000);
}
function treatmentTimeout()
{
req.abort();
document.FP_MoveFormRefresh.test.value = &quot;Ajax request timeout&quot;;
requestGetAJAX();
}
function treatmentDataError()
{
req.abort();
requestGetAJAX();
}
function treatmentDataOK()
{
req.abort();
requestGetAJAX();
}
function createRequest()
{
var request=null;
if (window.XMLHttpRequest) {
    request=new XMLHttpRequest();
    if (request.overrideMimeType)
        request.overrideMimeType(&quot;text/xml&quot;);
}
else if (window.ActiveXObject) {
    try {
        request=new ActiveXObject(&quot;Msxml2.XMLHTTP&quot;);
    }
    catch(e) {
        try {
            request=new ActiveXObject(&quot;Microsoft.XMLHTTP&quot;);
        }
        catch(e) {
            alert(&quot;Browser doesn&#39;t support AJAX&quot;);
        }
    }
}
return request;
}
function stateChange(dataText)
{
document.FP_MoveFormRefresh.test2.value = req.readyState + &quot;  &quot; + req.status;
if(req.readyState == 4) {
    if(req.status == 200) {
        if(timeout != null) {
            clearTimeout(timeout);
            timeout=null;
        }
        if(req.getResponseHeader(&quot;Content-Length&quot;) &gt; 0) {
            if((req.responseText.indexOf(&quot;{\n&quot;) &gt;= 0) &amp;&amp; (req.responseText.indexOf(&quot;]\n}&quot;) &gt; 0)) {
                var contenttype=req.getResponseHeader(&quot;Content-Type&quot;);
                if(contenttype.indexOf(&quot;Continuation or non-HTTP traffic&quot;) &gt;= 0) {  &lt;! This line doesn&#39;t work !!!!! /&gt;
                    document.FP_MoveFormRefresh.test.value = &quot;Continu/non-HTTP traffic&quot;;
                    setTimeout(&quot;treatmentDataOK()&quot;, 2000);
                }
                else {
                    document.FP_MoveFormRefresh.test.value = contenttype;
                    parseRequestData(req.responseText);
                    setTimeout(&quot;treatmentDataOK()&quot;, 200);
                }
            }
            else {
                document.FP_MoveFormRefresh.test.value = &quot;Ajax data error&quot;;
                setTimeout(&quot;treatmentDataError()&quot;, 2000);
            }
        }
        else {
            document.FP_MoveFormRefresh.test.value = &quot;Ajax data length zero&quot;;
            setTimeout(&quot;treatmentDataError()&quot;, 2000);
        }
    }
    else {
        document.FP_MoveFormRefresh.test.value = &quot;Error status(!=200)=&quot; + req.status;
        setTimeout(&quot;treatmentDataError()&quot;, 2000);
    }
}
}
function parseRequestData(dataText)
{
var aPos1=null;
aPos1=document.getElementById(&quot;ajpos1&quot;);
var aStat1=null;
aStat1=document.getElementById(&quot;ajstate1&quot;);
var aPos2=null;
aPos2=document.getElementById(&quot;ajpos2&quot;);
var aStat2=null;
aStat2=document.getElementById(&quot;ajstate2&quot;);
var aPos3=null;
aPos3=document.getElementById(&quot;ajpos3&quot;);
var aStat3=null;
aStat3=document.getElementById(&quot;ajstate3&quot;);
var aPos4=null;
aPos4=document.getElementById(&quot;ajpos4&quot;);
var aStat4=null;
aStat4=document.getElementById(&quot;ajstate4&quot;);
var aPos5=null;
aPos5=document.getElementById(&quot;ajpos5&quot;);
var aStat5=null;
aStat5=document.getElementById(&quot;ajstate5&quot;);
var aPos6=null;
aPos6=document.getElementById(&quot;ajpos6&quot;);
var aStat6=null;
aStat6=document.getElementById(&quot;ajstate6&quot;);
var aPos7=null;
aPos7=document.getElementById(&quot;ajpos7&quot;);
var aStat7=null;
aStat7=document.getElementById(&quot;ajstate7&quot;);
var data=null;
data=eval(&quot;(&quot; + dataText + &quot;)&quot;);
if(data != null) {
    if(aPos1 != null)
        aPos1.value=data.positioners[0].position;
    if(aStat1 != null)
        aStat1.value=data.positioners[0].state;
    if(aPos2 != null)
        aPos2.value=data.positioners[1].position;
    if(aStat2 != null)
        aStat2.value=data.positioners[1].state;
    if(aPos3 != null)
        aPos3.value=data.positioners[2].position;
    if(aStat3 != null)
        aStat3.value=data.positioners[2].state;
    if(aPos4 != null)
        aPos4.value=data.positioners[3].position;
    if(aStat4 != null)
        aStat4.value=data.positioners[3].state;
    if(aPos5 != null)
        aPos5.value=data.positioners[4].position;
    if(aStat5 != null)
        aStat5.value=data.positioners[4].state;
    if(aPos6 != null)
        aPos6.value=data.positioners[5].position;
    if(aStat6 != null)
        aStat6.value=data.positioners[5].state;
    if(aPos7 != null)
        aPos7.value=data.positioners[6].position;
    if(aStat7 != null)
        aStat7.value=data.positioners[6].state;
}
}
&lt;/script&gt;
&lt;/head&gt;
&lt;body onload=&quot;requestGetAJAX()&quot;&gt;
&lt;form action=&quot;/cgi-bin/post.cgi&quot; method=&quot;post&quot; name=&quot;FP_MoveFormRefresh&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;step&quot; value=&quot;131&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;numoption&quot; value=&quot;141&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;cmd&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;posStat0&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;posStat1&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;posStat2&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;posStat3&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;posStat4&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;posStat5&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;posStat6&quot; value=&quot;0&quot; /&gt;
&lt;div id=&quot;calqueMoveRefresh&quot;&gt;
&lt;h2&gt;TEST AJAX REQUESTS&lt;/h2&gt;
&lt;table width=&quot;50%&quot; border=&quot;0&quot; cellspacing=&quot;1&quot; cellpadding=&quot;0&quot;&gt;
&lt;tr&gt;
&lt;td&gt;&lt;b&gt;Position&lt;/b&gt;&lt;/td&gt;
&lt;td&gt;&lt;b&gt;State&lt;/b&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;position1&quot; id=&quot;ajpos1&quot; size=&quot;20&quot; value=&quot;0&quot;/&gt;
&lt;/td&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;state1&quot; id=&quot;ajstate1&quot; size=&quot;4&quot; value=&quot;0&quot;/&gt;
&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;position2&quot; id=&quot;ajpos2&quot; size=&quot;20&quot; value=&quot;0&quot;/&gt;
&lt;/td&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;state2&quot; id=&quot;ajstate2&quot; size=&quot;4&quot; value=&quot;0&quot;/&gt;
&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;position3&quot; id=&quot;ajpos3&quot; size=&quot;20&quot; value=&quot;0&quot;/&gt;
&lt;/td&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;state3&quot; id=&quot;ajstate3&quot; size=&quot;4&quot; value=&quot;0&quot;/&gt;
&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;position4&quot; id=&quot;ajpos4&quot; size=&quot;20&quot; value=&quot;0&quot;/&gt;
&lt;/td&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;state4&quot; id=&quot;ajstate4&quot; size=&quot;4&quot; value=&quot;0&quot;/&gt;
&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;position5&quot; id=&quot;ajpos5&quot; size=&quot;20&quot; value=&quot;0&quot;/&gt;
&lt;/td&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;state5&quot; id=&quot;ajstate5&quot; size=&quot;4&quot; value=&quot;0&quot;/&gt;
&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;position6&quot; id=&quot;ajpos6&quot; size=&quot;20&quot; value=&quot;0&quot;/&gt;
&lt;/td&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;state6&quot; id=&quot;ajstate6&quot; size=&quot;4&quot; value=&quot;0&quot;/&gt;
&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;position7&quot; id=&quot;ajpos7&quot; size=&quot;20&quot; value=&quot;0&quot;/&gt;
&lt;/td&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;state7&quot; id=&quot;ajstate7&quot; size=&quot;4&quot; value=&quot;0&quot;/&gt;
&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;br /&gt;
&lt;table width=&quot;50%&quot; border=&quot;0&quot; cellspacing=&quot;1&quot; cellpadding=&quot;0&quot;&gt;
&lt;tr&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;test&quot; size=&quot;50&quot; maxlength=&quot;50&quot; value=&quot;&quot;/&gt;
&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;
&lt;input type=&quot;text&quot; name=&quot;test2&quot; size=&quot;50&quot; maxlength=&quot;50&quot; value=&quot;&quot;/&gt;
&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;br /&gt;
&lt;/table&gt;
&lt;table width=&quot;50%&quot; border=&quot;0&quot; cellspacing=&quot;1&quot; cellpadding=&quot;0&quot;&gt;
&lt;tr&gt;
&lt;td&gt;
&lt;input type=&quot;button&quot; name=&quot;restart&quot; value=&quot;Re-Start&quot; onclick=&quot;requestGetAJAX()&quot;/&gt;
&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;/div&gt;
&lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre><p>Thank you very much for help. NewportMicro</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '13, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/f10a82d78508c185a8fcd3588f9ffab7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NewportMicro&#39;s gravatar image" /><p><span>NewportMicro</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NewportMicro has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jan '13, 10:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-17776" class="comments-container"><span id="18025"></span><div id="comment-18025" class="comment"><div id="post-18025-score" class="comment-score"></div><div class="comment-text"><p>Thank you. It is done. Below is the link :</p><p><a href="http://www.cloudshark.org/captures/c4b78426649d">http://www.cloudshark.org/captures/c4b78426649d</a></p><p>The IP of the Web server target is 192.168.33.242. The IP of the client web site is 192.168.32.109.</p><p>Thank you very much for taking a look at it.</p></div><div id="comment-18025-info" class="comment-info"><span class="comment-age">(29 Jan '13, 03:28)</span> <span class="comment-user userinfo">NewportMicro</span></div></div><span id="18029"></span><div id="comment-18029" class="comment"><div id="post-18029-score" class="comment-score"></div><div class="comment-text"><p>I converted your "answer" to a comment as that's how this site works, see the FAQ for more info.</p></div><div id="comment-18029-info" class="comment-info"><span class="comment-age">(29 Jan '13, 03:37)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-17776" class="comment-tools"></div><div class="clear"></div><div id="comment-17776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="17808"></span>

<div id="answer-container-17808" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17808-score" class="post-score" title="current number of votes">0</div><span id="post-17808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="NewportMicro has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>The document is updated periodically every 200ms by another process (priority superior than web server'one). <strong>There is no synchronization</strong> between two processes.</p></blockquote><p>without knowing any details about your OS (realtime or not), and the file update process, I believe you are running</p><ul><li>either into a race condition of the two processes</li><li>or into a bug of the update process</li></ul><p><strong>Race condition:</strong></p><p>One process opens the file for a write operation and possibly writes some bytes, then the next process (web server) opens the file for reading. This will end up in unpredictable results.</p><p>I suggest to redesign the whole process of updating the information in the file. From the information you gave, there <strong>should be</strong> some synchronization between the update process and the web server process.</p><p><strong>Bug of the update process:</strong></p><p>Another possible error could be: the update process itself is buggy and writes a bogus file after some time (did you check that?), which would explain why you run into this only after a few hours.</p><p>As <span><span>@SYN-bit</span></span> said, without a capture file it is hard to analyze. But even <strong>with</strong> a capture file, you may not see the real reason for the problem, without analyzing the problem on the system itself.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '13, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jan '13, 07:40</strong> </span></p></div></div><div id="comments-container-17808" class="comments-container"></div><div id="comment-tools-17808" class="comment-tools"></div><div class="clear"></div><div id="comment-17808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18036"></span>

<div id="answer-container-18036" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18036-score" class="post-score" title="current number of votes">2</div><span id="post-18036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have looked at your tracefile and found the cause of the problem. If you filter with "tcp.stream==1308" you will see that the server responds with a "Content-Length:754" header, while in fact the content is 756 bytes long.</p><p>The webserver should respond with the correct content-length. So you have to be aware that the file can get written to between functions. So if your code looks something like this:</p><pre><code>len=getLengthOfFile(&quot;file&quot;);
printf(&quot;Content-Length: %d\n&quot;, len);
printf(&quot;\r\n\r\n&quot;);
data=readFile(&quot;file&quot;);
printf(&quot;%s&quot;,data);</code></pre><p>You might get into this kind of problem (when a new file is being written between the getLengthOfFile() and readFile()).</p><p>Also, your client code could be made more robust in handling errors and exceptions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18036" class="comments-container"><span id="18080"></span><div id="comment-18080" class="comment"><div id="post-18080-score" class="comment-score"></div><div class="comment-text"><p>Great.</p><p>Thank you very much for the excellent analyse. I will do as you did and then inform to you the result.</p><p>Have a nice day.</p></div><div id="comment-18080-info" class="comment-info"><span class="comment-age">(30 Jan '13, 01:10)</span> <span class="comment-user userinfo">NewportMicro</span></div></div></div><div id="comment-tools-18036" class="comment-tools"></div><div class="clear"></div><div id="comment-18036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17796"></span>

<div id="answer-container-17796" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17796-score" class="post-score" title="current number of votes">0</div><span id="post-17796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I can think of a couple of reasons why wireshark displays the HTTP in those two ways. But I'd like to not guess but look at the packets to determine what the cause might be.</p><p>Could you please post the wireshark pcap file to www.cloudshark.org and paste the link here in a comment?</p><p>(Only if you are not revealing privacy sensitive information in the pcap file)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '13, 01:53</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17796" class="comments-container"><span id="18021"></span><div id="comment-18021" class="comment"><div id="post-18021-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your comments. I tried to upload a pcap file that showing the problem but I don't know how to do. Could you show me how to upload a pcap file to www.cloudshark.org ?</p></div><div id="comment-18021-info" class="comment-info"><span class="comment-age">(29 Jan '13, 00:45)</span> <span class="comment-user userinfo">NewportMicro</span></div></div><span id="18022"></span><div id="comment-18022" class="comment"><div id="post-18022-score" class="comment-score"></div><div class="comment-text"><p>Open 'cloudshark.org' in your browser, click the button (large panel really) with the label "Drag and Drop a capture file to upload" and then a file browser dialog should open which allows you to choose a capture to upload. Post a link back to the uploaded capture file by editing your question, or adding a comment to an existing answer.</p></div><div id="comment-18022-info" class="comment-info"><span class="comment-age">(29 Jan '13, 01:40)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-17796" class="comment-tools"></div><div class="clear"></div><div id="comment-17796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

