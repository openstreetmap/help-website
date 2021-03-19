+++
type = "question"
title = "Can&#x27;t see any packets originating from my IP."
description = '''I have a Dell Lattitude E5530 with a Broadcom NetXtreme 57xx Gigibit NIC in it. This isn&#x27;t wireless. I just installed Wireshark 1.10.2, this is the first time Wireshark has ever been installed on this laptop. I didn&#x27;t add any filters, capture or display. When I run a capture on my NIC, I never see a...'''
date = "2013-10-02T09:42:00Z"
lastmod = "2013-10-04T00:22:00Z"
weight = 25538
keywords = [ "ip.src" ]
aliases = [ "/questions/25538" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't see any packets originating from my IP.](/questions/25538/cant-see-any-packets-originating-from-my-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25538-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Dell Lattitude E5530 with a Broadcom NetXtreme 57xx Gigibit NIC in it. This isn't wireless. I just installed Wireshark 1.10.2, this is the first time Wireshark has ever been installed on this laptop. I didn't add any filters, capture or display. When I run a capture on my NIC, I never see any traffic that originated from my IP addresss. I do not have IPv6 installed. I see traffic that originates else where and my IP is the destination. Does anyone have any idea what might be the issue here?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">ip.src</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '13, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/a1cad96ff6916721feadf06c68b8fcb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sjc1969&#39;s gravatar image" /><p>sjc1969<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sjc1969 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Oct '13, 09:44</p></div></div><div id="comments-container-25538" class="comments-container"><span id="25540"></span><div id="comment-25540" class="comment"><div id="post-25540-score" class="comment-score"></div><div class="comment-text"><p>What firewall\av products are installed on the machine?</p></div><div id="comment-25540-info" class="comment-info"><span class="comment-age">(02 Oct '13, 10:32)</span> grahamb ♦</div></div><span id="25541"></span><div id="comment-25541" class="comment"><div id="post-25541-score" class="comment-score"></div><div class="comment-text"><p>And VPN Software...</p></div><div id="comment-25541-info" class="comment-info"><span class="comment-age">(02 Oct '13, 10:42)</span> Kurt Knochner ♦</div></div><span id="25608"></span><div id="comment-25608" class="comment"><div id="post-25608-score" class="comment-score"></div><div class="comment-text"><p>I turned off the windows firewall. I have Vipre AV. I do have VPN software however it was not running and the VPN adapter was disabled during my captures. The strange thing is I have a desktop with the same AV and firewall configuration, no VPN obviously but I have zero issues with Wireshark v 1.8.5</p></div><div id="comment-25608-info" class="comment-info"><span class="comment-age">(03 Oct '13, 13:56)</span> sjc1969</div></div></div><div id="comment-tools-25538" class="comment-tools"></div><div class="clear"></div><div id="comment-25538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25624"></span>

<div id="answer-container-25624" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25624-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since the VPN software installs drivers in the networking stack, it can interfere with the workings of WinPcap, even when the VPN adapter is disabled (the drivers are still there). Can you try removing the VPN software?</p><p>I try to avoid running VPN client software on any system that I need to make captures with.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '13, 00:22</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25624" class="comments-container"></div><div id="comment-tools-25624" class="comment-tools"></div><div class="clear"></div><div id="comment-25624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

