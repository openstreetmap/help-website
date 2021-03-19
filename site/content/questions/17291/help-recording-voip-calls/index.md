+++
type = "question"
title = "Help recording VoIP Calls?"
description = '''Hello everyone, I am trying to create an audio installation for an art show next season which requires live sampling of phone conversations from willing participants. I have turned to Wireshark as a means of recording these calls wirelessly. So far, I have tried to use the &quot;VoIP Calls&quot; feature under...'''
date = "2012-12-27T19:14:00Z"
lastmod = "2012-12-27T21:40:00Z"
weight = 17291
keywords = [ "sip", "rtp", "voip" ]
aliases = [ "/questions/17291" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Help recording VoIP Calls?](/questions/17291/help-recording-voip-calls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17291-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>I am trying to create an audio installation for an art show next season which requires live sampling of phone conversations from willing participants. I have turned to Wireshark as a means of recording these calls wirelessly. So far, I have tried to use the "VoIP Calls" feature under the Telephony menu to capture conversations and record them, but the calls i'm making are not being picked up by Wireshark.</p><p>Here is my setup: 2 smartphones (both Android) both connected to the same home internet service (Verizon FiOS). My computer is also connected to the same home wifi signal, but when I start capturing packets on this wifi signal I am NOT able to detect the VoIP call being made on these smartphones (using the smartphone app Viber).</p><p>Can anyone tell me what I'm doing wrong? Maybe suggest a better method of capturing VoIP calls on my laptop? Also, if there is a way to save these conversations to a folder on my computer AUTOMATICALLY it would save a lot of coding.</p><p>Any help would be GREATLY appreciated!</p><p>Thank you so much for your time, Sebastian</p></div><div id="question-tags" class="tags-container tags">sip rtp voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Dec '12, 19:14</strong></p><img src="https://secure.gravatar.com/avatar/56cdf5d2722f372c5b882e7085b8e40b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seba1685&#39;s gravatar image" /><p>seba1685<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seba1685 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Nov '13, 14:27</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-17291" class="comments-container"></div><div id="comment-tools-17291" class="comment-tools"></div><div class="clear"></div><div id="comment-17291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17293"></span>

<div id="answer-container-17293" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17293-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can anyone tell me what I'm doing wrong?</p></blockquote><p>Your capture setup is possibly not ready for wifi/wlan capturing. Please read the wiki about capturing traffic in such an environment: <code>http://wiki.wireshark.org/CaptureSetup/WLAN</code></p><blockquote><p>I am NOT able to detect the VoIP call being made on these smartphones (using the smartphone app Viber).</p></blockquote><p>well, even if see the wifi/wlan traffic of the phones, you may not be able to capture 'voip' calls made via <strong>viber.com</strong>. I don't know for sure, but I'm pretty confident, that they will use their own protocol and I hope they will use encryption, otherwise I would consider <strong>viber.com</strong> a security failure and not a service ;-). Unfortunately both issues (own protocol <strong>and</strong> encryption) will make it hard/impossible to extract any valuable information from the captured packets. Anyway, you will see how far you get, as soon as your wlan/wifi capture setup works.</p><p>HINT: wifi monitoring mode (see wiki) is not supported on Windows with WinPcap, so if you want to capture the wifi/wlan traffic of your android phones you either have to use a special adapter on Windows (AirPcap) or use Linux as the platform for Wireshark.</p><p><strong>UPDATE</strong><br />
Please read the following paper regarding viber security. It explains some concepts (protocol,'encryption/scrambling', etc.)</p><blockquote><p><code>https://www.os3.nl/2011-2012/students/jeffrey_bosma/courses/ssn/assignments/project</code><br />
</p></blockquote><p>Regards<br />
Kurt</p><p>[01/05/2015: Update [wmeier]: The above link appears to require a login]</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '12, 21:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jan '16, 07:50</p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></br></p></div></div><div id="comments-container-17293" class="comments-container"><span id="48845"></span><div id="comment-48845" class="comment"><div id="post-48845-score" class="comment-score"></div><div class="comment-text"><p>Hi I was trying to access the link above but seems I am not allowed. Is it possible to put it somewhere or to allow viewing?</p><p>thank you</p><p>Libor</p></div><div id="comment-48845-info" class="comment-info"><span class="comment-age">(04 Jan '16, 09:41)</span> Libor Ballaty</div></div><span id="48858"></span><div id="comment-48858" class="comment"><div id="post-48858-score" class="comment-score"></div><div class="comment-text"><p>The link is external to this site, and I believe is nothing to do with @Kurt Knochner, so we can't help unfortunately. Maybe someone else has a copy of the paper.</p></div><div id="comment-48858-info" class="comment-info"><span class="comment-age">(05 Jan '16, 00:25)</span> grahamb ♦</div></div></div><div id="comment-tools-17293" class="comment-tools"></div><div class="clear"></div><div id="comment-17293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

