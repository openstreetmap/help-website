+++
type = "question"
title = "how to counterscan a system capturing your packets"
description = '''if wireshark cannot, what software can?'''
date = "2012-05-16T01:38:00Z"
lastmod = "2012-05-16T01:41:00Z"
weight = 11030
keywords = [ "wireshark" ]
aliases = [ "/questions/11030" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to counterscan a system capturing your packets](/questions/11030/how-to-counterscan-a-system-capturing-your-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11030-score" class="post-score" title="current number of votes">0</div><span id="post-11030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>if wireshark cannot, what software can?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '12, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/b2a4006b4a0252f8be292c57acde97ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiresharkhelpers&#39;s gravatar image" /><p><span>wiresharkhel...</span><br />
<span class="score" title="30 reputation points">30</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiresharkhelpers has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 May '12, 01:39</strong> </span></p></div></div><div id="comments-container-11030" class="comments-container"></div><div id="comment-tools-11030" class="comment-tools"></div><div class="clear"></div><div id="comment-11030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11032"></span>

<div id="answer-container-11032" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11032-score" class="post-score" title="current number of votes">1</div><span id="post-11032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wiresharkhelpers has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't detect a sniffer if it is listening to traffic passively (on a switch mirror/span/monitor port or a TAP), as it will not interact with the network.</p><p>You may be able to detect hosts on your local network, that are running their interfaces in promiscuous mode (or using ARP tricks). Search google for: "detect a sniffer on network".</p><p>There are several papers that describe some methods, however they are all not very reliable.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '12, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 May '12, 01:45</strong> </span></p></div></div><div id="comments-container-11032" class="comments-container"></div><div id="comment-tools-11032" class="comment-tools"></div><div class="clear"></div><div id="comment-11032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

