+++
type = "question"
title = "ip_hosts,tree with IPv6"
description = '''I have recently upgraded from 1.10.3 to 1.12.4 and found that running the command tshark -q -r input.cap -z ip_hosts,tree does NOT include any IPv6 addresses even though they exist in the capture file. Is there an equivalent command for IPv6 or is this a bug?'''
date = "2015-07-15T17:05:00Z"
lastmod = "2015-07-16T05:40:00Z"
weight = 44193
keywords = [ "ipv6", "tree", "tshark", "ip_hosts" ]
aliases = [ "/questions/44193" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ip\_hosts,tree with IPv6](/questions/44193/ip_hoststree-with-ipv6)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44193-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have recently upgraded from 1.10.3 to 1.12.4 and found that running the command tshark -q -r input.cap -z ip_hosts,tree does NOT include any IPv6 addresses even though they exist in the capture file.</p><p>Is there an equivalent command for IPv6 or is this a bug?</p></div><div id="question-tags" class="tags-container tags">ipv6 tree tshark ip_hosts</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '15, 17:05</strong></p><img src="https://secure.gravatar.com/avatar/784ace8ebf1b0a68fc64be805990cf5e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matt&#39;s gravatar image" /><p>matt<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matt has no accepted answers">0%</span></p></div></div><div id="comments-container-44193" class="comments-container"></div><div id="comment-tools-44193" class="comment-tools"></div><div class="clear"></div><div id="comment-44193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44207"></span>

<div id="answer-container-44207" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44207-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>ip_hosts is an filter for the "ip" tap (internal thing), which is fed by packet-ip IP(v4) protocol dissector. The packet-ipv6 IPv6 dissector feeds the ipv6 tap (again the internal mechanism for statistics etc.) which does not have a corresponding statistics output filter AFAIK.</p><p>In short 'ip' is usually an abbreviation of ipv4 and (unfortunately maybe) not the aggregate of both protocols (although by itself is not strange, because of the sometimes significant differences between them)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '15, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-44207" class="comments-container"></div><div id="comment-tools-44207" class="comment-tools"></div><div class="clear"></div><div id="comment-44207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

