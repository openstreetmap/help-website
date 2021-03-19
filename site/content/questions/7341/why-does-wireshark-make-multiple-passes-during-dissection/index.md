+++
type = "question"
title = "Why does Wireshark make multiple passes during dissection?"
description = '''Wireshark makes multiple passes over captured packets during dissection. I have read the various doc/README.*s, and I it my understanding that the first pass is made without constructing protocol trees (the tree argument to each dissect_PROTONAME function is NULL), and that the second pass is made t...'''
date = "2011-11-09T15:21:00Z"
lastmod = "2012-08-24T04:40:00Z"
weight = 7341
keywords = [ "development", "dissector", "wireshark" ]
aliases = [ "/questions/7341" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why does Wireshark make multiple passes during dissection?](/questions/7341/why-does-wireshark-make-multiple-passes-during-dissection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7341-score" class="post-score" title="current number of votes">6</div><span id="post-7341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark makes multiple passes over captured packets during dissection. I have read the various <code>doc/README.*</code>s, and I it my understanding that the first pass is made without constructing protocol trees (the <code>tree</code> argument to each <code>dissect_PROTONAME</code> function is <code>NULL</code>), and that the second pass is made to construct the protocol trees. Are these the only two passes made, or are there more? Additionally, what is each pass supposed to accomplish, since the same dissection functions are called each time?</p><p><strong>tl;dr:</strong> What are the different passes over packets during dissection for?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '11, 15:21</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-7341" class="comments-container"></div><div id="comment-tools-7341" class="comment-tools"></div><div class="clear"></div><div id="comment-7341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7346"></span>

<div id="answer-container-7346" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7346-score" class="post-score" title="current number of votes">11</div><span id="post-7346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="multipleinterfaces has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When a capture file is read in, Wireshark processes every packet. Whether the protocol tree is constructed or not depends on the version of Wireshark and on whether the protocol tree happens to be required for some reason when reading in the capture. Whether that's the case depends on a number of things, which I don't happen to know of offhand; no dissector or user should make assumptions about whether the protocol tree will be constructed on the first pass, as that's subject to change from release to release without notice.</p><p>The packets whose summaries are on the screen will probably be redissected to generate some of the columns, such as the Info column; scrolling the packet list will probably cause the packets that appear on the screen to be redissected. Currently, the value of the column will be saved after it's created the first time, so they won't be redissected merely to generate those columns, but that is also subject to change in the future.</p><p>If you then click on a packet, the packet is redissected, in order to generate the protocol tree; saving dissected protocol trees for all packets would consume a huge amount of memory. This is not a "pass", as there is no guarantee that the redissections will happen in sequential order.</p><p>Various operations, such as calculating various statistics, filtering the display, printing the packets, etc. will cause the packets to be redissected to generate the columns or the protocol tree.</p><p>Changing protocol preferences will also cause a complete redissection, as changing them could change the way the packets are dissected.</p><p>Each dissection is supposed to accomplish as much as is necessary and as little as is possible. :-) I.e., it needs to generate something, even if it's internal state required to dissect later packets or even the <em>current</em> packet if it's revisited. However, the less it generates, the less time it takes, so we try not to generate stuff we don't need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '11, 16:43</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7346" class="comments-container"><span id="13869"></span><div id="comment-13869" class="comment"><div id="post-13869-score" class="comment-score"></div><div class="comment-text"><p>Is there any Doc/link for understanding it better ?. Comments in core are not sufficient to understand the architecture of dissector and its interaction called from Filter/Line Summary.</p></div><div id="comment-13869-info" class="comment-info"><span class="comment-age">(24 Aug '12, 04:40)</span> <span class="comment-user userinfo">Harsha</span></div></div></div><div id="comment-tools-7346" class="comment-tools"></div><div class="clear"></div><div id="comment-7346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

