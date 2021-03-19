+++
type = "question"
title = "TSHARK ADVANCED FILTER"
description = '''Hi, I have a very huge trace file, how can I filter on TSHARK the next data. expert.message == &quot;Duplicate ACK (#1)&quot; || expert.message == &quot;Duplicate ACK (#2)&quot; || expert.message == &quot;Duplicate ACK (#3)&quot; || expert.message == &quot;Duplicate ACK (#4)&quot; I would like to do it with tshark because this trace file ...'''
date = "2011-11-10T11:04:00Z"
lastmod = "2011-11-10T11:32:00Z"
weight = 7375
keywords = [ "filtering", "tshark", "advanced" ]
aliases = [ "/questions/7375" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TSHARK ADVANCED FILTER](/questions/7375/tshark-advanced-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7375-score" class="post-score" title="current number of votes">0</div><span id="post-7375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a very huge trace file, how can I filter on TSHARK the next data.</p><p>expert.message == "Duplicate ACK (#1)" || expert.message == "Duplicate ACK (#2)" || expert.message == "Duplicate ACK (#3)" || expert.message == "Duplicate ACK (#4)"</p><p>I would like to do it with tshark because this trace file is so large to open it with wireshark and It will be paintfull to split the file and open one by one and apply the filter on Wireshark I can't find any reference about filter expert.messages or something like that.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-advanced" rel="tag" title="see questions tagged &#39;advanced&#39;">advanced</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '11, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/3ef66901787d63851a2ed444a8cd27bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="l0k1&#39;s gravatar image" /><p><span>l0k1</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="l0k1 has no accepted answers">0%</span></p></div></div><div id="comments-container-7375" class="comments-container"></div><div id="comment-tools-7375" class="comment-tools"></div><div class="clear"></div><div id="comment-7375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7376"></span>

<div id="answer-container-7376" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7376-score" class="post-score" title="current number of votes">1</div><span id="post-7376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="l0k1 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use tshark's -R argument to apply a display filter to the file.</p><pre><code>tshark -r &lt;infile.cap&gt; -R &#39;expert.message == &quot;Duplicate ACK (#1)&quot; || expert.message == &quot;Duplicate ACK (#2)&quot;&#39;</code></pre><p>You will have to be careful about are the single vs. double quotes. If you use -R ' &lt;filter&gt; ' (single quotes around the whole thing) and then use " (double quotes) inside &lt;filter&gt; you should be all set.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '11, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/365cfc3c62b61b2ed219b5d146e8ad3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zachad&#39;s gravatar image" /><p><span>zachad</span><br />
<span class="score" title="331 reputation points">331</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zachad has 3 accepted answers">21%</span></p></div></div><div id="comments-container-7376" class="comments-container"><span id="7377"></span><div id="comment-7377" class="comment"><div id="post-7377-score" class="comment-score"></div><div class="comment-text"><p>Dude,,, awsome. It works like a charm</p><p>Thanks</p><p>Daniel Castillo</p></div><div id="comment-7377-info" class="comment-info"><span class="comment-age">(10 Nov '11, 11:32)</span> <span class="comment-user userinfo">l0k1</span></div></div></div><div id="comment-tools-7376" class="comment-tools"></div><div class="clear"></div><div id="comment-7376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

