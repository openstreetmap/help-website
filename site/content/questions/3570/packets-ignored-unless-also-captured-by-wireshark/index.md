+++
type = "question"
title = "Packets ignored unless also captured by Wireshark"
description = '''Is it possible for Wireshark to alleviate some sort of network effect that prevented packets from being received? I installed Wireshark to investigate a problem with packets not being received by an application I am developing, only to discover that packets are all received correctly while Wireshark...'''
date = "2011-04-18T08:55:00Z"
lastmod = "2011-04-18T09:02:00Z"
weight = 3570
keywords = [ "rcv_ng_w-o_wireshark", "multicast" ]
aliases = [ "/questions/3570" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packets ignored unless also captured by Wireshark](/questions/3570/packets-ignored-unless-also-captured-by-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3570-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible for Wireshark to alleviate some sort of network effect that prevented packets from being received?</p><p>I installed Wireshark to investigate a problem with packets not being received by an application I am developing, only to discover that packets are all received correctly while Wireshark is capturing on that interface. If I stop capturing in Wireshark, the packets stop being received by my application.</p><p>If it helps, these are UDP packets sent to and received from a multicast address. In my current setup, my application is the only one broadcasting or listening to that address. I am running a Broadcom NetXtreme 57xx Gigabit Controller network adapter.</p><p>Anyone have any ideas?</p></div><div id="question-tags" class="tags-container tags">rcv_ng_w-o_wireshark multicast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '11, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/84553f236b5c55b007b6d4ae865de11e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steve&#39;s gravatar image" /><p>Steve<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steve has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Apr '11, 09:47</p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-3570" class="comments-container"></div><div id="comment-tools-3570" class="comment-tools"></div><div class="clear"></div><div id="comment-3570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3571"></span>

<div id="answer-container-3571" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3571-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like an issue wherein the interface hardware is not being set to accept frames addressed to the multicast address when you run your application.</p><p>When Wireshark runs it sets the NIC to "promiscous" so all frames are accepted.</p><p>I don't remember all the details about how this works, but ISTR it has something to do do with how the socket is opened.</p><p>[Update] A quick Google search finds the following: <a href="http://ntrg.cs.tcd.ie/undergrad/4ba2/multicast/antony/">IP Multicast tutorial</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '11, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Apr '11, 09:14</p></div></div><div id="comments-container-3571" class="comments-container"></div><div id="comment-tools-3571" class="comment-tools"></div><div class="clear"></div><div id="comment-3571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

