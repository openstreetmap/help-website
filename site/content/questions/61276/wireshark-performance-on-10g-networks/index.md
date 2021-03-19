+++
type = "question"
title = "wireshark performance on 10g networks"
description = '''hello. i need to monitor 10g network.is there a version of wireshark which supports 10g traffic speed? thank you'''
date = "2017-05-07T09:20:00Z"
lastmod = "2017-05-07T10:30:00Z"
weight = 61276
keywords = [ "10g", "network" ]
aliases = [ "/questions/61276" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark performance on 10g networks](/questions/61276/wireshark-performance-on-10g-networks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61276-score" class="post-score" title="current number of votes">0</div><span id="post-61276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello. i need to monitor 10g network.is there a version of wireshark which supports 10g traffic speed? thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-10g" rel="tag" title="see questions tagged &#39;10g&#39;">10g</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '17, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/353a2ff67b3cf198e82f93399b74f097?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dima&#39;s gravatar image" /><p><span>Dima</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dima has no accepted answers">0%</span></p></div></div><div id="comments-container-61276" class="comments-container"></div><div id="comment-tools-61276" class="comment-tools"></div><div class="clear"></div><div id="comment-61276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61277"></span>

<div id="answer-container-61277" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61277-score" class="post-score" title="current number of votes">2</div><span id="post-61277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's not a question if Wireshark supports 10G traffic. It's more a question if the capture hardware can keep up with 10G.</p><p>With a full saturated 10G link capturing direct with Wireshark is not the best way.</p><p>Using tools like dumpcap (potentially with BPF filter) make more sense.</p><p>Luca Deri gave a nice <a href="https://sharkfesteurope.wireshark.org/assets/presentations16eu/02.pdf">presentation</a> at Sharkfest last year about high-speed links. Maybe this helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '17, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 May '17, 12:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-61277" class="comments-container"></div><div id="comment-tools-61277" class="comment-tools"></div><div class="clear"></div><div id="comment-61277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

