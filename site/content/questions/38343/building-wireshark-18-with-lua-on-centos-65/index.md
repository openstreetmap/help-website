+++
type = "question"
title = "Building Wireshark 1.8 with Lua on CentOS 6.5"
description = '''I successfully installed GTK2. &quot;sudo ./configure --with-lua --with-gtk2&quot; got further than before but ended with &quot;configure: error: Header file lua.h not found.&quot;. I downloaded, and unpacked, lua-5.2.3.tar.gz and tried &quot;make linux&quot;. This resulted in &quot;lua.c:297: warning: implicit declaration of functio...'''
date = "2014-12-04T18:45:00Z"
lastmod = "2014-12-05T07:52:00Z"
weight = 38343
keywords = [ "lua", "build", "centos" ]
aliases = [ "/questions/38343" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Building Wireshark 1.8 with Lua on CentOS 6.5](/questions/38343/building-wireshark-18-with-lua-on-centos-65)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38343-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I successfully installed GTK2. "sudo ./configure --with-lua --with-gtk2" got further than before but ended with "configure: error: Header file lua.h not found.". I downloaded, and unpacked, lua-5.2.3.tar.gz and tried "make linux". This resulted in "lua.c:297: warning: implicit declaration of function ‘add_history’" Despite the "warning", the effect was a fatal error (stopped compiling). Thanks,</p><p>Update. The following is lua related output from configure.log</p><pre><code> cat config.log | grep lua
   $ ./configure --with-lua --with-gtk2
 PATH: /home/OtagoHarbour/Downloads/lua-5.2.3/src
 conftest.c:39: error: logical &#39;&amp;&amp;&#39; with non-zero constant will always evaluate as true
 configure:33563: checking whether to use liblua for the Lua scripting plugin
 configure:33657: checking lua.h usability
 /usr/include/lua.h:16:21: error: luaconf.h: No such file or directory
 /usr/include/lua.h:103: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before                &#39;lua_Number&#39;
 /usr/include/lua.h:107: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before           &#39;lua_Integer&#39;     
 /usr/include/lua.h:110: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before                &#39;lua_Unsigned&#39;
 /usr/include/lua.h:131: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before                &#39;lua_State&#39;
 /usr/include/lua.h:132: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:133: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before                &#39;lua_State&#39;
 /usr/include/lua.h:135: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before                &#39;lua_CFunction&#39;
 /usr/include/lua.h:138: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;const&#39;
 /usr/include/lua.h:144: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:145: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:146: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:147: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:148: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:149: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:150: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:151: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:152: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:154: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:161: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:162: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:163: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:164: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:165: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:166: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;const&#39;
 /usr/include/lua.h:168: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;lua_Number&#39;
 /usr/include/lua.h:169: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before                &#39;lua_Integer&#39;
 /usr/include/lua.h:170: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before                &#39;lua_Unsigned&#39;
 /usr/include/lua.h:171: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:172: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;const&#39;
 /usr/include/lua.h:173: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;size_t&#39;
 /usr/include/lua.h:174: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before                &#39;lua_CFunction&#39;
 /usr/include/lua.h:175: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:176: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before                &#39;lua_State&#39;
 /usr/include/lua.h:177: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;const&#39;
 /usr/include/lua.h:192: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:198: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:199: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:205: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:206: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:207: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:208: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:209: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;const&#39;
 /usr/include/lua.h:210: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;const&#39;
 /usr/include/lua.h:211: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;const&#39;
 /usr/include/lua.h:213: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;const&#39;
 /usr/include/lua.h:214: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:215: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:216: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:217: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:223: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:224: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:225: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:226: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:227: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:228: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:229: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:230: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:231: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:232: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:238: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
   /usr/     include/lua.h:239: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:240: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:241: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:242: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:243: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:244: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:245: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:251: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:255: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:257: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:261: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:265: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:271: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:274: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:275: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:294: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:301: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:303: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:305: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:306: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:308: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before                &#39;lua_Alloc&#39;
 /usr/include/lua.h:309: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:382: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:383: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:384: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;const&#39;
 /usr/include/lua.h:385: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;const&#39;
 /usr/include/lua.h:386: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;const&#39;
 /usr/include/lua.h:387: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;const&#39;
 /usr/include/lua.h:389: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:390: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;void&#39;
 /usr/include/lua.h:393: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:394: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;lua_Hook&#39;
 /usr/include/lua.h:395: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:396: error: expected &#39;=&#39;, &#39;,&#39;, &#39;;&#39;, &#39;asm&#39; or &#39;__attribute__&#39; before &#39;int&#39;
 /usr/include/lua.h:412: error: &#39;LUA_IDSIZE&#39; undeclared here (not in a function)
 | #include &lt;lua.h&gt;
 configure:33657: checking lua.h presence
 /usr/include/lua.h:16:21: error: luaconf.h: No such file or directory
 | #include &lt;lua.h&gt;
 configure:33657: checking for lua.h
 configure:33668: checking lua5.2/lua.h usability
 conftest.c:88:24: error: lua5.2/lua.h: No such file or directory
 | #include &lt;lua5.2/lua.h&gt;
 configure:33668: checking lua5.2/lua.h presence
 conftest.c:55:24: error: lua5.2/lua.h: No such file or directory
 | #include &lt;lua5.2/lua.h&gt;
 configure:33668: checking for lua5.2/lua.h
 configure:33762: error: Header file lua.h not found.
 ac_cv_header_lua5_2_lua_h=no
 ac_cv_header_lua_h=no
 CONFIG_ARGS=&#39;--with-lua --with-gtk2&#39;</code></pre></div><div id="question-tags" class="tags-container tags">lua build centos</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '14, 18:45</strong></p><img src="https://secure.gravatar.com/avatar/87ec0ce8ac23df0e004db289a8677a34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OtagoHarbour&#39;s gravatar image" /><p>OtagoHarbour<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OtagoHarbour has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Dec '14, 18:28</p></div></div><div id="comments-container-38343" class="comments-container"></div><div id="comment-tools-38343" class="comment-tools"></div><div class="clear"></div><div id="comment-38343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38365"></span>

<div id="answer-container-38365" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38365-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>2 suggestions:</p><ol><li>Don't try to build Wireshark 1.8, build Wireshark 1.12.2 (it's the latest release).</li><li>Don't compile Lua, just <code>yum install lua-devel</code> (as root). That will install the necessary header files and libraries.</li></ol><p>(Anyway, problems compiling Lua shouldn't be reported here.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '14, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Dec '14, 08:17</p></div></div><div id="comments-container-38365" class="comments-container"><span id="38457"></span><div id="comment-38457" class="comment"><div id="post-38457-score" class="comment-score"></div><div class="comment-text"><p>I unpacked wireshark-1.12.2.tar.bz2 and tried "sudo ./configure --with-lua --with-gtk2" in wireshark-1.12.2. It still ends with "configure: error: Header file lua.h not found" although lua.h is in the search path. This seems like a wireshark installation issue. Thanks,</p></div><div id="comment-38457-info" class="comment-info"><span class="comment-age">(08 Dec '14, 18:03)</span> OtagoHarbour</div></div><span id="38458"></span><div id="comment-38458" class="comment"><div id="post-38458-score" class="comment-score"></div><div class="comment-text"><p>You did <code>yum install lua-devel</code> before you tried to run <code>sudo ./configure --with-lua --with-gtk2</code>, right?</p><p>If not, do <code>yum install lua-devel</code>, to make sure you <em>have</em> the necessary header files and libraries.</p><p>And, in either case, <em>don't</em> run the configure script with <code>sudo</code> - unless your system is badly set up, you should not need root privileges to run the configure script or compile anything.</p></div><div id="comment-38458-info" class="comment-info"><span class="comment-age">(08 Dec '14, 20:18)</span> Guy Harris ♦♦</div></div><span id="38505"></span><div id="comment-38505" class="comment"><div id="post-38505-score" class="comment-score"></div><div class="comment-text"><p>I did "sudo yum install lua-devel". Without the sudo, I get "You need to be root to perform this command.". "./configure --with-lua --with-gtk2" still ends with "configure: error: Header file lua.h not found." Thanks,</p></div><div id="comment-38505-info" class="comment-info"><span class="comment-age">(09 Dec '14, 19:55)</span> OtagoHarbour</div></div><span id="38506"></span><div id="comment-38506" class="comment"><div id="post-38506-score" class="comment-score"></div><div class="comment-text"><p>Why are you doing the yum install without the sudo? You need to do it as root or with sudo (effectively as root).</p></div><div id="comment-38506-info" class="comment-info"><span class="comment-age">(09 Dec '14, 21:19)</span> Quadratic</div></div><span id="38508"></span><div id="comment-38508" class="comment"><div id="post-38508-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Why are you doing the yum install without the sudo?</p></blockquote><p>Probably because the original answer didn't have the sudo. I added it to the answer.</p></div><div id="comment-38508-info" class="comment-info"><span class="comment-age">(10 Dec '14, 00:56)</span> Guy Harris ♦♦</div></div><span id="38509"></span><div id="comment-38509" class="comment not_top_scorer"><div id="post-38509-score" class="comment-score"></div><div class="comment-text"><blockquote><p>"./configure --with-lua --with-gtk2" still ends with "configure: error: Header file lua.h not found."</p></blockquote><p>What does <code>ls -l /usr/include/lua.h</code> print? If it reports that it exists, look at the file <code>config.log</code> in the Wireshark source directory, look for "lua", and report all the output that concerns Lua.</p></div><div id="comment-38509-info" class="comment-info"><span class="comment-age">(10 Dec '14, 00:58)</span> Guy Harris ♦♦</div></div><span id="38547"></span><div id="comment-38547" class="comment not_top_scorer"><div id="post-38547-score" class="comment-score"></div><div class="comment-text"><p>Sorry about my slow reply. lua.h was not in /usr/include but I copied it there. "./configure --with-lua --with-gtk2" still ends with "configure: error: Header file lua.h not found." The lua related out from config.log was to voluminous for a comment so I put it as an addendum to the question. Thanks,</p></div><div id="comment-38547-info" class="comment-info"><span class="comment-age">(12 Dec '14, 18:25)</span> OtagoHarbour</div></div><span id="38548"></span><div id="comment-38548" class="comment not_top_scorer"><div id="post-38548-score" class="comment-score"></div><div class="comment-text"><blockquote><p>lua.h was not in /usr/include</p></blockquote><p>Where was it? <code>/usr/include/lua5.1</code>, or <code>/usr/include/lua5.2</code>, or some directory such as that?</p></div><div id="comment-38548-info" class="comment-info"><span class="comment-age">(12 Dec '14, 19:35)</span> Guy Harris ♦♦</div></div><span id="38563"></span><div id="comment-38563" class="comment not_top_scorer"><div id="post-38563-score" class="comment-score"></div><div class="comment-text"><p>My apologies! I did not notice that "sudo yum install lua-devel" had not finished running. I made sure it had finished and my problem with the wireshark installation went away. Thanks,</p></div><div id="comment-38563-info" class="comment-info"><span class="comment-age">(14 Dec '14, 16:41)</span> OtagoHarbour</div></div></div><div id="comment-tools-38365" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-38365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

