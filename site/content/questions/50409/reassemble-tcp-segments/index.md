+++
type = "question"
title = "Reassemble TCP Segments"
description = '''This topic How does Wireshark reassemble TCP Segments is helpful, but does not fully answer &quot;correlation between the [] packets&quot;. It describes &quot;when an object has been completely transmitted&quot;, but how does WireShark correlate the packets to the same &quot;message&quot;? (e.g. does it use source ip + port?) (a...'''
date = "2016-02-22T08:24:00Z"
lastmod = "2016-02-22T08:44:00Z"
weight = 50409
keywords = [ "reassemble" ]
aliases = [ "/questions/50409" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reassemble TCP Segments](/questions/50409/reassemble-tcp-segments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50409-score" class="post-score" title="current number of votes">0</div><span id="post-50409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This topic <a href="https://ask.wireshark.org/questions/14280/how-does-wireshark-reassemble-tcp-segments">How does Wireshark reassemble TCP Segments</a> is helpful, but does not fully answer "correlation between the [] packets". It describes "when an object has been <strong>completely</strong> transmitted", but how does WireShark correlate the packets to the same "message"? (e.g. does it use source ip + port?)</p><p>(apologies for another question, but I don't see a 'comment' button on the other question. maybe I don't yet have enough karma)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassemble" rel="tag" title="see questions tagged &#39;reassemble&#39;">reassemble</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '16, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/7d1bd4bcd2430996dcd2c87af31d4b40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DennisR&#39;s gravatar image" /><p><span>DennisR</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DennisR has no accepted answers">0%</span></p></div></div><div id="comments-container-50409" class="comments-container"></div><div id="comment-tools-50409" class="comment-tools"></div><div class="clear"></div><div id="comment-50409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50410"></span>

<div id="answer-container-50410" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50410-score" class="post-score" title="current number of votes">1</div><span id="post-50410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try this blog post:</p><p><a href="https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/">https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '16, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-50410" class="comments-container"><span id="50411"></span><div id="comment-50411" class="comment"><div id="post-50411-score" class="comment-score"></div><div class="comment-text"><p>Ah! the 'the so-called “Five-Tuple” (or 5-tuple) [...] which contains the source IP, source port, destination IP, destination port, and the layer 4 protocol.'</p><p>Perfect! Thanks</p></div><div id="comment-50411-info" class="comment-info"><span class="comment-age">(22 Feb '16, 08:44)</span> <span class="comment-user userinfo">DennisR</span></div></div></div><div id="comment-tools-50410" class="comment-tools"></div><div class="clear"></div><div id="comment-50410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

