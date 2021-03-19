+++
type = "question"
title = "3GPP timezone decoding logic"
description = '''Hi Team, 3GPP-MS-TimeZone: 4a00 Timezone: GMT - 6 hours 0 minutes No adjustment Padding: 0000 please let me how hex value 4a was decoded as GMT-6.can you please share the logic of decoding that. dint find much info in 3gpp docs Best Regards Anand.R'''
date = "2013-11-05T11:22:00Z"
lastmod = "2014-05-27T20:19:00Z"
weight = 26682
keywords = [ "timezone" ]
aliases = [ "/questions/26682" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [3GPP timezone decoding logic](/questions/26682/3gpp-timezone-decoding-logic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26682-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Team,</p><p>3GPP-MS-TimeZone: 4a00 Timezone: GMT - 6 hours 0 minutes No adjustment Padding: 0000</p><p>please let me how hex value 4a was decoded as GMT-6.can you please share the logic of decoding that.</p><p>dint find much info in 3gpp docs</p><p>Best Regards Anand.R</p></div><div id="question-tags" class="tags-container tags">timezone</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '13, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/d78228e147cd39c8fd894a44aa8277bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AnandRoni&#39;s gravatar image" /><p>AnandRoni<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AnandRoni has no accepted answers">0%</span></p></div></div><div id="comments-container-26682" class="comments-container"></div><div id="comment-tools-26682" class="comment-tools"></div><div class="clear"></div><div id="comment-26682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26688"></span>

<div id="answer-container-26688" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26688-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>have a look at 3GPP TS 23.040 chapter 9.2.3.11.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '13, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-26688" class="comments-container"><span id="26691"></span><div id="comment-26691" class="comment"><div id="post-26691-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal, I already gone through 23.040 spec,i don't get it clear.</p><p>can you give a sample example how timezone parameter h'4A represents GMT -6.</p><p><strong>4</strong> A** 7654 3210 (bit order) 0100 1010 (3rd bit is zero so it is negative offset but how come we can determine as GMT-6 with remaining parameters)</p><p>Best Regards Anand.R</p></div><div id="comment-26691-info" class="comment-info"><span class="comment-age">(05 Nov '13, 19:26)</span> AnandRoni</div></div><span id="26692"></span><div id="comment-26692" class="comment"><div id="post-26692-score" class="comment-score"></div><div class="comment-text"><p>The timezone is expressed in multiple of 15 mns, as explained in the 3GPP spec. 0x4A &amp; 0x08 = 1 so it is a negative offset (0x4A)&gt;&gt;4 + 10<em>(0x4A&amp;0x7) = 4 + 10</em>2 = 24 units of 15 mns 24/4 = 6 hours</p></div><div id="comment-26692-info" class="comment-info"><span class="comment-age">(05 Nov '13, 23:14)</span> Pascal Quantin</div></div></div><div id="comment-tools-26688" class="comment-tools"></div><div class="clear"></div><div id="comment-26688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33123"></span>

<div id="answer-container-33123" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33123-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yeah it's in there (3GPP TS 23.040 under 9.2.3.11 TP-Service-Center-Time-Stamp (TP-SCTS) referenced by 3Gpp-TS-29.060 v8.9.0 7.7.52 MS Time Zone (and others). Looks strange because they are looking at the 1st byte as 2x 4-bit "semi-octets". So if you flip the 2x 4-bit octets, then take the high-order bit as the sign and the lower-order 7x bits as BCD digits it works fine:<br />
  4A = 0100 1010; swap = 1010 0100; sign = 1 (UTC-); 010 0100 (BCD) = 24(Dec) / 4 = UTC-6<br />
  8A = 1000 1010; swap = 1010 1000; sign = 1 (UTC-); 010 1000 (BCD) = 28(Dec) / 4 = UTC-7<br />
  69 = 0110 1001; swap = 1001 0110; sign = 1 (UTC-); 001 0110 (BCD) = 16(Dec) / 4 = UTC-4<br />
Wiki has some text on the BCD/Flipped nature of the whole timestamp field<br />
 <a href="http://en.wikipedia.org/wiki/GSM_03.40">http://en.wikipedia.org/wiki/GSM_03.40</a><br />
The wireshark 3GPP-MS-TimeZone fix has Pascal's algorithm in there too:<br />
 oct = (oct &gt;&gt; 4) + (oct &amp; 0x07) * 10;<br />
 <a href="https://bugs.wireshark.org/bugzilla/attachment.cgi?id=11503&amp;action=edit">https://bugs.wireshark.org/bugzilla/attachment.cgi?id=11503&amp;action=edit</a></p><p>Paul Bishop</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '14, 20:19</strong></p><img src="https://secure.gravatar.com/avatar/ab43aa0e9d11f6ff9c8b5796194b67a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Bishop&#39;s gravatar image" /><p>Paul Bishop<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Bishop has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-33123" class="comments-container"></div><div id="comment-tools-33123" class="comment-tools"></div><div class="clear"></div><div id="comment-33123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

