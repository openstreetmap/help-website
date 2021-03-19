+++
type = "question"
title = "3GPP Message Decoder by Vincent Helfre not working"
description = '''Hi,  I&#x27;ve installed the latest SW release (Decoder-0.7-Setup.exe) to read out user capabilities, but Wireshark path seems always wrong:  Could not find d:&#92;prog&#92;Wireshark&#92; wireshark.exe  - Install it from www.wireshark.org if not installed - if already installed, set the correct wireshark installatio...'''
date = "2012-03-29T03:06:00Z"
lastmod = "2012-03-29T13:12:00Z"
weight = 9833
keywords = [ "decoder", "asn1" ]
aliases = [ "/questions/9833" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [3GPP Message Decoder by Vincent Helfre not working](/questions/9833/3gpp-message-decoder-by-vincent-helfre-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9833-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've installed the latest SW release (Decoder-0.7-Setup.exe) to read out user capabilities, but Wireshark path seems always wrong:</p><blockquote><p>Could not find d:\prog\Wireshark\ wireshark.exe - Install it from <a href="http://www.wireshark.org">www.wireshark.org</a> if not installed - if already installed, set the correct wireshark installation path and restart 3GPP message decoder. Config file located in: d:\prog\Decoder\Preferences\<a href="http://ws_installation_dir.txt">ws_installation_dir.txt</a></p></blockquote><p>For sure the problem concerns installation paths or admin rights (although I'm currently useing D drive). I've already tried to edit the <a href="http://ws_installation_dir.txt">ws_installation_dir.txt</a> or to re-install both WS and Decoder, but unsuccessfully. Any hints?</p><p>Kr</p><p>most probably the problem depends on installation path (or similar)</p></div><div id="question-tags" class="tags-container tags">decoder asn1</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '12, 03:06</strong></p><img src="https://secure.gravatar.com/avatar/ba13b9636634ee6607902ed756982d72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wisdoms&#39;s gravatar image" /><p>wisdoms<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wisdoms has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Mar '12, 03:07</p></div></div><div id="comments-container-9833" class="comments-container"></div><div id="comment-tools-9833" class="comment-tools"></div><div class="clear"></div><div id="comment-9833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9834"></span>

<div id="answer-container-9834" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9834-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you need to contact the originator of the decoder about the issue. It's not something that Wireshark folks can do anything about.</p><p>Looking at the source I found <a href="http://code.google.com/p/phoneprotocoldecoder/source/browse/trunk/Decoder.cpp">HERE</a>, which is v 0.02, there seems to be some ugly fixed paths to the Wireshark executables, including defaulting the drive to that of the decoder executable. I see from your error message it's looking for Wireshark on the D: drive. Are you running the decoder on the D: driver with Wireshark installed on the C: drive?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '12, 03:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9834" class="comments-container"><span id="9835"></span><div id="comment-9835" class="comment"><div id="post-9835-score" class="comment-score"></div><div class="comment-text"><p>Hi grahamb,</p><p>I've tried both drives. No difference.</p></div><div id="comment-9835-info" class="comment-info"><span class="comment-age">(29 Mar '12, 03:52)</span> wisdoms</div></div><span id="9836"></span><div id="comment-9836" class="comment"><div id="post-9836-score" class="comment-score"></div><div class="comment-text"><p>I've converted your "answer" to a comment as that's how this site works. Please have a look at the <a href="http://ask.wireshark.org/faq/">FAQ</a>.</p><p>Do you have a link to the latest decoder? My Google fu is weak today.</p></div><div id="comment-9836-info" class="comment-info"><span class="comment-age">(29 Mar '12, 04:00)</span> grahamb ♦</div></div><span id="9849"></span><div id="comment-9849" class="comment"><div id="post-9849-score" class="comment-score"></div><div class="comment-text"><p>I found a link for v 0.7 <a href="http://3gppdecoder.free.fr/?q=node/1">HERE</a>. Unfortunately there is no source code so it's up to the author to support you. Sorry.</p></div><div id="comment-9849-info" class="comment-info"><span class="comment-age">(29 Mar '12, 13:44)</span> grahamb ♦</div></div></div><div id="comment-tools-9834" class="comment-tools"></div><div class="clear"></div><div id="comment-9834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9847"></span>

<div id="answer-container-9847" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9847-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, if you run Windows Vista or Windows 7, you need to turn off UAC (User Account Control in Control panel-&gt; User account)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '12, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/1c8a48406bf1113f2c852d62e6e97b18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="machin&#39;s gravatar image" /><p>machin<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="machin has no accepted answers">0%</span></p></div></div><div id="comments-container-9847" class="comments-container"></div><div id="comment-tools-9847" class="comment-tools"></div><div class="clear"></div><div id="comment-9847-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

