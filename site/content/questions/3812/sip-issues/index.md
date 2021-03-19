+++
type = "question"
title = "SIP Issues"
description = '''Okay hopefully someone will be able to shed some light on what I am trying to do. Keep in mind that I am a phone guy and not a Network guy! I am having a terrible Audio Issue with a voicemail server that is using SIP to connect to the PBX. I have been able to determine (through wireshark) that the a...'''
date = "2011-04-29T07:28:00Z"
lastmod = "2011-04-30T01:50:00Z"
weight = 3812
keywords = [ "sip" ]
aliases = [ "/questions/3812" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SIP Issues](/questions/3812/sip-issues)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3812-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Okay hopefully someone will be able to shed some light on what I am trying to do. Keep in mind that I am a phone guy and not a Network guy!</p><p>I am having a terrible Audio Issue with a voicemail server that is using SIP to connect to the PBX. I have been able to determine (through wireshark) that the audio is OK when leaving the server. I have done that by capturing a call and playing it back through the player.</p><p>So for example I call into the auto attendant and the audio is terrible, sometimes cutting out for up to 4-5 seconds. During that test call I had wireshark capturing this event. I then played back the file and the audio is fine. So logic tells me that the loss is happening after it leaves the server.</p><p>So the question is how to I determine where the loss is occuring. Can I play that file on the receiving end of the call. Meaning the IP address that the packets are sent too? For example the IP of the Voicemail Server is 10.0.0.1 and the IP of the phone equipment is 10.0.0.2, I need to know if there is a way to listen to it when it hits 10.0.0.2. If anyone is knowledable in this area, and could possibly help me out, that would be great!</p><p>Thanks Joe</p></div><div id="question-tags" class="tags-container tags">sip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '11, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/2459ee8a01b077a8719121183a8f8998?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoeD&#39;s gravatar image" /><p>JoeD<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoeD has no accepted answers">0%</span></p></div></div><div id="comments-container-3812" class="comments-container"></div><div id="comment-tools-3812" class="comment-tools"></div><div class="clear"></div><div id="comment-3812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3837"></span>

<div id="answer-container-3837" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3837-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is usually indicative of a packet size mismatch. If you have captured the SIP/SDP messages work your way down into the media negotiations. There will be ptime attributes in their which state what the desired packet size is (in ms of audio in the specified codec). Rough guess is 20 (ms) for codec 0 (G.711 u-law). That should lead to an RTP stream with 160 octets payload (G.711: 80 8it samples per 10 ms). If your media interface at the PBX side gets RTP packets with a size it does not like it may have trouble digesting them. Also try to figure out from the documentation what the allowed packets sizes are.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '11, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3837" class="comments-container"></div><div id="comment-tools-3837" class="comment-tools"></div><div class="clear"></div><div id="comment-3837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

