+++
type = "question"
title = "Search by specific bit in data field"
description = '''Hi, I am looking for filter expression that will enable search per specific bit in data filed. Do you have any idea?'''
date = "2013-06-12T06:27:00Z"
lastmod = "2013-06-12T07:07:00Z"
weight = 21957
keywords = [ "morton" ]
aliases = [ "/questions/21957" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Search by specific bit in data field](/questions/21957/search-by-specific-bit-in-data-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21957-score" class="post-score" title="current number of votes">0</div><span id="post-21957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am looking for filter expression that will enable search per specific bit in data filed. Do you have any idea?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-morton" rel="tag" title="see questions tagged &#39;morton&#39;">morton</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '13, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/182ef93b70cfdfc6b73831b8970f01b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="morton&#39;s gravatar image" /><p><span>morton</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="morton has no accepted answers">0%</span></p></div></div><div id="comments-container-21957" class="comments-container"></div><div id="comment-tools-21957" class="comment-tools"></div><div class="clear"></div><div id="comment-21957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="21958"></span>

<div id="answer-container-21958" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21958-score" class="post-score" title="current number of votes">0</div><span id="post-21958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I assume you are looking for a display filter. You can check for a specific bit value by using the "&amp;" operator. For instance, if I want to see all packets with the SYN flag set, I can use the filter "<code>tcp.flags&amp;2</code>". It will look at the second LSB of the TCP flags field and check whether the bit is set. If you don't want to see the SYN nor SYN/ACK packets, you can use "<code>!tcp.flags&amp;2</code>".</p><p>Here are some more examples, as I do not know in which part of the data you want to look:</p><pre><code>frame[0]&amp;1
eth[6]&amp;1
tcp[20]&amp;64
!data[5]&amp;4
tcp.seq&amp;16384</code></pre><p>(please note that the filters above are completely random)</p><p>In which data field do you need to test a bit value?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '13, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21958" class="comments-container"></div><div id="comment-tools-21958" class="comment-tools"></div><div class="clear"></div><div id="comment-21958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21959"></span>

<div id="answer-container-21959" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21959-score" class="post-score" title="current number of votes">0</div><span id="post-21959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use data.data[index] to filter on bytes in the data section e.g. data.data[0]==05. If you want to go down to the bit layer you'd have to use multiple expressions like that to specify the ranges. Edit: Or use SYN-Bit's method ;)</p><p>e.g. first bit in data section == 1 --&gt; data.data[0] can have a range from 80 to FF (1000 0000 to 1111 1111) --&gt; data.data[0] &gt;= 80</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '13, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jun '13, 06:56</strong> </span></p></div></div><div id="comments-container-21959" class="comments-container"></div><div id="comment-tools-21959" class="comment-tools"></div><div class="clear"></div><div id="comment-21959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21962"></span>

<div id="answer-container-21962" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21962-score" class="post-score" title="current number of votes">0</div><span id="post-21962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming a display filter is required, you can use the logical and to mask out the bit you're interested in, e.g.</p><p>prot.field &amp; 0x80</p><p>to mask out the top bit of a field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '13, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-21962" class="comments-container"><span id="21963"></span><div id="comment-21963" class="comment"><div id="post-21963-score" class="comment-score"></div><div class="comment-text"><p>Oops too slow.</p></div><div id="comment-21963-info" class="comment-info"><span class="comment-age">(12 Jun '13, 07:07)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-21962" class="comment-tools"></div><div class="clear"></div><div id="comment-21962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

