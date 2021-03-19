+++
type = "question"
title = "Wireshark Dump on GPRS Connection"
description = '''Hi folks, i&#x27;m a newby regarding tcp/ip analysis. Asking you for help seems the only way to get my questions answered. Hope u can help and i&#x27;m asking specificly enough =) I got a GPRS-connected Device communicating with my server. Every 5mins i send a HTTP Status so i know the device is still alive. ...'''
date = "2014-07-09T00:45:00Z"
lastmod = "2014-07-09T01:50:00Z"
weight = 34492
keywords = [ "dup-ack", "fin", "openwrt" ]
aliases = [ "/questions/34492" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Dump on GPRS Connection](/questions/34492/wireshark-dump-on-gprs-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34492-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks,</p><p>i'm a newby regarding tcp/ip analysis. Asking you for help seems the only way to get my questions answered. Hope u can help and i'm asking specificly enough =)</p><p>I got a GPRS-connected Device communicating with my server. Every 5mins i send a HTTP Status so i know the device is still alive. Every Minute the device sends data to my server.</p><p>My ISP called me and told me that my device's TCP/IP Stack isnt working correctly. (according to my isp the device is messing up FIN / ACK messages and doesnt listen to FINs from the server).</p><p>After checking the pcap file, i couldnt find something special...</p><p>Would someone be so kind and help me here?</p><p>The device is running openWRT and i did not modify the tcp/ip stack.</p><p>I would like to tell my ISP that the slow connection (pings to google or my server are more than 500ms... i even got a log where i got 18 secs. latency to google and to my server or my isp-server). Is there a possibility that the messages get messed up due the GPRS slow connection?</p><p>Hope i wrote understandably.</p><p>Link to pcap: <a href="https://dl.dropboxusercontent.com/u/15126116/tcpdump_252.pcap">https://dl.dropboxusercontent.com/u/15126116/tcpdump_252.pcap</a></p><p>best regards tom</p></div><div id="question-tags" class="tags-container tags">dup-ack fin openwrt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '14, 00:45</strong></p><img src="https://secure.gravatar.com/avatar/40c4f8ff540e6d105a73d3aea176a400?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rindolino&#39;s gravatar image" /><p>rindolino<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rindolino has no accepted answers">0%</span></p></div></div><div id="comments-container-34492" class="comments-container"></div><div id="comment-tools-34492" class="comment-tools"></div><div class="clear"></div><div id="comment-34492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34496"></span>

<div id="answer-container-34496" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34496-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are 181 connections to port 8080. 172 are absolutely identical, meaning same amount of frames, same content, same behavior. There are 9 frames that show re-transmissions.</p><p>Example: tcp.stream eq 10</p><p>You can see, that the SYN frame does not reach the server, so your client continues to send the SYN for 31 seconds. Finally, after 41 seconds the SYN gets through (SYN-ACK comes back) and the connection continues. There is no way to figure out why the SYN does not get through, unless you are able to monitor at different places on the way to the server, which is certainly not the case.</p><p>So, to me the capture file looks pretty normal. No signs for 'abnormal' FIN handling (maybe you should ask the ISP to provide an example). There are some connections that take very long due to the SYN no getting through, but I cannot offer an explanation or a solution, as the cause for that problem is totally unclear. It could be your device, it could be the network (including the internet), it could be the target server.</p><p><strong>UPDATE</strong>:<br />
I tend to say, it's the server, as the delta between the last SYN and the SYN-ACK is 10 seconds. It would be rather unusual if the SYN would 'circulate' 10 seconds somewhere in the network.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '14, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '14, 02:38</p></div></div><div id="comments-container-34496" class="comments-container"><span id="34543"></span><div id="comment-34543" class="comment"><div id="post-34543-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>thx very much for explaining those pakets to me. helps me a lot =)</p><p>best regards, tom</p></div><div id="comment-34543-info" class="comment-info"><span class="comment-age">(10 Jul '14, 01:28)</span> rindolino</div></div></div><div id="comment-tools-34496" class="comment-tools"></div><div class="clear"></div><div id="comment-34496-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

