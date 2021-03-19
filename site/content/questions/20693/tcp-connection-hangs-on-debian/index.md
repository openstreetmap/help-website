+++
type = "question"
title = "TCP connection hangs on Debian"
description = '''Hi, Some tcp connections hang sometimes and I can&#x27;t find the problem. When Maven is downloading libraries from maven repo, sometimes it blocks in one of the downloads, making the entire build hang. It is difficult to reproduce as it only happens rarely, but I was able to capture it on wireshark (wit...'''
date = "2013-04-22T01:28:00Z"
lastmod = "2013-04-22T01:57:00Z"
weight = 20693
keywords = [ "debian", "hangs" ]
aliases = [ "/questions/20693" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP connection hangs on Debian](/questions/20693/tcp-connection-hangs-on-debian)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20693-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Some tcp connections hang sometimes and I can't find the problem. When Maven is downloading libraries from maven repo, sometimes it blocks in one of the downloads, making the entire build hang. It is difficult to reproduce as it only happens rarely, but I was able to capture it on wireshark (with tshark).</p><p>This is the end of the build output:</p><pre><code>[INFO] Unable to find resource &#39;org.apache.maven.doxia:doxia-module-xhtml:jar:1.0&#39; in repository unicore.eu (http://unicore-dev.zam.kfa-juelich.de/maven)
Downloading: http://unicore-dev.zam.kfa-juelich.de/maven/org/apache/maven/doxia/doxia-module-xhtml/1.0/doxia-module-xhtml-1.0.jar
28K downloaded  (maven-invoker-2.0.11.jar)
[INFO] Unable to find resource &#39;org.apache.maven.doxia:doxia-module-xhtml:jar:1.0&#39; in repository unicore.eu (http://unicore-dev.zam.kfa-juelich.de/maven)
Downloading: http://repo1.maven.org/maven2/org/apache/maven/doxia/doxia-module-xhtml/1.0/doxia-module-xhtml-1.0.jar
21K downloaded  (doxia-module-xhtml-1.0.jar)</code></pre><p>It hangs here. It is in this state for some days without progress. With ss, I can see the problematic connection:</p><pre><code>ESTAB   0    0    ::ffff:128.142.136.87:57230 ::ffff:68.232.34.223:www  
cubic wscale:0,7 rto:216 rtt:16/8 ato:40 cwnd:10 send 7.3Mbps rcv_rtt:16 rcv_space:37960</code></pre><p>Now the wireshark output. I stopped capturing after a while - I know I should have continued. <a href="https://www.cloudshark.org/captures/36aa46f0f901">https://www.cloudshark.org/captures/36aa46f0f901</a></p><p>Thanks for any hints!</p></div><div id="question-tags" class="tags-container tags">debian hangs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '13, 01:28</strong></p><img src="https://secure.gravatar.com/avatar/1fb060b7a4d649f089f576d915e0bbb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmeneses&#39;s gravatar image" /><p>dmeneses<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmeneses has no accepted answers">0%</span></p></div></div><div id="comments-container-20693" class="comments-container"></div><div id="comment-tools-20693" class="comment-tools"></div><div class="clear"></div><div id="comment-20693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20695"></span>

<div id="answer-container-20695" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20695-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From a first glance at the tracefile, it looks like host repo1.maven.org is overloaded. Look at the time gaps between frames 94 and 95 and also between frames 114 and 115. Your client has acknowledged all data, still the server takes a long time to send new data. What is keeping it?</p><p>It might be on purpose to throttle bandwidth, although I would have expected a more granular control in that case. Or maybe there is a proxy in between that downloads chunks and then quickly passes the data down to you?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '13, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20695" class="comments-container"></div><div id="comment-tools-20695" class="comment-tools"></div><div class="clear"></div><div id="comment-20695-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

