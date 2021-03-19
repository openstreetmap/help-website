+++
type = "question"
title = "Client to Print Server trouble"
description = '''I have a remote LAN with multiple printers and some of these devices are taking a long time to spool and complete a print job (one in particular upwards of 10 minutes). I have taken captures from a Windows client on site to 4 different printers, but I can&#x27;t really see anything different in any of th...'''
date = "2013-08-21T09:56:00Z"
lastmod = "2013-08-21T11:23:00Z"
weight = 23915
keywords = [ "printer", "network" ]
aliases = [ "/questions/23915" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Client to Print Server trouble](/questions/23915/client-to-print-server-trouble)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23915-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a remote LAN with multiple printers and some of these devices are taking a long time to spool and complete a print job (one in particular upwards of 10 minutes). I have taken captures from a Windows client on site to 4 different printers, but I can't really see anything different in any of the 4 captures. Can someone advise what I should be looking for based on the symptoms?</p><p>Also, I've noticed that a few people use Cloudshark to upload captures to a central repository. Does anyone have any suggestions on a free repository or sharing solution?</p></div><div id="question-tags" class="tags-container tags">printer network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '13, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/bd6b5da2aa988528706fc3963beb5ccd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mkeith25&#39;s gravatar image" /><p>mkeith25<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mkeith25 has no accepted answers">0%</span></p></div></div><div id="comments-container-23915" class="comments-container"><span id="23916"></span><div id="comment-23916" class="comment"><div id="post-23916-score" class="comment-score"></div><div class="comment-text"><p>The special thing about Cloudshark is that it can interpret the capture file in the same manner as Wireshark so collaborators don't need to have their own copy of Wireshark.</p><p>For generally capture file sharing any shared file storage would do, e.g. Google Drive, SkyDrive, Dropbox etc.</p></div><div id="comment-23916-info" class="comment-info"><span class="comment-age">(21 Aug '13, 09:58)</span> grahamb ♦</div></div></div><div id="comment-tools-23915" class="comment-tools"></div><div class="clear"></div><div id="comment-23915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23917"></span>

<div id="answer-container-23917" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23917-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If it is just some printers in the same remote location, I'd start at comparing the syn_ack packets: tcp window size, window_scaling, offered mss option. Also, monitor the bytes_in_flight and see if this saturates the pipe.</p><p>Look at the delta_time between packets and see whether you wait for an ack, opening the window again.</p><p>tcp.analysis.flags should give you additional suspects ...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '13, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p>mrEEde2<br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div></div><div id="comments-container-23917" class="comments-container"></div><div id="comment-tools-23917" class="comment-tools"></div><div class="clear"></div><div id="comment-23917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

