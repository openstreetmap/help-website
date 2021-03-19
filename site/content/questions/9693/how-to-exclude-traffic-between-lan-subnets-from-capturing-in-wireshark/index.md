+++
type = "question"
title = "How to exclude traffic between LAN subnets from capturing in Wireshark"
description = '''How to exclude traffic between LAN subnets from capturing in Wireshark. We want to capture traffic only between LAN Subnets and subnets residing off the WAN external link and exclude any communication between LAN Subnets'''
date = "2012-03-22T04:14:00Z"
lastmod = "2012-03-22T07:37:00Z"
weight = 9693
keywords = [ "subnets", "lan" ]
aliases = [ "/questions/9693" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to exclude traffic between LAN subnets from capturing in Wireshark](/questions/9693/how-to-exclude-traffic-between-lan-subnets-from-capturing-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9693-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to exclude traffic between LAN subnets from capturing in Wireshark. We want to capture traffic only between LAN Subnets and subnets residing off the WAN external link and exclude any communication between LAN Subnets</p></div><div id="question-tags" class="tags-container tags">subnets lan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '12, 04:14</strong></p><img src="https://secure.gravatar.com/avatar/31622a3bbbbf992f90124b64273c466f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fbaig&#39;s gravatar image" /><p>fbaig<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fbaig has no accepted answers">0%</span></p></div></div><div id="comments-container-9693" class="comments-container"></div><div id="comment-tools-9693" class="comment-tools"></div><div class="clear"></div><div id="comment-9693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9700"></span>

<div id="answer-container-9700" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9700-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You do a filter which includes your internal networks as source and excludes them as destination and vice versa.</p><p>E.g. if your internal IP's consist of 10.0.0.0/8 addresses you do</p><p>(src net 10.0.0.0/8 and not dst net 10.0.0.0/8) or (not src net 10.0.0.0/8 and dst net 10.0.0.0/8)</p><p>by the way: if your previous question about filtering was answered please feel free to accept the given answer due to the FAQ of this site</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '12, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-9700" class="comments-container"></div><div id="comment-tools-9700" class="comment-tools"></div><div class="clear"></div><div id="comment-9700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

