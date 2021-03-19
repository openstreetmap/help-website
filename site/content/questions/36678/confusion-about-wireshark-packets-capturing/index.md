+++
type = "question"
title = "Confusion about wireshark packets capturing"
description = '''Hi everyone, i want to find the transmission time of each packet from respective source to destination in a network. in wire shark there a column named as &quot;Time&quot; which can be configured to show the captured packet time. my doubt is exactly when the wireshark captures the packets is it before the pac...'''
date = "2014-09-29T00:09:00Z"
lastmod = "2014-09-29T06:13:00Z"
weight = 36678
keywords = [ "wireshark" ]
aliases = [ "/questions/36678" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Confusion about wireshark packets capturing](/questions/36678/confusion-about-wireshark-packets-capturing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36678-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone, i want to find the transmission time of each packet from respective source to destination in a network. in wire shark there a column named as "Time" which can be configured to show the captured packet time.</p><p>my doubt is exactly when the wireshark captures the packets is it before the packet reaches to the destination or before it.</p><p>can i use wireshark for what i am trying to get?? can anyone reading this please help me out</p><p>Thanks..</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '14, 00:09</strong></p><img src="https://secure.gravatar.com/avatar/28bffe9260e694425fbe02eadd7371de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srinivas1117&#39;s gravatar image" /><p>srinivas1117<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srinivas1117 has no accepted answers">0%</span></p></div></div><div id="comments-container-36678" class="comments-container"></div><div id="comment-tools-36678" class="comment-tools"></div><div class="clear"></div><div id="comment-36678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36693"></span>

<div id="answer-container-36693" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36693-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Packet timestamping is done by the packet capturing code on Linux I think it's done in the kernel code(or libpcap) and on Windows by WinPcap.</p><blockquote><p>my doubt is exactly when the wireshark captures the packets is it before the packet reaches to the destination or before it.</p></blockquote><p>Not sure what you mean by this, timstamping happens on the server running the capturing program. So if you are using a span/mirror port on the switch the packet is timestanp after it's been copied to the mirroring port and received by the NIC card on the server and passed on to the network stack.</p><p>Idelly you need to capture on the sending and receiving system and compare the timestamps the accurassy on such an exercise might not be that great say +- 10 ms(ballpark (perhaps)).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '14, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-36693" class="comments-container"></div><div id="comment-tools-36693" class="comment-tools"></div><div class="clear"></div><div id="comment-36693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

