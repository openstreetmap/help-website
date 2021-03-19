+++
type = "question"
title = "Can TCP checksum be ZERO(0)??"
description = '''Hi All, I have implemented TCP protocol. For calculation of TCP Checksum I have used code from &quot;http://www.netfor2.com/tcpsum.htm&quot;. Some times it calculates checksum as zero.   My question is can TCP checksum be zero?? I have captured this in Wireshark and it displays as correct checksum. Neither th...'''
date = "2012-08-30T05:38:00Z"
lastmod = "2015-01-29T15:18:00Z"
weight = 13962
keywords = [ "checksum", "zero", "tcp" ]
aliases = [ "/questions/13962" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can TCP checksum be ZERO(0)??](/questions/13962/can-tcp-checksum-be-zero0)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13962-score" class="post-score" title="current number of votes">0</div><span id="post-13962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I have implemented TCP protocol. For calculation of TCP Checksum I have used code from "http://www.netfor2.com/tcpsum.htm". Some times it calculates checksum as zero.</p><ol><li>My question is can TCP checksum be zero??</li><li>I have captured this in Wireshark and it displays as correct checksum.</li><li>Neither the OS nor the network card is calculating the checksum. Both client and server application are written using my tcp. While debugging I have seen the my tcp lib is calculating checksum as zero.</li></ol><p>Thanks in advance. Prithvi</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span> <span class="post-tag tag-link-zero" rel="tag" title="see questions tagged &#39;zero&#39;">zero</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '12, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/f80796612a9bd2e5c17778ae0a41d8ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prithvi&#39;s gravatar image" /><p><span>prithvi</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prithvi has no accepted answers">0%</span></p></div></div><div id="comments-container-13962" class="comments-container"></div><div id="comment-tools-13962" class="comment-tools"></div><div class="clear"></div><div id="comment-13962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19845"></span>

<div id="answer-container-19845" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19845-score" class="post-score" title="current number of votes">2</div><span id="post-19845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SYN-bit has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A tcp checksum of 0x0000 <em>is</em> legal. The final ones complement in the algorithm can result in 0x0000. An answer of 0xffff is not legal. That is, prior to the final ones complement in the calculation, the answer can never be 0x0000.</p><p>This is also true for the IP header checksum, but it is not true for UDP. UDP has a special case where 0x0000 is reserved for "no checksum computed". Thus for UDP, 0x0000 is illegal and when calculated following the standard algorithm, replaced with 0xffff.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '13, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/8dc3c1d8b364b8f52c6d2b833851fe72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alank25&#39;s gravatar image" /><p><span>alank25</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alank25 has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Mar '13, 09:44</strong> </span></p></div></div><div id="comments-container-19845" class="comments-container"></div><div id="comment-tools-19845" class="comment-tools"></div><div class="clear"></div><div id="comment-19845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13964"></span>

<div id="answer-container-13964" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13964-score" class="post-score" title="current number of votes">1</div><span id="post-13964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, the checksum should not be 0x0000, but 0xffff. It all depends on the way you calculate the checksum. When using one-complement, there can be +0 and -0 which are different.</p><p>For more information see <a href="http://tools.ietf.org/html/rfc1624">RFC 1624: Computation of the Internet Checksum via Incremental Update</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '12, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-13964" class="comments-container"><span id="39487"></span><div id="comment-39487" class="comment"><div id="post-39487-score" class="comment-score"></div><div class="comment-text"><p>I don't think this is correct. <a href="http://tools.ietf.org/html/rfc1624">RFC 1624</a> appears to be clarifying a mistake made in <a href="http://tools.ietf.org/html/rfc1141">RFC 1141</a> whereby a checksum of <code>0xFFFF</code> was computed using incremental update when it should have been <code>0x0000</code>, as would have been computed using the checksum computation from scratch method, presumably the one provided in section 4.1 of <a href="http://tools.ietf.org/html/rfc1071">RFC 1071</a>.</p><p>I think alank25's answer is actually the correct one.</p><p>By the way, Wireshark considers both <code>0xFFFF</code> and <code>0x0000</code> as correct IP checksums. I'm not sure this is a good idea. If my (and alank25's) reading of RFC 1624 is correct, then it would seem that Wireshark should be indicating that <code>0xFFFF</code> is not correct, or perhaps only correct according to RFC 1141.</p></div><div id="comment-39487-info" class="comment-info"><span class="comment-age">(29 Jan '15, 12:49)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="39491"></span><div id="comment-39491" class="comment"><div id="post-39491-score" class="comment-score">1</div><div class="comment-text"><p>You're right! I will accept <span>@alank25</span>'s answer on behalf of the original poster.</p></div><div id="comment-39491-info" class="comment-info"><span class="comment-age">(29 Jan '15, 15:18)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-13964" class="comment-tools"></div><div class="clear"></div><div id="comment-13964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

