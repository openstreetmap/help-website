+++
type = "question"
title = "Get the Packet List, Packets Details and Packet byte in TShark using single Command"
description = '''Hi How can I get the above 3 mentioned details using a single Command tshark -i 1 gives the Packet List tshark -V -S &quot;EndofFile&quot; -x gives Packets Details and Packets Byte. But how can I write a single line query to get all the 3 details in single Command'''
date = "2014-11-13T02:05:00Z"
lastmod = "2014-11-13T02:44:00Z"
weight = 37809
keywords = [ "packets", "tshark" ]
aliases = [ "/questions/37809" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get the Packet List, Packets Details and Packet byte in TShark using single Command](/questions/37809/get-the-packet-list-packets-details-and-packet-byte-in-tshark-using-single-command)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37809-score" class="post-score" title="current number of votes">0</div><span id="post-37809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi How can I get the above 3 mentioned details using a single Command</p><p><code>tshark -i 1</code></p><p>gives the Packet List</p><p><code>tshark -V -S "EndofFile" -x</code></p><p>gives Packets Details and Packets Byte.</p><p>But how can I write a single line query to get all the 3 details in single Command</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '14, 02:05</strong></p><img src="https://secure.gravatar.com/avatar/d1fba3d75c7af8dc47876eede9fb1191?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erarijit&#39;s gravatar image" /><p><span>erarijit</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erarijit has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Nov '14, 02:23</strong> </span></p></div></div><div id="comments-container-37809" class="comments-container"></div><div id="comment-tools-37809" class="comment-tools"></div><div class="clear"></div><div id="comment-37809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37812"></span>

<div id="answer-container-37812" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37812-score" class="post-score" title="current number of votes">1</div><span id="post-37812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="erarijit has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Add <code>-P</code> to get the packet list (called packet summary in tshark help output).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '14, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37812" class="comments-container"></div><div id="comment-tools-37812" class="comment-tools"></div><div class="clear"></div><div id="comment-37812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

