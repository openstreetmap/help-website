+++
type = "question"
title = "Wireshark filling up Mac Harddrive"
description = '''Hello, every time I run Wireshark (v.1.12.3), a good deal of space is taken up from my hard drive. I suspect it is a rogue temp file that isn&#x27;t being deleted. Does anyone know where Wireshark store its temp files? OS: Mac OSX 10.11.1 (El Capitan) thanks for the help!'''
date = "2015-11-25T06:49:00Z"
lastmod = "2015-11-25T06:57:00Z"
weight = 47970
keywords = [ "osx", "macosx", "drive", "full" ]
aliases = [ "/questions/47970" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark filling up Mac Harddrive](/questions/47970/wireshark-filling-up-mac-harddrive)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47970-score" class="post-score" title="current number of votes">0</div><span id="post-47970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, every time I run Wireshark (v.1.12.3), a good deal of space is taken up from my hard drive. I suspect it is a rogue temp file that isn't being deleted. Does anyone know where Wireshark store its temp files?</p><p>OS: Mac OSX 10.11.1 (El Capitan)</p><p>thanks for the help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span> <span class="post-tag tag-link-drive" rel="tag" title="see questions tagged &#39;drive&#39;">drive</span> <span class="post-tag tag-link-full" rel="tag" title="see questions tagged &#39;full&#39;">full</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '15, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/ca14147f42e6721ce2529b80d2ec5a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adrian549092&#39;s gravatar image" /><p><span>adrian549092</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adrian549092 has no accepted answers">0%</span></p></div></div><div id="comments-container-47970" class="comments-container"><span id="47971"></span><div id="comment-47971" class="comment"><div id="post-47971-score" class="comment-score"></div><div class="comment-text"><p>Also, forgot to mention, that the space is not freed up even after I close the application.</p></div><div id="comment-47971-info" class="comment-info"><span class="comment-age">(25 Nov '15, 06:52)</span> <span class="comment-user userinfo">adrian549092</span></div></div></div><div id="comment-tools-47970" class="comment-tools"></div><div class="clear"></div><div id="comment-47970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47972"></span>

<div id="answer-container-47972" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47972-score" class="post-score" title="current number of votes">0</div><span id="post-47972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you start a capture and open "Statistics" -&gt; "Capture File Properties" you should see the current file name including the path.</p><p>Normally, Wireshark should clean up it's temporary files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '15, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-47972" class="comments-container"></div><div id="comment-tools-47972" class="comment-tools"></div><div class="clear"></div><div id="comment-47972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

