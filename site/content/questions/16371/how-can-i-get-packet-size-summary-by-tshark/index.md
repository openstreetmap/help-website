+++
type = "question"
title = "How can I get packet size summary by tshark ?"
description = '''I am using wireshark 1.6.11 on Fedora 17. I can see summary of packets grouped by their size from statistics --&amp;gt; packet lengths --&amp;gt; create state (without any filter) Is there a way to get this on command line or any script that you might be aware of ? I tried using various options with -z but ...'''
date = "2012-11-28T01:23:00Z"
lastmod = "2012-11-28T03:49:00Z"
weight = 16371
keywords = [ "statistics", "tshark", "size" ]
aliases = [ "/questions/16371" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I get packet size summary by tshark ?](/questions/16371/how-can-i-get-packet-size-summary-by-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16371-score" class="post-score" title="current number of votes">1</div><span id="post-16371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark 1.6.11 on Fedora 17. I can see summary of packets grouped by their size from statistics --&gt; packet lengths --&gt; create state (without any filter)</p><p>Is there a way to get this on command line or any script that you might be aware of ?</p><p>I tried using various options with -z but no luck till now.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '12, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/91b0f140b37c53d9f400216684a4d5f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nehaldattani&#39;s gravatar image" /><p><span>nehaldattani</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nehaldattani has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Nov '12, 01:23</strong> </span></p></div></div><div id="comments-container-16371" class="comments-container"></div><div id="comment-tools-16371" class="comment-tools"></div><div class="clear"></div><div id="comment-16371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16374"></span>

<div id="answer-container-16374" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16374-score" class="post-score" title="current number of votes">2</div><span id="post-16374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nehaldattani has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>with built-in commands:</p><blockquote><p><code>tshark -nr input.pcap -T fields -e frame.len | sort -n | uniq -c</code><br />
</p></blockquote><p>if your distribution supports gsl-histogram:</p><blockquote><p><code>tshark -nr input.pcap -T fields -e frame.len | gsl-histogram 0 1500 30</code><br />
</p></blockquote><p>Please check the man page of gsl-histogram for the options.</p><p>To <strong>install gsl-histogram</strong>, I had to run this command on Ubuntu: <code>apt-get install gsl-bin</code>.</p><p>If that's not exactly what you need, you could write a short script (perl/python).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '12, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Nov '12, 03:28</strong> </span></p></div></div><div id="comments-container-16374" class="comments-container"><span id="16375"></span><div id="comment-16375" class="comment"><div id="post-16375-score" class="comment-score"></div><div class="comment-text"><p>I got what I wanted. I think using sum with awk will give me the values in % . but thank you for pointing me in right direction.</p></div><div id="comment-16375-info" class="comment-info"><span class="comment-age">(28 Nov '12, 03:49)</span> <span class="comment-user userinfo">nehaldattani</span></div></div></div><div id="comment-tools-16374" class="comment-tools"></div><div class="clear"></div><div id="comment-16374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

