+++
type = "question"
title = "wireshark dissector timestamp feild"
description = '''I&#x27;m writing a wireshark dissector for a log dump. I have a 8 byte time stamp field in the PDU. Is it possible to display this time stamp value in the time column in wireshark. Also, this packet is not encapsulated by any other protocol. Thanks in Advance!'''
date = "2011-06-24T12:18:00Z"
lastmod = "2011-06-24T17:15:00Z"
weight = 4737
keywords = [ "timestamp", "dissector" ]
aliases = [ "/questions/4737" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark dissector timestamp feild](/questions/4737/wireshark-dissector-timestamp-feild)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4737-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a wireshark dissector for a log dump. I have a 8 byte time stamp field in the PDU. Is it possible to display this time stamp value in the time column in wireshark. Also, this packet is not encapsulated by any other protocol.</p><p>Thanks in Advance!</p></div><div id="question-tags" class="tags-container tags">timestamp dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '11, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/25b19db92f6c5c1102813db491e41432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tut087&#39;s gravatar image" /><p>tut087<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tut087 has no accepted answers">0%</span></p></div></div><div id="comments-container-4737" class="comments-container"></div><div id="comment-tools-4737" class="comment-tools"></div><div class="clear"></div><div id="comment-4737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4748"></span>

<div id="answer-container-4748" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4748-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can create a custom column that contains your timestamp field (and optionally hide the Time column if it's confusing to show both columns):</p><ol><li>Go to <strong>Edit &gt; Preferences &gt; User Interface &gt; Columns</strong></li><li>Click <strong>Add</strong></li><li>A new column is added to the column list. Rename it (e.g., to "Timestamp").</li><li>For <strong>Field type</strong>, pick <strong>Custom</strong></li><li>For <strong>Field name</strong>, enter the name of your timestamp field (defined at field registration).</li><li><em>OPTIONAL:</em> To hide the Time column, select it from the list and click <strong>Remove</strong> (you can add it back later).</li><li>Click <strong>OK</strong></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '11, 17:15</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jun '11, 17:16</p></div></div><div id="comments-container-4748" class="comments-container"><span id="4767"></span><div id="comment-4767" class="comment"><div id="post-4767-score" class="comment-score"></div><div class="comment-text"><p>Thanks. What function could I use to populate this new coloumn?</p></div><div id="comment-4767-info" class="comment-info"><span class="comment-age">(27 Jun '11, 07:47)</span> tut087</div></div><span id="4771"></span><div id="comment-4771" class="comment"><div id="post-4771-score" class="comment-score"></div><div class="comment-text"><p>If using the steps above, you don't need to use a function. Wireshark fills in the column for you automatically: each packet is evaluated for your timestamp field and its value is put in the Timestamp column.</p></div><div id="comment-4771-info" class="comment-info"><span class="comment-age">(27 Jun '11, 10:57)</span> helloworld</div></div></div><div id="comment-tools-4748" class="comment-tools"></div><div class="clear"></div><div id="comment-4748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

