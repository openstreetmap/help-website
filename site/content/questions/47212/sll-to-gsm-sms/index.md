+++
type = "question"
title = "SLL to GSM SMS"
description = '''Hi, I got a pcap with a SLL capture, I figure that&#x27;s a GSM SMS capture, but I m not totally sure. Anyways, I m trying to force wireshark to read it as a GSM SMS but I didn&#x27;t success. I need to reform the headers ? I mean to change the Frame / Linux cooked capture headers ? Moreover, the Linux cooked...'''
date = "2015-11-04T01:05:00Z"
lastmod = "2015-11-04T02:17:00Z"
weight = 47212
keywords = [ "sll", "gsm", "gsm_sms", "sms" ]
aliases = [ "/questions/47212" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SLL to GSM SMS](/questions/47212/sll-to-gsm-sms)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47212-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I got a pcap with a SLL capture, I figure that's a GSM SMS capture, but I m not totally sure. Anyways, I m trying to force wireshark to read it as a GSM SMS but I didn't success.</p><p>I need to reform the headers ? I mean to change the Frame / Linux cooked capture headers ? Moreover, the Linux cooked capture layer got an unknow protocol (0x00f5). Or can I just enforce a protocol about the wireshark reading ?</p></div><div id="question-tags" class="tags-container tags">sll gsm gsm_sms sms</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '15, 01:05</strong></p><img src="https://secure.gravatar.com/avatar/3f51a049eb7a400a53e07be237260bb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="V1shn0u&#39;s gravatar image" /><p>V1shn0u<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="V1shn0u has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Nov '15, 02:48</p></div></div><div id="comments-container-47212" class="comments-container"></div><div id="comment-tools-47212" class="comment-tools"></div><div class="clear"></div><div id="comment-47212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47220"></span>

<div id="answer-container-47220" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47220-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The unknown protocol refers to <em>Nokia Phonet frames</em>, according the the Linux kernel sources (<code>include/uapi/linux/if_ether.h</code>). Wireshark currently doesn't understand these frames.</p><p>You could file an <a href="https://bugs.wireshark.org">enhancement bug</a>, attaching this capture file, and if possible a reference to the Nokia Phonet Frame format, as found <code>include/uapi/linux/phonet.h</code>, so that it can be implemented.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '15, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-47220" class="comments-container"><span id="47223"></span><div id="comment-47223" class="comment"><div id="post-47223-score" class="comment-score"></div><div class="comment-text"><p>Do you know a software able to read theses frames ?</p><p>I will file an enhancement bug.</p></div><div id="comment-47223-info" class="comment-info"><span class="comment-age">(04 Nov '15, 03:10)</span> V1shn0u</div></div></div><div id="comment-tools-47220" class="comment-tools"></div><div class="clear"></div><div id="comment-47220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

