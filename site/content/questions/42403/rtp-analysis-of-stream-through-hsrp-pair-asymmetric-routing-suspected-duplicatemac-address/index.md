+++
type = "question"
title = "RTP Analysis of stream through HSRP pair + asymmetric routing = &quot;Suspected duplicate(MAC address)&quot;"
description = '''Could a configuration flag be added that will tell the RTP analyzer to ignore when a source MAC address for an RTP stream changes (or to ignore Layer 2 altogether)? I have an HSRP pair with asymmetric routing behind them. Sometimes the routing will change mid RTP stream which causes the flow to egre...'''
date = "2015-05-14T14:30:00Z"
lastmod = "2015-05-15T02:42:00Z"
weight = 42403
keywords = [ "rtp_statistics", "mac-address" ]
aliases = [ "/questions/42403" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [RTP Analysis of stream through HSRP pair + asymmetric routing = "Suspected duplicate(MAC address)"](/questions/42403/rtp-analysis-of-stream-through-hsrp-pair-asymmetric-routing-suspected-duplicatemac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42403-score" class="post-score" title="current number of votes">0</div><span id="post-42403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Could a configuration flag be added that will tell the RTP analyzer to ignore when a source MAC address for an RTP stream changes (or to ignore Layer 2 altogether)? I have an HSRP pair with asymmetric routing behind them. Sometimes the routing will change mid RTP stream which causes the flow to egress a different HSRP router, thus a different source MAC. The RTP analysis is picking up on this, flags the packets as "Suspected Duplicate (MAC Address)", marks them as lost, and it screws up the stats.</p><p>My collector is running 1.4 and the RTP analysis looks fine. Opening the PCAP in the most recent version, 1.12.5, has this problem. I'm not sure which exact version between 1.4 and 1.12 this was introduced in.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp_statistics" rel="tag" title="see questions tagged &#39;rtp_statistics&#39;">rtp_statistics</span> <span class="post-tag tag-link-mac-address" rel="tag" title="see questions tagged &#39;mac-address&#39;">mac-address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '15, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/f933f8bc8065b4746c944152d46ce04b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KranZ&#39;s gravatar image" /><p><span>KranZ</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KranZ has no accepted answers">0%</span></p></div></div><div id="comments-container-42403" class="comments-container"></div><div id="comment-tools-42403" class="comment-tools"></div><div class="clear"></div><div id="comment-42403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42411"></span>

<div id="answer-container-42411" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42411-score" class="post-score" title="current number of votes">0</div><span id="post-42411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The heuristics were tightened in time to better handle conflicting situations. Unfortunately your setup 'causes' such conflict to be detected. The best way to request this in a well documented Enhancement request (with sample capture file) in <a href="https://bugs.wireshark.org">bugs.wireshark.org</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '15, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-42411" class="comments-container"></div><div id="comment-tools-42411" class="comment-tools"></div><div class="clear"></div><div id="comment-42411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

