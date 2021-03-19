+++
type = "question"
title = "how to decode dynamic PT in RTP, e.g. RFC 2429 in RTP carring H.263+ video"
description = '''I am using Wireshark to decode a UDP/RTP stream. I can set the &quot;Decode as&quot; to decode RTP based on the dest port. This is working fine. However, by default, Wireshark is decoding the RTP payload using RFC 2198 (Redundant Audio Data). So it is deciding to decode the RTP payload using RFC 2198 specs. H...'''
date = "2012-08-25T12:20:00Z"
lastmod = "2012-08-28T00:52:00Z"
weight = 13891
keywords = [ "rtp" ]
aliases = [ "/questions/13891" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to decode dynamic PT in RTP, e.g. RFC 2429 in RTP carring H.263+ video](/questions/13891/how-to-decode-dynamic-pt-in-rtp-eg-rfc-2429-in-rtp-carring-h263-video)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13891-score" class="post-score" title="current number of votes">0</div><span id="post-13891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark to decode a UDP/RTP stream. I can set the "Decode as" to decode RTP based on the dest port. This is working fine. However, by default, Wireshark is decoding the RTP payload using RFC 2198 (Redundant Audio Data). So it is deciding to decode the RTP payload using RFC 2198 specs.</p><p>How is it deciding to decode the RTP payload using RFC 2198? The Payload Type I am using is 99 which is a dynamic payload type. How do I prevent Wireshark from decoding the RTP payload using RFC 2198?</p><p>My RTP stream carries video so I want to be able to select which RFC to use based on the RTP Payload Type. For example, I want to have Wireshark decode the RTP payload using RFC 2429 for H.263+ video.</p><p>How do I get Wireshark to decode the RTP payload based on a dynamic payload type? If Wireshark cannot do that, can I at least fix the decode for the RTP payload based on dest port number like I do for RTP?</p><p>In other words, I would like to set the RTP Payload Type "Decode as" just like I do for the UDP "Decode as RTP"</p><p>Thanks,</p><p>-Andres</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '12, 12:20</strong></p><img src="https://secure.gravatar.com/avatar/d9b77f44e775528eb825a2890774b64c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andres&#39;s gravatar image" /><p><span>Andres</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andres has no accepted answers">0%</span></p></div></div><div id="comments-container-13891" class="comments-container"></div><div id="comment-tools-13891" class="comment-tools"></div><div class="clear"></div><div id="comment-13891-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13893"></span>

<div id="answer-container-13893" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13893-score" class="post-score" title="current number of votes">2</div><span id="post-13893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Andres has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The RTP dissector dissects PT 99 as RFC2198 by default(It probably should not), change it by going to edit-&gt;preferences-&gt;protocols-&gt;RTP in the menu bar.</p><p>edit-&gt;preferences-&gt;protocols-&gt;H263P (aka H263+) also has a PT preference change that to 99.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '12, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-13893" class="comments-container"><span id="13918"></span><div id="comment-13918" class="comment"><div id="post-13918-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your response--just what I was looking for. -Andres</p></div><div id="comment-13918-info" class="comment-info"><span class="comment-age">(27 Aug '12, 16:55)</span> <span class="comment-user userinfo">Andres</span></div></div><span id="13920"></span><div id="comment-13920" class="comment"><div id="post-13920-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Andres</span>: if this is the correct answer please click the tick to that it's tagged as the accepted answer. That's how these Q&amp;A sites are supposed to work.</p></div><div id="comment-13920-info" class="comment-info"><span class="comment-age">(28 Aug '12, 00:52)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-13893" class="comment-tools"></div><div class="clear"></div><div id="comment-13893-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

