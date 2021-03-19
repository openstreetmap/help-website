+++
type = "question"
title = "Unable to decode GSM_MAP protocol layer..showing upto SCCP"
description = '''we are not able to decode MAP protocol data. All protocols have been enabled, however when analyzing the packets, Wireshark disects and displays packet details/attributes till SCCP layer. Its showing as only data after SCCP. Please guide me to see decoded layers of GSM_MAP protocol. I have already c...'''
date = "2016-04-22T00:50:00Z"
lastmod = "2016-04-22T02:04:00Z"
weight = 51860
keywords = [ "gsm_map" ]
aliases = [ "/questions/51860" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to decode GSM\_MAP protocol layer..showing upto SCCP](/questions/51860/unable-to-decode-gsm_map-protocol-layershowing-upto-sccp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51860-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>we are not able to decode MAP protocol data. All protocols have been enabled, however when analyzing the packets, Wireshark disects and displays packet details/attributes till SCCP layer. Its showing as only data after SCCP. Please guide me to see decoded layers of GSM_MAP protocol.</p><p>I have already configured SSN value as 0-8 in GSM MAP.packet is showing as SSN not present:--</p><p>{.... ..0. = SubSystem Number Indicator: SSN not present (0x00)}</p><p>Please look into the frame number 5 of wireshark traces attached in the below link</p><p><a href="https://www.cloudshark.org/captures/4b0aad03eef6">https://www.cloudshark.org/captures/4b0aad03eef6</a></p></div><div id="question-tags" class="tags-container tags">gsm_map</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '16, 00:50</strong></p><img src="https://secure.gravatar.com/avatar/1a914334d082779984cff58f5b9ee7be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunilp&#39;s gravatar image" /><p>sunilp<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunilp has no accepted answers">0%</span></p></div></div><div id="comments-container-51860" class="comments-container"></div><div id="comment-tools-51860" class="comment-tools"></div><div class="clear"></div><div id="comment-51860-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51864"></span>

<div id="answer-container-51864" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51864-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Worst case you can still enforce the next protocol level by going to Edit -&gt; Preferences -&gt; Protocol -&gt; SCCP and in the "Default Payload" text box type tcap</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '16, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-51864" class="comments-container"><span id="51869"></span><div id="comment-51869" class="comment"><div id="post-51869-score" class="comment-score"></div><div class="comment-text"><p>Yeah, that's why that default payload preference is there: because normally Wireshark uses the SSN to find the upper layer protocol.</p><p>You could also use the Users Table preference to achieve this but it looks like you need to enter an SSN of 255 (for no SSN); also it looks like the "Called PC" parameter is actually the L3 DPC. But I wouldn't advise doing this right now; Wireshark has crashed a couple of times while I've been adjusting that table.</p></div><div id="comment-51869-info" class="comment-info"><span class="comment-age">(22 Apr '16, 06:45)</span> JeffMorriss ♦</div></div><span id="51884"></span><div id="comment-51884" class="comment"><div id="post-51884-score" class="comment-score"></div><div class="comment-text"><p>I opened <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12364">bug 12364</a> for the crash.</p></div><div id="comment-51884-info" class="comment-info"><span class="comment-age">(22 Apr '16, 13:09)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-51864" class="comment-tools"></div><div class="clear"></div><div id="comment-51864-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

