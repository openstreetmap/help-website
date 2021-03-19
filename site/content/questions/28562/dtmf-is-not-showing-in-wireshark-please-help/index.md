+++
type = "question"
title = "DTMF is not showing in wireshark Please help."
description = '''Hi, I have configured CCT with our MSC. But while calling to IVR phone DTMF is not showing in wireshark. How to resolve this issue ? please help.'''
date = "2014-01-03T21:34:00Z"
lastmod = "2014-01-04T14:21:00Z"
weight = 28562
keywords = [ "dtmf" ]
aliases = [ "/questions/28562" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DTMF is not showing in wireshark Please help.](/questions/28562/dtmf-is-not-showing-in-wireshark-please-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28562-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have configured CCT with our MSC. But while calling to IVR phone DTMF is not showing in wireshark. How to resolve this issue ? please help.</p></div><div id="question-tags" class="tags-container tags">dtmf</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '14, 21:34</strong></p><img src="https://secure.gravatar.com/avatar/3a3d345ee04c1bc12be449e4f189bffa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AMITAG&#39;s gravatar image" /><p>AMITAG<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AMITAG has no accepted answers">0%</span></p></div></div><div id="comments-container-28562" class="comments-container"><span id="28568"></span><div id="comment-28568" class="comment"><div id="post-28568-score" class="comment-score"></div><div class="comment-text"><p>This question reminds me of <a href="http://goo.gl/McfFDX">this</a> clip from "Good Morning, Vietnam".</p></div><div id="comment-28568-info" class="comment-info"><span class="comment-age">(04 Jan '14, 07:35)</span> cmaynard ♦♦</div></div><span id="28570"></span><div id="comment-28570" class="comment"><div id="post-28570-score" class="comment-score"></div><div class="comment-text"><p>why ??? Is that song related with DTMF ??</p></div><div id="comment-28570-info" class="comment-info"><span class="comment-age">(04 Jan '14, 10:00)</span> AMITAG</div></div><span id="28578"></span><div id="comment-28578" class="comment"><div id="post-28578-score" class="comment-score"></div><div class="comment-text"><p>The abreviations CCT MSC and IVR are perhaps not known to all :-)</p><p>DTMF can be sent in the RTP packets or out of band or as RTP Events I beleve. What are you expecting to see? and where is your trace Point? what equipment is supposed to send the DTMF?</p></div><div id="comment-28578-info" class="comment-info"><span class="comment-age">(04 Jan '14, 15:45)</span> Anders ♦</div></div></div><div id="comment-tools-28562" class="comment-tools"></div><div class="clear"></div><div id="comment-28562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28577"></span>

<div id="answer-container-28577" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28577-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>Can you share the packet capture? the DTMF could be either inband and in this case it would be just represent as audio (RTP).</p><p>one out-band option could be as part of the SIP and you will be able to find it by using this display filter sip.Method == INFO</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '14, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/94630d1ea1108afeafb344e884044d15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Boaz%20Galil&#39;s gravatar image" /><p>Boaz Galil<br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Boaz Galil has no accepted answers">0%</span></p></div></div><div id="comments-container-28577" class="comments-container"></div><div id="comment-tools-28577" class="comment-tools"></div><div class="clear"></div><div id="comment-28577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

