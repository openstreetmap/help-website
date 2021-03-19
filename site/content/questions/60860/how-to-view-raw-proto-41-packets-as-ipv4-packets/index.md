+++
type = "question"
title = "How to view raw proto 41 packets as IPv4 packets"
description = '''Hello all, How can I view proto 41 packets as IPv4 traffic on an ethernet interface used as an endpoint in a 6in4 tunnel, without Wireshark interpreting the packets as IPv6 traffic? Thanks, Pim'''
date = "2017-04-16T14:18:00Z"
lastmod = "2017-04-17T01:01:00Z"
weight = 60860
keywords = [ "6in4", "ipv6" ]
aliases = [ "/questions/60860" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to view raw proto 41 packets as IPv4 packets](/questions/60860/how-to-view-raw-proto-41-packets-as-ipv4-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60860-score" class="post-score" title="current number of votes">0</div><span id="post-60860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>How can I view proto 41 packets as IPv4 traffic on an ethernet interface used as an endpoint in a 6in4 tunnel, without Wireshark interpreting the packets as IPv6 traffic?</p><p>Thanks, Pim</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-6in4" rel="tag" title="see questions tagged &#39;6in4&#39;">6in4</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '17, 14:18</strong></p><img src="https://secure.gravatar.com/avatar/026e1f980c9a84f92ecb14fc8af25846?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pimzand&#39;s gravatar image" /><p><span>pimzand</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pimzand has no accepted answers">0%</span></p></div></div><div id="comments-container-60860" class="comments-container"></div><div id="comment-tools-60860" class="comment-tools"></div><div class="clear"></div><div id="comment-60860-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60863"></span>

<div id="answer-container-60863" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60863-score" class="post-score" title="current number of votes">0</div><span id="post-60863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The easiest way is to disable the IPv6 dissector. Then you'll be left with the IPv4 packets carrying the IPv6 tunnelled traffic as data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '17, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-60863" class="comments-container"></div><div id="comment-tools-60863" class="comment-tools"></div><div class="clear"></div><div id="comment-60863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

