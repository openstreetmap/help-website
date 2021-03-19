+++
type = "question"
title = "Is it OK that GSM SMS are reassembled even though they have different TP-Originating Adresses?"
description = '''i have two &quot;gsm_sms&quot; packets in ss7 network. these packets contain two parts of a multipart SMS. in user data heaher (UDH) of these packets i saw Message parts =2 ,and other properties of first packet is : message part number =1 , message idendifier =35 and TP-MMS FLAG shows: more message are waitin...'''
date = "2017-04-06T04:10:00Z"
lastmod = "2017-04-07T08:21:00Z"
weight = 60610
keywords = [ "gsm_sms" ]
aliases = [ "/questions/60610" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Is it OK that GSM SMS are reassembled even though they have different TP-Originating Adresses?](/questions/60610/is-it-ok-that-gsm-sms-are-reassembled-even-though-they-have-different-tp-originating-adresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60610-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i have two "gsm_sms" packets in ss7 network. these packets contain two parts of a multipart SMS. in user data heaher (UDH) of these packets i saw Message parts =2 ,and other properties of first packet is : message part number =1 , message idendifier =35 and TP-MMS FLAG shows: more message are waiting for MS in this SC. properties of second packet is : message part number =2 , message idendifier =35 and TP-MMS FLAG shows: No more message are waiting for MS in this SC. in the wireshark these packets are reassembled, however TP-Originating Address of these packets are different. is it ok?</p></div><div id="question-tags" class="tags-container tags">gsm_sms</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '17, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/28d5dc133c31193058a99892f00a0213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ghader&#39;s gravatar image" /><p>ghader<br />
<span class="score" title="61 reputation points">61</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ghader has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Apr '17, 06:02</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-60610" class="comments-container"></div><div id="comment-tools-60610" class="comment-tools"></div><div class="clear"></div><div id="comment-60610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60655"></span>

<div id="answer-container-60655" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60655-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>it is a bug of wireshark (packet-gsm_sms.c). according to gsm 03.40 packets that have same message identifier and same TP-Originating Adresses and same Service center should be reassembled. however in packet-gsm_sms.c packets that have same message identifier are reassembled.</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '17, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/0b6bdfea45d7093830a2a0638a758239?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hhw&#39;s gravatar image" /><p>hhw<br />
<span class="score" title="10 reputation points">10</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hhw has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>wikified 07 Apr '17, 08:32</p></div></div><div id="comments-container-60655" class="comments-container"></div><div id="comment-tools-60655" class="comment-tools"></div><div class="clear"></div><div id="comment-60655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

