+++
type = "question"
title = "maintaining a local Wireshark subversion branch"
description = '''I want to fork off a local copy of the latest stable Wireshark on my computer to do local development, but I want to do it in such a way that will make pulling in updates from the main Wireshark trunk as easy as possible in the future. I want to initially fork releases/wireshark-1.6.1/. After forkin...'''
date = "2011-08-30T12:10:00Z"
lastmod = "2011-09-03T17:53:00Z"
weight = 5966
keywords = [ "subversion", "version-control" ]
aliases = [ "/questions/5966" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [maintaining a local Wireshark subversion branch](/questions/5966/maintaining-a-local-wireshark-subversion-branch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5966-score" class="post-score" title="current number of votes">0</div><span id="post-5966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to fork off a local copy of the latest stable Wireshark on my computer to do local development, but I want to do it in such a way that will make pulling in updates from the main Wireshark trunk as easy as possible in the future. I want to initially fork releases/wireshark-1.6.1/. After forking, in the short term, I want to be able to pull in revisions from the trunk-1.6/ branch for bug fixes, and in the long term I want to be able to pull in revisions from the trunk/ branch (or from the trunk-1.8/ branch when it is created) to get new major releases and feature additions.</p><p>I looked at the trunk-1.6/ and trunk/ branches, but the svn logs for these two branches don't seem to share any recent revision numbers. Is there an easy way to initially fork the 1.6 stable branch and later stay updated with the bug fixes and major releases? If I have to pick between being able to pull in 1.6 bug fixes and being able to easily upgrade to new major releases, I would prefer to be able to easily upgrade to new major releases.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-subversion" rel="tag" title="see questions tagged &#39;subversion&#39;">subversion</span> <span class="post-tag tag-link-version-control" rel="tag" title="see questions tagged &#39;version-control&#39;">version-control</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '11, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/199e687252bd158fbbb998dd44604a61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="infiniteloop&#39;s gravatar image" /><p><span>infiniteloop</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="infiniteloop has no accepted answers">0%</span></p></div></div><div id="comments-container-5966" class="comments-container"></div><div id="comment-tools-5966" class="comment-tools"></div><div class="clear"></div><div id="comment-5966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="5994"></span>

<div id="answer-container-5994" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5994-score" class="post-score" title="current number of votes">1</div><span id="post-5994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="infiniteloop has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is how we do it at work:</p><ul><li>Checkout https://anonsvn.wireshark.org/wireshark/tags/wireshark-1.6.0.</li><li>Remove the .svn data</li><li><p>Import the data into your SVN vendor directory.</p></li><li><p>Merge the data from the SVN vendor directory into your SVN work directory.</p></li><li>Do your damage there :-)</li></ul><p>When the 1.6.1 is released:</p><ul><li>Checkout https://anonsvn.wireshark.org/wireshark/tags/wireshark-1.6.1.</li><li>Remove the .svn data</li><li>Copy the the SVN vendor directory.</li><li>Commit the changes</li><li>Merge the changes between the two vendor versions into your SVN work directory.</li></ul><p>Works like a charm :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '11, 04:53</strong></p><img src="https://secure.gravatar.com/avatar/4ef2d4c556ddce42ac6371c4ebd35312?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MavEtJu&#39;s gravatar image" /><p><span>MavEtJu</span><br />
<span class="score" title="71 reputation points">71</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MavEtJu has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Aug '11, 04:55</strong> </span></p></div></div><div id="comments-container-5994" class="comments-container"><span id="5995"></span><div id="comment-5995" class="comment"><div id="post-5995-score" class="comment-score"></div><div class="comment-text"><p>Removing the .svn directories can be accomplished using <code>svn export</code>.</p></div><div id="comment-5995-info" class="comment-info"><span class="comment-age">(31 Aug '11, 06:03)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="6067"></span><div id="comment-6067" class="comment"><div id="post-6067-score" class="comment-score"></div><div class="comment-text"><p>Thanks MavEtJu! Also, thanks grahamb for the clarification.</p></div><div id="comment-6067-info" class="comment-info"><span class="comment-age">(03 Sep '11, 17:44)</span> <span class="comment-user userinfo">infiniteloop</span></div></div></div><div id="comment-tools-5994" class="comment-tools"></div><div class="clear"></div><div id="comment-5994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5972"></span>

<div id="answer-container-5972" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5972-score" class="post-score" title="current number of votes">1</div><span id="post-5972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>TBH svn isn't great for maintaining local branches. You could run a working copy carrying your local changes as uncommitted changes updating as required from trunk but it would be cludgy.</p><p>You find life easier using a dvcs such as Mercurial or Git with their support for svn, eg. <a href="http://mercurial.selenic.com/wiki/WorkingWithSubversion">hgSubversion</a> or <a href="http://www.kernel.org/pub/software/scm/git/docs/git-svn.html">git-svn</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '11, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-5972" class="comments-container"></div><div id="comment-tools-5972" class="comment-tools"></div><div class="clear"></div><div id="comment-5972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5974"></span>

<div id="answer-container-5974" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5974-score" class="post-score" title="current number of votes">0</div><span id="post-5974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sure you can do that. Have a look <a href="http://www.wireshark.org/develop.html">here</a>. Instead of /trunk/ use /trunk-1.6/ for now. Once trunk-1.8 is created you can switch there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '11, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5974" class="comments-container"><span id="6068"></span><div id="comment-6068" class="comment"><div id="post-6068-score" class="comment-score"></div><div class="comment-text"><p>My question was more about how to <em>easily</em> do the procedure you just described, not whether or not it's possible. In other words, with enough work it's possible to construct any repository with any arbitrary history since SVN is capable of storing arbitrary data. In principle, I could hand craft the svn log one revision at a time by manually applying every change that's ever been made to Wireshark, so obviously it's possible. I was asking how do this easily because I'm not an expert on merging branches (or svn logs).</p></div><div id="comment-6068-info" class="comment-info"><span class="comment-age">(03 Sep '11, 17:53)</span> <span class="comment-user userinfo">infiniteloop</span></div></div></div><div id="comment-tools-5974" class="comment-tools"></div><div class="clear"></div><div id="comment-5974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

