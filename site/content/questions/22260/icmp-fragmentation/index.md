+++
type = "question"
title = "ICMP fragmentation"
description = '''If you can&#x27;t see the full image, open the image URL in new window. On Windows 7, ping www.ea.com -l 32000 Why I am not seeing the fragmentation in Wireshark? I set payload to 32000 bytes but Wireshark is only seeing 1472 bytes (1500 bytes IP MTU- 20 bytes IP header - 8 bytes ICMP ECHO header). So wh...'''
date = "2013-06-23T18:56:00Z"
lastmod = "2013-06-23T19:11:00Z"
weight = 22260
keywords = [ "fragmentation", "icmp" ]
aliases = [ "/questions/22260" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ICMP fragmentation](/questions/22260/icmp-fragmentation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22260-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If you can't see the full image, open the image URL in new window.</p><p>On Windows 7, ping www.ea.com -l 32000</p><p>Why I am not seeing the fragmentation in Wireshark? I set payload to 32000 bytes but Wireshark is only seeing 1472 bytes (1500 bytes IP MTU- 20 bytes IP header - 8 bytes ICMP ECHO header). So where are the rest 30528 bytes?</p><p>I am pretty sure those fragments are actually sent because I still get fragment reassembly time exceeded minutes after the ping.</p><p>I unchecked IP Reassembly but it made no difference.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/icmp_fragmentation.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/icmp_fragmentation_return.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">fragmentation icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '13, 18:56</strong></p><img src="https://secure.gravatar.com/avatar/f52e4b433ac1a3dd397a26939f847faa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="realdreams&#39;s gravatar image" /><p>realdreams<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="realdreams has no accepted answers">0%</span></p></img></div></div><div id="comments-container-22260" class="comments-container"></div><div id="comment-tools-22260" class="comment-tools"></div><div class="clear"></div><div id="comment-22260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22261"></span>

<div id="answer-container-22261" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22261-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your display filter of "<code>icmp</code>" is what is causing you grief. The IP fragments don't match that filter (except for the 1st one in the case when you have IP reassembly disabled or the last one in the case when you have IP reassembly enabled), so they aren't shown. If you want to see all the fragments, you could try the following (which should work fairly well in most cases, unless there also happens to be other traffic besides your ICMP packets of interest included in that IP conversation filter, in which case you will have to filter that out with additional filters):</p><p>Right-click on an ICMP packet of interest and select, <code>"Conversation Filter -&gt; IP"</code></p><p><em>"I unchecked IP Reassembly but it made no difference."</em></p><p>Actually, it did/does make a difference. If you have IP reassembly turned off, the first packet will carry the ICMP header and be shown as ICMP, whereas if you have IP reassembly turned on, the last packet will be indicated as the entire reassembled ICMP packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '13, 19:11</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></img></div></div><div id="comments-container-22261" class="comments-container"></div><div id="comment-tools-22261" class="comment-tools"></div><div class="clear"></div><div id="comment-22261-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

