+++
type = "question"
title = "C# Dissector Plugin"
description = '''I would like to write a .NET dissector plugin to decode my own protocols.  Can wireshark read managed dlls (C# or managed C++), or does it have to be only native code or python script?  I have decoders written in C# already, and would like to reuse them if possible. Any ideas how this can be done? T...'''
date = "2013-11-19T02:13:00Z"
lastmod = "2013-11-19T03:52:00Z"
weight = 27091
keywords = [ "dissector", "wireshark", "plugin" ]
aliases = [ "/questions/27091" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [C\# Dissector Plugin](/questions/27091/c-dissector-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27091-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to write a .NET dissector plugin to decode my own protocols. Can wireshark read managed dlls (C# or managed C++), or does it have to be only native code or python script? I have decoders written in C# already, and would like to reuse them if possible. Any ideas how this can be done?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">dissector wireshark plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '13, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/10ba80b2d73f068e916ba35852a8a436?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lews%20Therin&#39;s gravatar image" /><p>Lews Therin<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lews Therin has one accepted answer">100%</span></p></div></div><div id="comments-container-27091" class="comments-container"></div><div id="comment-tools-27091" class="comment-tools"></div><div class="clear"></div><div id="comment-27091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27096"></span>

<div id="answer-container-27096" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27096-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is all native code. I have no idea if an unmanaged program can load a managed DLL, but if it is possible, then your DLL would have to present unmanaged interfaces so that Wireshark can call essential functions in it, your DLL may have to export some unmanaged data for Wireshark, and then any Wireshark infrastructure calls your DLL makes would have to be unmanaged and be passed and receive back unmanaged data structures.</p><p>In short if at all possible it's going to be a big chunk of work.</p><p>You may want to investigate other Wireshark dissector creation options such as text using <a href="http://wsgd.free.fr/">WSGD</a>, built-in languages such as Lua, or a C based dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '13, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-27096" class="comments-container"><span id="27097"></span><div id="comment-27097" class="comment"><div id="post-27097-score" class="comment-score"></div><div class="comment-text"><p>Hey Graham, thanks for the quick answer. The idea is to pretty much emulate WSGD -&gt; a generic native dll that will interface with any codecs/protocol I create in C#. It sounds like a lot of work indeed. I was hoping for experienced feedback, but seems there isn't a better way.</p></div><div id="comment-27097-info" class="comment-info"><span class="comment-age">(19 Nov '13, 05:15)</span> Lews Therin</div></div><span id="27121"></span><div id="comment-27121" class="comment"><div id="post-27121-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I have <strong>decoders written in C# already</strong>, and would like to reuse them if possible.</p></blockquote><p>Honestly, writing all the mananged -&gt; unmanaged interface code will be <strong>much more</strong> work (if it works at all) than simply rewriting your decoder logic (you already have that logic) in C and putting that into a template dissector (see Developer guide).</p><p>Regards<br />
Kurt</p></div><div id="comment-27121-info" class="comment-info"><span class="comment-age">(19 Nov '13, 15:25)</span> Kurt Knochner ♦</div></div><span id="27130"></span><div id="comment-27130" class="comment"><div id="post-27130-score" class="comment-score"></div><div class="comment-text"><p>Actually, you should be able to create a Lua dissector that uses a C# library via <a href="https://github.com/LuaDist/luainterface#lua-api">LuaInterface</a> to parse the payload. See a related <a href="http://ask.wireshark.org/questions/5868/how-do-i-setup-wireshark-to-run-luas-clrpackage">question</a> on how to set up LuaInterface with Wireshark.</p></div><div id="comment-27130-info" class="comment-info"><span class="comment-age">(19 Nov '13, 19:29)</span> helloworld</div></div><span id="27140"></span><div id="comment-27140" class="comment"><div id="post-27140-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the help guys.</p></div><div id="comment-27140-info" class="comment-info"><span class="comment-age">(20 Nov '13, 02:00)</span> Lews Therin</div></div><span id="27147"></span><div id="comment-27147" class="comment"><div id="post-27147-score" class="comment-score"></div><div class="comment-text"><p>@helloworld, Luainterface looks interesting, but I would suspect implementing a dissector that way might be less than optimal speed wise. I would also think that there will still need to be some translation between Wireshark data structures and whatever the original C# dissectors are doing.</p></div><div id="comment-27147-info" class="comment-info"><span class="comment-age">(20 Nov '13, 02:34)</span> grahamb ♦</div></div><span id="27149"></span><div id="comment-27149" class="comment not_top_scorer"><div id="post-27149-score" class="comment-score"></div><div class="comment-text"><p>It's even worse. You'll have to write a dissector in Lua, then pass the tvb data to the C# library and get back "some" data structure of the 'dissected' tvb (as you said). Then you'll have to walk through that data structure and add the proto fields within the Lua code based on the data structure you received from the C# code + convert data types between C# and Lua.</p><p>I don't see how that could be less (coding) work or how that could be in any way easier than a migration of the C# decoder logic to either C or Lua, as the dissector framework (handling tvb and proto fields) has to be coded in Lua/C anyways.</p></div><div id="comment-27149-info" class="comment-info"><span class="comment-age">(20 Nov '13, 03:11)</span> Kurt Knochner ♦</div></div><span id="27160"></span><div id="comment-27160" class="comment not_top_scorer"><div id="post-27160-score" class="comment-score"></div><div class="comment-text"><p>It might not be optimal in terms of speed, but that wasn't part of the question. The OP asks for a way to reuse his existing C# library. Depending on how much work was already invested into that library; and the size and complexity of the protocol, LuaInterface could be a shorter path than rewriting it.</p></div><div id="comment-27160-info" class="comment-info"><span class="comment-age">(20 Nov '13, 06:57)</span> helloworld</div></div></div><div id="comment-tools-27096" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-27096-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

