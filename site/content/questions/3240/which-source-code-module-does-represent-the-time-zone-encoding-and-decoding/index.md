+++
type = "question"
title = "Which source code module does represent the Time Zone encoding and decoding?"
description = '''I would like to ask for your help to let me know which wireshark source code module define how to encode and decode Time Zone? Also the mechanism to encode and decode Time Zone is based on 3GPP TS 23.040 section 9.2.3.11 or not?'''
date = "2011-03-30T20:28:00Z"
lastmod = "2011-04-02T21:23:00Z"
weight = 3240
keywords = [ "timezone" ]
aliases = [ "/questions/3240" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Which source code module does represent the Time Zone encoding and decoding?](/questions/3240/which-source-code-module-does-represent-the-time-zone-encoding-and-decoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3240-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to ask for your help to let me know which wireshark source code module define how to encode and decode Time Zone? Also the mechanism to encode and decode Time Zone is based on 3GPP TS 23.040 section 9.2.3.11 or not?</p></div><div id="question-tags" class="tags-container tags">timezone</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '11, 20:28</strong></p><img src="https://secure.gravatar.com/avatar/1209ea150f48bb8ca26adc492333aa40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sripat&#39;s gravatar image" /><p>Sripat<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sripat has no accepted answers">0%</span></p></div></div><div id="comments-container-3240" class="comments-container"><span id="3286"></span><div id="comment-3286" class="comment"><div id="post-3286-score" class="comment-score"></div><div class="comment-text"><p>That question is to broad, Time Zone where? in SMS signaling then probably yes, in what message(s)? In other places it should use the method used in that protocol standard.</p></div><div id="comment-3286-info" class="comment-info"><span class="comment-age">(02 Apr '11, 00:58)</span> Anders ♦</div></div><span id="3287"></span><div id="comment-3287" class="comment"><div id="post-3287-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders, sorry maybe my question is too board. What I mean is the MS Time Zone field in the message "create PDP context request" sending from SGSN to GGSN which is indicated in 3GPP TS 29.060 section 7.7.52. I would like to know wireshark encoding/decoding this field according to 3GPP standard or not. Also I would like to know how it code?</p></div><div id="comment-3287-info" class="comment-info"><span class="comment-age">(02 Apr '11, 01:32)</span> Sripat</div></div></div><div id="comment-tools-3240" class="comment-tools"></div><div class="clear"></div><div id="comment-3240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3298"></span>

<div id="answer-container-3298" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3298-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ahhh, i think I found it. What I have asked here should be located in</p><p>"/epan/dissectors/packet-gsm_sms.c"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '11, 21:23</strong></p><img src="https://secure.gravatar.com/avatar/1209ea150f48bb8ca26adc492333aa40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sripat&#39;s gravatar image" /><p>Sripat<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sripat has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Apr '11, 21:26</p></div></div><div id="comments-container-3298" class="comments-container"></div><div id="comment-tools-3298" class="comment-tools"></div><div class="clear"></div><div id="comment-3298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

