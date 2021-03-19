+++
type = "question"
title = "Retrieving an old SVN version snapshot"
description = '''I have done quite a bit of development on Wireshark a while ago (about a year and a half) and need to pick it up. I need to migrate changes to the latest Wireshark and I am sure it has changed considerably. What I would like to do is to be able to get hold of a SVN snapshot (47653 to be precise). Is...'''
date = "2014-04-17T11:31:00Z"
lastmod = "2014-04-17T11:47:00Z"
weight = 31936
keywords = [ "svn", "git", "checkout" ]
aliases = [ "/questions/31936" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Retrieving an old SVN version snapshot](/questions/31936/retrieving-an-old-svn-version-snapshot)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31936-score" class="post-score" title="current number of votes">0</div><span id="post-31936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have done quite a bit of development on Wireshark a while ago (about a year and a half) and need to pick it up. I need to migrate changes to the latest Wireshark and I am sure it has changed considerably. What I would like to do is to be able to get hold of a SVN snapshot (47653 to be precise). Is this possible using Git or am I now stuck?</p><p>Robert</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-svn" rel="tag" title="see questions tagged &#39;svn&#39;">svn</span> <span class="post-tag tag-link-git" rel="tag" title="see questions tagged &#39;git&#39;">git</span> <span class="post-tag tag-link-checkout" rel="tag" title="see questions tagged &#39;checkout&#39;">checkout</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '14, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/779f59be60430ef8c29aad3fab03338c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robertc808&#39;s gravatar image" /><p><span>robertc808</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robertc808 has no accepted answers">0%</span></p></div></div><div id="comments-container-31936" class="comments-container"></div><div id="comment-tools-31936" class="comment-tools"></div><div class="clear"></div><div id="comment-31936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31938"></span>

<div id="answer-container-31938" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31938-score" class="post-score" title="current number of votes">0</div><span id="post-31938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Each Git commit that was imported from SVN should contain revision information, e.g. "svn path=/trunk/; revision=47653". This means that you should be able to use <code>git log</code> to find a specific revision, then check out a branch based on that revision. For example, the following matches r47653 to commit 1019582c47cbf445f1079de6bddcfbcf654141f5, and creates a branch in my local repository named "svn-r47653" from that commit:</p><pre><code>git log -1 --grep revision=47653
git checkout -b svn-r47653 1019582c47</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '14, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Apr '14, 12:02</strong> </span></p></div></div><div id="comments-container-31938" class="comments-container"></div><div id="comment-tools-31938" class="comment-tools"></div><div class="clear"></div><div id="comment-31938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

