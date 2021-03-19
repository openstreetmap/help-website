+++
type = "question"
title = "Wireshark not capturing packets"
description = '''Hi to All. I have just installed WinPCap 4.1.2 &amp;amp; also Wireshark 1.6.5 but both my Wireshark &amp;amp; Windump are not capturing any packets. Is it bcoz I use broadband VPN wifi connection, or Windows 7 doesn’t support these?  Help pls. Many thanks.'''
date = "2012-02-21T04:38:00Z"
lastmod = "2012-02-21T14:13:00Z"
weight = 9160
keywords = [ "wireshark" ]
aliases = [ "/questions/9160" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not capturing packets](/questions/9160/wireshark-not-capturing-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9160-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi to All. I have just installed WinPCap 4.1.2 &amp; also Wireshark 1.6.5 but both my Wireshark &amp; Windump are not capturing any packets. Is it bcoz I use broadband VPN wifi connection, or Windows 7 doesn’t support these? Help pls. Many thanks.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '12, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/70a44410c357c8edb07e0403d0a86fa6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Warren&#39;s gravatar image" /><p>Warren<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Warren has no accepted answers">0%</span></p></div></div><div id="comments-container-9160" class="comments-container"></div><div id="comment-tools-9160" class="comment-tools"></div><div class="clear"></div><div id="comment-9160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9164"></span>

<div id="answer-container-9164" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9164-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The actual capturing mechanism on Windows, WinPCap, has issues with captures on WiFi interfaces. See the <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">WiFi Capture Setup</a> page on the Wiki for more info.</p><p>You might also try a newer version of Wireshark which will probably have a newer version of WinPCap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '12, 05:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Feb '12, 05:07</p></div></div><div id="comments-container-9164" class="comments-container"><span id="9166"></span><div id="comment-9166" class="comment"><div id="post-9166-score" class="comment-score"></div><div class="comment-text"><p>The Wireshark i'm using is 1.6.5, the very newest.How come?</p></div><div id="comment-9166-info" class="comment-info"><span class="comment-age">(21 Feb '12, 08:21)</span> Warren</div></div><span id="9167"></span><div id="comment-9167" class="comment"><div id="post-9167-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I misread your question, you have the latest WinPCap, so now the issue is down to your WiFI interface and it's drivers. I don't hold out much hope.</p><p>You could always try Network Monitor from Microsoft, any captures you manage to make can be saved and opened in Wireshark.</p></div><div id="comment-9167-info" class="comment-info"><span class="comment-age">(21 Feb '12, 08:46)</span> grahamb ♦</div></div></div><div id="comment-tools-9164" class="comment-tools"></div><div class="clear"></div><div id="comment-9164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9170"></span>

<div id="answer-container-9170" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9170-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>WinPcap <em>also</em> <a href="http://www.winpcap.org/misc/faq.htm#Q-5">has problems capturing on PPP interfaces</a>, <a href="http://www.winpcap.org/misc/faq.htm#Q-6">and that includes VPN interfaces</a>. NetMon may be able to capture on those as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '12, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9170" class="comments-container"></div><div id="comment-tools-9170" class="comment-tools"></div><div class="clear"></div><div id="comment-9170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

