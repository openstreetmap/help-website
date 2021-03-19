+++
type = "question"
title = "Trace of a phone call"
description = '''With the attached trace you can see a phone call from packet 710 14:06:43.761721 192.168.140.231 192.168.100.231 H.225.0 1012 CS: setup OpenLogicalChannel CS: setup OpenLogicalChannel  To me it looks like 1720 is open and responding, Alcatel says differently and that&#x27;s the problem. From a phone call...'''
date = "2012-12-12T06:36:00Z"
lastmod = "2012-12-13T05:10:00Z"
weight = 16801
keywords = [ "voice", "1720", "hdx" ]
aliases = [ "/questions/16801" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trace of a phone call](/questions/16801/trace-of-a-phone-call)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16801-score" class="post-score" title="current number of votes">0</div><span id="post-16801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>With the attached trace you can see a phone call from packet 710 14:06:43.761721 192.168.140.231 192.168.100.231 H.225.0 1012 CS: setup OpenLogicalChannel CS: setup OpenLogicalChannel</p><p>To me it looks like 1720 is open and responding, Alcatel says differently and that's the problem.</p><p>From a phone call perspective the extension is dialed from 192.168.140.231's location to 192.168.100.231 and the call connects, there's dead air for about 5 seconds, then the call disconnects.</p><p>How can i use this trace to figure out what's going on?</p><p>Thanks in advance!</p><p>Oh how do i attach?</p><p>TCP Stream 0:</p><p>710 14:06:43.761721 192.168.140.231 192.168.100.231 H.225.0 1012 CS: setup OpenLogicalChannel CS: setup OpenLogicalChannel</p><p>714 14:06:43.784934 192.168.100.231 192.168.140.231 H.225.0/H.225.0/H.245 458 CS: callProceeding CS: alerting OpenLogicalChannel CS: connect CS: empty roundTripDelayRequest CS: empty roundTripDelayRequest</p><p>715 14:06:43.785314 192.168.140.231 192.168.100.231 TCP 60 21021 &gt; h323hostcall [RST, ACK] Seq=3320372537 Ack=2 Win=0 Len=0</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-voice" rel="tag" title="see questions tagged &#39;voice&#39;">voice</span> <span class="post-tag tag-link-1720" rel="tag" title="see questions tagged &#39;1720&#39;">1720</span> <span class="post-tag tag-link-hdx" rel="tag" title="see questions tagged &#39;hdx&#39;">hdx</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '12, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/29c58be3d3185018b724cf9f0aebf8bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Willmeister&#39;s gravatar image" /><p><span>Willmeister</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Willmeister has no accepted answers">0%</span></p></div></div><div id="comments-container-16801" class="comments-container"><span id="16832"></span><div id="comment-16832" class="comment"><div id="post-16832-score" class="comment-score"></div><div class="comment-text"><p>Post the capture on CloudShark if you can.</p></div><div id="comment-16832-info" class="comment-info"><span class="comment-age">(13 Dec '12, 05:10)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-16801" class="comment-tools"></div><div class="clear"></div><div id="comment-16801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

