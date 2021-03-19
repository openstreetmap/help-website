+++
type = "question"
title = "Relative Frame Number"
description = '''Like most people I imagine, I have a frame number column in my preferred view. I also frequently use the very handy tcp.stream filter to isolate a particular connection. I have noticed that when I do this, I often would like the frame number to be relative to the stream I am filtered on. But the fra...'''
date = "2016-06-02T06:23:00Z"
lastmod = "2016-06-02T13:07:00Z"
weight = 53139
keywords = [ "tcp.stream", "number" ]
aliases = [ "/questions/53139" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Relative Frame Number](/questions/53139/relative-frame-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53139-score" class="post-score" title="current number of votes">0</div><span id="post-53139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Like most people I imagine, I have a frame number column in my preferred view. I also frequently use the very handy tcp.stream filter to isolate a particular connection. I have noticed that when I do this, I often would like the frame number to be relative to the stream I am filtered on. But the frame number column seems to be "absolute", so there are gaps in the sequence of frame numbers if there is more than one stream in the trace file.</p><p>Is there a "relative frame number" column I'm just not aware of that I could add to my view so that packets in a given stream are numbered relative to the stream?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp.stream" rel="tag" title="see questions tagged &#39;tcp.stream&#39;">tcp.stream</span> <span class="post-tag tag-link-number" rel="tag" title="see questions tagged &#39;number&#39;">number</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '16, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/32272e9efae0156b7a71e9b634428d14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smp&#39;s gravatar image" /><p><span>smp</span><br />
<span class="score" title="39 reputation points">39</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jun '16, 06:24</strong> </span></p></div></div><div id="comments-container-53139" class="comments-container"></div><div id="comment-tools-53139" class="comment-tools"></div><div class="clear"></div><div id="comment-53139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53140"></span>

<div id="answer-container-53140" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53140-score" class="post-score" title="current number of votes">1</div><span id="post-53140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="smp has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think Wireshark keeps a relative frame number per TCP conversation as a field, so you can't display it in a column. You might want to add a feature request at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> for this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '16, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-53140" class="comments-container"><span id="53151"></span><div id="comment-53151" class="comment"><div id="post-53151-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the confirmation!</p></div><div id="comment-53151-info" class="comment-info"><span class="comment-age">(02 Jun '16, 11:07)</span> <span class="comment-user userinfo">smp</span></div></div><span id="53155"></span><div id="comment-53155" class="comment"><div id="post-53155-score" class="comment-score"></div><div class="comment-text"><p>For reference, here's the bug report URL:</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12491">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12491</a></p><p>As far as I can tell the next dev builds will already have that feature.</p></div><div id="comment-53155-info" class="comment-info"><span class="comment-age">(02 Jun '16, 13:07)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-53140" class="comment-tools"></div><div class="clear"></div><div id="comment-53140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

