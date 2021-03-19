+++
type = "question"
title = "WiFi transfer issue causes loss of data after retransmission request"
description = '''On my late 2011 Macbook pro (running OSX 10.9) a connection to a device that is streaming physiologic data can be established via an adhoc wifi network. Everything is running fine, i.e., data is correctly streamed, however, after some random time interval (in the range of 10-60 minutes) suddenly the...'''
date = "2014-05-04T08:50:00Z"
lastmod = "2014-05-04T15:43:00Z"
weight = 32483
keywords = [ "wifi", "retransmission", "acknowledge" ]
aliases = [ "/questions/32483" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [WiFi transfer issue causes loss of data after retransmission request](/questions/32483/wifi-transfer-issue-causes-loss-of-data-after-retransmission-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32483-score" class="post-score" title="current number of votes">0</div><span id="post-32483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On my late 2011 Macbook pro (running OSX 10.9) a connection to a device that is streaming physiologic data can be established via an adhoc wifi network. Everything is running fine, i.e., data is correctly streamed, however, after some random time interval (in the range of 10-60 minutes) suddenly the wifi network entirely stops doing anything for a period of approximately 3 seconds and then continues working again. However, unfortunately at that moment physiologic data has been lost. Monitoring the incoming and outgoing TCP packets revealed the information shown below. After t=1459 s. (frame number 419728) there is a silent traffic period where no packets arrive at all. Anybody an idea what might cause the issue and more important how can it be solved?</p><p>Thanks in advance! Philip</p><pre><code>No.     Time           Source                Destination           Protocol Length Info

 419719 1458.952962000 10.11.12.13           10.11.12.14           TCP      806    4242 &gt; 49977 [PSH, ACK] Seq=125104919 Ack=843 Win=3600 Len=752

 419720 1458.952983000 10.11.12.14           10.11.12.13           TCP      54     49977 &gt; 4242 [ACK] Seq=843 Ack=125105671 Win=65535 Len=0

 419721 1458.983557000 10.11.12.13           10.11.12.14           TCP      1514   [TCP Previous segment not captured] 4242 &gt; 49977 [ACK] Seq=125106207 Ack=843 Win=3600 Len=1460

 419722 1458.983630000 10.11.12.14           10.11.12.13           TCP      54     [TCP Dup ACK 419720#1] 49977 &gt; 4242 [ACK] Seq=843 Ack=125105671 Win=65535 Len=0

 419723 1458.983921000 10.11.12.13           10.11.12.14           TCP      1514   4242 &gt; 49977 [ACK] Seq=125107667 Ack=843 Win=3600 Len=1460

 419724 1458.983947000 10.11.12.14           10.11.12.13           TCP      54     [TCP Dup ACK 419720#2] 49977 &gt; 4242 [ACK] Seq=843 Ack=125105671 Win=65535 Len=0

 419725 1458.999807000 10.11.12.13           10.11.12.14           TCP      1514   4242 &gt; 49977 [ACK] Seq=125109127 Ack=843 Win=3600 Len=1460

 419726 1458.999863000 10.11.12.14           10.11.12.13           TCP      54     [TCP Dup ACK 419720#3] 49977 &gt; 4242 [ACK] Seq=843 Ack=125105671 Win=65535 Len=0

 419727 1459.002706000 10.11.12.13           10.11.12.14           TCP      1514   [TCP Fast Retransmission] 4242 &gt; 49977 [ACK] Seq=125105671 Ack=843 Win=3600 Len=1460

 419728 1459.002751000 10.11.12.14           10.11.12.13           TCP      54     49977 &gt; 4242 [ACK] Seq=843 Ack=125107131 Win=65535 Len=0

 419729 1461.982928000 10.11.12.13           10.11.12.14           TCP      1514   [TCP Retransmission] 4242 &gt; 49977 [ACK] Seq=125107131 Ack=843 Win=3600 Len=1460

 419730 1461.983046000 10.11.12.14           10.11.12.13           TCP      54     49977 &gt; 4242 [ACK] Seq=843 Ack=125110587 Win=65535 Len=0

 419731 1461.983110000 10.11.12.14           10.11.12.13           TCP      60     49977 &gt; 4242 [PSH, ACK] Seq=843 Ack=125110587 Win=65535 Len=6

 419732 1461.986651000 10.11.12.13           10.11.12.14           TCP      1514   4242 &gt; 49977 [ACK] Seq=125110587 Ack=843 Win=3600 Len=1460</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span> <span class="post-tag tag-link-acknowledge" rel="tag" title="see questions tagged &#39;acknowledge&#39;">acknowledge</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 May '14, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/bf1f1392c1ad16404b666b3f7dfeb342?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phpvdb&#39;s gravatar image" /><p><span>phpvdb</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phpvdb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 May '14, 11:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-32483" class="comments-container"></div><div id="comment-tools-32483" class="comment-tools"></div><div class="clear"></div><div id="comment-32483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32486"></span>

<div id="answer-container-32486" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32486-score" class="post-score" title="current number of votes">0</div><span id="post-32486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Anybody an idea <strong>what might cause the issue</strong> and more important how can it be solved?</p></blockquote><p>Well ... That could be almost anything.</p><ul><li>the client stops sending or processing data due to a bug or overload</li><li>the server stops sending or processing data due to a bug or overload</li><li>there is packet loss due to a bug or overload in a network device (switch, router, firewall, etc.)</li><li>there is packet loss in the wifi/wlan network due to a bug or overload of the wifi/wlan AP/router, or one of the clients in your <strong>adhoc</strong> wifi network</li><li>there is packet loss in the wifi/wlan network due to interfering radiation (microwave, other medical devices), disturbing the wifi/wlan signals</li><li>there is packet loss in the wifi/wlan network because the radios signal gets absorbed by something with a lot of water in it (like a 'heavy' person sitting between the AP and the wifi/wlan clients - don't laugh, I have seen that in the field ;-))</li></ul><p>The list goes on and on.</p><p>Unfortunately the '[TCP Retransmission]' shown in your capture output could have several of the reasons mentioned above.</p><p>So, you should try to eliminate some things by applying logic and/or by doing tests to rule out</p><ul><li>the wifi/wlan network</li><li>the client and/or server</li><li>the network</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '14, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 May '14, 11:05</strong> </span></p></div></div><div id="comments-container-32486" class="comments-container"><span id="32508"></span><div id="comment-32508" class="comment"><div id="post-32508-score" class="comment-score"></div><div class="comment-text"><p>Thank you Kurt for your detailed answer and suggestions. I was wondering, could there also be a (Mac OS X related) setting that might cause the network to "stop" (between packet numbers 419728 and 419729) for about 3 seconds (for example scanning for new wifi networks), assuming both sender and receiver are still actively sending and receiving data?</p><p>Regards Philip</p></div><div id="comment-32508-info" class="comment-info"><span class="comment-age">(04 May '14, 14:32)</span> <span class="comment-user userinfo">phpvdb</span></div></div><span id="32509"></span><div id="comment-32509" class="comment"><div id="post-32509-score" class="comment-score"></div><div class="comment-text"><p>Well, everything seems possible. <strong>However</strong> if that was standard behavior, one would have heard of that earlier, so I don't think that's the reason. On the other side, ad-hoc networks are not that common, so maybe it is standard behavior. Sorry, never heard of it.</p><p>Can you use ethernet instead of wifi/wlan to rule out the wireless network as the source of the problem?</p></div><div id="comment-32509-info" class="comment-info"><span class="comment-age">(04 May '14, 15:43)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32486" class="comment-tools"></div><div class="clear"></div><div id="comment-32486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

