+++
type = "question"
title = "small window size"
description = '''https://www.cloudshark.org/captures/999d10324330 why are the windows sizes small in the capture, between the two servers, the communication between the same server 10.87.89.100 the windows size is 64k, and it is a VM 172.255.177 is a Salaris box '''
date = "2014-05-15T11:29:00Z"
lastmod = "2014-05-15T13:43:00Z"
weight = 32834
keywords = [ "small_windows_size" ]
aliases = [ "/questions/32834" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [small window size](/questions/32834/small-window-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32834-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="https://www.cloudshark.org/captures/999d10324330">https://www.cloudshark.org/captures/999d10324330</a></p><p>why are the windows sizes small in the capture, between the two servers, the communication between the same server 10.87.89.100 the windows size is 64k, and it is a VM 172.255.177 is a Salaris box</p></div><div id="question-tags" class="tags-container tags">small_windows_size</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '14, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/530b55f3fcb17b760aabdf113d9318aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ejohnson7&#39;s gravatar image" /><p>ejohnson7<br />
<span class="score" title="11 reputation points">11</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ejohnson7 has no accepted answers">0%</span></p></div></div><div id="comments-container-32834" class="comments-container"></div><div id="comment-tools-32834" class="comment-tools"></div><div class="clear"></div><div id="comment-32834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32839"></span>

<div id="answer-container-32839" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32839-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The trace did not capture the 3-way handshake so wireshark and we don't know what the window-scaling factor is that the windows client was offering. The maximum advertized windowsize offered in the TCP header is 513 which is clearly NOT the real windowsize. Take another trace showing a SYN packet from the client, then you know what the window_scaling factor is. You can set the window_scaling factor if it is unknown under Edit - Preferences - Protocol - TCP to instruct wireshark to calculate the correct tcp.window_size.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '14, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-32839" class="comments-container"></div><div id="comment-tools-32839" class="comment-tools"></div><div class="clear"></div><div id="comment-32839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

