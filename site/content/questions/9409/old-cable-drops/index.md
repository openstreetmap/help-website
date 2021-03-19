+++
type = "question"
title = "old cable drops"
description = '''I am a desktop support analyst with no formal training. part of the area I support has several computers that are EXTREEMLY slow. I have brought this to the attention of the approprate staff a few times, they continue to blame it on the desktops... I knew it isn&#x27;t the issue because they were dual pr...'''
date = "2012-03-06T14:28:00Z"
lastmod = "2012-03-06T14:43:00Z"
weight = 9409
keywords = [ "data", "cable" ]
aliases = [ "/questions/9409" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [old cable drops](/questions/9409/old-cable-drops)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9409-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am a desktop support analyst with no formal training. part of the area I support has several computers that are EXTREEMLY slow. I have brought this to the attention of the approprate staff a few times, they continue to blame it on the desktops... I knew it isn't the issue because they were dual processor machines with at least 2 g ram... but i went along... we have reciently replaced that lease with new machines that have i5 processors and 4 gig ram... win7... so the users have new machines now ... and Arch's excuse has grown old...I am determined to help these folks out. the switches going out of the data area have excelent stats, or simmilar to the other areas. this area is at the far end of the floor, I am fairly certain that something is just not wired correctly from the patch panel to the user. I just feel like it is bad cable, crossed wires when it was punched down, something like that. can I use wireshark to identify bad cable?</p></div><div id="question-tags" class="tags-container tags">data cable</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '12, 14:28</strong></p><img src="https://secure.gravatar.com/avatar/52461162c66f61efe665ee59301def88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Butigli&#39;s gravatar image" /><p>Butigli<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Butigli has no accepted answers">0%</span></p></div></div><div id="comments-container-9409" class="comments-container"></div><div id="comment-tools-9409" class="comment-tools"></div><div class="clear"></div><div id="comment-9409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9410"></span>

<div id="answer-container-9410" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9410-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, wireshark can not detect bad cabling, you neeed a cable tester/analyzer to test the cabling.</p><p>What you <strong>can</strong> see in Wireshark are the effects of bad cabling, packet loss. Even though you need to take into account that there can be multiple sources for packet loss.</p><p>One thing that you need to check first is whether the switchport and system have the same duplex setting. Set both sides on AUTO and check what they negotiate or set both on fixed. A mix between auto and fixed full duplex is always resulting in a mismatch and lousy performance.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '12, 14:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9410" class="comments-container"></div><div id="comment-tools-9410" class="comment-tools"></div><div class="clear"></div><div id="comment-9410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

