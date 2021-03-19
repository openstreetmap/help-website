+++
type = "question"
title = "How can I capture 3g usb modem packets?"
description = '''Hi, I want to capture packets from a 3g usb modem via wireshark. Currently I am unable to view the usb modem in the Interface list. Is there any way or workaround by which I can let wireshark identify the usb modem and capture packets from it. Thanks'''
date = "2010-11-25T14:46:00Z"
lastmod = "2010-11-26T23:18:00Z"
weight = 1128
keywords = [ "modem", "3g", "usb" ]
aliases = [ "/questions/1128" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I capture 3g usb modem packets?](/questions/1128/how-can-i-capture-3g-usb-modem-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1128-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I want to capture packets from a 3g usb modem via wireshark. Currently I am unable to view the usb modem in the Interface list. Is there any way or workaround by which I can let wireshark identify the usb modem and capture packets from it. Thanks</p></div><div id="question-tags" class="tags-container tags">modem 3g usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '10, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/909580001d1d8b578da18ce92ba5ad39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mayank1love&#39;s gravatar image" /><p>mayank1love<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mayank1love has no accepted answers">0%</span></p></div></div><div id="comments-container-1128" class="comments-container"></div><div id="comment-tools-1128" class="comment-tools"></div><div class="clear"></div><div id="comment-1128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1133"></span>

<div id="answer-container-1133" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1133-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If this is on Windows, unfortunately, capturing on PPP-based interfaces such as dial-up interfaces - and mobile phone modem interfaces, which, I think, look like dial-up interfaces on Windows - is only supported by WinPcap, and thus only supported by Wireshark, on Windows 2000 and 32-bit versions of Windows XP and Windows Server 2003, as per <a href="http://www.winpcap.org/misc/faq.htm#Q-5">the WinPcap FAQ question Q-5</a>. It is not, for example, supported on WIndows Vista or WIndows 7.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '10, 23:18</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-1133" class="comments-container"><span id="40066"></span><div id="comment-40066" class="comment"><div id="post-40066-score" class="comment-score"></div><div class="comment-text"><p>when will you provide this USB network interface monitoring in Win8/8.1/10 etc....</p></div><div id="comment-40066-info" class="comment-info"><span class="comment-age">(25 Feb '15, 02:58)</span> gks</div></div><span id="40068"></span><div id="comment-40068" class="comment"><div id="post-40068-score" class="comment-score"></div><div class="comment-text"><p>This needs to be asked to the WinPcap folks, which a separate project that not affiliated to Wireshark. In the meantime, you can capture the traffic at USB level by using USBPcap: <a href="http://desowin.org/usbpcap/">http://desowin.org/usbpcap/</a></p></div><div id="comment-40068-info" class="comment-info"><span class="comment-age">(25 Feb '15, 04:41)</span> Pascal Quantin</div></div></div><div id="comment-tools-1133" class="comment-tools"></div><div class="clear"></div><div id="comment-1133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

