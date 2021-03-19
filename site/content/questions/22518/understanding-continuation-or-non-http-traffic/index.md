+++
type = "question"
title = "Understanding Continuation or non-HTTP traffic"
description = '''I&#x27;m writing some code to integrate an in-house app into a DVR to retrieve a video file. This is all reverse engineered as there isn&#x27;t any official documentation, and I&#x27;m having trouble understanding the following sequence of events (captured by playing with the DVR&#x27;s Android app). 936 72.985204 192....'''
date = "2013-07-01T12:57:00Z"
lastmod = "2013-07-01T13:27:00Z"
weight = 22518
keywords = [ "continuation", "post", "http" ]
aliases = [ "/questions/22518" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Understanding Continuation or non-HTTP traffic](/questions/22518/understanding-continuation-or-non-http-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22518-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing some code to integrate an in-house app into a DVR to retrieve a video file. This is all reverse engineered as there isn't any official documentation, and I'm having trouble understanding the following sequence of events (captured by playing with the DVR's Android app).</p><pre><code>936 72.985204   192.168.0.1     192.168.0.200   HTTP    468     POST /cgi-bin/supervisor/NetworkBk.cgi HTTP/1.1  (application/x-www-form-urlencoded)
937 72.985368   192.168.0.200   192.168.0.1     TCP     54      mit-ml-dev &gt; 41859 [ACK] Seq=1 Ack=415 Win=65535 Len=0
938 73.933676   192.168.0.200   192.168.0.1     HTTP    275     HTTP/1.0 200 OK  (video/mpeg4)
939 73.933983   192.168.0.1     192.168.0.200   TCP     54      41859 &gt; mit-ml-dev [ACK] Seq=415 Ack=222 Win=15544 Len=0
940 74.004433   192.168.0.200   192.168.0.1     TCP     74      [TCP segment of a reassembled PDU]
941 74.004887   192.168.0.1     192.168.0.200   TCP     54      41859 &gt; mit-ml-dev [ACK] Seq=415 Ack=242 Win=15544 Len=0
942 74.024669   192.168.0.200   192.168.0.1     HTTP    1346    Continuation or non-HTTP traffic</code></pre><p>The HTTP POST requests the video file, which then results in an HTTP 200 response consisting of the string "OK". I get confused as to what happens next. It looks like the video file comes later as part of the Continuation or non-HTTP traffic as I get a lot of these. Isn't the request complete when the HTTP 200 response is received? Why then is it continuing to receive TCP data and then getting a HTTP Continuation or non-HTTP traffic? The subsequent TCP packets contain the video file I'm intending to download. When I manually craft a HTTP POST I get the HTTP OK response and then I'm stumped. How do I access the non-HTTP packets?</p><p>This is the code I use to simulate the HTTP POST.</p><pre><code>import requests
dc = {&quot;action&quot;:&quot;download&quot;, &quot;start_time&quot;:&quot;2013 7 1 13 59 00&quot;, &quot;end_time&quot;:&quot;2013 7 14 3 0&quot;, &quot;num&quot;:&quot;255&quot;, &quot;ch&quot;:&quot;5&quot;}
r = requests.post(&quot;http://192.168.0.200/cgi-bin/supervisor/NetworkBk.cgi&quot;, data=dc, auth=(username, password))</code></pre><p>This is the RAW response of the HTTP OK reply. As far as I can tell, there is nothing there about expecting extra content.</p><pre><code>HTTP/1.0 200 OK
Date: Mon, 01 Jul 2013 15:01:34 GMT
nServer: Linux/2.x UPnP/1.0 Avtech/1.0
Expires: 0
Pragma: no-cache
Cache-Control: no-cache
Connection: close
Content-Type: video/mpeg4
Content-Length: 5

0
OK</code></pre><p>What's going on and how do I get to the Continuation or non-HTTP traffic?</p></div><div id="question-tags" class="tags-container tags">continuation post http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '13, 12:57</strong></p><img src="https://secure.gravatar.com/avatar/e949f61d6c30ea44c4f970ffcdc34925?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CadentOrange&#39;s gravatar image" /><p>CadentOrange<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CadentOrange has no accepted answers">0%</span></p></div></div><div id="comments-container-22518" class="comments-container"></div><div id="comment-tools-22518" class="comment-tools"></div><div class="clear"></div><div id="comment-22518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22521"></span>

<div id="answer-container-22521" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22521-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The HTTP data part of the response is:</p><pre><code>0\r\n
OK</code></pre><p>Which is a response of 5 bytes. This is inline with the Content-Length header. The server should not send any more data after these 5 bytes. If it does, it is not following the RFC's. That is probably why Wireshark has some difficulty showing the HTTP data in a normal manner.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '13, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22521" class="comments-container"><span id="22536"></span><div id="comment-22536" class="comment"><div id="post-22536-score" class="comment-score"></div><div class="comment-text"><p>This is what I suspected which would explain why tools like wget and my own Python code don't work as expected.</p></div><div id="comment-22536-info" class="comment-info"><span class="comment-age">(01 Jul '13, 23:49)</span> CadentOrange</div></div></div><div id="comment-tools-22521" class="comment-tools"></div><div class="clear"></div><div id="comment-22521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22520"></span>

<div id="answer-container-22520" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22520-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The 200 OK is HTTPs return code to the request you sent before - if data is to be delivered as part of the requests answer it will immediately start delivering it withing the very same packet containing the HTTP (Response) Header with the Return Code. So the 200 OK is the start of the data transmission following your request</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '13, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-22520" class="comments-container"><span id="22537"></span><div id="comment-22537" class="comment"><div id="post-22537-score" class="comment-score"></div><div class="comment-text"><p>I guess the part that throws me off is that the content of the HTTP OK response is 5 bytes and the connection is closed immediately after. As SYN-bit has said, this is not RFC compliant and is probably why I'm having trouble reading the response with standard tools. It looks like I will have to keep the socket open and read from it once I've got the OK response.</p></div><div id="comment-22537-info" class="comment-info"><span class="comment-age">(01 Jul '13, 23:51)</span> CadentOrange</div></div></div><div id="comment-tools-22520" class="comment-tools"></div><div class="clear"></div><div id="comment-22520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

