+++
type = "question"
title = "How much data can I capture in one session?"
description = '''Is there a maximum size of the capture log (PCAP)? If a 30 minute capture filter = 500meg, how long before the capture stops working? Thanks'''
date = "2015-02-10T14:22:00Z"
lastmod = "2015-02-10T15:27:00Z"
weight = 39783
keywords = [ "maximum" ]
aliases = [ "/questions/39783" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How much data can I capture in one session?](/questions/39783/how-much-data-can-i-capture-in-one-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39783-score" class="post-score" title="current number of votes">0</div><span id="post-39783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a maximum size of the capture log (PCAP)? If a 30 minute capture filter = 500meg, how long before the capture stops working?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-maximum" rel="tag" title="see questions tagged &#39;maximum&#39;">maximum</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '15, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/8e254cf3ff026f82551c06f4f75926f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="w_1qaz&#39;s gravatar image" /><p><span>w_1qaz</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="w_1qaz has no accepted answers">0%</span></p></div></div><div id="comments-container-39783" class="comments-container"></div><div id="comment-tools-39783" class="comment-tools"></div><div class="clear"></div><div id="comment-39783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39784"></span>

<div id="answer-container-39784" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39784-score" class="post-score" title="current number of votes">1</div><span id="post-39784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Simple: if you use dumpcap instead of Wireshark/tshark it will capture until your disk is full (otherwise Wireshark/tshark will probably crash at some point). If you tell dumpcap to write a ring buffer (-b files and -b filesize parameters) it will run forever.</p><p>See <a href="https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a> and</p><p><a href="https://blog.packet-foo.com/2014/07/wireshark-file-storage/">https://blog.packet-foo.com/2014/07/wireshark-file-storage/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '15, 15:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Feb '15, 15:28</strong> </span></p></div></div><div id="comments-container-39784" class="comments-container"></div><div id="comment-tools-39784" class="comment-tools"></div><div class="clear"></div><div id="comment-39784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

