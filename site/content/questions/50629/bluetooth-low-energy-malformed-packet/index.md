+++
type = "question"
title = "Bluetooth Low Energy Malformed Packet"
description = '''I&#x27;ve correctly created a Bluetooth Low Energy advertising packet using the GAP Service Data type (0x16). Unfortunately, Wireshark is showing this as a Malformed Packet. If I switch the data type to some other type of format (say Manufacturing Specific), the dissector works fine. But when I select th...'''
date = "2016-03-01T11:16:00Z"
lastmod = "2016-09-07T00:54:00Z"
weight = 50629
keywords = [ "bug", "bluetooth" ]
aliases = [ "/questions/50629" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bluetooth Low Energy Malformed Packet](/questions/50629/bluetooth-low-energy-malformed-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50629-score" class="post-score" title="current number of votes">0</div><span id="post-50629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've correctly created a Bluetooth Low Energy advertising packet using the GAP Service Data type (0x16). Unfortunately, Wireshark is showing this as a Malformed Packet. If I switch the data type to some other type of format (say Manufacturing Specific), the dissector works fine. But when I select the Service Data type (BLE Supplement specification V6-2, page 19 - section 1.11 Service Data) it clearly states that the Service Data format (16 bit) contains two octets followed by additional service data.</p><p>From Additional debugging the problem of malformed packets seems to be that the dissector is requiring data to be in even octets - which is not a requirement of the specification. If I adjust the data enclosed within this field - wireshark does not produce a failure.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span> <span class="post-tag tag-link-bluetooth" rel="tag" title="see questions tagged &#39;bluetooth&#39;">bluetooth</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '16, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/11a5172904a4a3bda47b8effcf4e0be6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanielLSS&#39;s gravatar image" /><p><span>DanielLSS</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanielLSS has no accepted answers">0%</span></p></div></div><div id="comments-container-50629" class="comments-container"><span id="50631"></span><div id="comment-50631" class="comment"><div id="post-50631-score" class="comment-score"></div><div class="comment-text"><p>If you are sure it is a bug, <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi">Wireshark bugzilla</a> is the right place to report it, not a Q&amp;A site.</p></div><div id="comment-50631-info" class="comment-info"><span class="comment-age">(01 Mar '16, 12:20)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-50629" class="comment-tools"></div><div class="clear"></div><div id="comment-50629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55366"></span>

<div id="answer-container-55366" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55366-score" class="post-score" title="current number of votes">0</div><span id="post-55366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It seems to be fixed in: <a href="https://code.wireshark.org/review/6902">https://code.wireshark.org/review/6902</a> (before you request it :)) Try Wireshark 2.0 or the latest.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '16, 00:54</strong></p><img src="https://secure.gravatar.com/avatar/6eabf35b1168a8242bb2d69db18a8a7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micha%C5%82%20%C5%81ab%C4%99dzki&#39;s gravatar image" /><p><span>Michał Łabędzki</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michał Łabędzki has one accepted answer">8%</span></p></div></div><div id="comments-container-55366" class="comments-container"></div><div id="comment-tools-55366" class="comment-tools"></div><div class="clear"></div><div id="comment-55366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

