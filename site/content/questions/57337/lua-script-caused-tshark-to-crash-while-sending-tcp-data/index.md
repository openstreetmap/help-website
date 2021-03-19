+++
type = "question"
title = "Lua script caused tshark to crash while sending tcp data"
description = '''Tried to run a simple lua script in tshark, the socket connection worked fine but sending data caused the crash. Here is the simple lua script (called te.lua),  local host, port = &quot;127.0.0.1&quot;, 80 local socket = require(&quot;socket&quot;) local tcp = assert(socket.tcp())  tcp:connect(host, port); --note the n...'''
date = "2016-11-12T09:48:00Z"
lastmod = "2017-01-10T05:59:00Z"
weight = 57337
keywords = [ "lua" ]
aliases = [ "/questions/57337" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua script caused tshark to crash while sending tcp data](/questions/57337/lua-script-caused-tshark-to-crash-while-sending-tcp-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57337-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Tried to run a simple lua script in tshark, the socket connection worked fine but sending data caused the crash.</p><p>Here is the simple lua script (called te.lua),</p><pre><code>local host, port = &quot;127.0.0.1&quot;, 80
local socket = require(&quot;socket&quot;)
local tcp = assert(socket.tcp())

tcp:connect(host, port);
--note the newline below
io.write(&quot;sending...\n&quot;);
tcp:send(&quot;GET / HTTP/1.1\r\n\r\n&quot;);
io.write(&quot;finished sending...\n&quot;);</code></pre><p>Here is the command line</p><pre><code>tshark -Xlua_script:te.lua -r /0000.pcap tcp.port == 0</code></pre><p>Using a debugger, here is the stack trace</p><pre><code>#0  0x00007fffec4287fc in timeout_markstart ()
   from /usr/local/lib/lua/5.2/socket/core.so
#1  0x00007fffec428b49 in buffer_meth_send ()
   from /usr/local/lib/lua/5.2/socket/core.so
#2  0x00007ffff268c61d in ?? () from /usr/lib/x86_64-linux-gnu/liblua5.2.so.0
#3  0x00007ffff26979b4 in ?? () from /usr/lib/x86_64-linux-gnu/liblua5.2.so.0
#4  0x00007ffff268c989 in ?? () from /usr/lib/x86_64-linux-gnu/liblua5.2.so.0
#5  0x00007ffff268bfac in ?? () from /usr/lib/x86_64-linux-gnu/liblua5.2.so.0
#6  0x00007ffff268cbc1 in ?? () from /usr/lib/x86_64-linux-gnu/liblua5.2.so.0
#7  0x00007ffff2688c9d in lua_pcallk ()
   from /usr/lib/x86_64-linux-gnu/liblua5.2.so.0
#8  0x00007ffff5837293 in ?? ()
   from /usr/lib/x86_64-linux-gnu/libwireshark.so.3
#9  0x00007ffff5837b80 in ?? ()
   from /usr/lib/x86_64-linux-gnu/libwireshark.so.3
#10 0x00000000004097be in ?? ()
#11 0x00007ffff28d3f45 in __libc_start_main (main=0x409500, argc=7, 
    argv=0x7fffffffde98, init=&lt;optimized out&gt;, fini=&lt;optimized out&gt;, 
    rtld_fini=&lt;optimized out&gt;, stack_end=0x7fffffffde88) at libc-start.c:287
#12 0x000000000040c1d3 in _start ()</code></pre><p>I am using tshark 1.10.6 on ubuntu 14.04 (64bit).</p><p>Any ideas?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '16, 09:48</strong></p><img src="https://secure.gravatar.com/avatar/0228802baecfa9b8d8764a043fea883b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharkfun&#39;s gravatar image" /><p>sharkfun<br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharkfun has no accepted answers">0%</span></p></div></div><div id="comments-container-57337" class="comments-container"></div><div id="comment-tools-57337" class="comment-tools"></div><div class="clear"></div><div id="comment-57337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58638"></span>

<div id="answer-container-58638" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58638-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Interestingly another project <a href="https://github.com/diegonehab/luasocket/issues/179">reported</a> an almost identical crash backtrace. It looks like the problem was a symbol conflict between that project's <code>buffer_init</code> routine and Lua's.</p><p>Wireshark in version 1.10 had a global symbol in <code>libwsutil.so</code> by that name. It was <a href="https://code.wireshark.org/review/3351">renamed</a> (in time for 2.0.0) to <code>ws_buffer_init</code>.</p><p>So: you should upgrade to 2.0.0 or later to fix the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '17, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-58638" class="comments-container"><span id="58652"></span><div id="comment-58652" class="comment"><div id="post-58652-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the idea, I tried 2.0.0 and don't see the crash. However, it doesn't seem to make the TCP connection though. Any ideas?</p></div><div id="comment-58652-info" class="comment-info"><span class="comment-age">(10 Jan '17, 18:44)</span> pktUser1001</div></div><span id="58663"></span><div id="comment-58663" class="comment"><div id="post-58663-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I've got no ideas about why the TCP connection wouldn't work in the newer version.</p></div><div id="comment-58663-info" class="comment-info"><span class="comment-age">(11 Jan '17, 06:20)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-58638" class="comment-tools"></div><div class="clear"></div><div id="comment-58638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

