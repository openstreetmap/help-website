+++
type = "question"
title = "Win64 build problems"
description = '''Hello, I&#x27;m trying to build Wireshark 2.0 from the source on Windows 7 64-bit. I&#x27;ve been following this guide: https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChWin32Generate Everything went fine until the Wireshark Build phase. So, cmake generated build files correctly. The only t...'''
date = "2016-03-14T07:06:00Z"
lastmod = "2016-03-18T07:56:00Z"
weight = 50895
keywords = [ "win64", "qt5", "build", "wireshark" ]
aliases = [ "/questions/50895" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Win64 build problems](/questions/50895/win64-build-problems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50895-score" class="post-score" title="current number of votes">0</div><span id="post-50895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to build Wireshark 2.0 from the source on Windows 7 64-bit. I've been following this guide: <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChWin32Generate">https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChWin32Generate</a> Everything went fine until the Wireshark Build phase. So, cmake generated build files correctly. The only thing different from the guide is Qt version. I have 5.4 installed which was used to build Wireshark 1.12 (successfully). I'm adding error logs below (if you look down below you can see many are concerning Qt). I compared them with build logs from Wireshark buildbot and the trouble started when Qt should be compiled.</p><p>Any help or suggestion is welcome.</p><p>Logs: <a href="http://pastebin.com/m6asVPuv">http://pastebin.com/m6asVPuv</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-win64" rel="tag" title="see questions tagged &#39;win64&#39;">win64</span> <span class="post-tag tag-link-qt5" rel="tag" title="see questions tagged &#39;qt5&#39;">qt5</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '16, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/a03fa5b340afab78d2e44b63e8dcf3d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aliniel&#39;s gravatar image" /><p><span>Aliniel</span><br />
<span class="score" title="30 reputation points">30</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aliniel has 2 accepted answers">100%</span></p></div></div><div id="comments-container-50895" class="comments-container"></div><div id="comment-tools-50895" class="comment-tools"></div><div class="clear"></div><div id="comment-50895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50896"></span>

<div id="answer-container-50896" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50896-score" class="post-score" title="current number of votes">0</div><span id="post-50896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Aliniel has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks to be an issue with missing docbook components, have you installed the following Cygwin packages as per the Developers Guide, in particular the 2nd one on the list:</p><ul><li>Text/asciidoc</li><li>Text/docbook-xml45</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '16, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50896" class="comments-container"><span id="50897"></span><div id="comment-50897" class="comment"><div id="post-50897-score" class="comment-score"></div><div class="comment-text"><p>I was indeed missing docbook-xml45. But it only took 3 erros away. I also installed Qt 5.5 just to be sure and it didn't help. New logs: <a href="http://pastebin.com/hpr6VyLs">http://pastebin.com/hpr6VyLs</a></p></div><div id="comment-50897-info" class="comment-info"><span class="comment-age">(14 Mar '16, 08:43)</span> <span class="comment-user userinfo">Aliniel</span></div></div><span id="50898"></span><div id="comment-50898" class="comment"><div id="post-50898-score" class="comment-score"></div><div class="comment-text"><p>Odd results, what's the contents of <code>C:\Development\bmakan\wsbuild64\version.h</code>?</p></div><div id="comment-50898-info" class="comment-info"><span class="comment-age">(14 Mar '16, 08:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="50899"></span><div id="comment-50899" class="comment"><div id="post-50899-score" class="comment-score"></div><div class="comment-text"><p>There were only these 3 lines:</p><p>Unable to open C:/Development/bmakan/wireshark/.svn/entries</p><p>#define VCSVERSION "SVN Rev Unknown"</p><p>#define VCSBRANCH "unknown"</p></div><div id="comment-50899-info" class="comment-info"><span class="comment-age">(14 Mar '16, 08:52)</span> <span class="comment-user userinfo">Aliniel</span></div></div><span id="50900"></span><div id="comment-50900" class="comment"><div id="post-50900-score" class="comment-score"></div><div class="comment-text"><p>The first line is an error and not meant to be there. <code>version.h</code> is configured by CMake, and uses the output of tools\make-version.pl to generate the contents.</p><p>In your case it seems to be attempting to use svn. Is this because you don't have git on your path? In your build directory, have a look in CMakeCache.txt for a line beginning with <code>GIT_EXECUTABLE:FILEPATH=</code>, report back what you find.</p></div><div id="comment-50900-info" class="comment-info"><span class="comment-age">(14 Mar '16, 09:11)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="50901"></span><div id="comment-50901" class="comment"><div id="post-50901-score" class="comment-score">1</div><div class="comment-text"><p>This happens because of a bug in make-version.pl file. Try editing the file and in line 317 replace:</p><pre><code>        print (&quot;Unable to open $srcdir/.svn/entries\n&quot;);</code></pre><p>by</p><pre><code>        print STDERR &quot;Unable to open $srcdir/.svn/entries\n&quot;;</code></pre></div><div id="comment-50901-info" class="comment-info"><span class="comment-age">(14 Mar '16, 09:14)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="51017"></span><div id="comment-51017" class="comment not_top_scorer"><div id="post-51017-score" class="comment-score"></div><div class="comment-text"><p>Pascal's solution worked. Thanks a lot!</p></div><div id="comment-51017-info" class="comment-info"><span class="comment-age">(18 Mar '16, 02:11)</span> <span class="comment-user userinfo">Aliniel</span></div></div><span id="51018"></span><div id="comment-51018" class="comment not_top_scorer"><div id="post-51018-score" class="comment-score"></div><div class="comment-text"><p>Note this bug was fixed in the master branch in October 2015, change <a href="https://code.wireshark.org/review/#/c/11041/">11041</a>.</p><p><span>@Aliniel</span>, what version are you building?</p></div><div id="comment-51018-info" class="comment-info"><span class="comment-age">(18 Mar '16, 03:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51032"></span><div id="comment-51032" class="comment not_top_scorer"><div id="post-51032-score" class="comment-score"></div><div class="comment-text"><p>It's a custom build branched from 2.0 at some earlier point. It was probably before thix fix was applied.</p></div><div id="comment-51032-info" class="comment-info"><span class="comment-age">(18 Mar '16, 07:56)</span> <span class="comment-user userinfo">Aliniel</span></div></div></div><div id="comment-tools-50896" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-50896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

