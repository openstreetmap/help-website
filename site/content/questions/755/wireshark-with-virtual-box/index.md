+++
type = "question"
title = "Wireshark with Virtual Box"
description = '''I am using Sun Virtual Box with Win7 64 bit as the host and an MSDOS guest and want to sniff the traffic using a Packet Driver on MSDOS. Wireshark does not capture the data. Microsoft VPC works as expected with Wireshark capturing the traffic.'''
date = "2010-10-31T02:11:00Z"
lastmod = "2013-05-02T02:52:00Z"
weight = 755
keywords = [ "msdos", "virtualbox" ]
aliases = [ "/questions/755" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark with Virtual Box](/questions/755/wireshark-with-virtual-box)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-755-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Sun Virtual Box with Win7 64 bit as the host and an MSDOS guest and want to sniff the traffic using a Packet Driver on MSDOS. Wireshark does not capture the data. Microsoft VPC works as expected with Wireshark capturing the traffic.</p></div><div id="question-tags" class="tags-container tags">msdos virtualbox</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '10, 02:11</strong></p><img src="https://secure.gravatar.com/avatar/dfaff9b86090ac736a9da8e2673f3755?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gerritvn&#39;s gravatar image" /><p>gerritvn<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gerritvn has no accepted answers">0%</span></p></div></div><div id="comments-container-755" class="comments-container"></div><div id="comment-tools-755" class="comment-tools"></div><div class="clear"></div><div id="comment-755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="807"></span>

<div id="answer-container-807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-807-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hmmmm....are you using VirtualBox's "bridged networking" mode? If so, it's bypassing the host OS network stack entirely...</p><p>Taking a look at the VirtualBox networking documentation (<a href="http://www.virtualbox.org/manual/ch06.html">http://www.virtualbox.org/manual/ch06.html</a>), it looks like the "host-only" mode might also create some problems for packet captures.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '10, 20:01</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-807" class="comments-container"></div><div id="comment-tools-807" class="comment-tools"></div><div class="clear"></div><div id="comment-807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20896"></span>

<div id="answer-container-20896" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20896-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have an idea for solve your issue , too late but hope it help somebody else:)</p><p>Create Host-Only Adapter and bridge with your LAN Adapter. run wireshark on LAN Adapter, It will do the work</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '13, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/56b733160265f7190db7e856182ded33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aji&#39;s gravatar image" /><p>Aji<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aji has no accepted answers">0%</span></p></div></div><div id="comments-container-20896" class="comments-container"><span id="20906"></span><div id="comment-20906" class="comment"><div id="post-20906-score" class="comment-score"></div><div class="comment-text"><p>Isn't that what @wesmorgan1 suggested (see above)?</p></div><div id="comment-20906-info" class="comment-info"><span class="comment-age">(02 May '13, 05:12)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20896" class="comment-tools"></div><div class="clear"></div><div id="comment-20896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

