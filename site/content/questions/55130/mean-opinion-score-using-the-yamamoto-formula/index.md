+++
type = "question"
title = "Mean Opinion Score using the Yamamoto Formula"
description = '''Hello, I would like to calculate the mean opinion score using the Yamamoto Formula : P_Mos = 4.0 - 0.7 ln (packet_loss ratio) - 0.1 ln (duration of the missing segment in ms)  I can easily calculate packet loss ratio from packet capture. is there any way to get the duration of the missing segment fr...'''
date = "2016-08-26T11:57:00Z"
lastmod = "2016-08-27T00:41:00Z"
weight = 55130
keywords = [ "mos", "packetloss" ]
aliases = [ "/questions/55130" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mean Opinion Score using the Yamamoto Formula](/questions/55130/mean-opinion-score-using-the-yamamoto-formula)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55130-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I would like to calculate the mean opinion score using the <a href="http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=CCD92036D0C50DE295DC307DE70C1E7A?doi=10.1.1.21.5576&amp;rep=rep1&amp;type=pdf">Yamamoto Formula</a> :</p><pre><code>P_Mos = 4.0 - 0.7 ln (packet_loss ratio) - 0.1 ln (duration of the missing segment in ms)</code></pre><p>I can easily calculate packet loss ratio from packet capture. is there any way to get the duration of the missing segment from Wireshark/Tshark?</p></div><div id="question-tags" class="tags-container tags">mos packetloss</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '16, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/6d0c766426423882a424db011d1b5cff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wirecod&#39;s gravatar image" /><p>Wirecod<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wirecod has no accepted answers">0%</span></p></div></div><div id="comments-container-55130" class="comments-container"></div><div id="comment-tools-55130" class="comment-tools"></div><div class="clear"></div><div id="comment-55130-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55140"></span>

<div id="answer-container-55140" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55140-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The paper you refer to describes missing segment duration the following way:</p><blockquote><p>the <em>size</em> is the <strong>packet size</strong> (actually the duration of the missing segment) in milliseconds (from 3 to 96 ms).</p></blockquote><p>From such wording we can deduce that the case of loss of several adjacent RTP packets is not taken into account.</p><p>So the task is to convert the packet size in bytes into the packet size in time domain (i.e. in milliseconds). There are several approaches to that:</p><ul><li><p>to count the packet duration as <code>total time / number of packets</code>, but as there is packet loss, you may feel the result won't be precise enough (but if there is 10 % packet loss, causing the calculated size of the "missing segment" to be 10 % longer, I'm afraid the <code>-0.7 ln (packet loss ratio)</code> element of the formula becomes so dominant that the precision of the missing segment size has little impact on the total. This method is definitely unusable if any "silence suppression" (actually, bandwidth saving by transmission suppression during silence periods) mechanism is active, or intentional packet duplication is used, etc.</p></li><li><p>to look at the size in bytes of the payload of a single RTP packet of the basic codec (i.e. no comfort noise or telephone-event packets), and use a table as below to convert this value into milliseconds:</p></li></ul><p><code>codec    sample rate [Hz]    bytes of payload per millisecond</code><br />
<code>PCMA     8000                 8</code><br />
<code>G729     8000                 1</code><br />
</p><p>The sample rate is normally stated in the SDP, but for some codecs there is a default one. You have to look to the SDP anyway as the translation of payload type number (as found in the RTP packet) to codec name is there; theoretically, even the well-known values like 0, 8, 18 may be overridden.</p><ul><li>to take the difference of RTP timestamps (not of capture frame timestamps!) of two adjacent packets (i.e. those whose RTP sequential numbers differ by 1), and divide the difference by the sample rate in Hz. This way, you don't need to know what the actual codec is unless the sample rate is missing in the SDP and you need to find the default one. But again, the sample rate in the SDP may theoretically differ per codec so you must look for the one matching the payload type number in the RTP packet.</li></ul><p>For variable bitrate codecs (like e.g. Opus), none of these methods is reliable, yet there the whole formula would give unreliable results - with these codecs, the impact of loss of a particular packet on MOS differs depending on the informational value of that packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '16, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Aug '16, 00:47</p></div></div><div id="comments-container-55140" class="comments-container"></div><div id="comment-tools-55140" class="comment-tools"></div><div class="clear"></div><div id="comment-55140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

