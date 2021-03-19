+++
type = "question"
title = "Crash in Mountain Lion"
description = '''I am trying to use Wireshark on a mac with 10.8.4. The first time I opened it, it said to make sure X11 was installed. X11 no longer comes with mac OS&#x27;s (as of the release of Mountain Lion) so I downloaded it from MacUpdate. Apparently, X11 can&#x27;t run on 10.8 at all. After a lot of googling, I found ...'''
date = "2013-07-12T09:39:00Z"
lastmod = "2013-07-15T14:50:00Z"
weight = 22922
keywords = [ "crash" ]
aliases = [ "/questions/22922" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Crash in Mountain Lion](/questions/22922/crash-in-mountain-lion)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22922-score" class="post-score" title="current number of votes">0</div><span id="post-22922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to use Wireshark on a mac with 10.8.4. The first time I opened it, it said to make sure X11 was installed. X11 no longer comes with mac OS's (as of the release of Mountain Lion) so I downloaded it from MacUpdate. Apparently, X11 can't run on 10.8 at all. After a lot of googling, I found that XQuartz was the new version of X11, but it doesn't seem to help. I don't know if the lack of X11 is the problem, but about 30 seconds after Wireshark opens, it crashes. No windows open and no categories on the menu bar appear before it crashes.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '13, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/017eb3c50e7a3397735cbbeb11f6a1fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="acc&#39;s gravatar image" /><p><span>acc</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="acc has no accepted answers">0%</span></p></div></div><div id="comments-container-22922" class="comments-container"><span id="22946"></span><div id="comment-22946" class="comment"><div id="post-22946-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response! After sifting through the error messages in console, I found that I had "Conduit" (spyware?) installed, and that was what was causing it. I deleted all traces of "Conduit" and now it works great!</p></div><div id="comment-22946-info" class="comment-info"><span class="comment-age">(14 Jul '13, 03:57)</span> <span class="comment-user userinfo">acc</span></div></div><span id="22979"></span><div id="comment-22979" class="comment"><div id="post-22979-score" class="comment-score"></div><div class="comment-text"><p>Acc, if my reply was a answer (resolution) to your questions please except it as an answer by checking it. Thanks, Edmond.</p></div><div id="comment-22979-info" class="comment-info"><span class="comment-age">(15 Jul '13, 14:50)</span> <span class="comment-user userinfo">Edmond</span></div></div></div><div id="comment-tools-22922" class="comment-tools"></div><div class="clear"></div><div id="comment-22922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22945"></span>

<div id="answer-container-22945" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22945-score" class="post-score" title="current number of votes">1</div><span id="post-22945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's working okay for me: OS X 10.8.4 (12E55) XQuartz 2.7.4 (xorg-server 1.13.0) Wireshark Version 1.10.0 (SVN Rev 49790 from /trunk-1.10).</p><p>Follow the steps on: <a href="http://support.apple.com/kb/ht5293">http://support.apple.com/kb/ht5293</a> For XQuartz and you should be fine.</p><p>BTW if you open it from terminal you can view the error it generates.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '13, 03:39</strong></p><img src="https://secure.gravatar.com/avatar/57dca282828fcb7b6086c0a77af93ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Edmond&#39;s gravatar image" /><p><span>Edmond</span><br />
<span class="score" title="181 reputation points">181</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Edmond has 2 accepted answers">33%</span></p></div></div><div id="comments-container-22945" class="comments-container"></div><div id="comment-tools-22945" class="comment-tools"></div><div class="clear"></div><div id="comment-22945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

