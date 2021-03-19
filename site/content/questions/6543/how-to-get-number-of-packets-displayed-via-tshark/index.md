+++
type = "question"
title = "how to get number of packets displayed via tshark?"
description = '''I&#x27;m using to tshark in my bash script and i want to get the number of packets displayed after filtering.'''
date = "2011-09-25T02:52:00Z"
lastmod = "2011-09-26T02:27:00Z"
weight = 6543
keywords = [ "tshark" ]
aliases = [ "/questions/6543" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [how to get number of packets displayed via tshark?](/questions/6543/how-to-get-number-of-packets-displayed-via-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6543-score" class="post-score" title="current number of votes">0</div><span id="post-6543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using to tshark in my bash script and i want to get the number of packets displayed after filtering.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '11, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/5d64d21de6598960bf2db61f1ca705cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddayan&#39;s gravatar image" /><p><span>ddayan</span><br />
<span class="score" title="41 reputation points">41</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddayan has no accepted answers">0%</span></p></div></div><div id="comments-container-6543" class="comments-container"></div><div id="comment-tools-6543" class="comment-tools"></div><div class="clear"></div><div id="comment-6543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6545"></span>

<div id="answer-container-6545" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6545-score" class="post-score" title="current number of votes">2</div><span id="post-6545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ddayan has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Does <code>tshark -r file.pcap -R &lt;filter&gt; | wc -l</code> work for you?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '11, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-6545" class="comments-container"><span id="6553"></span><div id="comment-6553" class="comment"><div id="post-6553-score" class="comment-score"></div><div class="comment-text"><p>I ended up using <code>tshark -r p2/packet_dumps/packet_dump-$file_id -z io,phs,$filter | grep radiotap</code> but your solution works as well</p></div><div id="comment-6553-info" class="comment-info"><span class="comment-age">(26 Sep '11, 02:27)</span> <span class="comment-user userinfo">ddayan</span></div></div></div><div id="comment-tools-6545" class="comment-tools"></div><div class="clear"></div><div id="comment-6545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6544"></span>

<div id="answer-container-6544" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6544-score" class="post-score" title="current number of votes">1</div><span id="post-6544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://www.wireshark.org/docs/man-pages/tshark.html">TShark statistics</a></p><pre><code>$ tshark -r test.pcap -qz io,stat,30,&quot;COUNT(frame) frame&quot;
===================================================================
IO Statistics
Interval: 30.000 secs
Column #0: COUNT(frame) frame
                |   Column #0
Time            |          COUNT
000.000-030.000               943
030.000-060.000               677
060.000-090.000                25
===================================================================</code></pre>You can change the interval:<pre><code>$ tshark -r test.pcap -qz io,stat,90,&quot;COUNT(frame) frame&quot;
===================================================================
IO Statistics
Interval: 90.000 secs
Column #0: COUNT(frame) frame
                |   Column #0
Time            |          COUNT
000.000-090.000              1645
===================================================================</code></pre><p>Hope this helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '11, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span></p></div></div><div id="comments-container-6544" class="comments-container"></div><div id="comment-tools-6544" class="comment-tools"></div><div class="clear"></div><div id="comment-6544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

