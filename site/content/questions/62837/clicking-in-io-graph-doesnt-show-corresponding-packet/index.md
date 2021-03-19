+++
type = "question"
title = "Clicking in I/O Graph doesn&#x27;t show corresponding packet"
description = '''Clicking in the I/O graph doesn&#x27;t show the corresponding packet in the packet details window. Am I doing something wrong? Version 2.2.7 (v2.2.7-0-g1861a96) '''
date = "2017-07-18T06:06:00Z"
lastmod = "2017-07-18T11:47:00Z"
weight = 62837
keywords = [ "#iograph" ]
aliases = [ "/questions/62837" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Clicking in I/O Graph doesn't show corresponding packet](/questions/62837/clicking-in-io-graph-doesnt-show-corresponding-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62837-score" class="post-score" title="current number of votes">0</div><span id="post-62837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Clicking in the I/O graph doesn't show the corresponding packet in the packet details window. Am I doing something wrong?</p><p>Version 2.2.7 (v2.2.7-0-g1861a96)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-#iograph" rel="tag" title="see questions tagged &#39;#iograph&#39;">#iograph</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '17, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/746f25240c5f0a3afd05a41fa4889bab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sampsont&#39;s gravatar image" /><p><span>sampsont</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sampsont has no accepted answers">0%</span></p></div></div><div id="comments-container-62837" class="comments-container"></div><div id="comment-tools-62837" class="comment-tools"></div><div class="clear"></div><div id="comment-62837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62838"></span>

<div id="answer-container-62838" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62838-score" class="post-score" title="current number of votes">0</div><span id="post-62838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Possibly you've encountered <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10922">Bug 10922</a>, <em>"wireshark QT could not jump to right time stamp in packet list pane upon clicking a point on IO graph if Time of day is selected."</em>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '17, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-62838" class="comments-container"></div><div id="comment-tools-62838" class="comment-tools"></div><div class="clear"></div><div id="comment-62838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62841"></span>

<div id="answer-container-62841" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62841-score" class="post-score" title="current number of votes">0</div><span id="post-62841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is the Packet List display going to the wrong packet, or is it not moving at all? If you're using a line graph, the graph line will be continuous, but in order for Wireshark to change its position in the Packet List, there has to actually be a packet at the point on the graph that you clicked on. It's possible there aren't very many packets in that part of the file, and you are not actually clicking on a point where there is a packet.</p><p>To see exactly where the packets are, you could temporarily switch to the dot, square, or diamond graph type.</p><p>It's also possible that you have encountered <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12401">Bug 12401</a>, which will be fixed in v2.4.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '17, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-62841" class="comments-container"><span id="62847"></span><div id="comment-62847" class="comment"><div id="post-62847-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your help!</p></div><div id="comment-62847-info" class="comment-info"><span class="comment-age">(18 Jul '17, 10:53)</span> <span class="comment-user userinfo">sampsont</span></div></div><span id="62850"></span><div id="comment-62850" class="comment"><div id="post-62850-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>I'm not sure which of us you were thanking, so I moved your comment under Jim's answer.</p><p>Lastly, if an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-62850-info" class="comment-info"><span class="comment-age">(18 Jul '17, 11:47)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-62841" class="comment-tools"></div><div class="clear"></div><div id="comment-62841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

