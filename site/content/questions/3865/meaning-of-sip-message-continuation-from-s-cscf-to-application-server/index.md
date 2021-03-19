+++
type = "question"
title = "meaning of SIP message &quot;Continuation&quot; from S-CSCF to Application Server?"
description = '''What can/could this message mean? '''
date = "2011-05-01T16:29:00Z"
lastmod = "2011-05-04T19:12:00Z"
weight = 3865
keywords = [ "s-cscf", "message", "continue", "server", "application" ]
aliases = [ "/questions/3865" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [meaning of SIP message "Continuation" from S-CSCF to Application Server?](/questions/3865/meaning-of-sip-message-continuation-from-s-cscf-to-application-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3865-score" class="post-score" title="current number of votes">0</div><span id="post-3865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What can/could this message mean?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-s-cscf" rel="tag" title="see questions tagged &#39;s-cscf&#39;">s-cscf</span> <span class="post-tag tag-link-message" rel="tag" title="see questions tagged &#39;message&#39;">message</span> <span class="post-tag tag-link-continue" rel="tag" title="see questions tagged &#39;continue&#39;">continue</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-application" rel="tag" title="see questions tagged &#39;application&#39;">application</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '11, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/13231e33ab17a93476f7b98c9d5b272a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wired&#39;s gravatar image" /><p><span>wired</span><br />
<span class="score" title="44 reputation points">44</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wired has one accepted answer">9%</span></p></div></div><div id="comments-container-3865" class="comments-container"><span id="3866"></span><div id="comment-3866" class="comment"><div id="post-3866-score" class="comment-score"></div><div class="comment-text"><p>Are "Continuation" messages TCP keep-alive messages?</p><p>Or is this just information message which (can) tell us that INVITE requests and (re)tries (Status: 100 Trying) (will) continue?</p></div><div id="comment-3866-info" class="comment-info"><span class="comment-age">(01 May '11, 16:40)</span> <span class="comment-user userinfo">wired</span></div></div></div><div id="comment-tools-3865" class="comment-tools"></div><div class="clear"></div><div id="comment-3865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="3871"></span>

<div id="answer-container-3871" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3871-score" class="post-score" title="current number of votes">0</div><span id="post-3871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>i, "Continuation" in SIP messages means that Wireshark couldn't parse the SIP message properly probably because reassembly did not work properly a couple of bugs/improvements has been made in the TCP dissector in trunk. If you have the possibility to download a build bot build you could try that. Regards Anders</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '11, 01:16</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-3871" class="comments-container"></div><div id="comment-tools-3871" class="comment-tools"></div><div class="clear"></div><div id="comment-3871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3875"></span>

<div id="answer-container-3875" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3875-score" class="post-score" title="current number of votes">0</div><span id="post-3875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is reassembling actually encapsulation?</p><p>TCP dissector in trunk - What's dissector? Trunk has many meanings, what's the right one in this case?</p><p>If S-CSCF sends Continuation message to AS, this means that S-CSCF will continue with reassembling the SIP message?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '11, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/13231e33ab17a93476f7b98c9d5b272a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wired&#39;s gravatar image" /><p><span>wired</span><br />
<span class="score" title="44 reputation points">44</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wired has one accepted answer">9%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 May '11, 06:30</strong> </span></p></div></div><div id="comments-container-3875" class="comments-container"><span id="3878"></span><div id="comment-3878" class="comment"><div id="post-3878-score" class="comment-score"></div><div class="comment-text"><p>When something is transfered over TCP the higher level PDU, in this case SIP may be fragmented e.g there will not be a complete SIP message in a TCP frame. So Wireshark may need to "reassemble" TCP messages to build a complete SIP message to display. In wireshark the programs displaying the protocols are called dissectors. Trunk reefers to the working SW repository where the Wireshark sources are keept. I don't think the S-CSCF has any problems with these messages. Is something not working right?</p></div><div id="comment-3878-info" class="comment-info"><span class="comment-age">(02 May '11, 08:20)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-3875" class="comment-tools"></div><div class="clear"></div><div id="comment-3875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3881"></span>

<div id="answer-container-3881" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3881-score" class="post-score" title="current number of votes">0</div><span id="post-3881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi.</p><p>Probably something wasnt' ok, but I can't be sure. I got the trace from my coworker . Anyway, thanks for explanation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '11, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/13231e33ab17a93476f7b98c9d5b272a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wired&#39;s gravatar image" /><p><span>wired</span><br />
<span class="score" title="44 reputation points">44</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wired has one accepted answer">9%</span></p></div></div><div id="comments-container-3881" class="comments-container"></div><div id="comment-tools-3881" class="comment-tools"></div><div class="clear"></div><div id="comment-3881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3929"></span>

<div id="answer-container-3929" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3929-score" class="post-score" title="current number of votes">0</div><span id="post-3929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I noticed something:</p><p>When I filtered SIP traffic directly from original trace file, message Continuation didn't show up. But when I gave to Wireshark "IP command" to ignore some IP addresses and then filtered SIP traffic again, there it was this Continuation message.</p><p>So, if I think clearly and I'm right, Continuation isn't neither SIP request neither SIP answer, but simply application message from Wireshark? ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '11, 19:12</strong></p><img src="https://secure.gravatar.com/avatar/13231e33ab17a93476f7b98c9d5b272a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wired&#39;s gravatar image" /><p><span>wired</span><br />
<span class="score" title="44 reputation points">44</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wired has one accepted answer">9%</span></p></div></div><div id="comments-container-3929" class="comments-container"></div><div id="comment-tools-3929" class="comment-tools"></div><div class="clear"></div><div id="comment-3929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

