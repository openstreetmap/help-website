+++
type = "question"
title = "Why do all mongodb query show as [Malformed Packet: MONGO]?"
description = '''When I update Wireshark from 1.8.2 to 1.10.0, all the mongodb query can be showed clearly in version 1.8.2 can not be shown correctly, all the mongo queries were showed as [Malformed Packet: MONGO](Both in ubuntu and windows). The mongodb reply also work as in both version 1.8.2 and 1.10.0. '''
date = "2013-07-22T10:12:00Z"
lastmod = "2013-07-22T11:49:00Z"
weight = 23241
keywords = [ "mongodb" ]
aliases = [ "/questions/23241" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why do all mongodb query show as \[Malformed Packet: MONGO\]?](/questions/23241/why-do-all-mongodb-query-show-as-malformed-packet-mongo)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23241-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I update Wireshark from 1.8.2 to 1.10.0, all the mongodb query can be showed clearly in version 1.8.2 can not be shown correctly, all the mongo queries were showed as [Malformed Packet: MONGO](Both in ubuntu and windows). The mongodb reply also work as in both version 1.8.2 and 1.10.0.</p></div><div id="question-tags" class="tags-container tags">mongodb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '13, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/c499400bca34a63928772bc6064d8d0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ricky&#39;s gravatar image" /><p>ricky<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ricky has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jul '13, 11:48</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-23241" class="comments-container"></div><div id="comment-tools-23241" class="comment-tools"></div><div class="clear"></div><div id="comment-23241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23247"></span>

<div id="answer-container-23247" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23247-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Probably a bug in the MongoDB dissector introduced in 1.10. File a bug at <a href="http://bugs.wireshark.org">the Wireshark bugzilla</a>; please attach a capture file showing the problem if you possibly can.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '13, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23247" class="comments-container"><span id="23258"></span><div id="comment-23258" class="comment"><div id="post-23258-score" class="comment-score"></div><div class="comment-text"><p>Seems to be a bug in 1.10.0. You can test it with the following file</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=mongodb.pcap">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=mongodb.pcap</a></p></blockquote></div><div id="comment-23258-info" class="comment-info"><span class="comment-age">(22 Jul '13, 14:51)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-23247" class="comment-tools"></div><div class="clear"></div><div id="comment-23247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

