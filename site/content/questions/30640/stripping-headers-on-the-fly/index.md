+++
type = "question"
title = "Stripping Headers on the Fly"
description = '''A lot of folks use bittwiste, perl/python scripts, or maybe even the DLT_USER method to do something similar based on their goals, but to this point I haven&#x27;t found an embedded method to process packets on the fly and wanted to know if others thought it was possible before I even tried. I have a sce...'''
date = "2014-03-10T04:47:00Z"
lastmod = "2014-03-10T05:50:00Z"
weight = 30640
keywords = [ "headers", "stripping" ]
aliases = [ "/questions/30640" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Stripping Headers on the Fly](/questions/30640/stripping-headers-on-the-fly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30640-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A lot of folks use bittwiste, perl/python scripts, or maybe even the DLT_USER method to do something similar based on their goals, but to this point I haven't found an embedded method to process packets on the fly and wanted to know if others thought it was possible before I even tried. I have a scenario where I have a UDP packet that always uses a UDP src/dst port of say XXXX and the headers are always 42 bytes in length. Within the payload of the frame is the actual data frame to include headers, etc. I was thinking that it would be possible to write a dissector to filter on 'static int global_protocol_port = XXXX', strip off 42 bytes and handoff. However, the more I read into the process of how Wireshark dissects packets, I'm not sure this is even possible to do on the fly as packets are being received on the wire. Any thoughts on this are more than welcome and appreciated.</p></div><div id="question-tags" class="tags-container tags">headers stripping</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '14, 04:47</strong></p><img src="https://secure.gravatar.com/avatar/cc815814d652a0029797c0ceb6591bf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LonestarZ06&#39;s gravatar image" /><p>LonestarZ06<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LonestarZ06 has no accepted answers">0%</span></p></div></div><div id="comments-container-30640" class="comments-container"><span id="30647"></span><div id="comment-30647" class="comment"><div id="post-30647-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I'm not sure this is even possible to do on the fly as packets are being received on the wire.</p></blockquote><p>do you need a <strong>continuous</strong> monitoring solution (running 24x7) that prints parts of your UDP payload as the frames fly by?</p></div><div id="comment-30647-info" class="comment-info"><span class="comment-age">(10 Mar '14, 06:39)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-30640" class="comment-tools"></div><div class="clear"></div><div id="comment-30640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30643"></span>

<div id="answer-container-30643" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30643-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should look into tap listeners, in this case for the udp_follow tap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '14, 05:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-30643" class="comments-container"></div><div id="comment-tools-30643" class="comment-tools"></div><div class="clear"></div><div id="comment-30643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

