+++
type = "question"
title = "HTTP 400 Status Code response from Apache to a client"
description = '''A Wireshark was taken simultanously at both sides:  ========= Trace at the client ============  ------------ 08:18:01h -------------------- 1181 :01.766 SYN [204-&amp;gt; 53] 1186 :01.841 SYN,ACK [204 &amp;lt;-53] ACK to segment in frame 1181  1187 :01.841 ACK [204-&amp;gt; 53] ACK to segment in frame 1186 1188...'''
date = "2014-03-29T17:45:00Z"
lastmod = "2014-03-29T23:24:00Z"
weight = 31289
keywords = [ "http", "400" ]
aliases = [ "/questions/31289" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP 400 Status Code response from Apache to a client](/questions/31289/http-400-status-code-response-from-apache-to-a-client)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31289-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A Wireshark was taken simultanously at both sides:</p><pre><code>    ========= Trace at the client ============ 
------------ 08:18:01h --------------------
1181  :01.766 SYN     [204-&gt; 53]
1186  :01.841 SYN,ACK [204 &lt;-53] ACK to segment in frame 1181 
1187  :01.841 ACK     [204-&gt; 53] ACK to segment in frame 1186
1188  :01.842 PSH,ACK [204-&gt; 53] SEQ=1, Next SEQ=1965, ACK=1
1189  :01.917 ACK     [204 &lt;-53] SEQ=1, ACK=1381
1190  :01.917 ACK     [204 &lt;-53] SEQ=1, ACK=1965 ACK to segment in frame 1188

========= Trace at the server ==============
------------ 08:18:01h --------------------
11942 :01.998 SYN     [204-&gt; 53]
11943 :01.998 SYN,ACK [204 &lt;-53] ACK to segment in frame 11942
11944 :02.073 ACK     [204-&gt; 53] ACK to segment in frame 11943
11945 :02.074 ACK     [204-&gt; 53] SEQ=1, Next SEQ=1381, ACK=1
11946 :02.074 PSH,ACK [204-&gt; 53] SEQ=1381, Next SEQ=1965, ACK=1
11947 :02.075 ACK     [204-&gt; 53] SEQ=1, ACK=678943619 ACKs a segment not seen 
11948 :02.076 ACK     [204-&gt; 53] SEQ=1, Next SEQ=1381, ACK=678953619
11949 :02.076 PSH,ACK [204-&gt; 53] SEQ=1381, Next SEQ=1965, ACK=678953619 
11950 :02.076 ACK     [204 &lt;-53] SEQ=1, ACK=1965 ACK to segment in frame 11946
11951  ???
11952  ???
------------ 08:23:02h --------------------
12453 02.145 FIN-ACK  [204 &lt;-53]</code></pre></div><div id="question-tags" class="tags-container tags">http 400</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '14, 17:45</strong></p><img src="https://secure.gravatar.com/avatar/90c9a2a4b7db59e1026f39af5e1e9bbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hflinn&#39;s gravatar image" /><p>hflinn<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hflinn has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Mar '14, 23:11</p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span></p></div></div><div id="comments-container-31289" class="comments-container"><span id="31290"></span><div id="comment-31290" class="comment"><div id="post-31290-score" class="comment-score"></div><div class="comment-text"><p>And your question is why does the Apache send an "HTTP-400 Bad Request" message?</p></div><div id="comment-31290-info" class="comment-info"><span class="comment-age">(29 Mar '14, 22:36)</span> mrEEde</div></div><span id="31292"></span><div id="comment-31292" class="comment"><div id="post-31292-score" class="comment-score"></div><div class="comment-text"><p>I have uploaded 'workstation_tcp_stream_16.pcapng' and 'Apache_tcp_stream_56.cap'. Note there are 6 network hops from the client workstation to the Apache network side. The client was sending an HTTP POST.</p><p>Any help would be appreciated.</p></div><div id="comment-31292-info" class="comment-info"><span class="comment-age">(30 Mar '14, 10:02)</span> hflinn</div></div><span id="31293"></span><div id="comment-31293" class="comment"><div id="post-31293-score" class="comment-score"></div><div class="comment-text"><p>You need to provide the full URL to each file.</p></div><div id="comment-31293-info" class="comment-info"><span class="comment-age">(30 Mar '14, 11:25)</span> mrEEde</div></div><span id="31296"></span><div id="comment-31296" class="comment"><div id="post-31296-score" class="comment-score"></div><div class="comment-text"><p>[Answer converted to a comment given the way ask.wireshark.org works; Please see the FAQ].</p><p>Workstation capture: <a href="https://www.cloudshark.org/captures/60d79fdf73de">https://www.cloudshark.org/captures/60d79fdf73de</a></p><p>Apache capture: <a href="https://www.cloudshark.org/captures/5f0a5ec3eab2">https://www.cloudshark.org/captures/5f0a5ec3eab2</a></p></div><div id="comment-31296-info" class="comment-info"><span class="comment-age">(30 Mar '14, 13:43)</span> hflinn</div></div></div><div id="comment-tools-31289" class="comment-tools"></div><div class="clear"></div><div id="comment-31289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31291"></span>

<div id="answer-container-31291" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31291-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>With the information provided - which does not show the HTTP 400 message and is very confusing in the way you provided it (I changed the formatting a bit)- this can only be guesswork. Here's my interpretation of what is happening. There is a device that is duplicating the client's packets which may confuse the server.<br />
<img src="https://osqa-ask.wireshark.org/upfiles/Selection_002_1.jpeg" alt="alt text" /></p><p>If you need more explanation, please put the traces filtered on the TCP sessions at each side to <a href="http://cloudshark.org"></a><a href="http://cloudshark.org">http://cloudshark.org</a>.</p><hr /><p>After looking at the full traces I think the problem is an incorrect Content-length field inthe client's POST request.</p><p>Both, wireshark and the Apache Webserver, expect more data. The webserver sends back the following message after waiting for 5 minutes.<br />
</p><pre><code>Failure of server APACHE bridge:
Error reading POST data from client</code></pre><p>Wireshark fails to interpret the POST request unless you change preferences for HTTP protocol to not "Reassemble HTTP bodiess ...". Doing so it will find a <strong>[truncated]</strong> cookie indicating there's more data than what's actually contained in the segment. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_043_2.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '14, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 30 Mar '14, 22:17</p></div></div><div id="comments-container-31291" class="comments-container"></div><div id="comment-tools-31291" class="comment-tools"></div><div class="clear"></div><div id="comment-31291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

