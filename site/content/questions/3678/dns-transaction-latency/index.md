+++
type = "question"
title = "DNS transaction latency"
description = '''I want to know response delay between DNS client and server.  1&amp;gt; How can wireshark help in this?  2&amp;gt; How can I generate I/O graph that displays this information? Regards, Vijay'''
date = "2011-04-21T04:52:00Z"
lastmod = "2012-11-28T05:21:00Z"
weight = 3678
keywords = [ "performance", "dns" ]
aliases = [ "/questions/3678" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [DNS transaction latency](/questions/3678/dns-transaction-latency)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3678-score" class="post-score" title="current number of votes">0</div><span id="post-3678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">3</div></div></td><td><div id="item-right"><div class="question-body"><p>I want to know response delay between DNS client and server.</p><p>1&gt; How can wireshark help in this?</p><p>2&gt; How can I generate I/O graph that displays this information?</p><p>Regards,</p><p>Vijay</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '11, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/d1e5efe891c907bf6be8231eca9db31a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Gharge&#39;s gravatar image" /><p><span>Vijay Gharge</span><br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Gharge has no accepted answers">0%</span></p></div></div><div id="comments-container-3678" class="comments-container"><span id="3696"></span><div id="comment-3696" class="comment"><div id="post-3696-score" class="comment-score"></div><div class="comment-text"><p>Unless you use their Turbocap card or a Shark Appliance, timestamps are not accurate in some cases.</p></div><div id="comment-3696-info" class="comment-info"><span class="comment-age">(22 Apr '11, 12:10)</span> <span class="comment-user userinfo">eelarry</span></div></div></div><div id="comment-tools-3678" class="comment-tools"></div><div class="clear"></div><div id="comment-3678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3752"></span>

<div id="answer-container-3752" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3752-score" class="post-score" title="current number of votes">3</div><span id="post-3752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Vijay Gharge has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can look at the field "dns.time" in the DNS response and you can create an I/O graph as follows:</p><ul><li>Use "Advanced" units on the Y-axis.</li><li>Fill in the filter "dns.time" and calc: "AVG(*)" with again "dns.time"</li><li>Enable the graph by clicking on "Graph 1"</li></ul><p>(similarly you can add "MAX(*)" and "MIN(*)" graphs)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '11, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3752" class="comments-container"><span id="3794"></span><div id="comment-3794" class="comment"><div id="post-3794-score" class="comment-score"></div><div class="comment-text"><p>Thanks SYNbit! I will try...</p></div><div id="comment-3794-info" class="comment-info"><span class="comment-age">(28 Apr '11, 11:47)</span> <span class="comment-user userinfo">Vijay Gharge</span></div></div><span id="16381"></span><div id="comment-16381" class="comment"><div id="post-16381-score" class="comment-score"></div><div class="comment-text"><p>Awesome, that help a lot.</p></div><div id="comment-16381-info" class="comment-info"><span class="comment-age">(28 Nov '12, 05:21)</span> <span class="comment-user userinfo">jobauer</span></div></div></div><div id="comment-tools-3752" class="comment-tools"></div><div class="clear"></div><div id="comment-3752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

