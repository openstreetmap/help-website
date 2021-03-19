+++
type = "question"
title = "how to build a release verson of wireshark?"
description = '''Hi all, I have downloaded the 1.6.4 source code for 32 bit machines. Now, i want to build a release version of wireshark, but I do not know how to change the file &quot;config.nmake&quot;, Any ideas?'''
date = "2012-10-08T01:08:00Z"
lastmod = "2012-10-08T02:16:00Z"
weight = 14768
keywords = [ "build" ]
aliases = [ "/questions/14768" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to build a release verson of wireshark?](/questions/14768/how-to-build-a-release-verson-of-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14768-score" class="post-score" title="current number of votes">0</div><span id="post-14768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I have downloaded the 1.6.4 source code for 32 bit machines. Now, i want to build a release version of wireshark, but I do not know how to change the file "config.nmake", Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '12, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/e59c9285946461a31a8f20309d8979b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ekgh&#39;s gravatar image" /><p><span>ekgh</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ekgh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Oct '12, 01:10</strong> </span></p></div></div><div id="comments-container-14768" class="comments-container"></div><div id="comment-tools-14768" class="comment-tools"></div><div class="clear"></div><div id="comment-14768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14769"></span>

<div id="answer-container-14769" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14769-score" class="post-score" title="current number of votes">1</div><span id="post-14769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to read the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">Developers Guide</a> which has all the gory details of building Wireshark on Windows. To build a "release" version, i.e. create an installer you use the command: <code>make -f Makefile.nmake packaging</code> as detailed in the Developers Guide section <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#id36128086">Optional: Create a Wireshark Installer</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '12, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-14769" class="comments-container"><span id="14771"></span><div id="comment-14771" class="comment"><div id="post-14771-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer. I have succesed to build the wireshark 1.6.4 in MSVC 2010, I think it was the debug version. Now I don't know how to modify the "config.nmake" to build a release version?</p></div><div id="comment-14771-info" class="comment-info"><span class="comment-age">(08 Oct '12, 01:39)</span> <span class="comment-user userinfo">ekgh</span></div></div><span id="14772"></span><div id="comment-14772" class="comment"><div id="post-14772-score" class="comment-score">1</div><div class="comment-text"><p>Presuming you want to add some optimisation settings, e.g. <code>/O??</code> then I think you would need to modify the value of LOCAL_CFLAGS (affects all compiled objects) or STANDARD_CFLAGS (affects only "Wireshark" compiled objects).</p><p>If you do this it would be interesting to report your experiences back to the developers mailing list.</p></div><div id="comment-14772-info" class="comment-info"><span class="comment-age">(08 Oct '12, 02:16)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-14769" class="comment-tools"></div><div class="clear"></div><div id="comment-14769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

