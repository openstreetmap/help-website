+++
type = "question"
title = "Capture packet to SQL Database"
description = '''I&#x27;m using a serial to ethernet bridge (static IP) to connect a serial device to my network. I need a piece of software to grab the data from the ethernet bridge and store it in a SQL database (ideal) or a text file. The software needs to be able to run on a Win 2008 server when it is logged off. Can...'''
date = "2011-10-31T09:09:00Z"
lastmod = "2011-10-31T12:27:00Z"
weight = 7174
keywords = [ "ethernet", "serial", "sql", "bridge" ]
aliases = [ "/questions/7174" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture packet to SQL Database](/questions/7174/capture-packet-to-sql-database)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7174-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using a serial to ethernet bridge (static IP) to connect a serial device to my network. I need a piece of software to grab the data from the ethernet bridge and store it in a SQL database (ideal) or a text file. The software needs to be able to run on a Win 2008 server when it is logged off. Can Wireshark do this?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">ethernet serial sql bridge</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '11, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/cb0c25f241f9514782e740a6fab02b9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DeadCenter&#39;s gravatar image" /><p>DeadCenter<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DeadCenter has no accepted answers">0%</span></p></div></div><div id="comments-container-7174" class="comments-container"></div><div id="comment-tools-7174" class="comment-tools"></div><div class="clear"></div><div id="comment-7174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7177"></span>

<div id="answer-container-7177" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7177-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark and TShark can't save data to an SQL database, as it has no idea what the schema of the database is. If somebody wants that capability, it would help if they indicated what it means to "save data to an SQL database" - do they want particular fields extracted from the packet as columns in a table, do they want the raw packet data stored as a blob, or what?</p><p>Wireshark is a GUI application, so it would be inappropriate to save a text file. TShark might be able to do it, but it might not be able to save anything more than a hex dump of the raw Ethernet packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '11, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7177" class="comments-container"></div><div id="comment-tools-7177" class="comment-tools"></div><div class="clear"></div><div id="comment-7177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

