+++
type = "question"
title = "All Protocols Unknown"
description = '''When I run Wireshark (1.4.2) I never see any packets on my LAN, I just get packet after packet of unknown protocol where WTAP_ENCAP=1. I am connected to a Cisco 2950 Cat switch. I tried capturing via my WLAN connection and got the same result.  I have the latest version of WinPCAP. THoughts?'''
date = "2010-11-23T08:45:00Z"
lastmod = "2010-11-23T11:22:00Z"
weight = 1080
keywords = [ "unknown", "protocol" ]
aliases = [ "/questions/1080" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [All Protocols Unknown](/questions/1080/all-protocols-unknown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1080-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I run Wireshark (1.4.2) I never see any packets on my LAN, I just get packet after packet of unknown protocol where WTAP_ENCAP=1. I am connected to a Cisco 2950 Cat switch.</p><p>I tried capturing via my WLAN connection and got the same result.</p><p>I have the latest version of WinPCAP.</p><p>THoughts?</p></div><div id="question-tags" class="tags-container tags">unknown protocol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '10, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/8af3b78376ac7d5e8134e4af7d1c5bed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MIke65&#39;s gravatar image" /><p>MIke65<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MIke65 has no accepted answers">0%</span></p></div></div><div id="comments-container-1080" class="comments-container"></div><div id="comment-tools-1080" class="comment-tools"></div><div class="clear"></div><div id="comment-1080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1086"></span>

<div id="answer-container-1086" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1086-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at "Analyze =&gt; Enabled Protocols" and scroll down to "Ethernet", it is most probably unchecked, therefor Wireshark is not able to interpret packets with encapsulation type 1 (which corresponds to Ethernet).</p><p>Check "Ethernet" and click "OK" and you should be fine...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '10, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Feb '11, 07:36</p></div></div><div id="comments-container-1086" class="comments-container"><span id="53313"></span><div id="comment-53313" class="comment"><div id="post-53313-score" class="comment-score"></div><div class="comment-text"><p>I resolved the problem by following the above instructions.</p></div><div id="comment-53313-info" class="comment-info"><span class="comment-age">(08 Jun '16, 04:23)</span> Satya_Mokalla</div></div></div><div id="comment-tools-1086" class="comment-tools"></div><div class="clear"></div><div id="comment-1086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

