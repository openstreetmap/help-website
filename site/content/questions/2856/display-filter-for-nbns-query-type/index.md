+++
type = "question"
title = "Display filter for nbns query type"
description = '''How can I filter NetBIOS frames on hostnames or query types or names? I am looking for something elegant like dns.qry.name. Right now I using a cludge like &quot;udp.port == 137 and frame[88:2] == 00:20&quot; which is not nice when working with VLANs. Any hint is appreciated.'''
date = "2011-03-15T17:43:00Z"
lastmod = "2011-03-15T18:02:00Z"
weight = 2856
keywords = [ "nbns", "display-filter" ]
aliases = [ "/questions/2856" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Display filter for nbns query type](/questions/2856/display-filter-for-nbns-query-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2856-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I filter NetBIOS frames on hostnames or query types or names?</p><p>I am looking for something elegant like dns.qry.name.</p><p>Right now I using a cludge like "udp.port == 137 and frame[88:2] == 00:20" which is not nice when working with VLANs.</p><p>Any hint is appreciated.</p></div><div id="question-tags" class="tags-container tags">nbns display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '11, 17:43</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Mar '11, 17:46</p></div></div><div id="comments-container-2856" class="comments-container"></div><div id="comment-tools-2856" class="comment-tools"></div><div class="clear"></div><div id="comment-2856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2857"></span>

<div id="answer-container-2857" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2857-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>nbns.flags.opcode == {the query type} if you want to look for particular NBNS packet types. You can either use the numerical value of the field, e.g. 0 of a query, 5 for a registration, 6 for a release, 7 for wait for acknowledgement, 8 for refresh, 9 for alternate refresh, and 15 for multi-homed registration, or you can put the descriptive name in quotes, e.g. "Name query", "Registration", "Release", etc..</p><p>Unfortunately, the NBNS dissector currently doesn't have named fields for the names in packets, so you can't filter on them except by looking at raw packet data; however, try "nbns[offset:2] == 00:20", where "offset" is the offset from the beginning of the NBNS header, instead of "frame[88:2] == 00:20" - that should at least fix the VLAN issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '11, 18:02</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2857" class="comments-container"></div><div id="comment-tools-2857" class="comment-tools"></div><div class="clear"></div><div id="comment-2857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

