+++
type = "question"
title = "stdint.h error on building wireshark 1.12.6"
description = '''ERROR in Stdint.h  c:&#92;Program Files (x86)&#92;Microsoft Visual Studio 9.0&#92;VC&#92;INCLUDE&#92;stdint.h(1) : error C2018: unknown character &#x27;0x12&#x27; c:&#92;Program Files (x86)&#92;Microsoft Visual Studio 9.0&#92;VC&#92;INCLUDE&#92;stdint.h(1) : error C2018: unknown character &#x27;0x2&#x27; c:&#92;Program Files (x86)&#92;Microsoft Visual Studio 9.0&#92;VC&#92;...'''
date = "2017-03-17T03:19:00Z"
lastmod = "2017-03-17T03:54:00Z"
weight = 60141
keywords = [ "1.12.6", "stdint.h" ]
aliases = [ "/questions/60141" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [stdint.h error on building wireshark 1.12.6](/questions/60141/stdinth-error-on-building-wireshark-1126)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60141-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>ERROR in Stdint.h

c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2018: unknown character &#39;0x12&#39;
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2018: unknown character &#39;0x2&#39;
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2061: syntax error : identifier &#39;stdint&#39;
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2059: syntax error : &#39;;&#39;
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2059: syntax error : &#39;.&#39;
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2017: illegal escape sequence
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2017: illegal escape sequence
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2017: illegal escape sequence
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2017: illegal escape sequence
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2017: illegal escape sequence
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2018: unknown character &#39;0x3&#39;
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2017: illegal escape sequence
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2017: illegal escape sequence
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2017: illegal escape sequence
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2017: illegal escape sequence
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2017: illegal escape sequence
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2017: illegal escape sequence
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(1) : error C2018: unknown character &#39;0x10&#39;
c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\INCLUDE\stdint.h(143) : fatal error C1071: unexpected end of file found in comment
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\cl.EXE&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre></div><div id="question-tags" class="tags-container tags">1.12.6 stdint.h</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '17, 03:19</strong></p><img src="https://secure.gravatar.com/avatar/600778689935688cd4eaaa966e880cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DhanuShalz&#39;s gravatar image" /><p>DhanuShalz<br />
<span class="score" title="36 reputation points">36</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DhanuShalz has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Mar '17, 04:46</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-60141" class="comments-container"><span id="60142"></span><div id="comment-60142" class="comment"><div id="post-60142-score" class="comment-score">1</div><div class="comment-text"><p>What version of Wireshark are you attempting to build?</p></div><div id="comment-60142-info" class="comment-info"><span class="comment-age">(17 Mar '17, 03:47)</span> grahamb ♦</div></div><span id="60143"></span><div id="comment-60143" class="comment"><div id="post-60143-score" class="comment-score"></div><div class="comment-text"><p>wireshark 1.12.6</p></div><div id="comment-60143-info" class="comment-info"><span class="comment-age">(17 Mar '17, 03:52)</span> DhanuShalz</div></div></div><div id="comment-tools-60141" class="comment-tools"></div><div class="clear"></div><div id="comment-60141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60144"></span>

<div id="answer-container-60144" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60144-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Microsoft Visual Studio 9.0</p></blockquote><p>Is that Visual Studio 2008?</p><p>If so, we haven't use VS 2008 to build Wireshark releases since Wireshark 1.6. <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChToolsMSChain.html">The Windows toolchain page in the Developer's Guide</a> only talks about VS 2010 and later. There's no guarantee that current versions of Wireshark will build on VS 2008 - and there's no guarantee that, if you take some random version of <code>stdint.h</code> and install it, it will work with VS 2008.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '17, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-60144" class="comments-container"><span id="60145"></span><div id="comment-60145" class="comment"><div id="post-60145-score" class="comment-score"></div><div class="comment-text"><p>Thanks, That worked but very further it throught the error</p><p>packet-ipmi-app.c packet-ipmi-bridge.c packet-ipmi-chassis.c packet-ipmi-picmg.c packet-ipmi-se.c packet-ipmi-storage.c packet-ipmi-transport.c packet-ipmi-pps.c packet-ipmi-update.c packet-ipmi-vita.c packet-dcerpc-nt.c usb.c NMAKE : fatal error U1077: '"c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\cl.EXE"' : return code '0x2' Stop. NMAKE : fatal error U1077: '"c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe"' : return code '0x2' Stop. NMAKE : fatal error U1077: '"c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe"' : return code '0x2' Stop.</p></div><div id="comment-60145-info" class="comment-info"><span class="comment-age">(17 Mar '17, 04:30)</span> DhanuShalz</div></div><span id="60146"></span><div id="comment-60146" class="comment"><div id="post-60146-score" class="comment-score"></div><div class="comment-text"><p>The "official" build toolchain for 1.12.6 is Visual Studio 2010.</p></div><div id="comment-60146-info" class="comment-info"><span class="comment-age">(17 Mar '17, 04:45)</span> grahamb ♦</div></div><span id="60147"></span><div id="comment-60147" class="comment"><div id="post-60147-score" class="comment-score"></div><div class="comment-text"><p>the same was working for the VS2008</p></div><div id="comment-60147-info" class="comment-info"><span class="comment-age">(17 Mar '17, 04:50)</span> DhanuShalz</div></div><span id="60148"></span><div id="comment-60148" class="comment"><div id="post-60148-score" class="comment-score"></div><div class="comment-text"><p>packet-frame.c file-file.c C:\Aravind\Project\SVN\CalyposoGeneralTools\trunk\Wireshark_Plugin\WSI_Simple\epan\color_filters.h(40) : error C2371: 'color_t' : redefinition; different basic types C:\Aravind\Project\SVN\CalyposoGeneralTools\trunk\Wireshark_Plugin\WSI_Simple\color.h(44) : see declaration of 'color_t' C:\Aravind\Project\SVN\CalyposoGeneralTools\trunk\Wireshark_Plugin\WSI_Simple\epan\color_filters.h(40) : error C2371: 'color_t' : redefinition; different basic types C:\Aravind\Project\SVN\CalyposoGeneralTools\trunk\Wireshark_Plugin\WSI_Simple\color.h(44) : see declaration of 'color_t' NMAKE : fatal error U1077: '"c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\cl.EXE"' : return code '0x2' Stop. NMAKE : fatal error U1077: '"c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe"' : return code '0x2' Stop. NMAKE : fatal error U1077: '"c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe"' : return code '0x2' Stop.</p></div><div id="comment-60148-info" class="comment-info"><span class="comment-age">(17 Mar '17, 04:51)</span> DhanuShalz</div></div><span id="60149"></span><div id="comment-60149" class="comment"><div id="post-60149-score" class="comment-score"></div><div class="comment-text"><p>The official builds were made with VS 2010 SP1 and 1.12 is now out of support so you're pretty much on your own, especially if trying to persist with VS 2008 which was last officially used for 1.6.</p></div><div id="comment-60149-info" class="comment-info"><span class="comment-age">(17 Mar '17, 04:55)</span> grahamb ♦</div></div><span id="60150"></span><div id="comment-60150" class="comment not_top_scorer"><div id="post-60150-score" class="comment-score"></div><div class="comment-text"><p>epan\color_filters.h(40) : error C2371: 'color_t' : redefinition; different basic types _Simple\color.h(44) : see declaration of 'color_t' epan\color_filters.h(40) : error C2371: 'color_t' : redefinition; different basic types _Simple\color.h(44) : see declaration of 'color_t'</p><p>ANY INPUT ON THIS PARTICULAR ERROR</p></div><div id="comment-60150-info" class="comment-info"><span class="comment-age">(17 Mar '17, 04:58)</span> DhanuShalz</div></div><span id="60154"></span><div id="comment-60154" class="comment not_top_scorer"><div id="post-60154-score" class="comment-score"></div><div class="comment-text"><p>You seem to have a proprietary file color.h that uses a structure named color_t like the one provided by Wireshark (in epan\color_filters.h) but with a different content. You need to modify your code to avoid this error (either rename the structure, or ensure they are defined the same way. As we do not have access to your local modifications, you are on your own here.</p></div><div id="comment-60154-info" class="comment-info"><span class="comment-age">(17 Mar '17, 08:00)</span> Pascal Quantin</div></div></div><div id="comment-tools-60144" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-60144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

