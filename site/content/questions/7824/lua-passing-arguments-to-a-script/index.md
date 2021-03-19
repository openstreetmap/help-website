+++
type = "question"
title = "Lua - passing arguments to a script"
description = '''How can I pass arguments (from the command line) to a tshark/Lua script? Specifically, I&#x27;m interested in having a DEBUG flag, that changes the script&#x27;s logics.'''
date = "2011-12-07T07:51:00Z"
lastmod = "2014-03-07T18:16:00Z"
weight = 7824
keywords = [ "lua", "tshark" ]
aliases = [ "/questions/7824" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Lua - passing arguments to a script](/questions/7824/lua-passing-arguments-to-a-script)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7824-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I pass arguments (from the command line) to a tshark/Lua script?<br />
Specifically, I'm interested in having a DEBUG flag, that changes the script's logics.</p></div><div id="question-tags" class="tags-container tags">lua tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '11, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/920a90d8a3dca941060cc1e39cc76346?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trevor&#39;s gravatar image" /><p>Trevor<br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trevor has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Dec '11, 07:52</p></div></div><div id="comments-container-7824" class="comments-container"></div><div id="comment-tools-7824" class="comment-tools"></div><div class="clear"></div><div id="comment-7824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="30591"></span>

<div id="answer-container-30591" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30591-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>[This is a really old question, but I came upon it while searching through Lua-related questions and thought it should be updated]</p><p>The latest wireshark automated builds (nightly 1.11.3) have the ability to pass one or more arguments to a Lua script. It's done with a '<code>-X lua_script[num]:arg</code>' syntax, where <code>[num]</code> is replaced by an integer for which lua script to pass the argument to (since you can load multiple scripts). So the number needs to match which <code>-X lua_script:filename</code> it was, like so:</p><pre><code>tshark -X lua_script:foo.lua -X lua_script:bar.lua -X lua_script1:arg1 -X lua_script2:arg2</code></pre><p>In the above command, the string "<code>arg1</code>" is passed to the foo.lua script, while the string "<code>arg2</code>" is passed to the bar.lua script. If you had another '<code>-X lua_script1:arg3</code>' at the end, then the string "<code>arg3</code>" would be passed to foo.lua.</p><p>Note that inside your script (i.e., inside foo.lua or bar.lua) you access the passed-in arguments through the '<code>...</code>' Lua varargs notation. So like this:</p><pre><code>-- put the passed-in args into a table
local args = {...}
-- print them out
for i,v in ipairs(args) do
    print(&quot;argument #&quot; .. i .. &quot; is:&quot; .. v)
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '14, 18:16</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30591" class="comments-container"></div><div id="comment-tools-30591" class="comment-tools"></div><div class="clear"></div><div id="comment-30591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7838"></span>

<div id="answer-container-7838" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7838-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I recently learned how to make lua scripts for tshark. I believe I recall seeing in passing that passing args from command line to script cannot be done at this time. I don't recall where that was though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '11, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/88d413834375dbc71f5d3146aca1cd3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="studog&#39;s gravatar image" /><p>studog<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="studog has no accepted answers">0%</span></p></div></div><div id="comments-container-7838" class="comments-container"></div><div id="comment-tools-7838" class="comment-tools"></div><div class="clear"></div><div id="comment-7838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7840"></span>

<div id="answer-container-7840" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7840-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Someone had <a href="http://seclists.org/wireshark/2011/Jul/519">asked</a> this a while ago on one of the <a href="http://www.wireshark.org/lists/">mailing lists</a>...</p><p>The only way (AFAIK) to pass arguments to a WS Lua script is to use environment variables, as shown here:</p><pre><code>$ echo &quot;print(&#39;DEBUG&#39;, os.getenv(&#39;DEBUG&#39;))&quot; &gt; test.lua
$ DEBUG=1 tshark -v -Xlua_script:test.lua 
DEBUG   1
TShark 1.7.1 (SVN Rev 39998 from /trunk)

Copyright 1998-2011 Gerald Combs &lt;[email protected]&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (64-bit) with GLib 2.28.8, with libpcap 1.1.1, with libz 1.2.5, without
POSIX capabilities, with SMI 0.4.8, with c-ares 1.7.4, with Lua 5.1, with Python
2.7.1, with GnuTLS 2.8.6, with Gcrypt 1.5.0, with MIT Kerberos, with GeoIP.

Running on Mac OS 10.7.2 (Darwin 11.2.0), with locale en_US.UTF-8, with libpcap
version 1.1.1, with libz 1.2.5.

Built using llvm-gcc 4.2.1 (Based on Apple Inc. build 5658) (LLVM build
2336.1.00).</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '11, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-7840" class="comments-container"></div><div id="comment-tools-7840" class="comment-tools"></div><div class="clear"></div><div id="comment-7840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

