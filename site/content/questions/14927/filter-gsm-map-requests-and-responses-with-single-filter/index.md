+++
type = "question"
title = "filter GSM MAP requests and responses with single filter"
description = '''I&#x27;m trying to find a proper way to filter requests and responses for GSM MAP operations. So, usualy capture looks like this: TCAP  - Transaction ID  - Components   GSM MAP  - opCode  - MSISDN  - etc  I.e., GSM MAP is payload of TCAP. I filter requests based on MAP values (opCode and msisdn), such as...'''
date = "2012-10-11T06:47:00Z"
lastmod = "2012-10-11T10:45:00Z"
weight = 14927
keywords = [ "filter", "map", "request", "response" ]
aliases = [ "/questions/14927" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [filter GSM MAP requests and responses with single filter](/questions/14927/filter-gsm-map-requests-and-responses-with-single-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14927-score" class="post-score" title="current number of votes">0</div><span id="post-14927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to find a proper way to filter requests and responses for GSM MAP operations. So, usualy capture looks like this:</p><pre><code>TCAP
     - Transaction ID
     - Components

    GSM MAP
     - opCode
     - MSISDN
     - etc</code></pre><p>I.e., GSM MAP is payload of TCAP. I filter requests based on MAP values (opCode and msisdn), such as</p><pre><code>(gsm_map.address.digits == &quot;123456789&quot;) &amp;&amp; (gsm_old.localValue == 45)</code></pre><p>Response comes with the same TCAP Transaction ID, so I manualy extract it from request and filter again:</p><pre><code>tcap.tid == 78:16</code></pre><p>This shows both needed request and response. All this can be done by hand by writing filters twice, as described above. I was wondering if it's possible to write one single filter to extract both requests and responses at once (by using msisdn and opCode as inputs only). Is that possible or should one write a postdissector in Lua to do such tasks?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '12, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/0d235ba4e7903c0e6959c36d85697a77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mariusm&#39;s gravatar image" /><p><span>mariusm</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mariusm has no accepted answers">0%</span></p></div></div><div id="comments-container-14927" class="comments-container"></div><div id="comment-tools-14927" class="comment-tools"></div><div class="clear"></div><div id="comment-14927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14939"></span>

<div id="answer-container-14939" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14939-score" class="post-score" title="current number of votes">0</div><span id="post-14939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think you can do that with just display filters.</p><p>Another way (besides using Lua) would be to use <a href="http://wiki.wireshark.org/Mate">MATE</a>. I'd think you could create a Group Of Packets (GOP) for each MSISDN + opCode and filter on that. Of course you'd probably end up with multiple transactions in each GOP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '12, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-14939" class="comments-container"></div><div id="comment-tools-14939" class="comment-tools"></div><div class="clear"></div><div id="comment-14939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

