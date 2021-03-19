+++
type = "question"
title = "Missing SYN or SYN / ACK"
description = '''I just noticed that on my computers I am no longer able to capture my first SYN outgoing in a conversation. If I start a conversation, there is [SYN, ACK] [ACK] and if someone else starts there is [SYN][ACK] All offloading is off, there were no driver updates from me ( on the one machine I just upda...'''
date = "2016-08-02T06:26:00Z"
lastmod = "2016-08-02T22:37:00Z"
weight = 54510
keywords = [ "syn", "missing" ]
aliases = [ "/questions/54510" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Missing SYN or SYN / ACK](/questions/54510/missing-syn-or-syn-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54510-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just noticed that on my computers I am no longer able to capture my first SYN outgoing in a conversation. If I start a conversation, there is [SYN, ACK] [ACK] and if someone else starts there is [SYN][ACK]</p><p>All offloading is off, there were no driver updates from me ( on the one machine I just updated NIC Drivers and Wireshark to 2.05, no change)</p><p>If I plug in the profishark, everything is there, I just cannot see it on my windows 7 boxes when I capture locally. Just checked with colleague on a different computer model, he has the same issue. AV uninstalled, firewall off, same issue. This is also on legacy wireshark. Version is QT.</p><p>Bit strange that it should just appear, it was okay. Could be windows updates etc.. anyone got an idea? Probably just ticked something I shouldn't have...</p></div><div id="question-tags" class="tags-container tags">syn missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '16, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p>DarrenWright<br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-54510" class="comments-container"></div><div id="comment-tools-54510" class="comment-tools"></div><div class="clear"></div><div id="comment-54510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54529"></span>

<div id="answer-container-54529" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54529-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>1: NEVER trust MS..</p><p>2: Looked at the NIC saved settings again and noticed a lot of missing options.. MS Windows update has also updated my NIC driver / Caused a reset of its settings.</p><p>3: NIC deleted, removed including device drivers, re-installed. Set all Offloading again correctly, [SYN] Packets back.</p><p>Probably a perfect example of never trust anything you see at first glance, check check and recheck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '16, 22:37</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p>DarrenWright<br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-54529" class="comments-container"></div><div id="comment-tools-54529" class="comment-tools"></div><div class="clear"></div><div id="comment-54529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

