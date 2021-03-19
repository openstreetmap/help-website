+++
type = "question"
title = "List of source IP Addresses"
description = '''How can I obtain a list of all source IP addresses from the captured data?'''
date = "2012-11-27T13:32:00Z"
lastmod = "2012-11-27T14:01:00Z"
weight = 16353
keywords = [ "ip" ]
aliases = [ "/questions/16353" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [List of source IP Addresses](/questions/16353/list-of-source-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16353-score" class="post-score" title="current number of votes">0</div><span id="post-16353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I obtain a list of all source IP addresses from the captured data?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '12, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/37101269aea1e7451347b450a404a61d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cdisler&#39;s gravatar image" /><p><span>cdisler</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cdisler has no accepted answers">0%</span></p></div></div><div id="comments-container-16353" class="comments-container"></div><div id="comment-tools-16353" class="comment-tools"></div><div class="clear"></div><div id="comment-16353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16354"></span>

<div id="answer-container-16354" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16354-score" class="post-score" title="current number of votes">1</div><span id="post-16354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to "Statistics -&gt; endpoints" and click on the "IPv4" (or "IPv6") tab. You can also export to CSV by clicking on "Copy"...</p><p>... or you can use tshark with "-T fields -e ip.src" and pipe the output to "sort | uniq" :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '12, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-16354" class="comments-container"></div><div id="comment-tools-16354" class="comment-tools"></div><div class="clear"></div><div id="comment-16354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

