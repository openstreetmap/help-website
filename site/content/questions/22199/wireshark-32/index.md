+++
type = "question"
title = "Wireshark 32"
description = '''Hi,  I downloaded and installed Wireshark 32 bit for Windows XP. When I try to run the Wireshark application, I am receiving the error &quot;The procedure entry point DecodePointer could not be located in the dynamic link library KERNEL32.dll&quot;.  Thanks and Regards, Anamika'''
date = "2013-06-20T06:42:00Z"
lastmod = "2013-06-20T08:54:00Z"
weight = 22199
keywords = [ "kernel32.dll", "decodepointer", "windowsxp", "wireshark" ]
aliases = [ "/questions/22199" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark 32](/questions/22199/wireshark-32)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22199-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I downloaded and installed Wireshark 32 bit for Windows XP. When I try to run the Wireshark application, I am receiving the error "The procedure entry point DecodePointer could not be located in the dynamic link library KERNEL32.dll".</p><p>Thanks and Regards, Anamika</p></div><div id="question-tags" class="tags-container tags">kernel32.dll decodepointer windowsxp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '13, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/e86025b2a2ff3ab60829d4cff3be9aa4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anamika117&#39;s gravatar image" /><p>Anamika117<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anamika117 has no accepted answers">0%</span></p></div></div><div id="comments-container-22199" class="comments-container"></div><div id="comment-tools-22199" class="comment-tools"></div><div class="clear"></div><div id="comment-22199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22201"></span>

<div id="answer-container-22201" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22201-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://msdn.microsoft.com/en-us/library/bb432242%28v=vs.85%29.aspx">DecodePointer</a> is a Windows API call that is present in XP SP2 or later. I suspect that your copy of XP is earlier than this. To run Wireshark you will have to upgrade your OS.</p><p>As an aside, having such an old version of XP (2004 or earlier) will render your system extremely vulnerable to malware, even by just browsing the internet with the stock browser.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '13, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22201" class="comments-container"><span id="22203"></span><div id="comment-22203" class="comment"><div id="post-22203-score" class="comment-score"></div><div class="comment-text"><p>Hi Grahamb, I am using XP version 5.1 (Build 2600.xpsp1.0 with Service Pack 2). DecodePointer problem used to occur for SSCheduler.exe, I downloaded Service Pack2 and Installed again. I am not receiving error for SScheduler.exe, but I am not able to run Wireshark because of this error. i will try to upgrade the system.</p><p>Thanks and Regards, Anamika</p></div><div id="comment-22203-info" class="comment-info"><span class="comment-age">(20 Jun '13, 09:59)</span> Anamika117</div></div><span id="22302"></span><div id="comment-22302" class="comment"><div id="post-22302-score" class="comment-score"></div><div class="comment-text"><p>I have upgraded the system with Windows Service Pack 3 and the problem is solved. I am able to capture Packets. How do I capture packets for wireless connections?</p><p>Regards, Anamika</p></div><div id="comment-22302-info" class="comment-info"><span class="comment-age">(24 Jun '13, 23:16)</span> Anamika117</div></div><span id="22304"></span><div id="comment-22304" class="comment"><div id="post-22304-score" class="comment-score"></div><div class="comment-text"><blockquote><p>How do I capture packets for wireless connections?</p></blockquote><p>please open another question for this.</p></div><div id="comment-22304-info" class="comment-info"><span class="comment-age">(24 Jun '13, 23:58)</span> Kurt Knochner ♦</div></div><span id="22310"></span><div id="comment-22310" class="comment"><div id="post-22310-score" class="comment-score"></div><div class="comment-text"><p>@Anamika</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-22310-info" class="comment-info"><span class="comment-age">(25 Jun '13, 01:51)</span> grahamb ♦</div></div><span id="22312"></span><div id="comment-22312" class="comment"><div id="post-22312-score" class="comment-score"></div><div class="comment-text"><p>@grahamb Thanks.</p></div><div id="comment-22312-info" class="comment-info"><span class="comment-age">(25 Jun '13, 04:12)</span> Anamika117</div></div></div><div id="comment-tools-22201" class="comment-tools"></div><div class="clear"></div><div id="comment-22201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22200"></span>

<div id="answer-container-22200" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22200-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please see my answer to a similar question.</p><blockquote><p><a href="http://ask.wireshark.org/questions/20921/not-compatible-regardless-if-i-choose-32-or-64">http://ask.wireshark.org/questions/20921/not-compatible-regardless-if-i-choose-32-or-64</a></p></blockquote><p>I guess that some security software modified the Wireshark installer image.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '13, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22200" class="comments-container"></div><div id="comment-tools-22200" class="comment-tools"></div><div class="clear"></div><div id="comment-22200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

