+++
type = "question"
title = "Is Business Data captured by WireShark."
description = '''Hello! First time user here. My concern is if the business transaction data such as sales, names, etc. Will they be captured in WireShark? If so, Is this an option that can be turned off? I read through the FAQ but didn&#x27;t find the answers. Thanks In Advance. Thanks Ken.'''
date = "2015-04-23T12:23:00Z"
lastmod = "2015-04-23T15:05:00Z"
weight = 41738
keywords = [ "data", "business" ]
aliases = [ "/questions/41738" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is Business Data captured by WireShark.](/questions/41738/is-business-data-captured-by-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41738-score" class="post-score" title="current number of votes">0</div><span id="post-41738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! First time user here.</p><p>My concern is if the business transaction data such as sales, names, etc. Will they be captured in WireShark?</p><p>If so, Is this an option that can be turned off?</p><p>I read through the FAQ but didn't find the answers. Thanks In Advance.</p><p>Thanks Ken.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-business" rel="tag" title="see questions tagged &#39;business&#39;">business</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '15, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/51b6de15fd404cad66e26477db1b5c3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="saytoben&#39;s gravatar image" /><p><span>saytoben</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="saytoben has no accepted answers">0%</span></p></div></div><div id="comments-container-41738" class="comments-container"></div><div id="comment-tools-41738" class="comment-tools"></div><div class="clear"></div><div id="comment-41738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41741"></span>

<div id="answer-container-41741" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41741-score" class="post-score" title="current number of votes">2</div><span id="post-41741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My concern is if the business transaction data such as sales, names, etc. Will they be captured in WireShark?</p></blockquote><p>That's not a problem you can fix in Wireshark. If data is transmitted without being encrypted, everybody can capture and read that information, no matter if he is using Wireshark, Ettercap, tcpdump or any other sniffer.</p><p>The only solution: Use encryption (like SSL/TLS) if you have to transmit sensitive data over a network.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '15, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41741" class="comments-container"><span id="41753"></span><div id="comment-41753" class="comment"><div id="post-41753-score" class="comment-score"></div><div class="comment-text"><p>I assume the data captured is easily readable,, i.e. plain text. Is that right, or is it in Hex..etc? Can we strip the data off if we are to produce a report?</p></div><div id="comment-41753-info" class="comment-info"><span class="comment-age">(23 Apr '15, 14:29)</span> <span class="comment-user userinfo">saytoben</span></div></div><span id="41763"></span><div id="comment-41763" class="comment"><div id="post-41763-score" class="comment-score"></div><div class="comment-text"><p>It depends on the protocols carried in the packets of what it is, but Hex and sometimes ASCII should be it. And yes, you can strip the data if you're only interested in certain protocol headers.</p><p>Use TraceWrangler[1], add your capture file, add a anonymization task, and configure the task to strip everything it doesn't recognize plus everything after Layer 4 (TCP/UDP). That should do it.</p><p>[1] <a href="https://www.tracewrangler.com">https://www.tracewrangler.com</a></p></div><div id="comment-41763-info" class="comment-info"><span class="comment-age">(23 Apr '15, 15:05)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-41741" class="comment-tools"></div><div class="clear"></div><div id="comment-41741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

