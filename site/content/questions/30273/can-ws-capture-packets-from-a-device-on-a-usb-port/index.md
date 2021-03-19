+++
type = "question"
title = "Can WS capture packets from a device on a USB port?"
description = '''I&#x27;m trying to figure out how my firewall is blocking my BlackBerry Z10 phone, from mounting as a network drive on my laptop. Is it possible to sniff packaets between the BB device on a USB port and the internal firewall? I know it&#x27;s a firewall issue, as when I turn the firewall off the device works ...'''
date = "2014-02-28T07:53:00Z"
lastmod = "2014-03-02T08:59:00Z"
weight = 30273
keywords = [ "blackberry" ]
aliases = [ "/questions/30273" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can WS capture packets from a device on a USB port?](/questions/30273/can-ws-capture-packets-from-a-device-on-a-usb-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30273-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to figure out how my firewall is blocking my BlackBerry Z10 phone, from mounting as a network drive on my laptop. Is it possible to sniff packaets between the BB device on a USB port and the internal firewall?</p><p>I know it's a firewall issue, as when I turn the firewall off the device works normally. I've reviewed all the rules within the firewall and all the BlackBerry ones have full access without restrictions.</p></div><div id="question-tags" class="tags-container tags">blackberry</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '14, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/f44f712fb5482a0b90e69dec4b9d20f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kbouzan&#39;s gravatar image" /><p>kbouzan<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kbouzan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Feb '14, 08:28</p></div></div><div id="comments-container-30273" class="comments-container"><span id="30275"></span><div id="comment-30275" class="comment"><div id="post-30275-score" class="comment-score"></div><div class="comment-text"><p>What is your OS and OS version?</p></div><div id="comment-30275-info" class="comment-info"><span class="comment-age">(28 Feb '14, 08:33)</span> Kurt Knochner ♦</div></div><span id="30287"></span><div id="comment-30287" class="comment"><div id="post-30287-score" class="comment-score"></div><div class="comment-text"><p>I'm using Win 7 Enterprise.</p></div><div id="comment-30287-info" class="comment-info"><span class="comment-age">(28 Feb '14, 12:36)</span> kbouzan</div></div></div><div id="comment-tools-30273" class="comment-tools"></div><div class="clear"></div><div id="comment-30273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30326"></span>

<div id="answer-container-30326" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30326-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On Windows Wireshark cannot capture USB traffic directly. But there is a tool available that can do it for you: <a href="http://desowin.org/usbpcap/">USBpcap</a>.</p><p>See also:</p><p><a href="http://wiki.wireshark.org/CaptureSetup/USB#Windows">http://wiki.wireshark.org/CaptureSetup/USB#Windows</a></p><p>Wireshark will be able to read those files.</p><p><strong>HOWEVER:</strong> That (most certainly) won't help you with your firewall issue. In your case Wireshark is simply the wrong tool.</p><p>You could try to use <a href="http://technet.microsoft.com/en-us/library/jj649776.aspx">Microsoft Message Analyzer</a>, but I'm not sure if that will work!!</p><p>As you know it's a firewall problem, you should contact the vendor of the firewall and ask for help.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '14, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30326" class="comments-container"></div><div id="comment-tools-30326" class="comment-tools"></div><div class="clear"></div><div id="comment-30326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

