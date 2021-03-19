+++
type = "question"
title = "adding a listener?"
description = '''Hi, I am trying to customize a version of wireshark. I believe what I am trying to do is add a listener, but I&#x27;m not sure. I want to be able to take certain packets, including packets with errors, and send them over a socket to another application. I will need to do some customized processing of the...'''
date = "2011-08-17T11:49:00Z"
lastmod = "2011-08-17T22:07:00Z"
weight = 5724
keywords = [ "listener", "lua", "development" ]
aliases = [ "/questions/5724" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [adding a listener?](/questions/5724/adding-a-listener)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5724-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to customize a version of wireshark. I believe what I am trying to do is add a listener, but I'm not sure. I want to be able to take certain packets, including packets with errors, and send them over a socket to another application. I will need to do some customized processing of these packets, although I can either do that processing as part of wireshark, or I can do it on the other side of my socket.</p><p>Does it sound like I need to add a "Listener"?</p><p>If so, is adding a listener best done in a lua script, or by modifying the wireshark C code? In the lua documentation, I see information on adding a listener, but I did not see that in the wireshark development (C) documentation. I have used C/C++ for many years but have never used lua.</p></div><div id="question-tags" class="tags-container tags">listener lua development</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Aug '11, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/851676df3c7a09999c0522099f40d6e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JVo&#39;s gravatar image" /><p>JVo<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JVo has no accepted answers">0%</span></p></div></div><div id="comments-container-5724" class="comments-container"><span id="5732"></span><div id="comment-5732" class="comment"><div id="post-5732-score" class="comment-score"></div><div class="comment-text"><p>possible <a href="http://ask.wireshark.org/questions/5659/how-best-to-customize-wireshark">duplicate</a></p></div><div id="comment-5732-info" class="comment-info"><span class="comment-age">(17 Aug '11, 22:08)</span> helloworld</div></div></div><div id="comment-tools-5724" class="comment-tools"></div><div class="clear"></div><div id="comment-5724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5731"></span>

<div id="answer-container-5731" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5731-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, a Listener (aka "Tap") is appropriate for the task. I would pick Lua over C. Don't be afraid of Lua...it's easy to learn:</p><ul><li><a href="http://lua-users.org/wiki/LuaTutorial">Lua Tutorial</a></li><li><a href="http://wiki.wireshark.org/LuaAPI">Wireshark Lua API Wiki</a></li><li><a href="http://www.wireshark.org/docs/wsug_html_chunked/wsluarm.html">Wireshark Lua Manual</a></li><li><a href="http://www.wireshark.org/docs/wsug_html_chunked/wslua_tap_example.html">Lua Listener Example</a></li><li><a href="http://wiki.wireshark.org/Lua/Taps">More Lua Listener Examples</a></li><li><a href="http://wiki.wireshark.org/Lua/Examples#dumping_to_multiple_files">Listener that extracts packets to multiple files</a></li></ul><h2 id="lua-vs-c">Lua vs C</h2><p>Here are a few points:</p><p><em>PROS</em></p><ol><li><p>Bugs in Lua scripts are less likely to crash Wireshark. The few crashes I've seen are from bugs in underlying C code that the Lua API invokes.</p></li><li><p>Lua scripts are compatible across multiple versions of Wireshark. On the other hand, it's recommended that C dissectors be re-compiled for the target Wireshark version to maintain compatibility.</p></li><li><p>Lua development is faster than in C. Need to make a change? Edit the Lua script and restart Wireshark. (This ease of development is not seen for C dissectors.) A Wireshark installation, which includes a Lua interpreter, is all you need to run a Lua script. No need for compilers or specific versions of libraries.</p></li></ol><p><em>CONS</em></p><ol><li><p>Lua scripts can be difficult to debug with Wireshark (there are few tools). You'll have to rely on print-outs to the console.</p></li><li><p>Lua can be less efficient (performance and memory) than C, but that's inherent in scripting languages. You might not even notice unless you open huge pcaps.</p></li><li><p>Lua can be less powerful than C because only a subset of Wireshark's functions are available to the Lua API, but you can use <a href="https://github.com/LuaDist/alien">LuaAlien</a> to invoke functions from libwireshark.dll/.so (or any other library). You probably won't need the unavailable functions anyway.</p></li></ol><h2 id="sockets">Sockets</h2><p>See <a href="http://w3.impa.br/~diego/software/luasocket/">LuaSocket</a> (or you can use LuaAlien to call your own C library).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Aug '11, 22:07</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-5731" class="comments-container"><span id="5742"></span><div id="comment-5742" class="comment"><div id="post-5742-score" class="comment-score"></div><div class="comment-text"><p>Wow, thanks for a very thorough response. I will go through everything you gave me, and let you know when I have more specific questions.</p><p>I do like being able to debug C, and the fact that I already know C makes me think that for me, C development would be faster than Lua. But I also don't want to muck with something that might cause wireshark. So, I guess I'll explore my options for now. Okay, so a listener is a tap, huh? I still need to get a handle on the terminology I guess.</p></div><div id="comment-5742-info" class="comment-info"><span class="comment-age">(18 Aug '11, 08:37)</span> JVo</div></div><span id="5749"></span><div id="comment-5749" class="comment"><div id="post-5749-score" class="comment-score"></div><div class="comment-text"><p>So, I'm also looking at adding various dissectors and will need to determine whether to do those in C or lua. It looks like using C provides me with an easy way to reassemble TCP packets: http://www.wireshark.org/docs/wsdg_html_chunked/ChDissectReassemble.html. Can I get TCP reassembly with lua?</p></div><div id="comment-5749-info" class="comment-info"><span class="comment-age">(18 Aug '11, 16:29)</span> JVo</div></div><span id="5751"></span><div id="comment-5751" class="comment"><div id="post-5751-score" class="comment-score"></div><div class="comment-text"><p>When I said "Lua development is faster", I meant the time between making a change in code and seeing its effect in action (you simply restart Wireshark to see the change). This is opposed to the time it takes to re-compile a C dissector and re-deploy it. (Not to mention the time it takes to setup your dev environment for building Wireshark)</p><p>Then again, faster or not, I certainly agree that you should go with the language you're most comfortable with.</p></div><div id="comment-5751-info" class="comment-info"><span class="comment-age">(18 Aug '11, 17:57)</span> helloworld</div></div><span id="5752"></span><div id="comment-5752" class="comment"><div id="post-5752-score" class="comment-score"></div><div class="comment-text"><p>Wireshark Lua does not expose the TCP reassembly function (namely <code>tcp_dissect_pdus</code>). However, you can use LuaAlien to invoke it.</p></div><div id="comment-5752-info" class="comment-info"><span class="comment-age">(18 Aug '11, 18:02)</span> helloworld</div></div><span id="5763"></span><div id="comment-5763" class="comment"><div id="post-5763-score" class="comment-score"></div><div class="comment-text"><p>Cool, thanks! Okay, I'm getting a better handle on my options. :o)</p></div><div id="comment-5763-info" class="comment-info"><span class="comment-age">(19 Aug '11, 12:20)</span> JVo</div></div></div><div id="comment-tools-5731" class="comment-tools"></div><div class="clear"></div><div id="comment-5731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

