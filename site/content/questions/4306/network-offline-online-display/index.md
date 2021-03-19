+++
type = "question"
title = "Network offline - online display"
description = '''I have some computers connected with each other through wireless LAN.  I want to know if i install this software into the server then can i get to know that which computer is online and which one is offline in real- time or not. Please let me know..!!'''
date = "2011-06-01T00:13:00Z"
lastmod = "2011-06-01T01:47:00Z"
weight = 4306
keywords = [ "about_wireshark" ]
aliases = [ "/questions/4306" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Network offline - online display](/questions/4306/network-offline-online-display)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4306-score" class="post-score" title="current number of votes">0</div><span id="post-4306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have some computers connected with each other through wireless LAN.</p><p>I want to know if i install this software into the server then can i get to know that which computer is online and which one is offline in real- time or not.</p><p>Please let me know..!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-about_wireshark" rel="tag" title="see questions tagged &#39;about_wireshark&#39;">about_wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '11, 00:13</strong></p><img src="https://secure.gravatar.com/avatar/c4f50f29a599ede3feae11e35c1e9b07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Avinash&#39;s gravatar image" /><p><span>Avinash</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Avinash has no accepted answers">0%</span></p></div></div><div id="comments-container-4306" class="comments-container"></div><div id="comment-tools-4306" class="comment-tools"></div><div class="clear"></div><div id="comment-4306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4307"></span>

<div id="answer-container-4307" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4307-score" class="post-score" title="current number of votes">1</div><span id="post-4307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds more like a network monitoring task than a network analysis task. You might do something like that with simple ping scripts (if the computers have predictable IP addresses), or go for something more complex (and mostly not completely realtime) like Nagios/Icinga.</p><p>Of course you can use Wireshark, too... capture on your wireless and filter on ARP packets. As long as a PC is turned on you'll see it ARPing every now and then, but if you don't see ARPs it might not mean the PC is turned off - it might just be quiet for a while.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '11, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4307" class="comments-container"></div><div id="comment-tools-4307" class="comment-tools"></div><div class="clear"></div><div id="comment-4307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

