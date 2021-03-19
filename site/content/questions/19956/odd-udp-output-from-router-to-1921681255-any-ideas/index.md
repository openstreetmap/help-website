+++
type = "question"
title = "Odd UDP output from router to 192.168.1.255 -- any ideas?"
description = '''Hello I&#x27;m trying to understand a piece of Wireshark output. Every five seconds it records this same transaction, showing the router broadcasting to 192.168.1.255 on UDP port 9246: 192.168.1.1 192.168.1.255 UDP 100 Source port: 9246 Destination port: 9246 The follow UDP stream gives lines of this: &quot;i...'''
date = "2013-03-30T08:30:00Z"
lastmod = "2013-03-30T10:41:00Z"
weight = 19956
keywords = [ "udp", "192.168.1.255" ]
aliases = [ "/questions/19956" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Odd UDP output from router to 192.168.1.255 -- any ideas?](/questions/19956/odd-udp-output-from-router-to-1921681255-any-ideas)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19956-score" class="post-score" title="current number of votes">0</div><span id="post-19956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I'm trying to understand a piece of Wireshark output. Every five seconds it records this same transaction, showing the router broadcasting to 192.168.1.255 on UDP port 9246:</p><p>192.168.1.1 192.168.1.255 UDP 100 Source port: 9246 Destination port: 9246</p><p>The follow UDP stream gives lines of this:</p><p>"ism://192.168.1.1:9246/?nameGateway=GwcVoice&amp;sslMthd=none.ism://192.168.1.1:9246/?"</p><p>Any clues as to what might be causing this behaviour much appreciated.</p><p>D</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-192.168.1.255" rel="tag" title="see questions tagged &#39;192.168.1.255&#39;">192.168.1.255</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '13, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/13d609e5a2f6ceeb5a3335a095480fbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sysadmin43&#39;s gravatar image" /><p><span>Sysadmin43</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sysadmin43 has no accepted answers">0%</span></p></div></div><div id="comments-container-19956" class="comments-container"></div><div id="comment-tools-19956" class="comment-tools"></div><div class="clear"></div><div id="comment-19956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19959"></span>

<div id="answer-container-19959" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19959-score" class="post-score" title="current number of votes">0</div><span id="post-19959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>not sure but I think this might be Nortel protocol. Gateway Controller (GWC) acts as a call processing protocol converter between the CS 2000 series messages and the open-standard H.248 messages used by the MG 9000 and the Universal Audio Server (UAS) Integrated Services Module (ISM) provides conference circuits, enhanced digital announcement machine (EDRAM) announcements, and line test, trunk test, and office alarm unit interfaces</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '13, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-19959" class="comments-container"></div><div id="comment-tools-19959" class="comment-tools"></div><div class="clear"></div><div id="comment-19959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19961"></span>

<div id="answer-container-19961" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19961-score" class="post-score" title="current number of votes">0</div><span id="post-19961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hmm..."ism://" doesn't show up in any of the various URI/URL scheme references.</p><p>Just guessing from the content, I'd say that your wireless router has some sort of VoIP support, and that these broadcasts are its hooks for server/gateway discovery by clients. Many wireless routers support VoIP in the ISM band...</p><p>You could prove/disprove this by disabling VoIP support in the wireless router and grabbing a fresh capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '13, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Mar '13, 10:42</strong> </span></p></div></div><div id="comments-container-19961" class="comments-container"></div><div id="comment-tools-19961" class="comment-tools"></div><div class="clear"></div><div id="comment-19961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

