+++
type = "question"
title = "Nb RTP multiplex packets stream analysis &quot;RTP Version!=2 not supported&quot;"
description = '''Hi All, Trying to save RTP multiplex packets payloads to raw file. Any clues if it can be done?'''
date = "2013-02-27T03:58:00Z"
lastmod = "2013-02-28T21:13:00Z"
weight = 18926
keywords = [ "stream", "rtp", "analysis", "multiplex" ]
aliases = [ "/questions/18926" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Nb RTP multiplex packets stream analysis "RTP Version!=2 not supported"](/questions/18926/nb-rtp-multiplex-packets-stream-analysis-rtp-version2-not-supported)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18926-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>Trying to save RTP multiplex packets payloads to raw file. Any clues if it can be done?</p></div><div id="question-tags" class="tags-container tags">stream rtp analysis multiplex</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '13, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/cd02174db2db63251b74f896865ad885?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dees123&#39;s gravatar image" /><p>Dees123<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dees123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Mar '13, 13:53</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-18926" class="comments-container"></div><div id="comment-tools-18926" class="comment-tools"></div><div class="clear"></div><div id="comment-18926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18927"></span>

<div id="answer-container-18927" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18927-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think so, because the compressed RTP headers cannot be handled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '13, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-18927" class="comments-container"><span id="18980"></span><div id="comment-18980" class="comment"><div id="post-18980-score" class="comment-score"></div><div class="comment-text"><p>Is there any intention to support so?</p></div><div id="comment-18980-info" class="comment-info"><span class="comment-age">(28 Feb '13, 07:53)</span> Dees123</div></div><span id="18982"></span><div id="comment-18982" class="comment"><div id="post-18982-score" class="comment-score"></div><div class="comment-text"><p>Probably not, patches are always welcome.</p></div><div id="comment-18982-info" class="comment-info"><span class="comment-age">(28 Feb '13, 08:14)</span> Anders ♦</div></div></div><div id="comment-tools-18927" class="comment-tools"></div><div class="clear"></div><div id="comment-18927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19009"></span>

<div id="answer-container-19009" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19009-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you mean RFC 5761, there's an enhancement request for it in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8355">8355</a>. They're waiting for a pcap capture example.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 21:13</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-19009" class="comments-container"><span id="19018"></span><div id="comment-19018" class="comment"><div id="post-19018-score" class="comment-score"></div><div class="comment-text"><p>Not covered under Bug 8355, I have few sample traces for RTP multiplex packets covered by 3GPP TS 29.414 Release 7, useful for implementation of RTP stream analysis.</p></div><div id="comment-19018-info" class="comment-info"><span class="comment-age">(01 Mar '13, 02:19)</span> Dees123</div></div><span id="19026"></span><div id="comment-19026" class="comment"><div id="post-19026-score" class="comment-score"></div><div class="comment-text"><p>@Hadriel: it's a bit confusing, but Dees123 is talking about 3GPP RTP Multiplex dissection, as defined in 3GPP TS 29.414. The bug you're referring to is about RTP and RTCP on the same UDP port.</p></div><div id="comment-19026-info" class="comment-info"><span class="comment-age">(01 Mar '13, 05:22)</span> Jaap ♦</div></div><span id="19065"></span><div id="comment-19065" class="comment"><div id="post-19065-score" class="comment-score"></div><div class="comment-text"><p>Oh, I mistook the characters "NB" in the title as some acronym used on this website, like "Need Badly" or something. Dees123 meant "Nb". Yuck, good luck with that. :)</p></div><div id="comment-19065-info" class="comment-info"><span class="comment-age">(01 Mar '13, 12:44)</span> Hadriel</div></div><span id="19072"></span><div id="comment-19072" class="comment"><div id="post-19072-score" class="comment-score"></div><div class="comment-text"><p>@Hadriel: FTFY</p></div><div id="comment-19072-info" class="comment-info"><span class="comment-age">(01 Mar '13, 13:54)</span> Jaap ♦</div></div></div><div id="comment-tools-19009" class="comment-tools"></div><div class="clear"></div><div id="comment-19009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

