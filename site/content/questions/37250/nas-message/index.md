+++
type = "question"
title = "NAS message"
description = '''Hi Iam developing custom dissector where in one of the part i need to dissect NAS message (3G based) 3gpp spec.  Does wireshark support nas dissection? If yes how do i call the dissector and what parameters to pass. Thanks Raj'''
date = "2014-10-21T12:03:00Z"
lastmod = "2014-10-21T13:17:00Z"
weight = 37250
keywords = [ "nas", "message" ]
aliases = [ "/questions/37250" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [NAS message](/questions/37250/nas-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37250-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Iam developing custom dissector where in one of the part i need to dissect NAS message (3G based) 3gpp spec.</p><p>Does wireshark support nas dissection? If yes how do i call the dissector and what parameters to pass.</p><p>Thanks</p><p>Raj</p></div><div id="question-tags" class="tags-container tags">nas message</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '14, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p>umar<br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div></div><div id="comments-container-37250" class="comments-container"></div><div id="comment-tools-37250" class="comment-tools"></div><div class="clear"></div><div id="comment-37250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37256"></span>

<div id="answer-container-37256" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37256-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes it is supported. You just need to call the "gsm_a_dtap" dissector with a tvb containing the message payload.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '14, 13:17</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-37256" class="comments-container"><span id="37300"></span><div id="comment-37300" class="comment"><div id="post-37300-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal Quantin,</p><p>This Works for me :) Many Thanks!</p><p>Need to confirm, Instead of Header Name NAS Message : ------ it display as GSM A-I/F DTAP : --- ---</p><p>Iam looking for TS 24.008 version 4.3 Is there any other function i have to use instead of gsm_a_dtap??</p><p>Thanks!</p><p>Best Regards Raj</p></div><div id="comment-37300-info" class="comment-info"><span class="comment-age">(22 Oct '14, 22:52)</span> umar</div></div><span id="37306"></span><div id="comment-37306" class="comment"><div id="post-37306-score" class="comment-score">1</div><div class="comment-text"><p>If you look at the header of file packet-gsm_a_dtap.c you can see which specifications are covered, the info may not be up to date with the latest specs covered.</p></div><div id="comment-37306-info" class="comment-info"><span class="comment-age">(23 Oct '14, 04:01)</span> Anders ♦</div></div><span id="37307"></span><div id="comment-37307" class="comment"><div id="post-37307-score" class="comment-score">1</div><div class="comment-text"><p>It displays GSM A-IF DTAP because historically those dissectors were added for the corresponding network interface. As stated at the beginning of packet-gsm_a_dtap.c file:</p><p>Routines for GSM A Interface DTAP dissection - A.K.A. GSM layer 3</p><p>NOTE: it actually includes RR messages, which are (generally) not carried over the A interface on DTAP, but are part of the same Layer 3 protocol set</p></div><div id="comment-37307-info" class="comment-info"><span class="comment-age">(23 Oct '14, 04:16)</span> Pascal Quantin</div></div></div><div id="comment-tools-37256" class="comment-tools"></div><div class="clear"></div><div id="comment-37256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

