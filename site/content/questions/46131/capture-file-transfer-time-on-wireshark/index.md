+++
type = "question"
title = "Capture file transfer time on Wireshark"
description = '''Hi all, As i am going to upload some files and ISO from my laptop to the Onedrive. I would like to know is it possible for Wireshark to measure the total amount of time from the beginning to the end of the file transfer. thanks.'''
date = "2015-09-24T20:50:00Z"
lastmod = "2015-09-24T22:52:00Z"
weight = 46131
keywords = [ "transfer", "drive", "file", "one" ]
aliases = [ "/questions/46131" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture file transfer time on Wireshark](/questions/46131/capture-file-transfer-time-on-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46131-score" class="post-score" title="current number of votes">0</div><span id="post-46131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>As i am going to upload some files and ISO from my laptop to the Onedrive. I would like to know is it possible for Wireshark to measure the total amount of time from the beginning to the end of the file transfer. thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-transfer" rel="tag" title="see questions tagged &#39;transfer&#39;">transfer</span> <span class="post-tag tag-link-drive" rel="tag" title="see questions tagged &#39;drive&#39;">drive</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span> <span class="post-tag tag-link-one" rel="tag" title="see questions tagged &#39;one&#39;">one</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '15, 20:50</strong></p><img src="https://secure.gravatar.com/avatar/d9ac7efa84eff8c04bb9b4e6d83347ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Daveli&#39;s gravatar image" /><p><span>Daveli</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Daveli has no accepted answers">0%</span></p></div></div><div id="comments-container-46131" class="comments-container"></div><div id="comment-tools-46131" class="comment-tools"></div><div class="clear"></div><div id="comment-46131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46132"></span>

<div id="answer-container-46132" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46132-score" class="post-score" title="current number of votes">1</div><span id="post-46132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can find the initial handshake and set a time reference on it: then just scroll to the last packet and see how much time has passed. If it is all done in one stream it will be very easy to see; if there is more than one stream involved you will have to make sure you scroll to the end of the last stream.</p><p>But to be honest, Stopwatches are just as good when measuring something like that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '15, 22:52</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p><span>DarrenWright</span><br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-46132" class="comments-container"></div><div id="comment-tools-46132" class="comment-tools"></div><div class="clear"></div><div id="comment-46132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

