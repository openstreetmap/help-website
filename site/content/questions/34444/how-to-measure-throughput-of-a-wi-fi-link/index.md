+++
type = "question"
title = "How to measure throughput of a Wi-Fi link?"
description = '''Hi, I want to measure the throughput of a Wi-Fi Link created between a Wi-Fi module and my PC. The module is running a TCP server on it and acts as a Wi-Fi access point and the PC is running TCP client(At PC side I have used D-Link USB-WIFI dongle). I want to measure the throughput of that link. How...'''
date = "2014-07-06T23:21:00Z"
lastmod = "2014-07-08T06:48:00Z"
weight = 34444
keywords = [ "wi-fi" ]
aliases = [ "/questions/34444" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to measure throughput of a Wi-Fi link?](/questions/34444/how-to-measure-throughput-of-a-wi-fi-link)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34444-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to measure the throughput of a Wi-Fi Link created between a Wi-Fi module and my PC. The module is running a TCP server on it and acts as a Wi-Fi access point and the PC is running TCP client(At PC side I have used D-Link USB-WIFI dongle). I want to measure the throughput of that link. How Can I measure that with Help of Wire shark.?? Can you provide the method for it?? I have found on internet that Wireshark supports Throughput graph. Please suggest for my case how can I measure it??</p></div><div id="question-tags" class="tags-container tags">wi-fi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '14, 23:21</strong></p><img src="https://secure.gravatar.com/avatar/a1138b087b045e494c78b7e19ddf80d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gunjan&#39;s gravatar image" /><p>Gunjan<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gunjan has no accepted answers">0%</span></p></div></div><div id="comments-container-34444" class="comments-container"><span id="34448"></span><div id="comment-34448" class="comment"><div id="post-34448-score" class="comment-score"></div><div class="comment-text"><p>Have you tried iperf?</p></div><div id="comment-34448-info" class="comment-info"><span class="comment-age">(07 Jul '14, 07:34)</span> Lekensteyn</div></div></div><div id="comment-tools-34444" class="comment-tools"></div><div class="clear"></div><div id="comment-34444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34463"></span>

<div id="answer-container-34463" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34463-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I want to measure the <strong>throughput of that link</strong></p></blockquote><p>Unfortunately you cannot 'measure' the throughput of the 'link' with Wireshark only, as Wireshark won't send traffic, all it can do is to watch the traffic on the 'line/link' and then calculate some statistics. <strong>However</strong> that will give you no information at all about the (possible) throughput of that 'link', as the measured throughput is only that what was on the line at that time, so if there was only a connection that sent data with 1 Mbit/s you will see exactly that.</p><p>So, what you can do to actually <strong>measure</strong> the throughput is to use specialized tools for that purpose, like <a href="https://iperf.fr/">iperf</a> (<a href="https://code.google.com/p/xjperf/">jperf</a>) or similar tools. They will measure show the max. possible throughput over that link, by sending test data. Obviously you can also monitor that traffic with Wireshark to get an additional view.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '14, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34463" class="comments-container"><span id="34498"></span><div id="comment-34498" class="comment"><div id="post-34498-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt,</p><p>The specialized tool-iperf which you have mentioned here must be run on two PCs which are connected to a WiFi access point(in my case I have a Wi-Fi module). Correct me if I am wrong.</p><p>If it is true then that is not the case I want to get the throughput. I want to measure the throughput when I transfer the data only between a PC and a module(module has TCP server running on it and the client on the PC will try to send the data). Please suggest if you have any thing.</p><p>Regards, Gunjan</p></div><div id="comment-34498-info" class="comment-info"><span class="comment-age">(09 Jul '14, 05:17)</span> Gunjan</div></div><span id="34499"></span><div id="comment-34499" class="comment"><div id="post-34499-score" class="comment-score"></div><div class="comment-text"><blockquote><p>tool-iperf which you have mentioned here must be run on two PCs</p></blockquote><p>Yes, that correct. iperf must run on two hosts, one is the client and the other is the server.</p><blockquote><p>Please suggest if you have any thing.</p></blockquote><p>Hm.. I would need more information about the 'module'. What kind of device is that?</p></div><div id="comment-34499-info" class="comment-info"><span class="comment-age">(09 Jul '14, 05:24)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-34463" class="comment-tools"></div><div class="clear"></div><div id="comment-34463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

