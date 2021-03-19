+++
type = "question"
title = "udp packet loss"
description = '''how do i find packet loss in this udp packets can i merge 2 files and then with compare option and ip.id filter,is it possible?Thanks'''
date = "2013-05-09T23:15:00Z"
lastmod = "2013-05-10T02:26:00Z"
weight = 21080
keywords = [ "udp" ]
aliases = [ "/questions/21080" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [udp packet loss](/questions/21080/udp-packet-loss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21080-score" class="post-score" title="current number of votes">0</div><span id="post-21080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how do i find packet loss in this udp packets can i merge 2 files and then with compare option and ip.id filter,is it possible?Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '13, 23:15</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p><span>kishan pandey</span><br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-21080" class="comments-container"></div><div id="comment-tools-21080" class="comment-tools"></div><div class="clear"></div><div id="comment-21080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21082"></span>

<div id="answer-container-21082" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21082-score" class="post-score" title="current number of votes">0</div><span id="post-21082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kishan pandey has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can do this:</p><blockquote><p><code>tshark -ni file_1.pcap -T fields -e ip.id -e frame.number | sort &gt; file_1.txt</code><br />
<code>tshark -ni file_2.pcap -T fields -e ip.id -e frame.number | sort &gt; file_2.txt</code><br />
</p></blockquote><p>Then compare file_1.txt and file_2.txt (diff on Unix or <a href="http://winmerge.org">WinMerge</a> on Windows).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '13, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-21082" class="comments-container"></div><div id="comment-tools-21082" class="comment-tools"></div><div class="clear"></div><div id="comment-21082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

