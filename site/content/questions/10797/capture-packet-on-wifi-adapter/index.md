+++
type = "question"
title = "Capture packet on wifi adapter"
description = '''Hello everybody I need some help how i can capture packet form the wifi adapter (TP-Link). Its interface is not displayed in the list where to start capturing in wireshark. Thanks in advance.'''
date = "2012-05-08T21:46:00Z"
lastmod = "2012-05-09T00:46:00Z"
weight = 10797
keywords = [ "adapter", "wifi", "wireshark" ]
aliases = [ "/questions/10797" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture packet on wifi adapter](/questions/10797/capture-packet-on-wifi-adapter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10797-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody I need some help how i can capture packet form the wifi adapter (TP-Link). Its interface is not displayed in the list where to start capturing in wireshark.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">adapter wifi wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '12, 21:46</strong></p><img src="https://secure.gravatar.com/avatar/94e6ea6baf338a1b647a6e3d60bd121e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aamir%20screen&#39;s gravatar image" /><p>aamir screen<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aamir screen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 May '12, 02:10</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-10797" class="comments-container"></div><div id="comment-tools-10797" class="comment-tools"></div><div class="clear"></div><div id="comment-10797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10811"></span>

<div id="answer-container-10811" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10811-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I asume it's a usb adapter (due to TP-Link). If that's the case, you might have problems sniffing on that adapter, as winpcap (i asume it's windows), might not porperly support it.</p><p>See also here:</p><p><strong>Wireless adapters</strong><br />
<a href="http://www.winpcap.org/misc/faq.htm#Q-16">http://www.winpcap.org/misc/faq.htm#Q-16</a></p><p>BTW: What's the output of 'dumcap -D -M'? Can you identify the adapter based on it's IP address even if it's not named "TP-Link something". Winpcap returns Wifi adapters often just as "Microsoft".</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '12, 00:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 May '12, 00:54</p></div></div><div id="comments-container-10811" class="comments-container"></div><div id="comment-tools-10811" class="comment-tools"></div><div class="clear"></div><div id="comment-10811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

