+++
type = "question"
title = "MGCP signaling in the &quot;Voip Calls&quot; flow"
description = '''In previous versions 1.2.x, I saw that the MGCP signaling was included in the flow generated from the &quot;VoIP Calls&quot; selection (after selecting the desired calls and clicking on &quot;Flow&quot;). Is there a setting/workaround to have both SIP and MGCP in the flows generated from &quot;VoIP Calls&quot;. Regards, Antonios...'''
date = "2010-10-11T03:25:00Z"
lastmod = "2010-10-12T22:59:00Z"
weight = 475
keywords = [ "flow", "mgcp", "voip" ]
aliases = [ "/questions/475" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MGCP signaling in the "Voip Calls" flow](/questions/475/mgcp-signaling-in-the-voip-calls-flow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-475-score" class="post-score" title="current number of votes">0</div><span id="post-475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In previous versions 1.2.x, I saw that the MGCP signaling was included in the flow generated from the "VoIP Calls" selection (after selecting the desired calls and clicking on "Flow"). Is there a setting/workaround to have both SIP and MGCP in the flows generated from "VoIP Calls".</p><p>Regards, Antonios</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-flow" rel="tag" title="see questions tagged &#39;flow&#39;">flow</span> <span class="post-tag tag-link-mgcp" rel="tag" title="see questions tagged &#39;mgcp&#39;">mgcp</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '10, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/3bee86f8fe1baca8cc9348ef75868501?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="antpap&#39;s gravatar image" /><p><span>antpap</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="antpap has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Nov '10, 06:54</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-475" class="comments-container"></div><div id="comment-tools-475" class="comment-tools"></div><div class="clear"></div><div id="comment-475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="476"></span>

<div id="answer-container-476" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-476-score" class="post-score" title="current number of votes">3</div><span id="post-476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can select multiple calls in the VoIP calls dialog, irrespective of protocol. These will all be rendered in the flow.</p><p>Oh, and make sure you've Wireshark 1.4.1, which fixes <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5167">bug 5167</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '10, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Oct '10, 02:14</strong> </span></p></div></div><div id="comments-container-476" class="comments-container"><span id="498"></span><div id="comment-498" class="comment"><div id="post-498-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jaap for your answer.</p></div><div id="comment-498-info" class="comment-info"><span class="comment-age">(12 Oct '10, 22:59)</span> <span class="comment-user userinfo">antpap</span></div></div></div><div id="comment-tools-476" class="comment-tools"></div><div class="clear"></div><div id="comment-476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

