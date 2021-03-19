+++
type = "question"
title = "Captured IP address but which application using it in PC ?"
description = '''Hi ,  I&#x27;m getting unwanted packet from particular PC which is getting denied on firewall due to policy, So we used packet capture in that PC which application or resource from PC trying to generate the packet. We found the destination IP which is microsoft IP. But still though we dont know which app...'''
date = "2013-10-09T09:00:00Z"
lastmod = "2013-10-09T13:29:00Z"
weight = 25838
keywords = [ "diwa" ]
aliases = [ "/questions/25838" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Captured IP address but which application using it in PC ?](/questions/25838/captured-ip-address-but-which-application-using-it-in-pc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25838-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>I'm getting unwanted packet from particular PC which is getting denied on firewall due to policy, So we used packet capture in that PC which application or resource from PC trying to generate the packet. We found the destination IP which is microsoft IP. But still though we dont know which application trying to generate that Traffic from that PC.</p><p>Is there a way to identify which application from the PC trying to generate the traffic ?</p><p>--Diwa</p></div><div id="question-tags" class="tags-container tags">diwa</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '13, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/455f59ecfa22edc16af894ba42407797?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Diwa&#39;s gravatar image" /><p>Diwa<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Diwa has no accepted answers">0%</span></p></div></div><div id="comments-container-25838" class="comments-container"><span id="25840"></span><div id="comment-25840" class="comment"><div id="post-25840-score" class="comment-score"></div><div class="comment-text"><p>This isn't really a wireshark question...and there's probably lots of different ways people would do this. If it were me and I had access to the source PC, I try to get "netstat -b" output when you see one of these connections. Then you can map the connection to a process, and work backwards from there.</p></div><div id="comment-25840-info" class="comment-info"><span class="comment-age">(09 Oct '13, 10:07)</span> smp</div></div></div><div id="comment-tools-25838" class="comment-tools"></div><div class="clear"></div><div id="comment-25838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25844"></span>

<div id="answer-container-25844" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25844-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe this blog post can help a little:</p><p><a href="http://blog.packet-foo.com/2013/04/the-packet-analysts-self-check/">http://blog.packet-foo.com/2013/04/the-packet-analysts-self-check/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '13, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-25844" class="comments-container"><span id="25887"></span><div id="comment-25887" class="comment"><div id="post-25887-score" class="comment-score"></div><div class="comment-text"><p>Thanks For the Answer, Let me follow ur steps.</p><p>Thanks Once again</p><p>--Diwa</p></div><div id="comment-25887-info" class="comment-info"><span class="comment-age">(10 Oct '13, 10:18)</span> Diwa</div></div></div><div id="comment-tools-25844" class="comment-tools"></div><div class="clear"></div><div id="comment-25844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25846"></span>

<div id="answer-container-25846" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25846-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way to identify which application from the PC trying to generate the traffic ?</p></blockquote><p>Yes, use <a href="http://www.microsoft.com/en-us/download/details.aspx?id=4865">Microsoft Network Monitor</a> and capture with it while the PC generates the traffic. Netmon will also list the process that created the traffic.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '13, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '13, 13:30</p></div></div><div id="comments-container-25846" class="comments-container"><span id="25888"></span><div id="comment-25888" class="comment"><div id="post-25888-score" class="comment-score"></div><div class="comment-text"><p>Thanks For the Answer, Let me follow ur steps.</p><p>Thanks Once again</p><p>--Diwa</p></div><div id="comment-25888-info" class="comment-info"><span class="comment-age">(10 Oct '13, 10:18)</span> Diwa</div></div></div><div id="comment-tools-25846" class="comment-tools"></div><div class="clear"></div><div id="comment-25846-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

