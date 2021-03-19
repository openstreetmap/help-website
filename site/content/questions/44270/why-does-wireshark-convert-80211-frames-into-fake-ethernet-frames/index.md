+++
type = "question"
title = "Why does Wireshark convert 802.11 frames into &#x27;fake&#x27; Ethernet frames?"
description = '''Hi, I was wondering why Wireshark converts 802.11 frames into &#x27;fake&#x27; Ethernet frames during captures. Why would it be such a problem to send the actual 802.11 frame to the packet capture mechanism? Thanks.'''
date = "2015-07-17T15:13:00Z"
lastmod = "2015-07-17T17:05:00Z"
weight = 44270
keywords = [ "ethernet", "frame", "802.11", "fake" ]
aliases = [ "/questions/44270" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why does Wireshark convert 802.11 frames into 'fake' Ethernet frames?](/questions/44270/why-does-wireshark-convert-80211-frames-into-fake-ethernet-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44270-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I was wondering why Wireshark converts 802.11 frames into 'fake' Ethernet frames during captures. Why would it be such a problem to send the actual 802.11 frame to the packet capture mechanism?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">ethernet frame 802.11 fake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '15, 15:13</strong></p><img src="https://secure.gravatar.com/avatar/b4b980e73fe09f3367d0d813bbec21b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfer3351&#39;s gravatar image" /><p>jfer3351<br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfer3351 has no accepted answers">0%</span></p></div></div><div id="comments-container-44270" class="comments-container"></div><div id="comment-tools-44270" class="comment-tools"></div><div class="clear"></div><div id="comment-44270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44275"></span>

<div id="answer-container-44275" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44275-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark does not convert 802.11 frames into fake Ethernet frames. This is not something unique to Wireshark; you will see the same behavior with tcpdump, for example.</p><p>The OS software (driver, networking stack) that supplies packets to the capture mechanism does so. Wireshark is stuck with what gets delivered to it from the capture mechanism.</p><p>For whatever reason, unless you're capturing in monitor mode, you get fake Ethernet frames, on several OSes, and you only get data frames, not management or control frames.</p><p>You'd have to ask the developers of the drivers and networking stack for the OS you're using why they chose to do that. There was, as I remember, a time where, in FreeBSD, you could select either fake Ethernet or 802.11 headers when capturing, even when not capturing in monitor mode, but I'm not sure they still support that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '15, 17:05</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-44275" class="comments-container"><span id="44288"></span><div id="comment-44288" class="comment"><div id="post-44288-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy,</p><p>Thanks for your very comprehensive answer.</p><p>I will try to find out why the driver/networking stack developers made such decision and, if successful, I will post the answer here.</p><p>Cheers.</p></div><div id="comment-44288-info" class="comment-info"><span class="comment-age">(18 Jul '15, 15:03)</span> jfer3351</div></div></div><div id="comment-tools-44275" class="comment-tools"></div><div class="clear"></div><div id="comment-44275-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

