+++
type = "question"
title = "create OPCUA columns"
description = '''Hi folks! Is it possible to create columns (eg the No. Time Source and so on) with OPC UA informations? Display Name, Namespace Index, NodeID, Datatype, Value? I tried to help myself but unfortunatly I was not successfull in creating a new column.'''
date = "2016-08-03T07:03:00Z"
lastmod = "2016-08-03T07:34:00Z"
weight = 54555
keywords = [ "nodeid", "opcua" ]
aliases = [ "/questions/54555" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [create OPCUA columns](/questions/54555/create-opcua-columns)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54555-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks!</p><p>Is it possible to create columns (eg the No. Time Source and so on) with OPC UA informations? Display Name, Namespace Index, NodeID, Datatype, Value?</p><p>I tried to help myself but unfortunatly I was not successfull in creating a new column.</p></div><div id="question-tags" class="tags-container tags">nodeid opcua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '16, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/35c1280c10135bd7a9b0245b5abebaf2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eva02&#39;s gravatar image" /><p>eva02<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eva02 has no accepted answers">0%</span></p></div></div><div id="comments-container-54555" class="comments-container"><span id="54557"></span><div id="comment-54557" class="comment"><div id="post-54557-score" class="comment-score"></div><div class="comment-text"><p>Normally any protocol field which can be dissected can also be made a column in the packet list - in the dissection pane, right-click that field and choose <code>Apply as Column</code> from the context menu. Does this not work for OPCUA fields?</p></div><div id="comment-54557-info" class="comment-info"><span class="comment-age">(03 Aug '16, 07:28)</span> sindy</div></div></div><div id="comment-tools-54555" class="comment-tools"></div><div class="clear"></div><div id="comment-54555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54558"></span>

<div id="answer-container-54558" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54558-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>In Wireshark there are two primary ways to add a column:</p><ol><li><code>Edit -&gt; Preferences -&gt; Columns -&gt; Add -&gt; Field type: Custom, Field name: &lt;field&gt;, Click on default Title name of "New Column" and rename it to something more meaningful, and finally, click on the Field type at the bottom of the list of columns and drag the newly added column to the desired location</code>. Here, <code>&lt;field&gt;</code> is the Wireshark <a href="https://wireshark.org/docs/dfref/o/opcua.html">opcua filter name</a> you're interested in.</li><li>If you already have a capture file containing the field of interest, find a packet containing that field and then right-click on it and choose, "Apply as Column". Drag the column to its desired location.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '16, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54558" class="comments-container"><span id="54564"></span><div id="comment-54564" class="comment"><div id="post-54564-score" class="comment-score"></div><div class="comment-text"><p>awesome! Thats great, Thank you very much!</p></div><div id="comment-54564-info" class="comment-info"><span class="comment-age">(03 Aug '16, 22:24)</span> eva02</div></div></div><div id="comment-tools-54558" class="comment-tools"></div><div class="clear"></div><div id="comment-54558-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

