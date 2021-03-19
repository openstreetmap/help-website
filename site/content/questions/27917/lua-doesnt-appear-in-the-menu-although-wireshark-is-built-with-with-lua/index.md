+++
type = "question"
title = "Lua doesn&#x27;t appear in the menu although wireshark is built with --with-lua"
description = '''Hello, I&#x27;m quite new at wireshark and I have built wireshark from the source on my ubuntu 13.10 (64bits). All went fine, but when I start wireshark, I do not see the &quot;LUA&quot; support added into the menu. I have built wireshark 1.8.11 with &quot;--with-lua&quot;. Any idea why? Thanks in advance, /maghrebi'''
date = "2013-12-08T07:05:00Z"
lastmod = "2013-12-13T04:25:00Z"
weight = 27917
keywords = [ "lua" ]
aliases = [ "/questions/27917" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Lua doesn't appear in the menu although wireshark is built with --with-lua](/questions/27917/lua-doesnt-appear-in-the-menu-although-wireshark-is-built-with-with-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27917-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm quite new at wireshark and I have built wireshark from the source on my ubuntu 13.10 (64bits). All went fine, but when I start wireshark, I do not see the "LUA" support added into the menu. I have built wireshark 1.8.11 with "--with-lua".</p><p>Any idea why?</p><p>Thanks in advance, /maghrebi</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '13, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/dc7c50e244edf0016b0958a24924a90f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maghrebi&#39;s gravatar image" /><p>maghrebi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maghrebi has no accepted answers">0%</span></p></div></div><div id="comments-container-27917" class="comments-container"></div><div id="comment-tools-27917" class="comment-tools"></div><div class="clear"></div><div id="comment-27917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27922"></span>

<div id="answer-container-27922" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27922-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What is the output of</p><blockquote><p>grep LUA config.status</p></blockquote><p>It should look similar to this</p><pre><code>S[&quot;HAVE_LIBLUA_FALSE&quot;]=&quot;#&quot;
S[&quot;HAVE_LIBLUA_TRUE&quot;]=&quot;&quot;
S[&quot;LUA_INCLUDES&quot;]=&quot;-I/usr/include/lua5.1&quot;
S[&quot;LUA_LIBS&quot;]=&quot; -llua5.1 -lm&quot;
D[&quot;HAVE_LUA5_1_LUA_H&quot;]=&quot; 1&quot;
D[&quot;HAVE_LUA5_1_LUALIB_H&quot;]=&quot; 1&quot;
D[&quot;HAVE_LUA5_1_LAUXLIB_H&quot;]=&quot; 1&quot;
D[&quot;HAVE_LUA5_1_LUA_H&quot;]=&quot; 1&quot;
D[&quot;HAVE_LUA5_1_LUALIB_H&quot;]=&quot; 1&quot;
D[&quot;HAVE_LUA5_1_LAUXLIB_H&quot;]=&quot; 1&quot;
D[&quot;HAVE_LUA5_1_LUA_H&quot;]=&quot; 1&quot;
D[&quot;HAVE_LUA5_1_LUALIB_H&quot;]=&quot; 1&quot;
D[&quot;HAVE_LUA5_1_LAUXLIB_H&quot;]=&quot; 1&quot;
D[&quot;HAVE_LUA&quot;]=&quot; 1&quot;</code></pre><p>If it does not, you probably did not install the Lua development package.</p><blockquote><p>apt-get install liblua5.1-0-dev</p></blockquote><p>'liblua5.1-0-dev' might be named differently on Ubuntu 13.10. In that case, try to find it with "apt-cache search".</p><p>BTW: What is the output of</p><blockquote><p>wireshark -v<br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '13, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-27922" class="comments-container"><span id="27997"></span><div id="comment-27997" class="comment"><div id="post-27997-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>Thanks Kurt for the quick feedback. The version I have is shown below:</p><p>=======================================================================================</p><p>wireshark 1.8.11 (SVN Rev Unknown from unknown)</p><p>Copyright 1998-2013 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GTK+ 2.24.20, with Cairo 1.12.16, with Pango 1.32.5, with GLib 2.38.1, with libpcap, with libz 1.2.8, without POSIX capabilities, without SMI, without c-ares, without ADNS, with Lua 5.1, with Python 2.7.5+, without GnuTLS, without Gcrypt, without Kerberos, without GeoIP, without PortAudio, with AirPcap.</p><p>Running on Linux 3.11.0-14-generic, with locale en_US.UTF-8, with libpcap version 1.4.0, with libz 1.2.8, without AirPcap.</p><p>Built using gcc 4.8.1.</p><p>=======================================================================================</p><p>I also checked and I have liblua5.1.0-dev installed.</p><p>When doing "grep LUA config.status, I get the following which looks like yours:</p><p>===================================================<br />
</p><p>S["HAVE_LIBLUA_FALSE"]="#" S["HAVE_LIBLUA_TRUE"]="" S["LUA_INCLUDES"]="-I/usr/include/lua5.1" S["LUA_LIBS"]=" -llua5.1 -lm" D["HAVE_LUA5_1_LUA_H"]=" 1" D["HAVE_LUA5_1_LUALIB_H"]=" 1" D["HAVE_LUA5_1_LAUXLIB_H"]=" 1" D["HAVE_LUA5_1_LUA_H"]=" 1" D["HAVE_LUA5_1_LUALIB_H"]=" 1" D["HAVE_LUA5_1_LAUXLIB_H"]=" 1" D["HAVE_LUA5_1_LUA_H"]=" 1" D["HAVE_LUA5_1_LUALIB_H"]=" 1" D["HAVE_LUA5_1_LAUXLIB_H"]=" 1" D["HAVE_LUA_5_1"]=" 1"</p><p>===================================================<br />
</p><p>I'm not sure what could be the problem.</p><p>Any more things to check?</p><p>Best regards, Maghrebi</p></div><div id="comment-27997-info" class="comment-info"><span class="comment-age">(11 Dec '13, 04:44)</span> maghrebi</div></div><span id="27998"></span><div id="comment-27998" class="comment"><div id="post-27998-score" class="comment-score"></div><div class="comment-text"><p>O.K. your binary is built with Lua support.</p><p>So, what exactly is missing in the GUI?</p><p>Besides the menu</p><blockquote><p>Tools -&gt; Lua</p></blockquote><p>there is no other menu item for Lua. Do you see Tools -&gt; Lua ?</p></div><div id="comment-27998-info" class="comment-info"><span class="comment-age">(11 Dec '13, 04:48)</span> Kurt Knochner ♦</div></div><span id="28008"></span><div id="comment-28008" class="comment"><div id="post-28008-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>That is the problem. Under Tools-&gt; I do not see Lua.</p><p>Best regards,</p></div><div id="comment-28008-info" class="comment-info"><span class="comment-age">(11 Dec '13, 09:27)</span> maghrebi</div></div><span id="28011"></span><div id="comment-28011" class="comment"><div id="post-28011-score" class="comment-score"></div><div class="comment-text"><p>O.K., strange... what happens if you compile 1.10.x vor 1.11.x??</p></div><div id="comment-28011-info" class="comment-info"><span class="comment-age">(11 Dec '13, 09:53)</span> Kurt Knochner ♦</div></div><span id="28014"></span><div id="comment-28014" class="comment"><div id="post-28014-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>I just built 1.11.2 and I still cannot see Tools-&gt; Lua.</p><p>It seems very strange.</p><p>Best regards</p></div><div id="comment-28014-info" class="comment-info"><span class="comment-age">(11 Dec '13, 11:01)</span> maghrebi</div></div><span id="28015"></span><div id="comment-28015" class="comment not_top_scorer"><div id="post-28015-score" class="comment-score"></div><div class="comment-text"><p>Can you please post a screenshot with the opened Tools menu?</p></div><div id="comment-28015-info" class="comment-info"><span class="comment-age">(11 Dec '13, 11:24)</span> Kurt Knochner ♦</div></div><span id="28021"></span><div id="comment-28021" class="comment not_top_scorer"><div id="post-28021-score" class="comment-score"></div><div class="comment-text"><p>BTW: Just an idea: are you starting an older (or different) version of Wireshark unintentionally, instead of your own build? Please check: <strong><code>Help -&gt; About</code></strong> in GUI were <code>Tools -&gt; Lua</code> is missing.</p></div><div id="comment-28021-info" class="comment-info"><span class="comment-age">(11 Dec '13, 13:19)</span> Kurt Knochner ♦</div></div><span id="28067"></span><div id="comment-28067" class="comment not_top_scorer"><div id="post-28067-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>I made sure that I start wireshark from my build (./wireshark). I have taken a screenshot for Tools. There seems to be nothing there. Also, if I check what my wireshark has, it says with Lua5.2</p><p>============================================================================</p><p>Compiled (64-bit) with GTK+ 3.8.6, with Cairo 1.12.16, with Pango 1.32.5, with GLib 2.38.1, with libpcap, with libz 1.2.8, without POSIX capabilities, without libnl, without SMI, without c-ares, without ADNS, with Lua 5.2, without Python, without GnuTLS, without Gcrypt, without Kerberos, without GeoIP, without PortAudio, with AirPcap.</p><p>============================================================================</p><p>This last trial was done on a freshly new build dir.</p><p>Best regards, Chafik</p></div><div id="comment-28067-info" class="comment-info"><span class="comment-age">(12 Dec '13, 23:24)</span> maghrebi</div></div><span id="28074"></span><div id="comment-28074" class="comment not_top_scorer"><div id="post-28074-score" class="comment-score"></div><div class="comment-text"><p>see my other answer for the solution.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-28074-info" class="comment-info"><span class="comment-age">(13 Dec '13, 04:26)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27922" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-27922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28073"></span>

<div id="answer-container-28073" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28073-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I made sure that I start wireshark from my build (./wireshark)</p></blockquote><p>O.K. I've found the problem. <code>init.lua</code> will <strong>not</strong> be loaded if you start Wireshark from the build directory, even if you run Wireshark with the following environment variable set</p><blockquote><p>WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1 ./wireshark</p></blockquote><p>Within <code>init.lua</code> the file <code>console.lua</code> gets called, which does the menu registration</p><pre><code>    register_menu(&quot;Lua/Evaluate&quot;, evaluate_lua, MENU_TOOLS_UNSORTED)
    register_menu(&quot;Lua/Console&quot;, run_console, MENU_TOOLS_UNSORTED)
    register_menu(&quot;Lua/Manual&quot;, ref_manual, MENU_TOOLS_UNSORTED)
    register_menu(&quot;Lua/Wiki&quot;, wiki_page, MENU_TOOLS_UNSORTED)</code></pre><p>If you install Wireshark (make install) everything will work as expected.</p><p>Hint: I had to run the following command, because <code>libwiretap</code> was not found after <code>make install</code>.</p><blockquote><p>sudo ldconfig</p></blockquote><p>I'm not sure if there is an easy way to run Wireshark from the build directory, <strong>including</strong> the Lua initialization.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '13, 04:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Dec '13, 06:49</p></div></div><div id="comments-container-28073" class="comments-container"><span id="28271"></span><div id="comment-28271" class="comment"><div id="post-28271-score" class="comment-score"></div><div class="comment-text"><p>Hello Kurt,</p><p>I tried several times the following but still no success in getting the Lua to show up in Tools:</p><p>./configure --with-lua make sudo make install</p><p>Best regards,</p></div><div id="comment-28271-info" class="comment-info"><span class="comment-age">(18 Dec '13, 12:29)</span> maghrebi</div></div><span id="28275"></span><div id="comment-28275" class="comment"><div id="post-28275-score" class="comment-score"></div><div class="comment-text"><p>How did you start Wireshark after 'make install'?</p></div><div id="comment-28275-info" class="comment-info"><span class="comment-age">(18 Dec '13, 13:43)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28073" class="comment-tools"></div><div class="clear"></div><div id="comment-28073-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

