+++
type = "question"
title = "PCRF - Diameter authorisation Rejected"
description = '''What all parameters need to be checked if PCRF gives Diameter Authorisation Rejected for CCR-I in LTE for customer in roaming connected to 3g network of foreign sgsn?'''
date = "2016-02-16T03:39:00Z"
lastmod = "2016-02-16T16:58:00Z"
weight = 50237
keywords = [ "pcrf" ]
aliases = [ "/questions/50237" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PCRF - Diameter authorisation Rejected](/questions/50237/pcrf-diameter-authorisation-rejected)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50237-score" class="post-score" title="current number of votes">0</div><span id="post-50237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What all parameters need to be checked if PCRF gives Diameter Authorisation Rejected for CCR-I in LTE for customer in roaming connected to 3g network of foreign sgsn?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcrf" rel="tag" title="see questions tagged &#39;pcrf&#39;">pcrf</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '16, 03:39</strong></p><img src="https://secure.gravatar.com/avatar/56c67589393df445272fc6b307cc8fbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="venu&#39;s gravatar image" /><p><span>venu</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="venu has no accepted answers">0%</span></p></div></div><div id="comments-container-50237" class="comments-container"></div><div id="comment-tools-50237" class="comment-tools"></div><div class="clear"></div><div id="comment-50237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50249"></span>

<div id="answer-container-50249" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50249-score" class="post-score" title="current number of votes">0</div><span id="post-50249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This really isn't a Wireshark question, but in concept when a PCRF rejects a CCR-I it's generally going to be because of a policy decision that it has made. While 3GPP does define some specific codes which can be sent for specific reasons on Gx (see TS 29.212, also RFCs 4006/6733 as referenced), in practice PCRFs virtually all have some kind of policy engine with which they accept/reject a CCR for all sorts of different reasons. In your scenario, possibly the PCRF has a policy to deny based on location, or serving network, or serving radio type, etc.</p><p>If it's only being rejected in that scenario, one question would be if it works in other scenarios and what AVP differences there are between the two of them (to give you a lead, if you're limiting the troubleshooting to 'on the wire' as opposed to the PCRF's policy configuration).</p><p>Also, what do you mean when you say the subscriber is "in LTE" and connected via an SGSN? That doesn't compute - no interface exists between an LTE radio network and the SGSN of a GPRS CN. Do you possibly mean an S3/S4-based roaming model from a visited SGSN from a UMTS network into your operator's PGW (<em>NOT</em> LTE)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '16, 16:58</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Feb '16, 16:59</strong> </span></p></div></div><div id="comments-container-50249" class="comments-container"></div><div id="comment-tools-50249" class="comment-tools"></div><div class="clear"></div><div id="comment-50249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

