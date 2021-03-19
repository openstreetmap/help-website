+++
type = "question"
title = "WIRESHARK GRAPH"
description = '''How to read output from tcp stevens graph?'''
date = "2013-05-31T09:27:00Z"
lastmod = "2013-06-03T18:45:00Z"
weight = 21678
keywords = [ "tcp" ]
aliases = [ "/questions/21678" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [WIRESHARK GRAPH](/questions/21678/wireshark-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21678-score" class="post-score" title="current number of votes">0</div><span id="post-21678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to read output from tcp stevens graph?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '13, 09:27</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p><span>kishan pandey</span><br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-21678" class="comments-container"></div><div id="comment-tools-21678" class="comment-tools"></div><div class="clear"></div><div id="comment-21678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21682"></span>

<div id="answer-container-21682" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21682-score" class="post-score" title="current number of votes">0</div><span id="post-21682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's TCP sequence numbers as they increment over time. It's a useful spotcheck for some TCP performance problems. For example if there is packet loss and Wireshark is in a spot to catch the retransmissions, you'll see the same Y value at two or more spots on the graph rather than a constant incline. If your question is what it literally means, it's the TCP sequence number increments over time for the TCP session belonging to the packet you have selected.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '13, 19:26</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-21682" class="comments-container"><span id="21707"></span><div id="comment-21707" class="comment"><div id="post-21707-score" class="comment-score"></div><div class="comment-text"><p>Thankx for reply,can u provide some documents to read on this.</p></div><div id="comment-21707-info" class="comment-info"><span class="comment-age">(03 Jun '13, 02:01)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="21721"></span><div id="comment-21721" class="comment"><div id="post-21721-score" class="comment-score"></div><div class="comment-text"><p>For the graph, here's a section from Google books that goes over it: <a href="http://books.google.ca/books?id=-AdTE9S3kigC&amp;pg=PA197&amp;lpg=PA197&amp;dq=wireshark+stevens+graph&amp;source=bl&amp;ots=Y6BVvXKIuL&amp;sig=9fkBSnmMuCA_Dhw1gYkBSeJE_9c&amp;hl=en&amp;sa=X&amp;ei=rEWtUdbZF6HayAHArYHAAw&amp;ved=0CFMQ6AEwBg#v=onepage&amp;q=wireshark%20stevens%20graph&amp;f=false">http://books.google.ca/books?id=-AdTE9S3kigC&amp;pg=PA197&amp;lpg=PA197&amp;dq=wireshark+stevens+graph&amp;source=bl&amp;ots=Y6BVvXKIuL&amp;sig=9fkBSnmMuCA_Dhw1gYkBSeJE_9c&amp;hl=en&amp;sa=X&amp;ei=rEWtUdbZF6HayAHArYHAAw&amp;ved=0CFMQ6AEwBg#v=onepage&amp;q=wireshark%20stevens%20graph&amp;f=false</a></p><p>For what TCP sequence numbers fundamentally are, the only thing I can think to reference would be RFC 793, section 3.3 which defines them: <a href="http://www.ietf.org/rfc/rfc793.txt">http://www.ietf.org/rfc/rfc793.txt</a></p></div><div id="comment-21721-info" class="comment-info"><span class="comment-age">(03 Jun '13, 18:45)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-21682" class="comment-tools"></div><div class="clear"></div><div id="comment-21682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

