+++
type = "question"
title = "How to include LuaExpat for parsing XML files in Lua Scripts?"
description = '''Hi all, i am writing a Wireshark listener in Lua which needs to process a XML file before registering the listener. For parsing the XML file I used LuaExpat (lxp) and tried the parsing functionality in the Lua interpreter 1 which runs fine. Unfortunately, when Wireshark tries to execute the script i...'''
date = "2013-09-16T05:41:00Z"
lastmod = "2013-09-16T06:36:00Z"
weight = 24749
keywords = [ "lua", "luaexpat", "module" ]
aliases = [ "/questions/24749" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to include LuaExpat for parsing XML files in Lua Scripts?](/questions/24749/how-to-include-luaexpat-for-parsing-xml-files-in-lua-scripts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24749-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>i am writing a Wireshark listener in Lua which needs to process a XML file before registering the listener. For parsing the XML file I used LuaExpat (lxp) and tried the parsing functionality in the Lua interpreter <a href="http://code.google.com/p/luaforwindows/">1</a> which runs fine. Unfortunately, when Wireshark tries to execute the script it fails:</p><pre><code>tshark: Lua: Error during loading:
 [string &quot;res.lua&quot;]:2: module &#39;lxp&#39; not found:
        no field package.preload[&#39;lxp&#39;]
        no file &#39;.\lxp.lua&#39;
        no file &#39;C:\Program Files\Wireshark\lua\lxp.lua&#39;
        no file &#39;C:\Program Files\Wireshark\lua\lxp\init.lua&#39;
        no file &#39;C:\Program Files\Wireshark\lxp.lua&#39;
        no file &#39;C:\Program Files\Wireshark\lxp\init.lua&#39;
        no file &#39;C:\Program Files (x86)\Lua\5.1\lua\lxp.luac&#39;
        no file &#39;.\lxp.dll&#39;
        no file &#39;C:\Program Files\Wireshark\lxp.dll&#39;
        no file &#39;C:\Program Files\Wireshark\loadall.dll&#39;
        no file &#39;C:\Program Files\Wireshark\clibs\lxp.dll&#39;
        no file &#39;C:\Program Files\Wireshark\clibs\loadall.dll&#39;
        no file &#39;.\lxp51.dll&#39;
        no file &#39;C:\Program Files\Wireshark\lxp51.dll&#39;
        no file &#39;C:\Program Files\Wireshark\clibs\lxp51.dll&#39;</code></pre><p>I am running Wireshark version 1.10 on Windows 7 64bit.</p><p>Any ideas? Thanks! Jonas</p></div><div id="question-tags" class="tags-container tags">lua luaexpat module</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '13, 05:41</strong></p><img src="https://secure.gravatar.com/avatar/29fc7e1b8b26c86a12f68617a425c66f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johannes24&#39;s gravatar image" /><p>johannes24<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johannes24 has one accepted answer">100%</span></p></div></div><div id="comments-container-24749" class="comments-container"></div><div id="comment-tools-24749" class="comment-tools"></div><div class="clear"></div><div id="comment-24749-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24753"></span>

<div id="answer-container-24753" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24753-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Get a copy of lxp.dll from the link below.</p><blockquote><p><a href="http://files.luaforge.net/releases/luaexpat/LuaExpat/LuaExpat1.1.0">http://files.luaforge.net/releases/luaexpat/LuaExpat/LuaExpat1.1.0</a></p></blockquote><p>Then copy lxp.dll to the directory C:\Program Files\Wireshark\, or any of the other directories where Wireshark tried to find it (see your output above).</p><p><strong>UPDATE</strong><br />
Following the hint of @grahamb (see his comment below): The <strong>'bittedness'</strong> of the LuaExpat DLL mentioned above is 32 (Bit). You cannot load that into a 64 Bit version of Wireshark.</p><p>These are your options:</p><ol><li>Install a 32 Bit version of Wireshark on your 64 Bit OS. Loading the 32 Bit version of lxp.dll will work in such a setup</li><li>Get or compile a 64 Bit version of the DLL</li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '13, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Sep '13, 03:23</p></div></div><div id="comments-container-24753" class="comments-container"><span id="24758"></span><div id="comment-24758" class="comment"><div id="post-24758-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, thanks for your reply. I tried your suggestion but unfortunately Wireshak can't execute my script:</p><p>tshark: Lua: Error during loading: error loading module 'lxp' from file '.\lxp.dll': %1 ist keine zulΣssige Win32-Anwendung.</p><p>In case you don't understand German, it means: %1 is not a valid Win32 application.</p><p>Do you have any further ideas? Thanks!</p></div><div id="comment-24758-info" class="comment-info"><span class="comment-age">(16 Sep '13, 07:01)</span> johannes24</div></div><span id="24759"></span><div id="comment-24759" class="comment"><div id="post-24759-score" class="comment-score"></div><div class="comment-text"><p>I also tried setting the environment variables LUA_PATH and LUA_CPATHS like my Lua interpreter shows their values:</p><blockquote><p>print (package.path) ;.\?.lua;C:\Program Files (x86)\Lua\5.1\lua\?.lua;C:\Program Files (x86)\Lua\5.1\lua\?\init.lua;C:\Program Files (x86)\Lua\5.1\?.lua;C:\Program Files (x86)\Lua\5.1\?\init.lua;C:\Program Files (x86)\Lua\5.1\lua\?.luac print (package.cpath) .\?.dll;.\?51.dll;C:\Program Files (x86)\Lua\5.1\?.dll;C:\Program Files (x86)\Lua\5.1\?51.dll;C:\Program Files (x86)\Lua\5.1\clibs\?.dll;C:\Program Files (x86)\Lua\5.1\clibs\?51.dll;C:\Program Files (x86)\Lua\5.1\loadall.dll;C:\Program Files (x86)\Lua\5.1\clibs\loadall.dll</p></blockquote><p>But this results in the same error like copying lxp.dll to the wireshark directory.</p></div><div id="comment-24759-info" class="comment-info"><span class="comment-age">(16 Sep '13, 07:04)</span> johannes24</div></div><span id="24760"></span><div id="comment-24760" class="comment"><div id="post-24760-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, I don't have an answer yet. But maybe this is a 32/64bit problem?</p><p>The Lua interpreter I used is from <a href="http://code.google.com/p/luaforwindows/">1</a>. Thanks, Jo</p></div><div id="comment-24760-info" class="comment-info"><span class="comment-age">(16 Sep '13, 07:21)</span> johannes24</div></div><span id="24762"></span><div id="comment-24762" class="comment not_top_scorer"><div id="post-24762-score" class="comment-score"></div><div class="comment-text"><blockquote><p>In case you don't understand German, it means: %1 is not a valid Win32 application.</p></blockquote><p>Never mind, I was able to read it (I'm from Munich) ;-)</p><p>However, I don't know why it rejects the DLL. Can you please post a small lua script that makes use of the library? I will then try to run it on my system.</p><blockquote><p>Unfortunately, I don't have an answer yet. But maybe this is a 32/64bit problem?</p></blockquote><p>Could well be.</p></div><div id="comment-24762-info" class="comment-info"><span class="comment-age">(16 Sep '13, 07:29)</span> Kurt Knochner ♦</div></div><span id="24763"></span><div id="comment-24763" class="comment not_top_scorer"><div id="post-24763-score" class="comment-score"></div><div class="comment-text"><p>--sample.lua</p><p>do local lxp = require("lxp") -- crashes</p><p>local function init_listener() local tap = Listener.new(nil, "eth")<br />
</p><pre><code>function tap.reset()
end    
function tap.packet(pinfo, tvb)
  print(&quot;packet rcvd&quot;)
end    
function tap.draw()
end</code></pre><p>end</p><p>-- Initialize the listener init_listener() end -- do</p><p>Afterwards, I run the above Lua script using either tshark or wireshark:</p><p>tshark.exe -i 1 -q -Xlua_script:sample.lua</p></div><div id="comment-24763-info" class="comment-info"><span class="comment-age">(16 Sep '13, 07:35)</span> johannes24</div></div><span id="24773"></span><div id="comment-24773" class="comment"><div id="post-24773-score" class="comment-score">1</div><div class="comment-text"><p>it works on WinXP 32 Bit. It fails to load the DLL on Win7 64Bit.</p><p>If you load the DLL into <a href="http://www.dependencywalker.com/">Dependency Walker</a>, you'll find that it's a 32 Bit DLL.</p><p>So, if you want to use that library in a 64 Bit OS (and/or Wireshark), you need a 64 Bit version of the DLL or create one yourself.</p><p>Maybe it helps to install a 32 Bit version of Wireshark on your 64 Bit OS. I have not tried that.</p></div><div id="comment-24773-info" class="comment-info"><span class="comment-age">(16 Sep '13, 08:52)</span> Kurt Knochner ♦</div></div><span id="24774"></span><div id="comment-24774" class="comment"><div id="post-24774-score" class="comment-score">2</div><div class="comment-text"><p>The bittedness of the DLL must match the bittedness of Wireshark. You can only run 32 bit apps on a 32 bit OS, you can user either on a 64 bit OS, but DLL's must match the program that's loading them.</p><p>32 bit Wireshark runs perfectly well on a 64 bit OS.</p></div><div id="comment-24774-info" class="comment-info"><span class="comment-age">(16 Sep '13, 09:38)</span> grahamb ♦</div></div><span id="24777"></span><div id="comment-24777" class="comment not_top_scorer"><div id="post-24777-score" class="comment-score"></div><div class="comment-text"><p>I did not know that this feature/characteristic was called <strong>bittedness</strong>. Do you know where that comes from?</p></div><div id="comment-24777-info" class="comment-info"><span class="comment-age">(16 Sep '13, 10:11)</span> Kurt Knochner ♦</div></div><span id="24784"></span><div id="comment-24784" class="comment not_top_scorer"><div id="post-24784-score" class="comment-score"></div><div class="comment-text"><p>I think I made it up :-) Or I might have come across it somewhere else, anyway that's the term we use in my day job.</p></div><div id="comment-24784-info" class="comment-info"><span class="comment-age">(16 Sep '13, 15:20)</span> grahamb ♦</div></div><span id="24796"></span><div id="comment-24796" class="comment not_top_scorer"><div id="post-24796-score" class="comment-score"></div><div class="comment-text"><p>Ok, thank you all for your help and suggestions. I just switched to the 32bit version of Wireshark and all works fine.</p><p>Thanks again for troubleshooting! Have a nice day! Jo</p></div><div id="comment-24796-info" class="comment-info"><span class="comment-age">(17 Sep '13, 00:29)</span> johannes24</div></div><span id="24797"></span><div id="comment-24797" class="comment not_top_scorer"><div id="post-24797-score" class="comment-score"></div><div class="comment-text"><p>@johannes24, if an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-24797-info" class="comment-info"><span class="comment-age">(17 Sep '13, 01:57)</span> grahamb ♦</div></div></div><div id="comment-tools-24753" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-24753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

