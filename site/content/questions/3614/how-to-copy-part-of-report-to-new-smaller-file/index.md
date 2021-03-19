+++
type = "question"
title = "How to copy part of report to new smaller file"
description = '''Hi My question is I don&#x27;t know how to copy part of report, to a new file. for example i have big wireshark file 400 Mega, and I need only 10 Mega in a new file ? Thanks  Benni'''
date = "2011-04-19T10:19:00Z"
lastmod = "2011-04-19T11:22:00Z"
weight = 3614
keywords = [ "copying" ]
aliases = [ "/questions/3614" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to copy part of report to new smaller file](/questions/3614/how-to-copy-part-of-report-to-new-smaller-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3614-score" class="post-score" title="current number of votes">0</div><span id="post-3614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi My question is I don't know how to copy part of report, to a new file. for example i have big wireshark file 400 Mega, and I need only 10 Mega in a new file ? Thanks Benni</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-copying" rel="tag" title="see questions tagged &#39;copying&#39;">copying</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '11, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/7025207868e357c0d53013c330eb05e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Benni&#39;s gravatar image" /><p><span>Benni</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Benni has no accepted answers">0%</span></p></div></div><div id="comments-container-3614" class="comments-container"><span id="3617"></span><div id="comment-3617" class="comment"><div id="post-3617-score" class="comment-score"></div><div class="comment-text"><p>I make a VOIP call, I want to isolate and copy only this conversation to a new file How do I do this Thanks</p></div><div id="comment-3617-info" class="comment-info"><span class="comment-age">(19 Apr '11, 11:22)</span> <span class="comment-user userinfo">Benni</span></div></div></div><div id="comment-tools-3614" class="comment-tools"></div><div class="clear"></div><div id="comment-3614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3615"></span>

<div id="answer-container-3615" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3615-score" class="post-score" title="current number of votes">0</div><span id="post-3615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can either filter on whatever you like, for example on the frame numbers, and save the partial file by using the "Displayed" radiobutton in the save dialog.</p><p>Or use the command line tool editcap (installed in the wireshark directory) to slice your file into smaller files, for example:</p><pre><code>editcap -c 7000 &lt;infile&gt; &lt;outfile&gt;</code></pre><p>You'll still have various file sizes depending on the size of the frames, but it should do.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '11, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3615" class="comments-container"></div><div id="comment-tools-3615" class="comment-tools"></div><div class="clear"></div><div id="comment-3615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

