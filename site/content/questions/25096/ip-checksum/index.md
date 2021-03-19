+++
type = "question"
title = "IP checksum"
description = '''Is the packet considered invalid and not read by applications if the ip header checksum is wrong? if so, help me in calculating it..'''
date = "2013-09-22T23:54:00Z"
lastmod = "2013-09-23T01:07:00Z"
weight = 25096
keywords = [ "ip" ]
aliases = [ "/questions/25096" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IP checksum](/questions/25096/ip-checksum)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25096-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is the packet considered invalid and not read by applications if the ip header checksum is wrong?</p><p>if so, help me in calculating it..</p></div><div id="question-tags" class="tags-container tags">ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '13, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/14ae6741f009eb9551c897744110e25f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raja%20Balaji&#39;s gravatar image" /><p>Raja Balaji<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raja Balaji has no accepted answers">0%</span></p></div></div><div id="comments-container-25096" class="comments-container"></div><div id="comment-tools-25096" class="comment-tools"></div><div class="clear"></div><div id="comment-25096-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25101"></span>

<div id="answer-container-25101" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25101-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is the packet considered invalid and not read by applications if the ip header checksum is wrong?</p></blockquote><p>The OS will drop the packet if the IP checksum is incorrect.</p><p>HOWEVER: Are you sure it is wrong? Maybe Wireshark just displays a different checksum due to <a href="http://wiki.wireshark.org/CaptureSetup/Offloading">TCP/IP offloading</a>.</p><blockquote><p>if so, help me in calculating it..</p></blockquote><p>See here</p><blockquote><p><a href="http://bit.ly/15OhIKQ">http://bit.ly/15OhIKQ</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '13, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Sep '13, 01:12</p></div></div><div id="comments-container-25101" class="comments-container"><span id="25110"></span><div id="comment-25110" class="comment"><div id="post-25110-score" class="comment-score"></div><div class="comment-text"><p>looks like you're getting slightly feed up with those kind of questions, Kurt - LmGtfY is working overtime today ;-)</p></div><div id="comment-25110-info" class="comment-info"><span class="comment-age">(23 Sep '13, 05:23)</span> Jasper ♦♦</div></div><span id="25111"></span><div id="comment-25111" class="comment"><div id="post-25111-score" class="comment-score"></div><div class="comment-text"><p>Actually no, but LmGtfY is a nice way to post google searches (I like the animation). O.K., I admit that it includes a tiny bit of 'education', especially for the very obvious questions. ;-)</p></div><div id="comment-25111-info" class="comment-info"><span class="comment-age">(23 Sep '13, 05:27)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-25101" class="comment-tools"></div><div class="clear"></div><div id="comment-25101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

