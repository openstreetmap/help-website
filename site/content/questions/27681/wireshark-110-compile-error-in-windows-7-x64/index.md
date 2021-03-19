+++
type = "question"
title = "wireshark 1.10 Compile error in windows 7 x64"
description = '''Hello everyone, I&#x27;d been trying to build the wireshark 1.10 release in windows 7 x64 following the Step-by-Step Guide in order to (later) apply a patch for a USB dissector that I have found in the web. Before I even applied the patch I tried to compile from the clean sources just to see if it works,...'''
date = "2013-12-02T17:05:00Z"
lastmod = "2013-12-02T17:49:00Z"
weight = 27681
keywords = [ "compile", "windows7", "x64", "error" ]
aliases = [ "/questions/27681" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark 1.10 Compile error in windows 7 x64](/questions/27681/wireshark-110-compile-error-in-windows-7-x64)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27681-score" class="post-score" title="current number of votes">0</div><span id="post-27681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone, I'd been trying to build the wireshark 1.10 release in windows 7 x64 following the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">Step-by-Step Guide</a> in order to (later) apply a patch for a USB dissector that I have found in the web.</p><p>Before I even applied the patch I tried to compile from the clean sources just to see if it works, which unfortunately didn't. The first error encountered is from the CRLF behavior of cygwin bash. I had to comment out lines 768 and 770 of config.nmake in order to force ignore CRLF:</p><pre><code>768: #!if &quot;$(SH_PROG)&quot;==&quot;bash&quot; &amp;&amp; [$(CYGWIN_PATH)\bash -c &quot;set -o igncr&quot; 2&gt;nul: ] == 0
769: SH_FLAGS=-o igncr
770: #!endif</code></pre><p>After that I can get all the libraries and can verify tools:<img src="https://osqa-ask.wireshark.org/upfiles/scrshot1.png" alt="alt text" /></p><p>And finally, when trying to build the release I get the following error whcich I have no clue on how to solve it: <img src="https://osqa-ask.wireshark.org/upfiles/scrshot2.png" alt="alt text" /></p><p>Any help is appreciated.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-x64" rel="tag" title="see questions tagged &#39;x64&#39;">x64</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '13, 17:05</strong></p><img src="https://secure.gravatar.com/avatar/013d888ea16f505c673aa246fd0427ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chaicko&#39;s gravatar image" /><p><span>chaicko</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chaicko has one accepted answer">100%</span></p></img></div></div><div id="comments-container-27681" class="comments-container"></div><div id="comment-tools-27681" class="comment-tools"></div><div class="clear"></div><div id="comment-27681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27682"></span>

<div id="answer-container-27682" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27682-score" class="post-score" title="current number of votes">0</div><span id="post-27682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="chaicko has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Already found the fix in <a href="http://ask.wireshark.org/questions/23713/error-building-wireshark-from-source">this thread!</a>. m4 package has to be installed in cygwin. Compilation was successful :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '13, 17:49</strong></p><img src="https://secure.gravatar.com/avatar/013d888ea16f505c673aa246fd0427ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chaicko&#39;s gravatar image" /><p><span>chaicko</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chaicko has one accepted answer">100%</span></p></img></div></div><div id="comments-container-27682" class="comments-container"></div><div id="comment-tools-27682" class="comment-tools"></div><div class="clear"></div><div id="comment-27682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

