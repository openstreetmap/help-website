+++
type = "question"
title = "no Remote interfaces tab"
description = '''Hi, I am using Wireshark 1.8.6 under Virtual machine with Win XP for remote capturing and there is no problems. But when I&#x27;ve tried to do this under host Debian (Wheezy) operating system with the Wireshark 1.8.2 there is no Remote Interfaces tab at all.'''
date = "2013-04-05T04:45:00Z"
lastmod = "2013-04-06T09:17:00Z"
weight = 20110
keywords = [ "interfaces", "remote", "tab" ]
aliases = [ "/questions/20110" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [no Remote interfaces tab](/questions/20110/no-remote-interfaces-tab)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20110-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am using Wireshark 1.8.6 under Virtual machine with Win XP for remote capturing and there is no problems. But when I've tried to do this under host Debian (Wheezy) operating system with the Wireshark 1.8.2 there is no Remote Interfaces tab at all.</p></div><div id="question-tags" class="tags-container tags">interfaces remote tab</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '13, 04:45</strong></p><img src="https://secure.gravatar.com/avatar/051dc3913f843de628623a41312561ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="furna&#39;s gravatar image" /><p>furna<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="furna has no accepted answers">0%</span></p></div></div><div id="comments-container-20110" class="comments-container"></div><div id="comment-tools-20110" class="comment-tools"></div><div class="clear"></div><div id="comment-20110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20121"></span>

<div id="answer-container-20121" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20121-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Remote capturing like this is a feature of WinPcap (which is what Wireshark uses to capture on Windows). libpcap (which Wireshark uses to capture on non-Windows systems) does not support remote capturing at the moment (AFAIK).</p><p>See also the <a href="http://wiki.wireshark.org/CaptureSetup/WinPcapRemote">CaptureSetup page for remote capturing</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '13, 12:39</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-20121" class="comments-container"></div><div id="comment-tools-20121" class="comment-tools"></div><div class="clear"></div><div id="comment-20121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20135"></span>

<div id="answer-container-20135" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20135-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need a libpcap version on Linux that supports remote capturing.</p><p>See the following bug</p><blockquote><p><code>https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2809</code><br />
</p></blockquote><p>and my answer to the following question:</p><blockquote><p><code>http://ask.wireshark.org/questions/16521/linux-remote-interface</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '13, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-20135" class="comments-container"></div><div id="comment-tools-20135" class="comment-tools"></div><div class="clear"></div><div id="comment-20135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

