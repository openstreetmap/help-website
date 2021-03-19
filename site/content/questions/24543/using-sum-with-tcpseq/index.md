+++
type = "question"
title = "Using Sum (*) with tcp.seq"
description = '''hello, If i am using sum(*) function on tcp.seq to graph out tcp sequence number, my y axis values are not equal to corresponding packet sequence number (adding Ack sequence number into it). Any suggestions why or am i missing something?'''
date = "2013-09-10T21:00:00Z"
lastmod = "2013-09-13T08:35:00Z"
weight = 24543
keywords = [ "graph" ]
aliases = [ "/questions/24543" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using Sum (\*) with tcp.seq](/questions/24543/using-sum-with-tcpseq)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24543-score" class="post-score" title="current number of votes">0</div><span id="post-24543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,</p><p>If i am using sum(*) function on tcp.seq to graph out tcp sequence number, my y axis values are not equal to corresponding packet sequence number (adding Ack sequence number into it). Any suggestions why or am i missing something?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '13, 21:00</strong></p><img src="https://secure.gravatar.com/avatar/39356e003826b924c6b683f177900afb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iWireshark&#39;s gravatar image" /><p><span>iWireshark</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iWireshark has no accepted answers">0%</span></p></div></div><div id="comments-container-24543" class="comments-container"></div><div id="comment-tools-24543" class="comment-tools"></div><div class="clear"></div><div id="comment-24543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24546"></span>

<div id="answer-container-24546" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24546-score" class="post-score" title="current number of votes">1</div><span id="post-24546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When using the advanced options in IO graphs, wireshark will use the function you specify on the field you specify for all packets that fall within the tick interval.</p><p>In case of sum() on the tcp.seq, it will add up all the tcp sequence numbers. This means if there are multiple packets in the tick interval, you will see a sum of all the sequence numbers in the graph. Depending on what you want to visualize, I think you want to use min(), avg() or max() on tcp.seq instead of sum() as chances are big that there are multiple packets in one tick interval.</p><p>Also please note that a tcp session has two flows (client to server and server to client) for which the sequence numbers are unrelated. You can best use the filter to select only one of the two streams (filter on tcp.srcport==xxx).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '13, 22:21</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-24546" class="comments-container"><span id="24650"></span><div id="comment-24650" class="comment"><div id="post-24650-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the explanation. Two quick questions</p><ol><li><p>Lets say my tick interval is set to 0.1 sec. Now will the value (tcp.seq with Sum(*) applied) at 2.0 be sum of sequence number of packets between 1.9 ~ 2.0 or 2.0 ~3.0 or someother interval?</p></li><li><p>How this handles re-transmissions or tcp previous segment not captured? If i have some "tcp previous segment not captured" packets in my tick interval, will they be added if i am using tcp.seq with Sum(*)?Does the same apply for re-transmission packets?</p></li></ol><p>Thanks in advance</p></div><div id="comment-24650-info" class="comment-info"><span class="comment-age">(13 Sep '13, 07:23)</span> <span class="comment-user userinfo">iWireshark</span></div></div><span id="24654"></span><div id="comment-24654" class="comment"><div id="post-24654-score" class="comment-score"></div><div class="comment-text"><ol><li><p>All points in the graph are drawn in the middle of the interval. So when the interval is 0.1 sec, the first point will be at 0.05, then 0.15, then 0.25. The calculations will be done on the intervals 0.0 to 0.1 sec, 0.1 to 0.2 sec, 0.2 to 0.3 sec, etc.</p></li><li><p>The IO graphs don't look at packet interpretations, it just does it's calculations on the fields. So if there are two packets with the same tcp.seq, it will add up both (when using sum(*)).</p></li></ol></div><div id="comment-24654-info" class="comment-info"><span class="comment-age">(13 Sep '13, 08:35)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-24546" class="comment-tools"></div><div class="clear"></div><div id="comment-24546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

