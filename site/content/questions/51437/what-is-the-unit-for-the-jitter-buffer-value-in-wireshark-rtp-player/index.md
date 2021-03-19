+++
type = "question"
title = "What is the unit for the jitter buffer value in Wireshark - RTP Player"
description = '''Hi, We are currently troubleshooting a delay issue in our network and I would like to know what unit the jitter buffer value is in the Wireshark - RTP Player? Thanks! Kind regards, Nicklas.'''
date = "2016-04-06T07:57:00Z"
lastmod = "2016-04-07T01:09:00Z"
weight = 51437
keywords = [ "buffer", "player", "jitter", "rtp" ]
aliases = [ "/questions/51437" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is the unit for the jitter buffer value in Wireshark - RTP Player](/questions/51437/what-is-the-unit-for-the-jitter-buffer-value-in-wireshark-rtp-player)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51437-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We are currently troubleshooting a delay issue in our network and I would like to know what unit the jitter buffer value is in the Wireshark - RTP Player?</p><p>Thanks!</p><p>Kind regards, Nicklas.</p></div><div id="question-tags" class="tags-container tags">buffer player jitter rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '16, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/767128887e7c9e47b9c0fb5cb760cc8a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nicklas%20Bargell&#39;s gravatar image" /><p>Nicklas Bargell<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nicklas Bargell has no accepted answers">0%</span></p></div></div><div id="comments-container-51437" class="comments-container"></div><div id="comment-tools-51437" class="comment-tools"></div><div class="clear"></div><div id="comment-51437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51451"></span>

<div id="answer-container-51451" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51451-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That would be milliseconds, or something odd is going on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '16, 01:09</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-51451" class="comments-container"><span id="51453"></span><div id="comment-51453" class="comment"><div id="post-51453-score" class="comment-score"></div><div class="comment-text"><p>That's what I thought, but when I replay the same sound stream both incoming and outgoing and change the value from 50 where there is almost no delay down to 5 I get lots of delay. More then a few seconds. And that seems strange?</p></div><div id="comment-51453-info" class="comment-info"><span class="comment-age">(07 Apr '16, 01:18)</span> Nicklas Bargell</div></div><span id="51462"></span><div id="comment-51462" class="comment"><div id="post-51462-score" class="comment-score"></div><div class="comment-text"><p>Not nessaserraly. You would have to delve into the internals of media play out to see what's going on. Effectively what you did is (depending on the specifics of the packet time stamp distribution) making it very hard for RTP packets to hit the window in which they can be accepted for play out. Usually a single packet represents 20 to 30 ms of speech, so 5 ms is very narrow in that respect, probably causing the play out mechanism to have to resync all the time, possibly causing these long mutes. As you see there are a lot of ifs, because it all depends on the specifics of your RTP stream. But you could start by looking at the packet time and use that as lower limit for jitter buffer.</p></div><div id="comment-51462-info" class="comment-info"><span class="comment-age">(07 Apr '16, 04:50)</span> Jaap ♦</div></div></div><div id="comment-tools-51451" class="comment-tools"></div><div class="clear"></div><div id="comment-51451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

