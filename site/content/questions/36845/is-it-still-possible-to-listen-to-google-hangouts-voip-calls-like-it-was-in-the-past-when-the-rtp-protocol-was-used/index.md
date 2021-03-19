+++
type = "question"
title = "Is it still possible to listen to Google Hangouts VoIP calls like it was in the past when the RTP protocol was used..."
description = '''From my understanding, in the past, when the RTP protocol was used, one could easily hear their entire VoIP conversation on wireshark by decoding an RTP stream.  From what I have seen testing the new Google Hangouts interface, I noticed a complete lack of the RTP protocol when I tried to initiate a ...'''
date = "2014-10-04T23:18:00Z"
lastmod = "2015-01-08T10:21:00Z"
weight = 36845
keywords = [ "udp", "google", "stun", "voip", "hangouts" ]
aliases = [ "/questions/36845" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it still possible to listen to Google Hangouts VoIP calls like it was in the past when the RTP protocol was used...](/questions/36845/is-it-still-possible-to-listen-to-google-hangouts-voip-calls-like-it-was-in-the-past-when-the-rtp-protocol-was-used)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36845-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From my understanding, in the past, when the RTP protocol was used, one could easily hear their entire VoIP conversation on wireshark by decoding an RTP stream.</p><p>From what I have seen testing the new Google Hangouts interface, I noticed a complete lack of the RTP protocol when I tried to initiate a similar test. I noticed that on wireshark I was able to observe UDP and STUN protocol traffic....</p><p>I guess my question is how does one still listen to VoIP calls within Wireshark if at all still possible....It seems as if Google has increased their security.</p></div><div id="question-tags" class="tags-container tags">udp google stun voip hangouts</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '14, 23:18</strong></p><img src="https://secure.gravatar.com/avatar/4784c5fb1a0142030d51a339706a456c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beldum&#39;s gravatar image" /><p>Beldum<br />
<span class="score" title="49 reputation points">49</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beldum has no accepted answers">0%</span></p></div></div><div id="comments-container-36845" class="comments-container"><span id="36896"></span><div id="comment-36896" class="comment"><div id="post-36896-score" class="comment-score"></div><div class="comment-text"><p>Does anyone not know or does Google now encrypt their VoIP calls going over the Google Hangouts interface? RTP Protocol is what they used to use for their VoIP protocol. It seems now that they use a different protocol for VoIP. Can anyone else confirm this?</p></div><div id="comment-36896-info" class="comment-info"><span class="comment-age">(07 Oct '14, 13:24)</span> Beldum</div></div></div><div id="comment-tools-36845" class="comment-tools"></div><div class="clear"></div><div id="comment-36845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38970"></span>

<div id="answer-container-38970" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38970-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes it appears they are now using <a href="http://en.wikipedia.org/wiki/Secure_Real-time_Transport_Protocol">SRTP</a>:</p><p><a href="https://support.google.com/a/answer/1279090?hl=en">https://support.google.com/a/answer/1279090?hl=en</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '15, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/f6418e5cfbcd9b3063b99375e7acefd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cride5&#39;s gravatar image" /><p>Cride5<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cride5 has no accepted answers">0%</span></p></div></div><div id="comments-container-38970" class="comments-container"></div><div id="comment-tools-38970" class="comment-tools"></div><div class="clear"></div><div id="comment-38970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

