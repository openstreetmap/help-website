+++
type = "question"
title = "How to hide the count of captured packets with tshark"
description = '''Hi, I would like to know how I could hide the count of the packets that tshark captured. I tried the options -q and -Q but it display only the count wheras I would like to display only the packets. I read the doc, but I didn&#x27;t find how to do this. Can somebody help me ? Thank you.'''
date = "2014-02-04T04:34:00Z"
lastmod = "2014-09-01T16:06:00Z"
weight = 29424
keywords = [ "count", "tshark" ]
aliases = [ "/questions/29424" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to hide the count of captured packets with tshark](/questions/29424/how-to-hide-the-count-of-captured-packets-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29424-score" class="post-score" title="current number of votes">0</div><span id="post-29424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I would like to know how I could hide the count of the packets that tshark captured. I tried the options -q and -Q but it display only the count wheras I would like to display only the packets. I read the doc, but I didn't find how to do this. Can somebody help me ?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-count" rel="tag" title="see questions tagged &#39;count&#39;">count</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '14, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/76d84d4f6f15e52dd95dbc314712864d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Olivier07&#39;s gravatar image" /><p><span>Olivier07</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Olivier07 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Feb '14, 07:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-29424" class="comments-container"></div><div id="comment-tools-29424" class="comment-tools"></div><div class="clear"></div><div id="comment-29424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29428"></span>

<div id="answer-container-29428" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29428-score" class="post-score" title="current number of votes">3</div><span id="post-29428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please try the following:</p><p>Bourne shell and compatible shells (ksh, bash, etc.) on Unix-compatible systems:</p><blockquote><p>tshark -ni 1 -w output.pcap &gt; /dev/null 2&gt;&amp;1</p></blockquote><p>C shell and compatible shells (tcsh, etc.) on Unix-compatible systems:</p><blockquote><p>tshark -ni 1 -w output.pcap &gt;&amp; /dev/null</p></blockquote><p>Windows:</p><blockquote><p><del>tshark -ni 1 -w output.pcap 2&gt; NUL &gt; NUL</del></p></blockquote><p>actually, the same syntax (2&gt;&amp;1) works for Windows.</p><blockquote><p>tshark -ni 1 -w output.pcap &gt; NUL 2&gt;&amp;1</p></blockquote><p>Both will redirect STDOUT and STDERR (descriptor 2) to the NUL(L) device.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '14, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Feb '14, 18:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-29428" class="comments-container"><span id="29431"></span><div id="comment-29431" class="comment"><div id="post-29431-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer, it works fine !</p></div><div id="comment-29431-info" class="comment-info"><span class="comment-age">(04 Feb '14, 07:15)</span> <span class="comment-user userinfo">Olivier07</span></div></div><span id="29432"></span><div id="comment-29432" class="comment"><div id="post-29432-score" class="comment-score"></div><div class="comment-text"><p>Good.</p><p>BTW: Please don't mark the title of a question with [RESOLVED].</p><p>If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p><p>See the FAQ for some information how this site works. Thank you!</p></div><div id="comment-29432-info" class="comment-info"><span class="comment-age">(04 Feb '14, 07:23)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="35912"></span><div id="comment-35912" class="comment"><div id="post-35912-score" class="comment-score"></div><div class="comment-text"><p>Doesn't work for me. tshark -ni eth0 -w output.pcap &gt; /dev/null 2&gt;&amp;1</p></div><div id="comment-35912-info" class="comment-info"><span class="comment-age">(01 Sep '14, 07:45)</span> <span class="comment-user userinfo">insekt</span></div></div><span id="35919"></span><div id="comment-35919" class="comment"><div id="post-35919-score" class="comment-score"></div><div class="comment-text"><p>What's your shell? You can check it by <code>echo $SHELL</code></p><p>It works for me:</p><p><code>host:~ edmond$ sudo tshark -ni en1 -w output.pcap &gt; /dev/null 2&gt;&amp;1 Password: ^Chost:~ edmond$ ls -l output.pcap  -rw-------  1 root  staff  1768 Sep  2 01:07 output.pcap host:~ edmond$</code></p></div><div id="comment-35919-info" class="comment-info"><span class="comment-age">(01 Sep '14, 16:06)</span> <span class="comment-user userinfo">Edmond</span></div></div></div><div id="comment-tools-29428" class="comment-tools"></div><div class="clear"></div><div id="comment-29428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

