+++
type = "question"
title = "S1AP Protocol - ciphered NAS"
description = '''Hello, We have two frames we&#x27;re looking at in Wireshark. Both have NAS with security header &quot;Integrity Protected and ciphered&quot;. In one of them, the rest is decoded as &quot;ciphered message&quot; and in the other one we can see the plain NAS header and the rest of the NAS message. Our question is: How can Wir...'''
date = "2013-06-13T06:16:00Z"
lastmod = "2013-06-16T04:24:00Z"
weight = 22008
keywords = [ "nas", "cipher", "s1ap" ]
aliases = [ "/questions/22008" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [S1AP Protocol - ciphered NAS](/questions/22008/s1ap-protocol-ciphered-nas)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22008-score" class="post-score" title="current number of votes">0</div><span id="post-22008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>We have two frames we're looking at in Wireshark. Both have NAS with security header "Integrity Protected and ciphered". In one of them, the rest is decoded as "ciphered message" and in the other one we can see the plain NAS header and the rest of the NAS message. Our question is: How can Wireshark determine how to decode86 the message right after the first security header (looks like it knows somehow if the rest is really ciphered or it's decodable) Thanks, Diana and Rotem</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nas" rel="tag" title="see questions tagged &#39;nas&#39;">nas</span> <span class="post-tag tag-link-cipher" rel="tag" title="see questions tagged &#39;cipher&#39;">cipher</span> <span class="post-tag tag-link-s1ap" rel="tag" title="see questions tagged &#39;s1ap&#39;">s1ap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '13, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p><span>Dianalab9</span><br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div></div><div id="comments-container-22008" class="comments-container"></div><div id="comment-tools-22008" class="comment-tools"></div><div class="clear"></div><div id="comment-22008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22016"></span>

<div id="answer-container-22016" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22016-score" class="post-score" title="current number of votes">1</div><span id="post-22016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is a basic heuristic: if the first byte following the security header / MAC / sequence number bytes (the one that contains the protocol discriminator / security header) seems to match the beginning of a EMM, ESM or Test Procedure message, then Wireshark attempts to dissect the message.</p><p>The idea is to try to differentiate a message with integrity only from a message with integrity + non null ciphering applied.</p><p>Of course like every heuristic it has some weaknesses; it could try to dissect a ciphered message.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '13, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-22016" class="comments-container"><span id="22104"></span><div id="comment-22104" class="comment"><div id="post-22104-score" class="comment-score"></div><div class="comment-text"><p>Thanks! that's helps us a lot.</p></div><div id="comment-22104-info" class="comment-info"><span class="comment-age">(16 Jun '13, 04:24)</span> <span class="comment-user userinfo">Dianalab9</span></div></div></div><div id="comment-tools-22016" class="comment-tools"></div><div class="clear"></div><div id="comment-22016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

