+++
type = "question"
title = "use wireshark to restore VOIP streams"
description = '''hello, I use wireshatk to capture RTP streams and restore them. But the waveform is in yellow background and there is no waveform curve.After I click play button, there is no voice. My wireshark version is 1.6.4. Thank you.'''
date = "2012-05-06T19:09:00Z"
lastmod = "2012-05-07T01:37:00Z"
weight = 10709
keywords = [ "restore" ]
aliases = [ "/questions/10709" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [use wireshark to restore VOIP streams](/questions/10709/use-wireshark-to-restore-voip-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10709-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello, I use wireshatk to capture RTP streams and restore them. But the waveform is in yellow background and there is no waveform curve.After I click play button, there is no voice. My wireshark version is 1.6.4. Thank you.</p></div><div id="question-tags" class="tags-container tags">restore</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '12, 19:09</strong></p><img src="https://secure.gravatar.com/avatar/c1a70302d32293a16d65857eb888427b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qingbaibai&#39;s gravatar image" /><p>qingbaibai<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qingbaibai has no accepted answers">0%</span></p></div></div><div id="comments-container-10709" class="comments-container"></div><div id="comment-tools-10709" class="comment-tools"></div><div class="clear"></div><div id="comment-10709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10722"></span>

<div id="answer-container-10722" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10722-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Then the codec used is probably not supported. Only PCM A-law and PCM u-law are supported by default.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '12, 01:37</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-10722" class="comments-container"><span id="10780"></span><div id="comment-10780" class="comment"><div id="post-10780-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I changed the codec and it worked. The previous codec is GSM. However, there are some vertical yellow lines marked "w" in waveform.</p></div><div id="comment-10780-info" class="comment-info"><span class="comment-age">(08 May '12, 06:55)</span> qingbaibai</div></div></div><div id="comment-tools-10722" class="comment-tools"></div><div class="clear"></div><div id="comment-10722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

