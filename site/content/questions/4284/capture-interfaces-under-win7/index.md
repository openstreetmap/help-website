+++
type = "question"
title = "Capture interfaces under Win7"
description = '''Hello,  I installed last few versions of wireshark/ethereal under Win7 profesional. I have problem with capturing. There are not possible capture packets from modem &quot;PPP&quot; or from modem Broadband like wifi adapter. I have only one adapter for capturing - LAN. I have Win XP too, but there are is possi...'''
date = "2011-05-30T02:49:00Z"
lastmod = "2011-05-31T00:10:00Z"
weight = 4284
keywords = [ "capture", "problem", "ppp", "modem" ]
aliases = [ "/questions/4284" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture interfaces under Win7](/questions/4284/capture-interfaces-under-win7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4284-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I installed last few versions of wireshark/ethereal under Win7 profesional. I have problem with capturing. There are not possible capture packets from modem "PPP" or from modem Broadband like wifi adapter. I have only one adapter for capturing - LAN.</p><p>I have Win XP too, but there are is possible capture both.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">capture problem ppp modem</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '11, 02:49</strong></p><img src="https://secure.gravatar.com/avatar/0f9ef4225f7a17ee9f8c7bb1329eb858?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stando&#39;s gravatar image" /><p>stando<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stando has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jun '11, 22:16</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-4284" class="comments-container"><span id="4289"></span><div id="comment-4289" class="comment"><div id="post-4289-score" class="comment-score"></div><div class="comment-text"><p>Which Version of Wireshark did you install ? Developer?<br />
Also, what do you mean by capturing? Do you wanna capture in monitor mode of WLAN? Regards, Amin</p></div><div id="comment-4289-info" class="comment-info"><span class="comment-age">(30 May '11, 07:25)</span> AminGho</div></div></div><div id="comment-tools-4284" class="comment-tools"></div><div class="clear"></div><div id="comment-4284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4293"></span>

<div id="answer-container-4293" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4293-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark uses WinPcap for traffic capture on Windows, just as it uses libpcap on UN*X. <a href="http://www.winpcap.org/misc/faq.htm#Q-5">Question Q-5 in the WinPcap FAQ</a> says that WinPcap supports PPP devices in Windows up to Windows XP, but doesn't support it in WIndows Vista or Windows 7. <a href="http://www.winpcap.org/misc/faq.htm#Q-16">Question Q-16</a> says that support for Wi-Fi devices is limited.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '11, 00:10</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></p></div></div><div id="comments-container-4293" class="comments-container"><span id="4466"></span><div id="comment-4466" class="comment"><div id="post-4466-score" class="comment-score"></div><div class="comment-text"><p>It is annoying :-(</p><p>Is there any other solution?</p></div><div id="comment-4466-info" class="comment-info"><span class="comment-age">(09 Jun '11, 00:46)</span> stando</div></div><span id="4475"></span><div id="comment-4475" class="comment"><div id="post-4475-score" class="comment-score"></div><div class="comment-text"><p>Use <a href="http://www.microsoft.com/downloads/en/details.aspx?familyid=983b941d-06cb-4658-b7f6-3088333d062f">Network Monitor</a>?</p></div><div id="comment-4475-info" class="comment-info"><span class="comment-age">(09 Jun '11, 12:56)</span> Guy Harris ♦♦</div></div><span id="4757"></span><div id="comment-4757" class="comment"><div id="post-4757-score" class="comment-score"></div><div class="comment-text"><p>NetMon can certainly be used for PPTP connections but I don't know about PPP devices.</p></div><div id="comment-4757-info" class="comment-info"><span class="comment-age">(26 Jun '11, 02:44)</span> grahamb ♦</div></div></div><div id="comment-tools-4293" class="comment-tools"></div><div class="clear"></div><div id="comment-4293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

