+++
type = "question"
title = "How to use capture on USB mobile phone modem on Windows"
description = '''Hi. I use EVO device for internet connectvity and it works on USB interface. I want to know if there is any method through which I can capture traffic on USB interface as the USB interfaces are not listed on the interface list. please help me on this.'''
date = "2011-04-18T02:05:00Z"
lastmod = "2011-04-20T02:00:00Z"
weight = 3551
keywords = [ "capture", "3g", "usb", "winpcap" ]
aliases = [ "/questions/3551" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to use capture on USB mobile phone modem on Windows](/questions/3551/how-to-use-capture-on-usb-mobile-phone-modem-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3551-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I use EVO device for internet connectvity and it works on USB interface. I want to know if there is any method through which I can capture traffic on USB interface as the USB interfaces are not listed on the interface list. please help me on this.</p></div><div id="question-tags" class="tags-container tags">capture 3g usb winpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '11, 02:05</strong></p><img src="https://secure.gravatar.com/avatar/2fc19f70da35585366cba09570809c89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="waseemsarwar103&#39;s gravatar image" /><p>waseemsarwar103<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="waseemsarwar103 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Aug '12, 20:18</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-3551" class="comments-container"><span id="3576"></span><div id="comment-3576" class="comment"><div id="post-3576-score" class="comment-score"></div><div class="comment-text"><p>So are you trying to capture low-level USB traffic, i.e. the USB protocol, or do you just want to capture network traffic to the device?</p><p>Is that device a wireless network adapter (Wi-Fi, mobile phone, etc.), and are you running on Windows? If so, it might not be supported by WinPcap.</p></div><div id="comment-3576-info" class="comment-info"><span class="comment-age">(18 Apr '11, 09:50)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-3551" class="comment-tools"></div><div class="clear"></div><div id="comment-3551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3631"></span>

<div id="answer-container-3631" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3631-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If your usb device is using a windows dialup adapter to connect try using winpcap 3.1 instead of the later versions. I use this to capture traffic from 3g and HSDPA usb modems (dongles).</p><p>Note wireshark will capture the data in the dial up connection not the signalling or air interface traffic...that gets expensive.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '11, 02:00</strong></p><img src="https://secure.gravatar.com/avatar/f2918caab20f5747d3263f63605b9934?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Doc&#39;s gravatar image" /><p>Doc<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Doc has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Aug '12, 06:59</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-3631" class="comments-container"><span id="13953"></span><div id="comment-13953" class="comment"><div id="post-13953-score" class="comment-score"></div><div class="comment-text"><p>Whoever Doc is....( 20 Apr 11, 2:00) you are a Blessing ...you just saved me a lot, thanks you...wincap 3.1 is doing quite fine .</p></div><div id="comment-13953-info" class="comment-info"><span class="comment-age">(29 Aug '12, 03:21)</span> gmirembe</div></div></div><div id="comment-tools-3631" class="comment-tools"></div><div class="clear"></div><div id="comment-3631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3563"></span>

<div id="answer-container-3563" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3563-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The ability to capture traffic over a USB interface depends largely on your OS. The following link should provide most of the relevant information to get you started: <a href="http://wiki.wireshark.org/CaptureSetup/USB">http://wiki.wireshark.org/CaptureSetup/USB</a>. You might also find some of the information available from <a href="http://ask.wireshark.org/questions/2801/usbmon-captures">this</a> question useful as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '11, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3563" class="comments-container"></div><div id="comment-tools-3563" class="comment-tools"></div><div class="clear"></div><div id="comment-3563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

