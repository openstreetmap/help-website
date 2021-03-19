+++
type = "question"
title = "SNMP Protocol on a different port than 161"
description = '''Wireshark automatically decode the packets if they are sent on port 161. Is there a way to configure Wireshark to do the decoding if packets are sent to a different port? I have a non responsive device that is supposedly using SNMP messages on port 300. I would love to have access to the decoded pay...'''
date = "2014-07-18T09:38:00Z"
lastmod = "2014-07-18T09:50:00Z"
weight = 34763
keywords = [ "snmp", "port", "161", "decoding" ]
aliases = [ "/questions/34763" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SNMP Protocol on a different port than 161](/questions/34763/snmp-protocol-on-a-different-port-than-161)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34763-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark automatically decode the packets if they are sent on port 161. Is there a way to configure Wireshark to do the decoding if packets are sent to a different port? I have a non responsive device that is supposedly using SNMP messages on port 300. I would love to have access to the decoded payload when I send my commands to port 300. TIA, Eddie</p></div><div id="question-tags" class="tags-container tags">snmp port 161 decoding</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '14, 09:38</strong></p><img src="https://secure.gravatar.com/avatar/427834b5160b260df4bc59a117d957f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eddie88&#39;s gravatar image" /><p>Eddie88<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eddie88 has no accepted answers">0%</span></p></div></div><div id="comments-container-34763" class="comments-container"></div><div id="comment-tools-34763" class="comment-tools"></div><div class="clear"></div><div id="comment-34763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34764"></span>

<div id="answer-container-34764" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34764-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Right click a packet, Choose "Decode As ..", select the transport tab and the appropriate port in the drop list (depends on whether you picked an snmp query or response) and then choose SNMP in the protocol list (you can select an entry in the list and type s and then n then m to get there easily). Click Close. Job done.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '14, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-34764" class="comments-container"><span id="34765"></span><div id="comment-34765" class="comment"><div id="post-34765-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that was really easy. Learned something new!</p><p>Cheers, Eddie</p></div><div id="comment-34765-info" class="comment-info"><span class="comment-age">(18 Jul '14, 09:55)</span> Eddie88</div></div><span id="34772"></span><div id="comment-34772" class="comment"><div id="post-34772-score" class="comment-score"></div><div class="comment-text"><p>Normally you accept a helpful answer by clicking the checkmark icon next to the answer rather than giving away your points. I've awarded yoiur points back to you. See the FAQ for more info.</p></div><div id="comment-34772-info" class="comment-info"><span class="comment-age">(18 Jul '14, 13:44)</span> grahamb ♦</div></div></div><div id="comment-tools-34764" class="comment-tools"></div><div class="clear"></div><div id="comment-34764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

