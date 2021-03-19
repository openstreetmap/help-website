+++
type = "question"
title = "dual wan router, detect wan id"
description = '''I have a dual wan router (openwrt with mwan3). All I want is to detect which wan (which network interface) is used by each pc or application.  How do I do this? '''
date = "2016-01-05T06:30:00Z"
lastmod = "2016-01-08T15:54:00Z"
weight = 48867
keywords = [ "wan", "multi" ]
aliases = [ "/questions/48867" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [dual wan router, detect wan id](/questions/48867/dual-wan-router-detect-wan-id)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48867-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a dual wan router (openwrt with mwan3). All I want is to detect which wan (which network interface) is used by each pc or application.</p><p>How do I do this?</p></div><div id="question-tags" class="tags-container tags">wan multi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '16, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/3ee3974ab415a7057a1783c77d807fbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bobptz&#39;s gravatar image" /><p>bobptz<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bobptz has no accepted answers">0%</span></p></div></div><div id="comments-container-48867" class="comments-container"></div><div id="comment-tools-48867" class="comment-tools"></div><div class="clear"></div><div id="comment-48867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48999"></span>

<div id="answer-container-48999" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48999-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How do I do this?</p></blockquote><p>By looking at both sides of the router and then comparing the capture files. Things like TCP SEQ numbers, IP ID, etc. will help to identify identical session on the LAN/WAN side, even though the router might have changed the source IP addresses with NAT. You can do that either by capturing traffic on the LAN and WAN side in parallel (probably not that easy on the WAN side) or by capturing on the router itself (with tcpdump).</p><p>But looking at the conntrack table on the router (<a href="http://conntrack-tools.netfilter.org/conntrack.html">conntrack -L</a>) is probably easier than analyzing pcap files in that way ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '16, 15:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-48999" class="comments-container"></div><div id="comment-tools-48999" class="comment-tools"></div><div class="clear"></div><div id="comment-48999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

