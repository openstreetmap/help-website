+++
type = "question"
title = "Wireshark Doesn&#x27;t detect USB datacards."
description = '''Hi,  Wireshark Doesn&#x27;t detect USB datacards. Is there anyway to get this detected and run captures ?'''
date = "2012-07-16T21:03:00Z"
lastmod = "2016-08-05T00:42:00Z"
weight = 12791
keywords = [ "usb" ]
aliases = [ "/questions/12791" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Doesn't detect USB datacards.](/questions/12791/wireshark-doesnt-detect-usb-datacards)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12791-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Wireshark Doesn't detect USB datacards. Is there anyway to get this detected and run captures ?</p></div><div id="question-tags" class="tags-container tags">usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '12, 21:03</strong></p><img src="https://secure.gravatar.com/avatar/e4a20545b14c626af42edd6b76e42c6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raghu_capture&#39;s gravatar image" /><p>Raghu_capture<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raghu_capture has no accepted answers">0%</span></p></div></div><div id="comments-container-12791" class="comments-container"></div><div id="comment-tools-12791" class="comment-tools"></div><div class="clear"></div><div id="comment-12791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="12810"></span>

<div id="answer-container-12810" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12810-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If by "USB datacard" you mean a USB adapter that connects to a mobile phone network for data access, then:</p><ul><li>if this is on Windows, you may be seeing <a href="http://www.winpcap.org/misc/faq.htm#Q-5">this problem with WinPcap</a>;</li><li>if this is on some flavor of UN*X, such as Linux, there <em>should</em> be a PPP interface available on which to capture if you're connected to the network.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '12, 14:04</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-12810" class="comments-container"><span id="54594"></span><div id="comment-54594" class="comment"><div id="post-54594-score" class="comment-score"></div><div class="comment-text"><p>how would you solve this on osx?</p></div><div id="comment-54594-info" class="comment-info"><span class="comment-age">(04 Aug '16, 23:42)</span> theduduk</div></div><span id="54595"></span><div id="comment-54595" class="comment"><div id="post-54595-score" class="comment-score"></div><div class="comment-text"><p>OS X is a flavor of UN*X (in fact, starting with Leopard, it's a UNIX(R)). If you have some mobile phone network USB network adapter plugged into a machine running OS X, you'll probably have an interface named <code>ppp0</code> or something such as that, and you should be able to capture on that.</p><p>If, however, you want to capture traffic on the USB bus, that would be more difficult; Apple don't document any mechanism for doing that.</p></div><div id="comment-54595-info" class="comment-info"><span class="comment-age">(05 Aug '16, 00:41)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-12810" class="comment-tools"></div><div class="clear"></div><div id="comment-12810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23483"></span>

<div id="answer-container-23483" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23483-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On Windows, I think you could work around this problem by capturing data using USBPcap and writing "USB datacards" dissector. I don't have any of such device and hence cannot precisely estimate how much work would that be.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '13, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/96637248dab9a269e98fbf0344e26a93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="desowin&#39;s gravatar image" /><p>desowin<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="desowin has no accepted answers">0%</span></p></div></div><div id="comments-container-23483" class="comments-container"></div><div id="comment-tools-23483" class="comment-tools"></div><div class="clear"></div><div id="comment-23483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54596"></span>

<div id="answer-container-54596" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54596-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On Windows, you <em>might</em> be able to do that if you're running Windows Vista/7/8/8.1/10 and have <a href="https://nmap.org/npcap/">Npcap</a>, rather than WinPcap, installed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '16, 00:42</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-54596" class="comments-container"></div><div id="comment-tools-54596" class="comment-tools"></div><div class="clear"></div><div id="comment-54596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

