+++
type = "question"
title = "Robotic sound when playing decode RTP traffic"
description = '''Wireshark version from 2.0.0 to 2.0.5 Windows 7 Pro 64bit'''
date = "2016-08-11T00:00:00Z"
lastmod = "2016-08-11T01:04:00Z"
weight = 54730
keywords = [ "problem", "rtp" ]
aliases = [ "/questions/54730" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Robotic sound when playing decode RTP traffic](/questions/54730/robotic-sound-when-playing-decode-rtp-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54730-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark version from 2.0.0 to 2.0.5 Windows 7 Pro 64bit</p></div><div id="question-tags" class="tags-container tags">problem rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '16, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/cba678334ea6cb3f257b35321d2e65de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MikeLog&#39;s gravatar image" /><p>MikeLog<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MikeLog has no accepted answers">0%</span></p></div></div><div id="comments-container-54730" class="comments-container"></div><div id="comment-tools-54730" class="comment-tools"></div><div class="clear"></div><div id="comment-54730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54732"></span>

<div id="answer-container-54732" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54732-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That is a typical effect of packet loss concealment, at a rate of about 20-30%. Why this happens in your case I don't know.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '16, 01:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54732" class="comments-container"><span id="54736"></span><div id="comment-54736" class="comment"><div id="post-54736-score" class="comment-score"></div><div class="comment-text"><p>@Jaap, "robotic sound" can also be a consequence of various other issues, so your favourite "42" would have been a much more appropriate answer to this non-question :)</p><p>@MikeLog, if you want a less generic answer than "42", publish the capture (the RTP stream in question is enough), and explain whether you complain about Wireshark 2.0.x playing it wrong because the same stream was played fine in 1.y.z Wireshark versions, or whether you want to help identify the reason why the stream sounds weird in Wireshark although it sounded fine during the actual call, ...</p></div><div id="comment-54736-info" class="comment-info"><span class="comment-age">(11 Aug '16, 01:26)</span> sindy</div></div><span id="54757"></span><div id="comment-54757" class="comment"><div id="post-54757-score" class="comment-score"></div><div class="comment-text"><p>@sindy: I've worked on a packet loss concealment solution in a VoIP product, where this very same effect became very noticeable at those packet loss rates with the solution engaged. Therefore I recognized that specific observation, as I made then.</p></div><div id="comment-54757-info" class="comment-info"><span class="comment-age">(11 Aug '16, 12:42)</span> Jaap ♦</div></div><span id="54758"></span><div id="comment-54758" class="comment"><div id="post-54758-score" class="comment-score"></div><div class="comment-text"><p>@Jaap, I don't have any issue with the fact that 20-30 % packet loss has heavy impact on voice quality; the reason why I've stated that many other reasons may exist is that my experience shows that different people may call different types of distortion "robotic voice". E.g., mere overload of the input amplifier, causing signal limitation before A-&gt;D conversion and thus leading to presence of harmonic frequencies in the signal spectrum, makes some receiving parties call the result a "robotic voice". Maybe it is because each of these people has seen a different episode of Sky Wars ;-)</p><p>But let's let the OP elaborate first. No doubt that the "Play Streams" functionality in the early versions of 2.0.x wasn't as good as it used to be in the GTK, but it is better with every version.</p></div><div id="comment-54758-info" class="comment-info"><span class="comment-age">(11 Aug '16, 12:59)</span> sindy</div></div></div><div id="comment-tools-54732" class="comment-tools"></div><div class="clear"></div><div id="comment-54732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

