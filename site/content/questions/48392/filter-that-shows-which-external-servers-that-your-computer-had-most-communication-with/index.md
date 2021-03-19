+++
type = "question"
title = "filter that shows which external servers that your computer had most communication with."
description = '''im new with Wireshark and im trying too create a filter that shows me whitch external servers my computer had most communication with. Any clues?'''
date = "2015-12-09T14:03:00Z"
lastmod = "2015-12-09T15:51:00Z"
weight = 48392
keywords = [ "wireshark" ]
aliases = [ "/questions/48392" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [filter that shows which external servers that your computer had most communication with.](/questions/48392/filter-that-shows-which-external-servers-that-your-computer-had-most-communication-with)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48392-score" class="post-score" title="current number of votes">0</div><span id="post-48392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>im new with Wireshark and im trying too create a filter that shows me whitch external servers my computer had most communication with. Any clues?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '15, 14:03</strong></p><img src="https://secure.gravatar.com/avatar/464c35db7abc9a7a3ec7b163eac84d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marko&#39;s gravatar image" /><p><span>Marko</span><br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marko has no accepted answers">0%</span></p></div></div><div id="comments-container-48392" class="comments-container"></div><div id="comment-tools-48392" class="comment-tools"></div><div class="clear"></div><div id="comment-48392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48403"></span>

<div id="answer-container-48403" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48403-score" class="post-score" title="current number of votes">0</div><span id="post-48403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is ready-made there. Set your display filter to</p><pre><code> ip.addr == your.pc.ip.address</code></pre><p>and apply it, this should show you only packets which went from or to your computer. Next, choose Statistics -&gt; Conversations from menu, and when the window pops up, tick the box "limit to display filter". The column headers of the table are clickable, the rows are sorted increasing or decreasing by the value of the selected column. In your case, it would be "packets" or "bytes", either summary or in one direction.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '15, 15:51</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48403" class="comments-container"></div><div id="comment-tools-48403" class="comment-tools"></div><div class="clear"></div><div id="comment-48403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

