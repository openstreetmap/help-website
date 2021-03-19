+++
type = "question"
title = "Cumulaive Column ip.len value"
description = '''Hello, Curently it is posible to add Column Cumulative which is giving cumulative value of frame leinght, Is it posible to have Cumulative column but for ip.len value Thank'''
date = "2011-03-10T09:27:00Z"
lastmod = "2011-03-10T09:48:00Z"
weight = 2765
keywords = [ "length" ]
aliases = [ "/questions/2765" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cumulaive Column ip.len value](/questions/2765/cumulaive-column-iplen-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2765-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2765-score" class="post-score" title="current number of votes">0</div><span id="post-2765-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Curently it is posible to add Column Cumulative which is giving cumulative value of frame leinght, Is it posible to have Cumulative column but for ip.len value Thank</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '11, 09:27</strong></p><img src="https://secure.gravatar.com/avatar/bd2e9fd5927ea5cb7a241c3a7454111b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lavpivolav&#39;s gravatar image" /><p><span>lavpivolav</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lavpivolav has no accepted answers">0%</span></p></div></div><div id="comments-container-2765" class="comments-container"></div><div id="comment-tools-2765" class="comment-tools"></div><div class="clear"></div><div id="comment-2765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2766"></span>

<div id="answer-container-2766" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2766-score" class="post-score" title="current number of votes">1</div><span id="post-2766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Nope, unless you write the code that would implement it or get someone else interested to write it. What would be the use case?</p><p>You can however do something like this with tshark:</p><pre><code>$ tshark -nlr http.cap -T fields -e frame.number -e frame.len -e ip.len -e tcp.len | \
    awk &#39;{frame+=$2;ip+=$3;tcp+=$4;printf(&quot;%5d %8d %8d %8d\n&quot;,$1,frame,ip,tcp)}&#39; | head
 1       78       64        0
 2      152      124        0
 3      218      176        0
 4      933      877      649
 5      999      929      649
 6     2277     2193     1861
 7     2343     2245     1861
 8     3827     3715     3279
 9     5311     5185     4697
10     5377     5237     4697</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '11, 09:48</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2766" class="comments-container"></div><div id="comment-tools-2766" class="comment-tools"></div><div class="clear"></div><div id="comment-2766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

