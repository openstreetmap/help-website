+++
type = "question"
title = "Write to file from Dissector"
description = '''I&#x27;m trying to print a specific data inside my Wireshark Custom Dissector to a file that I can upload to a different program. I tried opening and writing to a data using fopen and fprintf but Wireshark crashes when I upload my captured packet it crashes. Is there any way I can write a print-to-file f...'''
date = "2015-08-06T14:40:00Z"
lastmod = "2015-08-07T05:31:00Z"
weight = 44910
keywords = [ "print", "outwrite", "io.write", "export", "file" ]
aliases = [ "/questions/44910" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Write to file from Dissector](/questions/44910/write-to-file-from-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44910-score" class="post-score" title="current number of votes">0</div><span id="post-44910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to print a specific data inside my Wireshark Custom Dissector to a file that I can upload to a different program. I tried opening and writing to a data using <code>fopen</code> and <code>fprintf</code> but Wireshark crashes when I upload my captured packet it crashes. Is there any way I can write a print-to-file function inside a custom dissector?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-print" rel="tag" title="see questions tagged &#39;print&#39;">print</span> <span class="post-tag tag-link-outwrite" rel="tag" title="see questions tagged &#39;outwrite&#39;">outwrite</span> <span class="post-tag tag-link-io.write" rel="tag" title="see questions tagged &#39;io.write&#39;">io.write</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '15, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/66d32f7338820e81bed11c109bb8eaea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J1Ronnie&#39;s gravatar image" /><p><span>J1Ronnie</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J1Ronnie has no accepted answers">0%</span></p></div></div><div id="comments-container-44910" class="comments-container"></div><div id="comment-tools-44910" class="comment-tools"></div><div class="clear"></div><div id="comment-44910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44915"></span>

<div id="answer-container-44915" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44915-score" class="post-score" title="current number of votes">0</div><span id="post-44915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OS and Wireshark version?</p><p>There are platform independent file I/O routines in wsutil\file_util that might be handy.</p><p>Arguably though, writing to a file in a dissector is not a good idea, it will slow down dissection and live captures. Maybe it should be driven from a user generated action, e.g. a menu option.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '15, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44915" class="comments-container"><span id="44919"></span><div id="comment-44919" class="comment"><div id="post-44919-score" class="comment-score"></div><div class="comment-text"><p>Yes, look into using a tap for that.</p></div><div id="comment-44919-info" class="comment-info"><span class="comment-age">(07 Aug '15, 05:31)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-44915" class="comment-tools"></div><div class="clear"></div><div id="comment-44915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

