+++
type = "question"
title = "LUA API to get Wireshark installation info"
description = '''Is there any LUA API available through which i can get information like where Wireshark is installed in my machine, Which version of wireshark installed etc. from registry or from anwhere? I need it because i have developed my own plugin in lua and i am using wireshark installed path upto C:&#92;Program...'''
date = "2015-07-07T20:41:00Z"
lastmod = "2015-07-07T22:22:00Z"
weight = 43953
keywords = [ "directory", "lua", "wireshark" ]
aliases = [ "/questions/43953" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [LUA API to get Wireshark installation info](/questions/43953/lua-api-to-get-wireshark-installation-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43953-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any LUA API available through which i can get information like where Wireshark is installed in my machine, Which version of wireshark installed etc. from registry or from anwhere? I need it because i have developed my own plugin in lua and i am using wireshark installed path upto C:\ProgramFiles\Wireshark in to that plugin.</p></div><div id="question-tags" class="tags-container tags">directory lua wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '15, 20:41</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p>ankit<br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></div></div><div id="comments-container-43953" class="comments-container"><span id="43955"></span><div id="comment-43955" class="comment"><div id="post-43955-score" class="comment-score"></div><div class="comment-text"><blockquote><p>information like where Wireshark is installed in my machine</p></blockquote><p>I.e., you want the installation directory of Wireshark? What would your Lua plugin use this for?</p></div><div id="comment-43955-info" class="comment-info"><span class="comment-age">(07 Jul '15, 22:22)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-43953" class="comment-tools"></div><div class="clear"></div><div id="comment-43953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43954"></span>

<div id="answer-container-43954" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43954-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark version you can get through the global function "<code>get_version()</code>", documented in the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Utility.html">Utility functions section of the API docs</a>.</p><p>I don't believe there's a way to get the Wireshark path directly/only, but it's likely the first portion of the string returned with the global function "<code>Dir.global_config_path()</code>" or "<code>Dir.global_plugins_path()</code>", as documented in the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Dir.html">Directory functions section of the API docs</a>. (I don't use Windows so I'm not sure it's the same directory, but you can try it and find out)</p><p>But why do you need the path exactly? I ask because if there's some good reason, then we can add it into the Lua API. Usually, though, people don't need it for Lua plugins.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '15, 22:22</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43954" class="comments-container"><span id="43956"></span><div id="comment-43956" class="comment"><div id="post-43956-score" class="comment-score"></div><div class="comment-text"><p>I developed my whole plugin in structured way grouped some files into some folders and to traverse that folders i added dofile("path_to_wireshark_folder.."myfile.lua") in my_plugin_main.lua file. It is working fine with my environment. because i have manually given path_to_wireshark_folder = "C:\ProgramFiles\Wireshark" in my_plugin_main.lua</p><p>But Now, I need to generalize this plugin so that it can run in any person's machine and todo that i need the wireshark installation path where wireshark is installed into other person's enviornment.</p></div><div id="comment-43956-info" class="comment-info"><span class="comment-age">(07 Jul '15, 22:57)</span> ankit</div></div><span id="43957"></span><div id="comment-43957" class="comment"><div id="post-43957-score" class="comment-score"></div><div class="comment-text"><p>You shouldn't need to do that.</p><p>Are they <a href="http://lua-users.org/wiki/ModulesTutorial">Lua modules</a>? Or are they stand-alone scripts?</p><p>How are you loading your main Lua file? Through <code>dofile()</code>, or by having it in the personal plugins directory? Generally I recommend not using <code>dofile()</code>, and just putting your script in the personal plugins directory instead. That's where your new folder should be placed as well.</p></div><div id="comment-43957-info" class="comment-info"><span class="comment-age">(07 Jul '15, 23:39)</span> Hadriel</div></div><span id="43958"></span><div id="comment-43958" class="comment"><div id="post-43958-score" class="comment-score"></div><div class="comment-text"><p>it is foolish to ask but i am unable to use existing global functions.I tried to use as mentioned in below image and I am getting error like "attempt to index global 'Dir'(nil value) If something is wrong can anyone tell me how to use global functions?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_lua.png" /></p></div><div id="comment-43958-info" class="comment-info"><span class="comment-age">(08 Jul '15, 00:05)</span> ankit</div></div><span id="43963"></span><div id="comment-43963" class="comment"><div id="post-43963-score" class="comment-score"></div><div class="comment-text"><p>It's not a global function of Lua the language - it's a global function within Wireshark's Lua environment. So using ZeroBraneStudio to run the Lua script won't work.</p></div><div id="comment-43963-info" class="comment-info"><span class="comment-age">(08 Jul '15, 07:16)</span> Hadriel</div></div><span id="43973"></span><div id="comment-43973" class="comment"><div id="post-43973-score" class="comment-score"></div><div class="comment-text"><p>I suppose I should mention this requires running Wireshark 1.12.x or 1.99.x. The <code>Dir</code> stuff was added in 1.11.3, as mentioned in the API docs.</p></div><div id="comment-43973-info" class="comment-info"><span class="comment-age">(08 Jul '15, 09:48)</span> Hadriel</div></div><span id="43999"></span><div id="comment-43999" class="comment not_top_scorer"><div id="post-43999-score" class="comment-score"></div><div class="comment-text"><p>my main.lua file is under C:\ProgramFiles\Wireshark\plugin\1.12.6\ directory and my code is under C:\Programfiles\Wireshark\MYLUA ... under MYLUA folder there are some subfolder into which there are some lua scripts so to call this scripts from my_main.lua i did dofile(...)</p><p>and as you suggested for Dir.global_config_path() It is working fine. thanks @hadriel</p></div><div id="comment-43999-info" class="comment-info"><span class="comment-age">(09 Jul '15, 01:55)</span> ankit</div></div></div><div id="comment-tools-43954" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-43954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

