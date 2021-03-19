+++
type = "question"
title = "called party unknown"
description = '''Prepaid VoIP call with SIP phone on unknown fixed telephone number. You have addresses of HSS, SBC, SIP client, P-CSCF, SIP Application Server, S-CSCF and MGC. How to determine which number is called, for which requests and/or answers should I need to look for? Tnx.'''
date = "2011-05-02T13:01:00Z"
lastmod = "2011-05-03T03:31:00Z"
weight = 3883
keywords = [ "answer", "unknown", "request", "called", "party" ]
aliases = [ "/questions/3883" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [called party unknown](/questions/3883/called-party-unknown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3883-score" class="post-score" title="current number of votes">0</div><span id="post-3883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Prepaid VoIP call with SIP phone on unknown fixed telephone number. You have addresses of HSS, SBC, SIP client, P-CSCF, SIP Application Server, S-CSCF and MGC. How to determine which number is called, for which requests and/or answers should I need to look for?</p><p>Tnx.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-answer" rel="tag" title="see questions tagged &#39;answer&#39;">answer</span> <span class="post-tag tag-link-unknown" rel="tag" title="see questions tagged &#39;unknown&#39;">unknown</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-called" rel="tag" title="see questions tagged &#39;called&#39;">called</span> <span class="post-tag tag-link-party" rel="tag" title="see questions tagged &#39;party&#39;">party</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '11, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/13231e33ab17a93476f7b98c9d5b272a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wired&#39;s gravatar image" /><p><span>wired</span><br />
<span class="score" title="44 reputation points">44</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wired has one accepted answer">9%</span></p></div></div><div id="comments-container-3883" class="comments-container"><span id="3884"></span><div id="comment-3884" class="comment"><div id="post-3884-score" class="comment-score"></div><div class="comment-text"><p>Maybe code 180 Ringing?</p></div><div id="comment-3884-info" class="comment-info"><span class="comment-age">(02 May '11, 13:02)</span> <span class="comment-user userinfo">wired</span></div></div><span id="3887"></span><div id="comment-3887" class="comment"><div id="post-3887-score" class="comment-score"></div><div class="comment-text"><p>Could the RTP traffic be a stiching point? RTP traffic runs after VoIP connection is establised. So I filted out RTP traffic and there are only two IP addressed - first belongs to SIP phone client and the second could to called part (B)?</p></div><div id="comment-3887-info" class="comment-info"><span class="comment-age">(02 May '11, 16:27)</span> <span class="comment-user userinfo">wired</span></div></div><span id="3890"></span><div id="comment-3890" class="comment"><div id="post-3890-score" class="comment-score"></div><div class="comment-text"><p>Hi, Are you asking how to find the E164 adderss of the called party, the IP addresses of the involved nodes to set up a call to that number is of no consequence in that case. Media(RTP) and signaling paths are separated so the RTP IP addresses will be different from call signaling. Media path will be something like Client(IP1) --- MediProxy(IP2) MediaProxy(IP3) --- MediGAteway(IP4)MediaGateway)TDM circuit -&gt;PSTN The to header of the INVITE from the client might contain a tel URI or a phone context, containing the called party number. Regards Anders</p></div><div id="comment-3890-info" class="comment-info"><span class="comment-age">(02 May '11, 21:49)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="3891"></span><div id="comment-3891" class="comment"><div id="post-3891-score" class="comment-score"></div><div class="comment-text"><p>But the system could also use DNS to do translation from SIP URI to E164. Anders</p></div><div id="comment-3891-info" class="comment-info"><span class="comment-age">(02 May '11, 21:49)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-3883" class="comment-tools"></div><div class="clear"></div><div id="comment-3883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3895"></span>

<div id="answer-container-3895" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3895-score" class="post-score" title="current number of votes">0</div><span id="post-3895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Actually I'm not sure what to expect. But as You said, INVITE header may contain a telephone URI/phone context with called party number.</p><p>Now I also sent this trace to my other cooworker who'll try to determine what's a called party number.</p><p>For now, thanks. :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '11, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/13231e33ab17a93476f7b98c9d5b272a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wired&#39;s gravatar image" /><p><span>wired</span><br />
<span class="score" title="44 reputation points">44</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wired has one accepted answer">9%</span></p></div></div><div id="comments-container-3895" class="comments-container"></div><div id="comment-tools-3895" class="comment-tools"></div><div class="clear"></div><div id="comment-3895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

