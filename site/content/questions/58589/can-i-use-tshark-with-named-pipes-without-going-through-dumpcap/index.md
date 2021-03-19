+++
type = "question"
title = "can I use TShark with named pipes without going through dumpcap ?"
description = '''I&#x27;m sending traffic to TShark (packet by packet) through named pipe.  Dumpcap holds the data for up to 500ms, I want to get the result immediately.  Is there a way to send a packet to TShark without going through dumpcap ? '''
date = "2017-01-07T21:49:00Z"
lastmod = "2017-01-09T06:25:00Z"
weight = 58589
keywords = [ "tshark", "dumpcap" ]
aliases = [ "/questions/58589" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [can I use TShark with named pipes without going through dumpcap ?](/questions/58589/can-i-use-tshark-with-named-pipes-without-going-through-dumpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58589-score" class="post-score" title="current number of votes">0</div><span id="post-58589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm sending traffic to TShark (packet by packet) through named pipe. Dumpcap holds the data for up to 500ms, I want to get the result immediately. Is there a way to send a packet to TShark without going through dumpcap ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '17, 21:49</strong></p><img src="https://secure.gravatar.com/avatar/b50e05a5f1954d250dd908dacce081c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kdani&#39;s gravatar image" /><p><span>kdani</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kdani has no accepted answers">0%</span></p></div></div><div id="comments-container-58589" class="comments-container"></div><div id="comment-tools-58589" class="comment-tools"></div><div class="clear"></div><div id="comment-58589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58613"></span>

<div id="answer-container-58613" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58613-score" class="post-score" title="current number of votes">0</div><span id="post-58613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>According to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2874">bug 2874</a> if you run <code>tshark -i -</code> (to make tshark read from stdin) then dumpcap won't be spawned. If you can switch to using stdin rather than a named pipe then that should work for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '17, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-58613" class="comments-container"></div><div id="comment-tools-58613" class="comment-tools"></div><div class="clear"></div><div id="comment-58613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

