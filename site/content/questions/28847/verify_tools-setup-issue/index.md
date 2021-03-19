+++
type = "question"
title = "Verify_tools setup issue"
description = '''Hello I have followed the steps to hopefully build but I hit an issue when running  nmake -f Makefile.nmake verify_tools  The issue is ERROR: Can&#x27;t find &#x27;which&#x27;. Unable to proceed. NMAKE : fatal error U1077: &#x27;C:&#92;cygwin&#92;bin&#92;bash.EXE&#x27; : return code &#x27;0x1&#x27; Stop. However the which.exe is found in c:&#92;cygw...'''
date = "2014-01-13T12:29:00Z"
lastmod = "2014-06-02T14:23:00Z"
weight = 28847
keywords = [ "setup", "verify_tool", "cygwin" ]
aliases = [ "/questions/28847" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Verify\_tools setup issue](/questions/28847/verify_tools-setup-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28847-score" class="post-score" title="current number of votes">0</div><span id="post-28847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I have followed the steps to hopefully build but I hit an issue when running nmake -f Makefile.nmake verify_tools</p><p>The issue is ERROR: Can't find 'which'. Unable to proceed.</p><p>NMAKE : fatal error U1077: 'C:\cygwin\bin\bash.EXE' : return code '0x1' Stop.</p><p>However the which.exe is found in c:\cygwin\bin and can be called from the command line. Has this issue been seen before?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-verify_tool" rel="tag" title="see questions tagged &#39;verify_tool&#39;">verify_tool</span> <span class="post-tag tag-link-cygwin" rel="tag" title="see questions tagged &#39;cygwin&#39;">cygwin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '14, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/3c121d180682b1cf08dfb4e3e97eafcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="howardh&#39;s gravatar image" /><p><span>howardh</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="howardh has one accepted answer">100%</span></p></div></div><div id="comments-container-28847" class="comments-container"></div><div id="comment-tools-28847" class="comment-tools"></div><div class="clear"></div><div id="comment-28847-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28848"></span>

<div id="answer-container-28848" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28848-score" class="post-score" title="current number of votes">0</div><span id="post-28848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="howardh has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Figured out, stupid issue. I had another program of the "which" command inside one of my paths that took precedence over the cygwin version. It seems this other package just had naming issues with cygwin's own "which" functionality.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '14, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/3c121d180682b1cf08dfb4e3e97eafcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="howardh&#39;s gravatar image" /><p><span>howardh</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="howardh has one accepted answer">100%</span></p></div></div><div id="comments-container-28848" class="comments-container"><span id="33316"></span><div id="comment-33316" class="comment"><div id="post-33316-score" class="comment-score"></div><div class="comment-text"><p>please elaborate this a bit.. how did you solve it?</p></div><div id="comment-33316-info" class="comment-info"><span class="comment-age">(02 Jun '14, 13:25)</span> <span class="comment-user userinfo">aman</span></div></div><span id="33322"></span><div id="comment-33322" class="comment"><div id="post-33322-score" class="comment-score"></div><div class="comment-text"><p>The OP's PATH included a directory that preceded the cygwin bin directory and that directory had a "which.exe" that did not behave as the build environment intended.</p></div><div id="comment-33322-info" class="comment-info"><span class="comment-age">(02 Jun '14, 14:23)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-28848" class="comment-tools"></div><div class="clear"></div><div id="comment-28848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

