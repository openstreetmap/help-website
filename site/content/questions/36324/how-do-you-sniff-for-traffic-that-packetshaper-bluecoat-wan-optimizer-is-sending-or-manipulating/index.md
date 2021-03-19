+++
type = "question"
title = "How do you sniff for traffic that PacketShaper (Bluecoat Wan Optimizer) is sending or manipulating?"
description = '''How do you sniff for traffic that a PacketShaper (Bluecoat Wan Optimizer) is sending or manipulating? We want to understand what it&#x27;s doing. We know it optimizes and accelerates TCP traffic only but wanted to watch the behavior if possible. Can you help me?'''
date = "2014-09-15T08:09:00Z"
lastmod = "2014-09-15T14:31:00Z"
weight = 36324
keywords = [ "packetshaper" ]
aliases = [ "/questions/36324" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do you sniff for traffic that PacketShaper (Bluecoat Wan Optimizer) is sending or manipulating?](/questions/36324/how-do-you-sniff-for-traffic-that-packetshaper-bluecoat-wan-optimizer-is-sending-or-manipulating)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36324-score" class="post-score" title="current number of votes">0</div><span id="post-36324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do you sniff for traffic that a PacketShaper (Bluecoat Wan Optimizer) is sending or manipulating? We want to understand what it's doing. We know it optimizes and accelerates TCP traffic only but wanted to watch the behavior if possible. Can you help me?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packetshaper" rel="tag" title="see questions tagged &#39;packetshaper&#39;">packetshaper</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '14, 08:09</strong></p><img src="https://secure.gravatar.com/avatar/4041b3e635c6a9ba811034c139421a87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ocarrillo&#39;s gravatar image" /><p><span>ocarrillo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ocarrillo has no accepted answers">0%</span></p></div></div><div id="comments-container-36324" class="comments-container"></div><div id="comment-tools-36324" class="comment-tools"></div><div class="clear"></div><div id="comment-36324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36325"></span>

<div id="answer-container-36325" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36325-score" class="post-score" title="current number of votes">0</div><span id="post-36325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, usually I capture the traffic on both sides of the device at the same time, meaning packets going in and coming out. Then compare the conversations to each other, which can be a bit difficult depending on how easy it is to recognize the same packet content.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '14, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36325" class="comments-container"></div><div id="comment-tools-36325" class="comment-tools"></div><div class="clear"></div><div id="comment-36325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36343"></span>

<div id="answer-container-36343" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36343-score" class="post-score" title="current number of votes">0</div><span id="post-36343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks, I think I stated the question incorrectly. I was looking for a specific packeshaper filter since I didn't see it on the filter list. But I found what I was looking for. I was told you can use XTP &amp; UDP PORT 64600 filters to locate packetshaper flows on wireshark - thanks.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '14, 14:31</strong></p><img src="https://secure.gravatar.com/avatar/4041b3e635c6a9ba811034c139421a87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ocarrillo&#39;s gravatar image" /><p><span>ocarrillo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ocarrillo has no accepted answers">0%</span></p></div></div><div id="comments-container-36343" class="comments-container"></div><div id="comment-tools-36343" class="comment-tools"></div><div class="clear"></div><div id="comment-36343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

