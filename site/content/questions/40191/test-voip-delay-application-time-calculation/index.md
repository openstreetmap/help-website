+++
type = "question"
title = "Test Voip delay. Application time calculation"
description = '''Hello, I have a network that run voip application between two different locations. Basically, several voip devices connected to the switch and then to the router network at one location. Same exactly setup is at the different location. (east coast /west coast) I can use ping to calculate network del...'''
date = "2015-03-02T12:48:00Z"
lastmod = "2015-03-03T07:42:00Z"
weight = 40191
keywords = [ "delay", "applicaitondelay", "voiptime", "voip", "rtp" ]
aliases = [ "/questions/40191" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Test Voip delay. Application time calculation](/questions/40191/test-voip-delay-application-time-calculation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40191-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have a network that run voip application between two different locations. Basically, several voip devices connected to the switch and then to the router network at one location. Same exactly setup is at the different location. (east coast /west coast) I can use ping to calculate network delay between any device. How do i calculate total delay? (network delay plus application delay) By application delay i mean buffer time, decode/encode time, software processing time. I am interested in calculating voice delay from time i speak to the microphone to the time i hear voice at the other end. I am not sure if this is possible using wireshark..If not, what kind of test sets that will do this? thank you alex</p></div><div id="question-tags" class="tags-container tags">delay applicaitondelay voiptime voip rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '15, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/f442483e6ecbafaf8baad63877f86f2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexg1485&#39;s gravatar image" /><p>alexg1485<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexg1485 has no accepted answers">0%</span></p></div></div><div id="comments-container-40191" class="comments-container"></div><div id="comment-tools-40191" class="comment-tools"></div><div class="clear"></div><div id="comment-40191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40219"></span>

<div id="answer-container-40219" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40219-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For that you'll need an audio test. Make an impulse at the mic, and time the arrival at the speaker. The trick is to have synchronized clocks at both ends.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '15, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-40219" class="comments-container"><span id="40226"></span><div id="comment-40226" class="comment"><div id="post-40226-score" class="comment-score"></div><div class="comment-text"><p>This technique is common for the analog audio lines. Unfortunately, i am not familiar with any of the voip tests that will do this. Do you have a name of the audio test that you use?<br />
</p></div><div id="comment-40226-info" class="comment-info"><span class="comment-age">(03 Mar '15, 12:29)</span> alexg1485</div></div><span id="40258"></span><div id="comment-40258" class="comment"><div id="post-40258-score" class="comment-score"></div><div class="comment-text"><p>Well, as you describe it, it is very much like testing analog audio lines. The mic and speaker are analog devices after all.</p><p>If you want to remain in the digital domain and stick to your requirements, you'll have to hook up at the ADC near the mic and the DAC at the speaker. Otherwise you'll miss the application delay. Not easy when you have no access to the internals of the devices.</p><p>You could break up the measurements in blocks, measure the delay from audio input to network output (encoding delayt), network input to audio output (decoding delay) and then the end-to-end network delay. The first two are tricky to get the correlation right, but it's all local. The end-to-end network delay can be derived from synchronized captures, or using the RTCP info (if present). All is left is the possible variable packet buffer in the receiving terminal. That will depend on (variations in) end-to-end network conditions.</p></div><div id="comment-40258-info" class="comment-info"><span class="comment-age">(04 Mar '15, 05:36)</span> Jaap ♦</div></div></div><div id="comment-tools-40219" class="comment-tools"></div><div class="clear"></div><div id="comment-40219-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

