+++
type = "question"
title = "no packets visible, Verizon VZAccess wireless broadband"
description = '''I&#x27;m new, probably asking a dumb question, and expecting an obvious answer. I run on an HP laptop, Windows Vista, with a Verizon broadband internet connection and I can see no packet traffic. My WireShark interface list: Microsoft .... MS Tunnel Interface Driver ,,, Realtek RTL8102 PCI-E Fast Etherne...'''
date = "2012-05-13T16:11:00Z"
lastmod = "2012-05-13T17:55:00Z"
weight = 10965
keywords = [ "broadband", "packets", "verizon" ]
aliases = [ "/questions/10965" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [no packets visible, Verizon VZAccess wireless broadband](/questions/10965/no-packets-visible-verizon-vzaccess-wireless-broadband)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10965-score" class="post-score" title="current number of votes">0</div><span id="post-10965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new, probably asking a dumb question, and expecting an obvious answer.</p><p>I run on an HP laptop, Windows Vista, with a Verizon broadband internet connection and I can see no packet traffic.</p><p>My WireShark interface list:</p><pre><code>Microsoft  ....
MS Tunnel Interface Driver ,,,
Realtek RTL8102 PCI-E Fast Ethernet NIC ...</code></pre><p>None of these show any packet traffic. I've tried with promiscuous mode on and off.</p><p>None of the IP addresses match my VZAccess Manager IP address (Mobile Broadband (EV-RevA)) which is hooked up to a USB port.</p><p>Can I make WireShark work on my system?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broadband" rel="tag" title="see questions tagged &#39;broadband&#39;">broadband</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-verizon" rel="tag" title="see questions tagged &#39;verizon&#39;">verizon</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '12, 16:11</strong></p><img src="https://secure.gravatar.com/avatar/9d8f97eea6072fdd9a02bb8ad61f74c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oldreddog&#39;s gravatar image" /><p><span>oldreddog</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oldreddog has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 May '12, 18:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-10965" class="comments-container"></div><div id="comment-tools-10965" class="comment-tools"></div><div class="clear"></div><div id="comment-10965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10966"></span>

<div id="answer-container-10966" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10966-score" class="post-score" title="current number of votes">1</div><span id="post-10966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>AFAIK trying to capture traffic on the VZAccess connection with Wireshark won't work on Vista/Windows7.</p><p>I believe the default VZAccess mode acts like PPP and the alternative VZAccess NDIS mode is NDIS6, neither of which can be handled by WinPcap (the actual capture driver used by Wireshark) on these systems.</p><p>However, I believe that Microsoft Network Monitor can be used to do a capture (using VZAccess NDIS mode ?). (You can use Wireshark to view the netmon capture).</p><p>See: <a href="http://www.winpcap.org/misc/faq.htm#Q-5">Can I use WinPcap on a PPP connection?</a></p><p>See: <a href="http://www.mail-archive.com/winpcap-users@winpcap.org/msg00328.html">"packet Filtering in WinPcap"</a></p><p>See: <a href="http://www.wireshark.org/lists/wireshark-users/200911/msg00005.html">Sniffing Wireless with Wireshark?</a> (for info about Microsoft netmon)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '12, 17:55</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 May '12, 18:01</strong> </span></p></div></div><div id="comments-container-10966" class="comments-container"></div><div id="comment-tools-10966" class="comment-tools"></div><div class="clear"></div><div id="comment-10966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

