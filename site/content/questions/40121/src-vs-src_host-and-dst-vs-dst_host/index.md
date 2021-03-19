+++
type = "question"
title = "src vs src_host and dst vs dst_host"
description = '''E.g. for the IP protocol: ip.src vs ip.src_host or ip.dst vs ip.dst_host What is the difference?'''
date = "2015-02-27T02:46:00Z"
lastmod = "2015-02-27T03:18:00Z"
weight = 40121
keywords = [ "capture-filter" ]
aliases = [ "/questions/40121" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [src vs src\_host and dst vs dst\_host](/questions/40121/src-vs-src_host-and-dst-vs-dst_host)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40121-score" class="post-score" title="current number of votes">0</div><span id="post-40121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>E.g. for the IP protocol:</p><p><code>ip.src</code> vs <code>ip.src_host</code></p><p>or</p><p><code>ip.dst</code> vs <code>ip.dst_host</code></p><p>What is the difference?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '15, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/d6b99845e4107fbd95f61125b7eb66ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mads%20Skjern&#39;s gravatar image" /><p><span>Mads Skjern</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mads Skjern has no accepted answers">0%</span></p></div></div><div id="comments-container-40121" class="comments-container"></div><div id="comment-tools-40121" class="comment-tools"></div><div class="clear"></div><div id="comment-40121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40123"></span>

<div id="answer-container-40123" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40123-score" class="post-score" title="current number of votes">1</div><span id="post-40123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What is the difference?</p></blockquote><p>DNS resolution.</p><blockquote><p><a href="https://www.wireshark.org/docs/dfref/i/ip.html">https://www.wireshark.org/docs/dfref/i/ip.html</a></p></blockquote><p>ip.src: plain IP address<br />
ip.src_host: reverse resolved hostname of that IP address</p><p>See also the following questions/answers:</p><blockquote><p><a href="https://ask.wireshark.org/questions/14126/tshark-not-resolving-names-and-not-showing-protocol-as-text-when-exporting-to-csv-file">https://ask.wireshark.org/questions/14126/tshark-not-resolving-names-and-not-showing-protocol-as-text-when-exporting-to-csv-file</a><br />
<a href="https://ask.wireshark.org/questions/13310/how-to-enable-the-tshark-name-resolution-while-exporting-to-csv-from-an-already-captured-pcapng-file">https://ask.wireshark.org/questions/13310/how-to-enable-the-tshark-name-resolution-while-exporting-to-csv-from-an-already-captured-pcapng-file</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '15, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-40123" class="comments-container"></div><div id="comment-tools-40123" class="comment-tools"></div><div class="clear"></div><div id="comment-40123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

