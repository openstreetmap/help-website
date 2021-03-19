+++
type = "question"
title = "LTE-RRC packets dissection"
description = '''Hello, Is it possible to dissect by wireshark LTE-RRC packets only according to captured IP packets (without USER_DLT)? What information should be in IP packets in order to dissect LTE-RRC messages? Now I able to dissect LTE-RRC packets only offline (reading from pcap file that contains USER_DLT) Th...'''
date = "2013-06-16T03:25:00Z"
lastmod = "2013-06-16T07:21:00Z"
weight = 22101
keywords = [ "eshabtai" ]
aliases = [ "/questions/22101" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LTE-RRC packets dissection](/questions/22101/lte-rrc-packets-dissection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22101-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Is it possible to dissect by wireshark LTE-RRC packets only according to captured IP packets (without USER_DLT)? What information should be in IP packets in order to dissect LTE-RRC messages?</p><p>Now I able to dissect LTE-RRC packets only offline (reading from pcap file that contains USER_DLT)</p><p>Thanks, Erez</p></div><div id="question-tags" class="tags-container tags">eshabtai</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '13, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/20e90dbf63e6c01c6de4196bd3c5dc3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eshabtai&#39;s gravatar image" /><p>eshabtai<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eshabtai has no accepted answers">0%</span></p></div></div><div id="comments-container-22101" class="comments-container"></div><div id="comment-tools-22101" class="comment-tools"></div><div class="clear"></div><div id="comment-22101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22105"></span>

<div id="answer-container-22105" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22105-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No you can't do that: IP is not a native transport layer for LTE RRC messages. Moreover you need to know on which logical channel type your message is being transmitted (BCCH DL SCH, UL/DL CCCH/DCCH, ...) so as to be able to decode it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '13, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-22105" class="comments-container"></div><div id="comment-tools-22105" class="comment-tools"></div><div class="clear"></div><div id="comment-22105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

