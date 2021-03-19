+++
type = "question"
title = "KRB Error : KRB5KRB_ERR_RESPONSE_TOO_BIG"
description = '''anyone ever have this error on wireshark ? KRB Error : KRB5KRB_ERR_RESPONSE_TOO_BIG I get this error when I run a SPAN session to port that has attached a Scanner which authenticate to a DC and somebody tries to authenticate and they receive a Authentication Error and I get this throug wireshark via...'''
date = "2015-11-25T15:31:00Z"
lastmod = "2015-11-26T08:11:00Z"
weight = 47998
keywords = [ "krb", "error", "wireshark" ]
aliases = [ "/questions/47998" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [KRB Error : KRB5KRB\_ERR\_RESPONSE\_TOO\_BIG](/questions/47998/krb-error-krb5krb_err_response_too_big)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47998-score" class="post-score" title="current number of votes">0</div><span id="post-47998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>anyone ever have this error on wireshark ? KRB Error : KRB5KRB_ERR_RESPONSE_TOO_BIG</p><p>I get this error when I run a SPAN session to port that has attached a Scanner which authenticate to a DC and somebody tries to authenticate and they receive a Authentication Error and I get this throug wireshark via SPAN.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-krb" rel="tag" title="see questions tagged &#39;krb&#39;">krb</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '15, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/ec095f17451dde05aad8babd08fdac26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rloyd808&#39;s gravatar image" /><p><span>rloyd808</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rloyd808 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jul '16, 15:46</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-47998" class="comments-container"></div><div id="comment-tools-47998" class="comment-tools"></div><div class="clear"></div><div id="comment-47998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48006"></span>

<div id="answer-container-48006" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48006-score" class="post-score" title="current number of votes">0</div><span id="post-48006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong>KRB5KRB_ERR_RESPONSE_TOO_BIG</strong> is a sign that UDP is being used for Kerberos (normal and default) and a single UDP frame is not large enough to transmit the full Kerberos ticket. This can happen if a user is in a very large number of AD groups. The involved component (see the source IP of that frame in your capture file) will then send a <strong>KRB5KRB_ERR_RESPONSE_TOO_BIG</strong> to inform the 'other side' to use TCP instead. If there are authentication problems, this could mean that switching to TCP did not work or there was no attempt to switch to TCP.</p><p><strong>Possible solution</strong>: Analyze why TCP was not used and/or reduce the number of group memberships.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '15, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-48006" class="comments-container"></div><div id="comment-tools-48006" class="comment-tools"></div><div class="clear"></div><div id="comment-48006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

