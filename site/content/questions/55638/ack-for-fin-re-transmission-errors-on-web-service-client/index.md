+++
type = "question"
title = "ACK for FIN Re transmission errors on web service client."
description = '''Hi, We are troubleshooting a Java process making Web service call (Axis2 API) to another process IIB broker .Both are on Linux.  Problem: After the data transfer, Server sends [FIN,ACK] (frame:66) and client sends back ACK for this. Client does re-transmission of this ACK for fin for 15 times (take ...'''
date = "2016-09-18T20:49:00Z"
lastmod = "2016-09-18T21:38:00Z"
weight = 55638
keywords = [ "tcp_retransmission", "http", "persistent", "axis" ]
aliases = [ "/questions/55638" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ACK for FIN Re transmission errors on web service client.](/questions/55638/ack-for-fin-re-transmission-errors-on-web-service-client)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55638-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, We are troubleshooting a Java process making Web service call (Axis2 API) to another process IIB broker .Both are on Linux. Problem: After the data transfer, Server sends [FIN,ACK] (frame:66) and client sends back ACK for this. Client does re-transmission of this ACK for fin for 15 times (take nearly 15 mins) and finally RSTs the connection. This is causing Axis API at client is getting thread hung during socket write operation. I tried using persistence and non-persistence connections. Tried changing max connections and max connections to host. No Error on Firewall. On Firewall I can see aged-out status of connections.</p><p>What does it actually mean if ACK for FIN frame is being re transmitted during 4 phase connection release process? Where should I be looking to fix this?</p><p>Thanks in advance</p><p>Naren</p><p><img src="https://osqa-ask.wireshark.org/upfiles/TCP_Screenshot_Axixshource.._0ylR0pG.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">tcp_retransmission http persistent axis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '16, 20:49</strong></p><img src="https://secure.gravatar.com/avatar/4d87f5941c415b1d4592c488ec31e6d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="narenk&#39;s gravatar image" /><p>narenk<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="narenk has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 18 Sep '16, 20:55</p></div></div><div id="comments-container-55638" class="comments-container"></div><div id="comment-tools-55638" class="comment-tools"></div><div class="clear"></div><div id="comment-55638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55639"></span>

<div id="answer-container-55639" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55639-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The connection is only closed from one side (.61) indicating it wishes to send no more data, while the other side (.165) still has data to send. This data is never ACK'ed. After the retries it gives up with a RST.</p><p>The one side (.61) should accept this data, or send back RST, indicating the socket is closed. Now the other side (.165) can only assume the packets are lost, and retransmits until it gives up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '16, 21:38</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55639" class="comments-container"><span id="55647"></span><div id="comment-55647" class="comment"><div id="post-55647-score" class="comment-score"></div><div class="comment-text"><p>Thank you! Why would .61 close the connection abruptly when there is still data to be send? What should I be looking at .61 to fix this? .61 is on linux, IIB process listens to this.</p></div><div id="comment-55647-info" class="comment-info"><span class="comment-age">(19 Sep '16, 05:12)</span> narenk</div></div><span id="55649"></span><div id="comment-55649" class="comment"><div id="post-55649-score" class="comment-score"></div><div class="comment-text"><p>That is up to the vendor of that application to reveal (and out of scope of this Q&amp;A).</p></div><div id="comment-55649-info" class="comment-info"><span class="comment-age">(19 Sep '16, 05:37)</span> Jaap ♦</div></div></div><div id="comment-tools-55639" class="comment-tools"></div><div class="clear"></div><div id="comment-55639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

