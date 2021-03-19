+++
type = "question"
title = "ICMP PING checksum [correct]"
description = '''When looking at the ICMP (not IP) info from a PING conversation, what does the &#x27;[correct]&#x27; next to &#x27;checksum&#x27; pertain to? It appears the checksum being displayed is with respect to the data being sent; if that&#x27;s the case, how can the PING request say [correct] when it hasn&#x27;t received anything? What ...'''
date = "2012-11-05T08:21:00Z"
lastmod = "2012-11-05T14:26:00Z"
weight = 15543
keywords = [ "checksum", "icmp" ]
aliases = [ "/questions/15543" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ICMP PING checksum \[correct\]](/questions/15543/icmp-ping-checksum-correct)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15543-score" class="post-score" title="current number of votes">0</div><span id="post-15543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When looking at the ICMP (not IP) info from a PING conversation, what does the '[correct]' next to 'checksum' pertain to? It appears the checksum being displayed is with respect to the data being sent; if that's the case, how can the PING request say [correct] when it hasn't received anything?<br />
What is being checked to generate the [correct], not just on the requesting side, but both?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span> <span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '12, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/607eca7ed24572ee77e5abbb25beaa89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Diesel&#39;s gravatar image" /><p><span>Jim Diesel</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Diesel has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-15543" class="comments-container"></div><div id="comment-tools-15543" class="comment-tools"></div><div class="clear"></div><div id="comment-15543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15551"></span>

<div id="answer-container-15551" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15551-score" class="post-score" title="current number of votes">2</div><span id="post-15551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>[correct] means that Wireshark calculated the value that the checksum field in the ICMP header <em>should</em> have, according to <a href="http://tools.ietf.org/html/rfc792">RFC 792</a>, and it's equal to the value it <em>does</em> have. That's <em>all</em> it means. (And, yes, I'm familiar with the Wireshark code; this is the log entry for the checkin that added the code to check the checksum:</p><pre><code>------------------------------------------------------------------------
r2522 | guy | 2000-10-20 21:34:47 -0700 (Fri, 20 Oct 2000) | 3 lines

Check ICMP checksum.  XXX - won&#39;t work if the ICMP packet is inside a
fragmented IP datagram, although that&#39;s probably extremely unlikely.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '12, 12:39</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15551" class="comments-container"><span id="15553"></span><div id="comment-15553" class="comment"><div id="post-15553-score" class="comment-score"></div><div class="comment-text"><p>Thank you.</p></div><div id="comment-15553-info" class="comment-info"><span class="comment-age">(05 Nov '12, 13:00)</span> <span class="comment-user userinfo">Jim Diesel</span></div></div><span id="15554"></span><div id="comment-15554" class="comment"><div id="post-15554-score" class="comment-score"></div><div class="comment-text"><p>If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-15554-info" class="comment-info"><span class="comment-age">(05 Nov '12, 14:26)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-15551" class="comment-tools"></div><div class="clear"></div><div id="comment-15551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15544"></span>

<div id="answer-container-15544" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15544-score" class="post-score" title="current number of votes">1</div><span id="post-15544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's the ICMP <strong>checksum</strong> as defined in RFC 792. The checksum calculation is defined for each type/code combination.</p><blockquote><p><code>http://www.ietf.org/rfc/rfc792.txt</code><br />
</p></blockquote><p>Cite: Checksum for echo request/response.</p><p><code>   Checksum       The checksum is the 16-bit ones's complement of the one's       complement sum of the ICMP message starting with the ICMP Type.       For computing the checksum , the checksum field should be zero.       If the total length is odd, the received data is padded with one       octet of zeros for computing the checksum.  This checksum may be       replaced in the future.</code></p><p>So, to answer your question. The <strong>[correct]</strong> means that Wireshark calculated the value itself and found that it's the same as the one in the ICMP packet.</p><p>Please also check the following question:</p><blockquote><p><code>http://ask.wireshark.org/questions/11061/icmp-checksum</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '12, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Nov '12, 12:20</strong> </span></p></div></div><div id="comments-container-15544" class="comments-container"><span id="15546"></span><div id="comment-15546" class="comment"><div id="post-15546-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, that's not what I was asking for; please reread my question. In Wireshark, what is the [correct] next to the checksum saying is correct? I've already seen the documentation on calculating the checksum, that's not what I'm asking about, I want to know what Wireshark is saying is correct. Consider your answer before posting, if you aren't familiar with the Wireshark code, please let someone who is answer the question.</p></div><div id="comment-15546-info" class="comment-info"><span class="comment-age">(05 Nov '12, 10:16)</span> <span class="comment-user userinfo">Jim Diesel</span></div></div></div><div id="comment-tools-15544" class="comment-tools"></div><div class="clear"></div><div id="comment-15544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

