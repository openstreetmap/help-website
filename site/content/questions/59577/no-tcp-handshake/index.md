+++
type = "question"
title = "No tcp handshake"
description = '''Hi, Client said they received &quot; 502 error &quot;. After compare with our wireshark capture we didnt received some client data. But they already transmit as attached screenshot from client. .  Why no tcp handshake ? What is PSH ACK How to know the root cause.  '''
date = "2017-02-20T23:24:00Z"
lastmod = "2017-02-21T07:03:00Z"
weight = 59577
keywords = [ "error" ]
aliases = [ "/questions/59577" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No tcp handshake](/questions/59577/no-tcp-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59577-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Client said they received " 502 error ". After compare with our wireshark capture we didnt received some client data. But they already transmit as attached screenshot from client. .</p><ol><li>Why no tcp handshake ?</li><li>What is PSH ACK</li><li>How to know the root cause. <img src="https://osqa-ask.wireshark.org/upfiles/Contoh_0LSK51D.jpg" alt="alt text" /></li></ol></div><div id="question-tags" class="tags-container tags">error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '17, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/b8cbaa9ee7d5bf40e4c8f703e3197880?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="suarez123&#39;s gravatar image" /><p>suarez123<br />
<span class="score" title="1 reputation points">1</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="suarez123 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 20 Feb '17, 23:29</p></div></div><div id="comments-container-59577" class="comments-container"></div><div id="comment-tools-59577" class="comment-tools"></div><div class="clear"></div><div id="comment-59577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59582"></span>

<div id="answer-container-59582" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59582-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>It happened before time range demonstrated on your screenshot.</li><li>A request for receiving endpoint to transfer data you've sent up the stack immediately without storing it in the buffer. Your first POST request is likely to have it too.</li><li>You've not received any packets in reply to your POST. Eventually client gave up with FIN. To answer exactly what's the root cause you have to consider network diagram and probably get server-side capture.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '17, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/1e22670f8d643ca08d658b80a6782932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet_vlad&#39;s gravatar image" /><p>Packet_vlad<br />
<span class="score" title="436 reputation points">436</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet_vlad has 5 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Feb '17, 07:12</p></div></div><div id="comments-container-59582" class="comments-container"></div><div id="comment-tools-59582" class="comment-tools"></div><div class="clear"></div><div id="comment-59582-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

