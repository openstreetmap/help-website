+++
type = "question"
title = "How to capture 802.11ac packets with wireshark?"
description = '''Hi! I am new to wireshark and I am curently trying to figure out if there is any modification that needs to be done to the source code in order to capture and analyze 802.11ac packets. I found something on the internet about some VHT radiotaps that need to be added. Also, I suppose I need a capture ...'''
date = "2012-10-30T07:17:00Z"
lastmod = "2012-10-30T12:46:00Z"
weight = 15368
keywords = [ "802.11ac" ]
aliases = [ "/questions/15368" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture 802.11ac packets with wireshark?](/questions/15368/how-to-capture-80211ac-packets-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15368-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! I am new to wireshark and I am curently trying to figure out if there is any modification that needs to be done to the source code in order to capture and analyze 802.11ac packets. I found something on the internet about some VHT radiotaps that need to be added. Also, I suppose I need a capture card in order to be able to use wireshark on 802.11ac right? Thanks!</p></div><div id="question-tags" class="tags-container tags">802.11ac</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '12, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/ddea7d7490e52ea04f7f9de6142afc55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikidi&#39;s gravatar image" /><p>mikidi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikidi has no accepted answers">0%</span></p></div></div><div id="comments-container-15368" class="comments-container"></div><div id="comment-tools-15368" class="comment-tools"></div><div class="clear"></div><div id="comment-15368-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15395"></span>

<div id="answer-container-15395" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15395-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I found something on the internet about some VHT radiotaps that need to be added.</p></blockquote><p>Fortunately, radiotap was designed to be extensible in a fashion that allows programs unaware of new features to still handle the old stuff. If Wireshark doesn't know about <a href="http://www.radiotap.org/defined-fields/VHT">the new VHT fields</a>, it will still be able to handle 802.11ac packets, it just won't show the information in those fields, so, while it would be a Good Thing if Wireshark's radiotap dissector were to be enhanced to handle those fields, it's not an immediate requirement.</p><blockquote><p>Also, I suppose I need a capture card in order to be able to use wireshark on 802.11ac right?</p></blockquote><p>On Windows, yes, unless you only want to capture traffic to and from the host running Wireshark. On Linux/*BSD/OS X, you'd obviously need a network adapter that supports 802.11ac, but if you have a machine that already has such an adapter, that would be sufficient - you don't need a separate adapter for capturing (unless you want to remain associated to a wireless network while capturing in monitor mode and the driver and OS don't support that, but that's not an issue specific to ac).</p><p>Wireshark might have to be modified to handle any changes to the 802.11 frame format for 802.11ac, such as the new type and subtype values in the copy of Draft 10 that I have.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '12, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15395" class="comments-container"></div><div id="comment-tools-15395" class="comment-tools"></div><div class="clear"></div><div id="comment-15395-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

