+++
type = "question"
title = "Is it necessary for an RST packet to have an acknowledgement number?"
description = '''I am studying about TCP reset attack. I know that some RST packets have an acknowledgement number (with the ACK bit set), and some RST packets do not have an acknowledgement number (the acknowledgement number is set to 0, and the ACK bit is not set). Now if someone were to send a forged RST packet, ...'''
date = "2016-03-19T18:31:00Z"
lastmod = "2016-03-19T21:12:00Z"
weight = 51048
keywords = [ "tcpip", "tcp", "wireshark" ]
aliases = [ "/questions/51048" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is it necessary for an RST packet to have an acknowledgement number?](/questions/51048/is-it-necessary-for-an-rst-packet-to-have-an-acknowledgement-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51048-score" class="post-score" title="current number of votes">0</div><span id="post-51048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am studying about TCP reset attack. I know that some RST packets have an acknowledgement number (with the ACK bit set), and some RST packets do not have an acknowledgement number (the acknowledgement number is set to 0, and the ACK bit is not set).</p><p>Now if someone were to send a forged RST packet, is there a situation where it is necessary for the RST packet to have an acknowledgement number, or will an RST packet without the acknowledgement number always work?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpip" rel="tag" title="see questions tagged &#39;tcpip&#39;">tcpip</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '16, 18:31</strong></p><img src="https://secure.gravatar.com/avatar/633b94b5d3fe24751e56eb3cd795abe3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="john_9163&#39;s gravatar image" /><p><span>john_9163</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="john_9163 has no accepted answers">0%</span></p></div></div><div id="comments-container-51048" class="comments-container"></div><div id="comment-tools-51048" class="comment-tools"></div><div class="clear"></div><div id="comment-51048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51049"></span>

<div id="answer-container-51049" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51049-score" class="post-score" title="current number of votes">0</div><span id="post-51049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="john_9163 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it necessary for an RST packet to have an acknowledgement number?</p></blockquote><p>No. <a href="http://tools.ietf.org/html/rfc793#section-3.1">RFC 793, section 3.1 "Header format"</a>, says</p><blockquote><pre><code>Acknowledgment Number:  32 bits

   If the ACK control bit is set this field contains the value of the
   next sequence number the sender of the segment is expecting to
   receive.  Once a connection is established this is always sent.</code></pre></blockquote><p>so if a connection isn't established - for example, if a packet comes in for a connection that was closed - a packet sent out doesn't have to have an acknowledgment number and thus doesn't have to have ACK set.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '16, 18:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-51049" class="comments-container"><span id="51050"></span><div id="comment-51050" class="comment"><div id="post-51050-score" class="comment-score"></div><div class="comment-text"><p>"Once a connection is established this is always sent" So this means that if a connection is established and I would like to send an RST packet to end it, it is necessary to have an acknowledgement number, correct?</p></div><div id="comment-51050-info" class="comment-info"><span class="comment-age">(19 Mar '16, 20:51)</span> <span class="comment-user userinfo">john_9163</span></div></div><span id="51051"></span><div id="comment-51051" class="comment"><div id="post-51051-score" class="comment-score"></div><div class="comment-text"><p>Read <a href="https://tools.ietf.org/html/rfc793#section-3.9">RFC 793, section 3.9 "Event processing"</a> and <a href="https://tools.ietf.org/html/rfc1122#section-4.2.2.20">RFC 1122, section 4.2.2.20 "Event processing"</a> for indications of when an RST should, or shouldn't, have an accompanying ACK.</p></div><div id="comment-51051-info" class="comment-info"><span class="comment-age">(19 Mar '16, 21:12)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-51049" class="comment-tools"></div><div class="clear"></div><div id="comment-51049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

