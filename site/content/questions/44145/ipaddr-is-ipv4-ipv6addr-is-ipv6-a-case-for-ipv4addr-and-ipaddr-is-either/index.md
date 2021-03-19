+++
type = "question"
title = "ip.addr is Ipv4. ipv6.addr is ipv6. a case for ipv4.addr and ip.addr is either?"
description = '''ip.addr is the IPv4 address. ipv6.addr is the IPv6 address. I think, it would make sense for ip.addr to be neutral and be the inet_ntop() of whichever IP protocol type it is, and ipv4.addr and ipv6.addr to remain proto specific. is there eg a way to say &#x27;if its ipv6, put ipv6.addr in this field, oth...'''
date = "2015-07-14T11:12:00Z"
lastmod = "2015-07-14T23:15:00Z"
weight = 44145
keywords = [ "inet_ntop", "addresses", "ipv4", "ipv6" ]
aliases = [ "/questions/44145" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ip.addr is Ipv4. ipv6.addr is ipv6. a case for ipv4.addr and ip.addr is either?](/questions/44145/ipaddr-is-ipv4-ipv6addr-is-ipv6-a-case-for-ipv4addr-and-ipaddr-is-either)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44145-score" class="post-score" title="current number of votes">0</div><span id="post-44145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>ip.addr is the IPv4 address. ipv6.addr is the IPv6 address.</p><p>I think, it would make sense for ip.addr to be neutral and be the inet_ntop() of whichever IP protocol type it is, and ipv4.addr and ipv6.addr to remain proto specific.</p><p>is there eg a way to say 'if its ipv6, put ipv6.addr in this field, otherwise put ip.addr in this field' as a compact conditional test?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-inet_ntop" rel="tag" title="see questions tagged &#39;inet_ntop&#39;">inet_ntop</span> <span class="post-tag tag-link-addresses" rel="tag" title="see questions tagged &#39;addresses&#39;">addresses</span> <span class="post-tag tag-link-ipv4" rel="tag" title="see questions tagged &#39;ipv4&#39;">ipv4</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '15, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/dfce61ec7269c2847df55e785fcb8ee7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geeohgeegeeoh&#39;s gravatar image" /><p><span>geeohgeegeeoh</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geeohgeegeeoh has no accepted answers">0%</span></p></div></div><div id="comments-container-44145" class="comments-container"></div><div id="comment-tools-44145" class="comment-tools"></div><div class="clear"></div><div id="comment-44145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44162"></span>

<div id="answer-container-44162" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44162-score" class="post-score" title="current number of votes">0</div><span id="post-44162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In hindsight this would be great. The one challenge I see is that one needs to create a new ftype 'FT_IP' which fans out to IPv4 or IPv6 based on.... heuristics? There are aggregate fields (like ip.addr), but not types (like the proposed FT_IP).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '15, 22:35</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-44162" class="comments-container"><span id="44164"></span><div id="comment-44164" class="comment"><div id="post-44164-score" class="comment-score"></div><div class="comment-text"><p>I'm a realist and I understand ip.addr is glued to ipv4 forever unless a significant change in behaviour is accepted by somebody in code, and documented to users.</p><p>but inet_pton() and inet_ntop() exist for a reason. ip.type would signal which ip.addr it was, but the stringprep is dealt with by libc functions already!</p><p>the second part of my question stands: is there a syntax for (if ip then ip.addr else ipv6.addr) in a -e field?</p></div><div id="comment-44164-info" class="comment-info"><span class="comment-age">(14 Jul '15, 23:15)</span> <span class="comment-user userinfo">geeohgeegeeoh</span></div></div></div><div id="comment-tools-44162" class="comment-tools"></div><div class="clear"></div><div id="comment-44162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

