+++
type = "question"
title = "can&#x27;t capture network traffic"
description = '''Hi all i&#x27;m pretty new to all of this network profiling/sniffing and i will appriciate any help. first, I&#x27;ll detail my system: dell studio 1749 laptop,running Win 7 x64 home premuime. wireless card is Intel centrino 6200. I&#x27;m running the wireshark from the laptop and i&#x27;m able to watch my own traffic....'''
date = "2010-11-21T08:06:00Z"
lastmod = "2010-12-08T09:47:00Z"
weight = 1048
keywords = [ "wireless", "windows7", "wireshark" ]
aliases = [ "/questions/1048" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [can't capture network traffic](/questions/1048/cant-capture-network-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1048-score" class="post-score" title="current number of votes">1</div><span id="post-1048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all<br />
i'm pretty new to all of this network profiling/sniffing and i will appriciate any help.</p><p>first, I'll detail my system: dell studio 1749 laptop,running Win 7 x64 home premuime. wireless card is Intel centrino 6200.</p><p>I'm running the wireshark from the laptop and i'm able to watch my own traffic. can't see all the network traffic.<br />
what can be the reason for that?<br />
I read somewhere that my wireless card might be limited for mintor mode, didn't fully understood what does it means.<br />
many thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '10, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/ed77aa71c6d1230a03b9b77510997ce5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tamir&#39;s gravatar image" /><p><span>Tamir</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tamir has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-1048" class="comments-container"></div><div id="comment-tools-1048" class="comment-tools"></div><div class="clear"></div><div id="comment-1048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1057"></span>

<div id="answer-container-1057" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1057-score" class="post-score" title="current number of votes">4</div><span id="post-1057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thing with wireless cards and windows as OS is pretty simple: There is a 99.9% chance that your wireless NIC driver cannot put your card into the "promisuous mode" aka "monitor mode" for wireless cards.</p><p>Wireshark can try to talk your wireless NIC into delivering every frame it sees - but since wireshark can only kindly "ask" the driver to perform that task, there is no guarantee that this will actually happen. You can easily see the difference, when you look for "IEEE 802.11" in the protocol column. If your NIC support monitor mode, there will be lots of frames and if it cannot, you won't see any - even those which are addressed to your card! You can only see your "traffic" from the layers above your wireless L2 communication.</p><p>This is the situation under windows except you go and purchase some of the dedicated sniffing cards like for example the ones from Cacetech.</p><p>Under Linux, drivers are much more open to control, so there are possibilities (and tools) to talk your driver into entering monitor mode.</p><p>Don't ask me why that driver related control is an issue under windows - might be that vendor provided drivers simply do not enable that functionality by default, but I am just guessing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '10, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span> </br></br></p></div></div><div id="comments-container-1057" class="comments-container"><span id="1073"></span><div id="comment-1073" class="comment"><div id="post-1073-score" class="comment-score"></div><div class="comment-text"><p>well, I do catch my own traffic, many kinds of protocols: http/udp and many others protocol i'm not familiar with.<br />
Using wireshark, can I watch others users at the same network? like when I'm using my laptop and someone else using the PC and we are on the same router, can I watch his transportation? is it matter if the router uses WEP or WPA ? thanks</p></div><div id="comment-1073-info" class="comment-info"><span class="comment-age">(23 Nov '10, 01:14)</span> <span class="comment-user userinfo">Tamir</span></div></div><span id="1083"></span><div id="comment-1083" class="comment"><div id="post-1083-score" class="comment-score"></div><div class="comment-text"><blockquote><p>If your NIC support monitor mode,</p></blockquote><p>If your NIC supports monitor mode, Wireshark will not be able to put it into monitor mode; on Windows, Wireshark uses WinPcap to capture network traffic, and WinPcap doesn't support the mechanism added in Windows Vista, and supported in Windows 7 as well, to put 802.11 network adapters into monitor mode. You'd need an <a href="http://www.cacetech.com/products/airpcap.html">AirPcap adapter</a> from CACE Technologies for that.</p></div><div id="comment-1083-info" class="comment-info"><span class="comment-age">(23 Nov '10, 10:36)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="1285"></span><div id="comment-1285" class="comment"><div id="post-1285-score" class="comment-score"></div><div class="comment-text"><p>thanks, but I was looking for a solution without purchasing any new hardware adapters. I want to use the exist configuration and use the monitor mode. the NIC suppose to support by the documentation, so it's only driver issue?</p></div><div id="comment-1285-info" class="comment-info"><span class="comment-age">(08 Dec '10, 06:24)</span> <span class="comment-user userinfo">Tamir</span></div></div><span id="1287"></span><div id="comment-1287" class="comment"><div id="post-1287-score" class="comment-score"></div><div class="comment-text"><p>No, it's a WinPcap issue - WinPcap does not support the new mechanisms, added in Windows Vista and also present in Windows 7, for putting adapters into monitor mode on Windows.</p></div><div id="comment-1287-info" class="comment-info"><span class="comment-age">(08 Dec '10, 09:47)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-1057" class="comment-tools"></div><div class="clear"></div><div id="comment-1057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

