+++
type = "question"
title = "How to filter out MAC addresses with tcpdump"
description = '''Hi all. I am running tcpdump on DD-WRT routers in order to capture uplink data from mobile phones. I would like to listen only to some mac addresses. To do this I tried to run the command using a syntax similar to Wireshark: tcpdump -i prism0 ether src[0:3] 5c:95:ae -s0 -w | nc 192.168.1.147 31337 s...'''
date = "2012-10-26T05:14:00Z"
lastmod = "2012-10-26T18:19:00Z"
weight = 15293
keywords = [ "tcpdump", "wireshark" ]
aliases = [ "/questions/15293" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter out MAC addresses with tcpdump](/questions/15293/how-to-filter-out-mac-addresses-with-tcpdump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15293-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all.</p><p>I am running tcpdump on DD-WRT routers in order to capture uplink data from mobile phones. I would like to listen only to some mac addresses. To do this I tried to run the command using a syntax similar to Wireshark:</p><p>tcpdump -i prism0 ether src[0:3] 5c:95:ae -s0 -w | nc 192.168.1.147 31337</p><p>so that I can listen to all the devices that have as initial mac address <code>5c:95:ae</code>.</p><p>The problem is that the syntax is wrong and I was wondering if anyone of you knows the right syntax to get what I want.</p><p>Thanks in advance for the help!!!</p><p>Looking forward to hearing from you, Giovanni</p></div><div id="question-tags" class="tags-container tags">tcpdump wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '12, 05:14</strong></p><img src="https://secure.gravatar.com/avatar/0f9e9d97875e20337ca50e2709f4b929?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Giovanni%20Soldi&#39;s gravatar image" /><p>Giovanni Soldi<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Giovanni Soldi has no accepted answers">0%</span></p></div></div><div id="comments-container-15293" class="comments-container"></div><div id="comment-tools-15293" class="comment-tools"></div><div class="clear"></div><div id="comment-15293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15301"></span>

<div id="answer-container-15301" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15301-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://stackoverflow.com/questions/13086766/how-to-filter-mac-addresses-using-tcpdump">Yes, somebody knows</a> - the person named "graphite" does. And, no, you do not need "src" in the filter he/she lists - see my followup comment to your comment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '12, 18:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15301" class="comments-container"></div><div id="comment-tools-15301" class="comment-tools"></div><div class="clear"></div><div id="comment-15301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

