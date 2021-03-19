+++
type = "question"
title = "How do I list all of the packet types within a capture?"
description = '''I am running Wireshark, and I can view statistics, but what part of the output shows a &quot;packet type&quot;?'''
date = "2012-02-19T12:39:00Z"
lastmod = "2012-02-20T10:10:00Z"
weight = 9130
keywords = [ "packetlist", "statistics" ]
aliases = [ "/questions/9130" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I list all of the packet types within a capture?](/questions/9130/how-do-i-list-all-of-the-packet-types-within-a-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9130-score" class="post-score" title="current number of votes">0</div><span id="post-9130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running Wireshark, and I can view statistics, but what part of the output shows a "packet type"?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packetlist" rel="tag" title="see questions tagged &#39;packetlist&#39;">packetlist</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '12, 12:39</strong></p><img src="https://secure.gravatar.com/avatar/a3db010ac66d0db9efa2f8296a9cf25b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sssddd&#39;s gravatar image" /><p><span>sssddd</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sssddd has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Feb '12, 09:29</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-9130" class="comments-container"></div><div id="comment-tools-9130" class="comment-tools"></div><div class="clear"></div><div id="comment-9130-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9143"></span>

<div id="answer-container-9143" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9143-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9143-score" class="post-score" title="current number of votes">1</div><span id="post-9143-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm assuming by "packet type" you mean the protocol.</p><p>Go to Statistics &gt; Protocol Hierarchy to see a list of all the protocols present, and a count of the number of packets and bytes for each protocol. You can then right-click on a line and select Apply As Filter &gt; Selected to see all the packets of that protocol type.</p><p>If you just want to know the protocol type for an individual packet, simply look at the Protocol column in the Wireshark packet list pane.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '12, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-9143" class="comments-container"></div><div id="comment-tools-9143" class="comment-tools"></div><div class="clear"></div><div id="comment-9143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9136"></span>

<div id="answer-container-9136" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9136-score" class="post-score" title="current number of votes">0</div><span id="post-9136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I've got some info on my website @ http://www.thetechfirm.com and google is your friend.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '12, 15:23</strong></p><img src="https://secure.gravatar.com/avatar/dbc4d8cb6be85bd586ca4bf211e1337c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thetechfirm&#39;s gravatar image" /><p><span>thetechfirm</span><br />
<span class="score" title="64 reputation points">64</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thetechfirm has no accepted answers">0%</span></p></div></div><div id="comments-container-9136" class="comments-container"></div><div id="comment-tools-9136" class="comment-tools"></div><div class="clear"></div><div id="comment-9136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

