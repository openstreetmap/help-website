+++
type = "question"
title = "WireShark sending data to HTTP destinations"
description = '''Hello. Does anyone happen to know if WireShark is capable of sending data it finds to HTTP destinations? '''
date = "2012-10-09T13:01:00Z"
lastmod = "2012-10-10T07:15:00Z"
weight = 14832
keywords = [ "http" ]
aliases = [ "/questions/14832" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [WireShark sending data to HTTP destinations](/questions/14832/wireshark-sending-data-to-http-destinations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14832-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. Does anyone happen to know if WireShark is capable of sending data it finds to HTTP destinations?</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '12, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/0a6e86b318521b1ba2b860f5a773382a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InfusionDev20&#39;s gravatar image" /><p>InfusionDev20<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InfusionDev20 has no accepted answers">0%</span></p></div></div><div id="comments-container-14832" class="comments-container"><span id="14842"></span><div id="comment-14842" class="comment"><div id="post-14842-score" class="comment-score"></div><div class="comment-text"><p>what do you mean exactly by "sending data to HTTP destinations" (by using a HTTP POST request)?</p><p>What kind of data? Packets in pcap format? Payload bytes (which encoding)?</p></div><div id="comment-14842-info" class="comment-info"><span class="comment-age">(09 Oct '12, 14:30)</span> Kurt Knochner ♦</div></div><span id="14886"></span><div id="comment-14886" class="comment"><div id="post-14886-score" class="comment-score"></div><div class="comment-text"><p>It's more is it possible as WireShark is capturing the data to send the results to an HTTP server as it's being captured in real time.</p></div><div id="comment-14886-info" class="comment-info"><span class="comment-age">(10 Oct '12, 06:18)</span> InfusionDev20</div></div><span id="14888"></span><div id="comment-14888" class="comment"><div id="post-14888-score" class="comment-score"></div><div class="comment-text"><p>O.K. how do you want to send the data to the HTTP server? My question has a certain intention. I might have an idea how to do it, if you tell me how you want to send the data ;-)</p></div><div id="comment-14888-info" class="comment-info"><span class="comment-age">(10 Oct '12, 06:35)</span> Kurt Knochner ♦</div></div><span id="14889"></span><div id="comment-14889" class="comment"><div id="post-14889-score" class="comment-score"></div><div class="comment-text"><p>In a perfect world if it can be sent from WireShark itself that would be great. Someone else said they heard it was possible for WireShark to send data it finds to HTTP destinations, so I'm just trying to find out if such a thing is possible form within WireShark.</p></div><div id="comment-14889-info" class="comment-info"><span class="comment-age">(10 Oct '12, 06:40)</span> InfusionDev20</div></div></div><div id="comment-tools-14832" class="comment-tools"></div><div class="clear"></div><div id="comment-14832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="14839"></span>

<div id="answer-container-14839" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14839-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is a protocol analyser and as such does not generate traffic. The output of Wireshark analysis can be saved or exported in various formats to the file system but not to an HTTP server.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '12, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-14839" class="comments-container"></div><div id="comment-tools-14839" class="comment-tools"></div><div class="clear"></div><div id="comment-14839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14840"></span>

<div id="answer-container-14840" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14840-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark? No. Tshark, maybe. You could try to hook it up to <a href="http://curl.haxx.se">curl</a>. Or go all out with <a href="http://www.cloudshark.org/">CloudShark</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '12, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-14840" class="comments-container"><span id="14841"></span><div id="comment-14841" class="comment"><div id="post-14841-score" class="comment-score"></div><div class="comment-text"><p>Would something like CloudShark allow you to upload the data to an HTTP server let's say? And it looks like it's just a software based add-on to WireShark?</p></div><div id="comment-14841-info" class="comment-info"><span class="comment-age">(09 Oct '12, 14:18)</span> InfusionDev20</div></div></div><div id="comment-tools-14840" class="comment-tools"></div><div class="clear"></div><div id="comment-14840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14894"></span>

<div id="answer-container-14894" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14894-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Someone else said they heard it was possible for WireShark to send data it finds to HTTP destinations, so I'm just trying to find out if such a thing is possible form within WireShark.</p></blockquote><p>O.K. here is my suggestion:</p><p>You can create a Lua Listener and collect whatever data you want. Then use LuaSocket to send the data via SMTP, HTTP POST, FTP to another server. LuaSocket needs to be installed separately on Windows, as Wireshark does not provide that.</p><p>However on the receiving server you need something (an application) that is able to accept and process that data. There is no standard solution available that works out of the box, but it is doable with reasonable effort.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '12, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14894" class="comments-container"><span id="14896"></span><div id="comment-14896" class="comment"><div id="post-14896-score" class="comment-score"></div><div class="comment-text"><p>So WireShark itself has no capabilities to send such data without the help of a corresponding code correct? In this case writing, a Lua Listener to collect that data and have a Lua Socket on the other end to receive it.</p></div><div id="comment-14896-info" class="comment-info"><span class="comment-age">(10 Oct '12, 07:24)</span> InfusionDev20</div></div><span id="14897"></span><div id="comment-14897" class="comment"><div id="post-14897-score" class="comment-score"></div><div class="comment-text"><p>as mentioned by others, wireshark has no "ready-to-use" builtin capability to do that. However, as Lua is also a builtin feature, whireshark will have that capability if you write some code to do it ;-))</p><p>And yes, you could also have a LuaSocket at the other end to receive the data, but that's not necessary, as you can send the data to a regular ftp server or HTTP server (POST request) with Lua from Wireshark.</p></div><div id="comment-14897-info" class="comment-info"><span class="comment-age">(10 Oct '12, 07:25)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-14894" class="comment-tools"></div><div class="clear"></div><div id="comment-14894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

