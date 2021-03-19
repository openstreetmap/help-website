+++
type = "question"
title = "Windows build fails with return code &#x27;0xc0000135&#x27;"
description = '''I&#x27;m trying to build wireshark 1.8.3 release from source to build a plugin that isn&#x27;t distributed with it. I&#x27;m getting the below error.  The error happens whether I build from the command line or VS2010.  Googling the error brings me this which leads me to believe it isn&#x27;t able to find the compiler. ...'''
date = "2013-12-09T16:52:00Z"
lastmod = "2013-12-11T10:09:00Z"
weight = 27964
keywords = [ "windows", "build" ]
aliases = [ "/questions/27964" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Windows build fails with return code '0xc0000135'](/questions/27964/windows-build-fails-with-return-code-0xc0000135)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27964-score" class="post-score" title="current number of votes">0</div><span id="post-27964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to build wireshark 1.8.3 release from source to build a plugin that isn't distributed with it. I'm getting the below error.</p><p>The error happens whether I build from the command line or VS2010.<br />
</p><p>Googling the error brings me <a href="http://stackoverflow.com/questions/6622869/nmake-fatal-error-u1077-return-code-0xc0000135">this</a> which leads me to believe it isn't able to find the compiler. But I've ran vcvars32.bat and I can execute cl.exe and get confirmation that it sees the compiler.<br />
</p><p>There is a similar issue <a href="http://ask.wireshark.org/questions/23713/error-building-wireshark-from-source">here</a> It only says it was a dependency that wasn't installed by Cygwin. I double checked that at least verify_tools is giving the correct output. I'm not sure what to check after that.<br />
</p><h2 id="the-error">The Error</h2><p>"C:\Python27\python.exe" tools\rdps.py print.ps ps.c NMAKE :fatal error U1077: 'C:\Python27\python.exe' : return code '0xc0000135'</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '13, 16:52</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p><span>tlann</span><br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span> </br></br></p></div></div><div id="comments-container-27964" class="comments-container"><span id="27967"></span><div id="comment-27967" class="comment"><div id="post-27967-score" class="comment-score">1</div><div class="comment-text"><p>That error code is a pretty generic one that means the application broke in some way. Can you run the command specified just from the prompt?</p></div><div id="comment-27967-info" class="comment-info"><span class="comment-age">(10 Dec '13, 01:35)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="27973"></span><div id="comment-27973" class="comment"><div id="post-27973-score" class="comment-score">1</div><div class="comment-text"><p>The same error message has been reported in the following question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/23713/error-building-wireshark-from-source">http://ask.wireshark.org/questions/23713/error-building-wireshark-from-source</a></p></blockquote><p>See the first comment of <span>@miss_develop</span> in the answer of <span>@Gerald Combs</span> and then the <strong>'solution'</strong> in the second comment:</p><blockquote><p>Cite: Got it resolved. It was <strong>a dependency that was not installed during the Cygwin install</strong>.</p></blockquote><p>Unfortunately he/she did not tell which dependency was missing.</p><p>Running the command manually, as suggested by <span></span><span>@grahamb</span>, will probably reveal the missing dependency.</p></div><div id="comment-27973-info" class="comment-info"><span class="comment-age">(10 Dec '13, 07:04)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="27977"></span><div id="comment-27977" class="comment"><div id="post-27977-score" class="comment-score"></div><div class="comment-text"><p>Hey thanks for trying to help out. As I said in my post, "The error happens whether I build from the command line or VS2010."<br />
I also noticed that the problem had been reported previously. I put the link in the post above.<br />
When running the build from the command line, it gives me the terse error message with no other hints.<br />
</p><p>The output above the error just talks about building a resource for the wiretap lib<br />
rc /r image\reordercap.rc Microsoft (R) Windows (R) Resource Compiler Version 6.1.7600.16385 Copyright (C) Microsoft Corporation. All rights reserved.</p><p>After that, it shows the error quoted in my post.</p></div><div id="comment-27977-info" class="comment-info"><span class="comment-age">(10 Dec '13, 10:12)</span> <span class="comment-user userinfo">tlann</span></div></div><span id="28004"></span><div id="comment-28004" class="comment"><div id="post-28004-score" class="comment-score">1</div><div class="comment-text"><p>Sorry, I did not realize you already posted that question as a link. My fault!</p><p>Anyway: I'm not sure what you were running manually, but did you try this command in the directory where print.ps is located?</p><blockquote><p>C:\Python27\python.exe" tools\rdps.py print.ps ps.c</p></blockquote><p>What is the output of that command and what is the content of ps.c afterwards?</p></div><div id="comment-28004-info" class="comment-info"><span class="comment-age">(11 Dec '13, 07:12)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="28012"></span><div id="comment-28012" class="comment"><div id="post-28012-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Kurt Knochner</span> Ughh I wish I would of thought of running that by itself. That is so obvious.<br />
I ran it and got a pop up window saying it wasn't able to find python27.dll.<br />
So this is do to a path problem. After fixing that and rerunning the build it works. Thank you so much. I have learned a leason from this.</p></div><div id="comment-28012-info" class="comment-info"><span class="comment-age">(11 Dec '13, 10:04)</span> <span class="comment-user userinfo">tlann</span></div></div></div><div id="comment-tools-27964" class="comment-tools"></div><div class="clear"></div><div id="comment-27964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28013"></span>

<div id="answer-container-28013" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28013-score" class="post-score" title="current number of votes">0</div><span id="post-28013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tlann has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks to <span>@Kurt Knochner</span> for helping me troubleshoot this. After running the line the error was happening on by itself, I ran it and got a pop up window saying "The program can't start because python27.dll is missing from your computer. Try reinstalling the program to fix this problem." After fixing this issue, the build worked correctly.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '13, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p><span>tlann</span><br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span> </br></br></p></div></div><div id="comments-container-28013" class="comments-container"></div><div id="comment-tools-28013" class="comment-tools"></div><div class="clear"></div><div id="comment-28013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

