+++
type = "question"
title = "how to save wireshark session"
description = '''I need to keep my analysis information with pcap file. i.e. i have analyzed a .pcap log and added - Display filters, add marker, add coloum information etc. How to save the information with project, such that i can see those information when reopen the log file (.pcap)?'''
date = "2017-06-09T02:28:00Z"
lastmod = "2017-06-09T02:34:00Z"
weight = 61893
keywords = [ "session" ]
aliases = [ "/questions/61893" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [how to save wireshark session](/questions/61893/how-to-save-wireshark-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61893-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to keep my analysis information with pcap file. i.e. i have analyzed a .pcap log and added - Display filters, add marker, add coloum information etc.</p><p>How to save the information with project, such that i can see those information when reopen the log file (.pcap)?</p></div><div id="question-tags" class="tags-container tags">session</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '17, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/ca400298b8385318d9ac844a64e8a40e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sghorai&#39;s gravatar image" /><p>sghorai<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sghorai has one accepted answer">100%</span></p></div></div><div id="comments-container-61893" class="comments-container"></div><div id="comment-tools-61893" class="comment-tools"></div><div class="clear"></div><div id="comment-61893-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61895"></span>

<div id="answer-container-61895" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61895-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can save general and packet comments with the file if you save it in PCAPng format. The other things (filters, columns, etc) are profile settings, so you'd have to distribute them along with the pcapng file. You can find the settings files by opening the "About Wireshark" dialog and check the "folders" tab for the "Personal Configuration" path.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '17, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61895" class="comments-container"><span id="61904"></span><div id="comment-61904" class="comment"><div id="post-61904-score" class="comment-score"></div><div class="comment-text"><p>Thx Jasper, i see packet comments are saved with .PCAPng file. And is there anything else can be saved with this file format?</p></div><div id="comment-61904-info" class="comment-info"><span class="comment-age">(09 Jun '17, 06:09)</span> sghorai</div></div><span id="61910"></span><div id="comment-61910" class="comment"><div id="post-61910-score" class="comment-score"></div><div class="comment-text"><p>Yes, the interface statistics from the capture can be saved (you can see those in the Capture File Properties available in the Statistics menu), and name resolution entries from available FQDNs the time of the capture.</p></div><div id="comment-61910-info" class="comment-info"><span class="comment-age">(09 Jun '17, 08:06)</span> Jasper ♦♦</div></div></div><div id="comment-tools-61895" class="comment-tools"></div><div class="clear"></div><div id="comment-61895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

