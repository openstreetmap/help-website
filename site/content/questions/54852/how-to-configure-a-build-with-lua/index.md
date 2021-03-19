+++
type = "question"
title = "How to configure a build with Lua"
description = '''Thanks for your answer. So, I am trying to build Wireshark from source, but I have a problem with the Lua version: ./configure --with-lua  &amp;lt;snip&amp;gt; checking for LUA... no checking for the location of lua.h... /usr/include checking the Lua version... 5.3 - disabling Lua support configure: error: ...'''
date = "2016-08-16T03:43:00Z"
lastmod = "2016-08-16T07:04:00Z"
weight = 54852
keywords = [ "lua", "build" ]
aliases = [ "/questions/54852" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to configure a build with Lua](/questions/54852/how-to-configure-a-build-with-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54852-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Thanks for your answer. So, I am trying to build Wireshark from source, but I have a problem with the Lua version:</p><pre><code>./configure --with-lua

&lt;snip&gt;
checking for LUA... no
checking for the location of lua.h... /usr/include checking the Lua version... 5.3 - disabling Lua support
configure: error: Lua support was requested, but is not available</code></pre><p>Do I need to replace my Lua install with a version &lt;5.3?</p><p>If yes, how can I do that?</p></div><div id="question-tags" class="tags-container tags">lua build</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '16, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/cfb0228285e3c9494d763ba825e7a76c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidA_2015&#39;s gravatar image" /><p>DavidA_2015<br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidA_2015 has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Aug '16, 05:10</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54852" class="comments-container"><span id="54855"></span><div id="comment-54855" class="comment"><div id="post-54855-score" class="comment-score"></div><div class="comment-text"><p>Your comment has been converted to a question as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-54855-info" class="comment-info"><span class="comment-age">(16 Aug '16, 04:47)</span> Jaap ♦</div></div></div><div id="comment-tools-54852" class="comment-tools"></div><div class="clear"></div><div id="comment-54852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54868"></span>

<div id="answer-container-54868" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54868-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I succeeded in building Wireshark 2.0.5 with Lua 5.3 by installing patch:</p><p><a href="http://www.linuxfromscratch.org/patches/blfs/svn/wireshark-2.0.5-lua_5_3_1-1.patch">http://www.linuxfromscratch.org/patches/blfs/svn/wireshark-2.0.5-lua_5_3_1-1.patch</a></p><p>mentioned here:</p><p><a href="http://www.linuxfromscratch.org/blfs/view/svn/basicnet/wireshark.html">http://www.linuxfromscratch.org/blfs/view/svn/basicnet/wireshark.html</a></p><p>using:</p><p>patch -p1 &lt; wireshark-2.0.5-lua_5_3_1-1.patch</p><p>and then invoking:</p><p>./configure --with-lua</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '16, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/cfb0228285e3c9494d763ba825e7a76c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidA_2015&#39;s gravatar image" /><p>DavidA_2015<br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidA_2015 has one accepted answer">50%</span></p></div></div><div id="comments-container-54868" class="comments-container"></div><div id="comment-tools-54868" class="comment-tools"></div><div class="clear"></div><div id="comment-54868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54859"></span>

<div id="answer-container-54859" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54859-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes LUA 5.3 is not supported check if there is a package for LUA 5.2 available for your system sudo zypper se lua</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '16, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-54859" class="comments-container"></div><div id="comment-tools-54859" class="comment-tools"></div><div class="clear"></div><div id="comment-54859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

