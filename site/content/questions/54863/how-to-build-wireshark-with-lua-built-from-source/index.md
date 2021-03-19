+++
type = "question"
title = "How to build Wireshark with Lua built from source?"
description = '''Hi I am working on Fedora 22 and trying to build Wireshark with Lua enabled. The system has Lua 5.3 installed and there are dependencies on it, so I decided to build Lua 5.2.4 from source and link Wireshark against that. I built Lua 5.2.4 in my home directory: $ ls $HOME/Lua/lua-5.2.4/src/ | grep lu...'''
date = "2016-08-16T05:58:00Z"
lastmod = "2016-08-17T13:37:00Z"
weight = 54863
keywords = [ "lua", "linux" ]
aliases = [ "/questions/54863" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to build Wireshark with Lua built from source?](/questions/54863/how-to-build-wireshark-with-lua-built-from-source)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54863-score" class="post-score" title="current number of votes">0</div><span id="post-54863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am working on Fedora 22 and trying to build Wireshark with Lua enabled. The system has Lua 5.3 installed and there are dependencies on it, so I decided to build Lua 5.2.4 from source and link Wireshark against that.</p><p>I built Lua 5.2.4 in my home directory:</p><pre><code>$ ls $HOME/Lua/lua-5.2.4/src/ | grep lua.h
lua.h
lua.hpp</code></pre><p>but when I try to build Wireshark, the build system doesn't find Lua:</p><pre><code>$ ./configure --with-lua=$HOME/Lua/lua-5.2.4/src/ | grep lua    
checking for the location of lua.h... not found    
configure: error: Lua support was requested, but is not available</code></pre><p>What am I doing wrong please?</p><p>David</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '16, 05:58</strong></p><img src="https://secure.gravatar.com/avatar/cfb0228285e3c9494d763ba825e7a76c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidA_2015&#39;s gravatar image" /><p><span>DavidA_2015</span><br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidA_2015 has one accepted answer">50%</span></p></div></div><div id="comments-container-54863" class="comments-container"></div><div id="comment-tools-54863" class="comment-tools"></div><div class="clear"></div><div id="comment-54863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54867"></span>

<div id="answer-container-54867" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54867-score" class="post-score" title="current number of votes">0</div><span id="post-54867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I didn't manage to solve this. However, by installing patch:</p><p><a href="http://www.linuxfromscratch.org/patches/blfs/svn/wireshark-2.0.5-lua_5_3_1-1.patch">http://www.linuxfromscratch.org/patches/blfs/svn/wireshark-2.0.5-lua_5_3_1-1.patch</a></p><p>mentioned here:</p><p><a href="http://www.linuxfromscratch.org/blfs/view/svn/basicnet/wireshark.html">http://www.linuxfromscratch.org/blfs/view/svn/basicnet/wireshark.html</a></p><p>using:</p><p>patch -p1 &lt; wireshark-2.0.5-lua_5_3_1-1.patch</p><p>and then invoking:</p><p>./configure --with-lua</p><p>I succeeded in building Wireshark 2.0.5 with Lua 5.3.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '16, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/cfb0228285e3c9494d763ba825e7a76c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidA_2015&#39;s gravatar image" /><p><span>DavidA_2015</span><br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidA_2015 has one accepted answer">50%</span></p></div></div><div id="comments-container-54867" class="comments-container"><span id="54889"></span><div id="comment-54889" class="comment"><div id="post-54889-score" class="comment-score"></div><div class="comment-text"><p>FWIW this patch was considered and rejected for inclusion in Wireshark. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10881">bug 10881</a> and <a href="https://code.wireshark.org/review/#/c/8884/">change 8884</a>.</p></div><div id="comment-54889-info" class="comment-info"><span class="comment-age">(16 Aug '16, 14:43)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="54896"></span><div id="comment-54896" class="comment"><div id="post-54896-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your comment Jeff. The patch does seem to be working for me, but I note that it may be unreliable.</p><p>The bug link you specified suggests that the Lua detection code has been improved, but it's unclear to me whether those changes are included in 2.0.5.</p><p>The bottom line is that I'm unclear on how to get Wireshark 2.0.5 and Lua 5.2 installed on Fedora 22.</p></div><div id="comment-54896-info" class="comment-info"><span class="comment-age">(17 Aug '16, 02:03)</span> <span class="comment-user userinfo">DavidA_2015</span></div></div><span id="54928"></span><div id="comment-54928" class="comment"><div id="post-54928-score" class="comment-score"></div><div class="comment-text"><p>I took a look at our code for detecting Lua and it looks like it won't work to point it to a Lua build directory. In your example it won't find <code>lua.h</code> because it wants that file to be in, for example, <code>$dir/include/lua.h</code>.</p><p>So I'd guess that leaves you with 2 possibilities:</p><ol><li>Find a Fedora Lua (and -devel) package for Lua 5.2 or before. There's some discussion on bug 10881 that F24 has a compat-lua-devel package. Not sure about F20.</li><li>(or) "make install" the Lua you built and point Wireshark's ./configure at the installed location.</li></ol><p>It might be possible to make the configure script be able to pick up Lua from a non-installed location but it would require work--you could <a href="https://bugs.wireshark.org">open a bug report</a> if you want (if you do please reference this question and mention the bug number here--all for cross-referencing purposes).</p></div><div id="comment-54928-info" class="comment-info"><span class="comment-age">(17 Aug '16, 13:37)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-54867" class="comment-tools"></div><div class="clear"></div><div id="comment-54867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

