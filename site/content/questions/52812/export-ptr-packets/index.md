+++
type = "question"
title = "Export PTR packets"
description = '''Good afternoon, all! I wonder if Wireshark can do what I want, or if I need to recap and run through another process. Essentially, I need Wireshark to take a packet capture, sort out all DNS and export the packets to a text file that I can use to dedupe and isolate which PTR records are being querie...'''
date = "2016-05-20T13:59:00Z"
lastmod = "2016-05-20T14:53:00Z"
weight = 52812
keywords = [ "ptr", "dns" ]
aliases = [ "/questions/52812" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export PTR packets](/questions/52812/export-ptr-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52812-score" class="post-score" title="current number of votes">0</div><span id="post-52812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good afternoon, all!</p><p>I wonder if Wireshark can do what I want, or if I need to recap and run through another process.</p><p>Essentially, I need Wireshark to take a packet capture, sort out all DNS and export the packets to a text file that I can use to dedupe and isolate which PTR records are being queried on.</p><p>Is this something Wireshark can do?</p><p>Thanks!</p><p>Gregg</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ptr" rel="tag" title="see questions tagged &#39;ptr&#39;">ptr</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '16, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/dafd5368df864f409c3c964d242b5ec3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gregg_hughes&#39;s gravatar image" /><p><span>gregg_hughes</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gregg_hughes has no accepted answers">0%</span></p></div></div><div id="comments-container-52812" class="comments-container"></div><div id="comment-tools-52812" class="comment-tools"></div><div class="clear"></div><div id="comment-52812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52813"></span>

<div id="answer-container-52813" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52813-score" class="post-score" title="current number of votes">0</div><span id="post-52813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark currently doesn't have a mechanism to do tasks of that sort, but you might be able to do it with TShark - use a "read filter" to select only DNS packets with PTR queries and responses, and then use the <code>-T fields</code> and <code>-e</code> flags to write out particular DNS protocol fields.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '16, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-52813" class="comments-container"></div><div id="comment-tools-52813" class="comment-tools"></div><div class="clear"></div><div id="comment-52813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

