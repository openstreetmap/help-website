+++
type = "question"
title = "Error on Packaging File: failed opening file &quot;..&#92;..&#92;wireshark-gtk2&#92;COPYING.txt&quot;"
description = '''Command line defined: &quot;LUA_DIR=C:&#92;Wireshark-win32-libs-1.12&#92;lua5.2.3&quot; Command line defined: &quot;SMI_DIR=C:&#92;Wireshark-win32-libs-1.12&#92;libsmi-svn-40773-win32ws&quot; Command line defined: &quot;GEOIP_DIR=C:&#92;Wireshark-win32-libs-1.12&#92;GeoIP-1.5.1-2-win32ws&quot; Command line defined: &quot;WINSPARKLE_DIR=C:&#92;Wireshark-win32-li...'''
date = "2017-03-20T05:00:00Z"
lastmod = "2017-03-20T05:32:00Z"
weight = 60191
keywords = [ "packaging", "nsis", "build", "wireshark" ]
aliases = [ "/questions/60191" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error on Packaging File: failed opening file "..\\..\\wireshark-gtk2\\COPYING.txt"](/questions/60191/error-on-packaging-file-failed-opening-file-wireshark-gtk2copyingtxt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60191-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>Command line defined: &quot;LUA_DIR=C:\Wireshark-win32-libs-1.12\lua5.2.3&quot;
Command line defined: &quot;SMI_DIR=C:\Wireshark-win32-libs-1.12\libsmi-svn-40773-win32ws&quot;
Command line defined: &quot;GEOIP_DIR=C:\Wireshark-win32-libs-1.12\GeoIP-1.5.1-2-win32ws&quot;
Command line defined: &quot;WINSPARKLE_DIR=C:\Wireshark-win32-libs-1.12\WinSparkle-0.3-44-g2c8d9d3-win32ws&quot;
Command line defined: &quot;HHC_DIR=C:\Program Files (x86)\HTML Help Workshop&quot;
Processing config: C:\Program Files (x86)\NSIS\nsisconf.nsh
Processing script file: &quot;wireshark.nsi&quot; (ACP)
File: failed opening file &quot;..\..\wireshark-gtk2\COPYING.txt&quot;
Error in script &quot;wireshark.nsi&quot; on line 386 -- aborting creation process
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\NSIS\makensis.exe&quot;&#39; : return code &#39;0x1&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre></div><div id="question-tags" class="tags-container tags">packaging nsis build wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '17, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/600778689935688cd4eaaa966e880cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DhanuShalz&#39;s gravatar image" /><p>DhanuShalz<br />
<span class="score" title="36 reputation points">36</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DhanuShalz has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Mar '17, 05:31</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-60191" class="comments-container"></div><div id="comment-tools-60191" class="comment-tools"></div><div class="clear"></div><div id="comment-60191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60192"></span>

<div id="answer-container-60192" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60192-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As a totally plucked from the air guess I suspect that the file <code>wireshark-gtk2\COPYING.txt</code> is missing:</p><blockquote><p>File: failed opening file "..\..\wireshark-gtk2\COPYING.txt"</p></blockquote></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '17, 05:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Mar '17, 05:58</p></div></div><div id="comments-container-60192" class="comments-container"><span id="60193"></span><div id="comment-60193" class="comment"><div id="post-60193-score" class="comment-score"></div><div class="comment-text"><p>@grahamb The File do exists, i have checked it</p></div><div id="comment-60193-info" class="comment-info"><span class="comment-age">(20 Mar '17, 05:53)</span> DhanuShalz</div></div><span id="60194"></span><div id="comment-60194" class="comment"><div id="post-60194-score" class="comment-score"></div><div class="comment-text"><p>Are you sure the file exists in the place that nsis is expecting to find it? Note the nsis path is <code>..\..\wireshark-gtk2\COPYING.txt</code>.</p></div><div id="comment-60194-info" class="comment-info"><span class="comment-age">(20 Mar '17, 06:17)</span> grahamb ♦</div></div><span id="60195"></span><div id="comment-60195" class="comment"><div id="post-60195-score" class="comment-score"></div><div class="comment-text"><p>its in the exact path as .. \ ..\wireshark-gtk2\COPYING.txt @grahamb</p><p>when try to manually open the COPYING.txt its shows Access denied, inspite of having the adminstrator access</p></div><div id="comment-60195-info" class="comment-info"><span class="comment-age">(20 Mar '17, 06:28)</span> DhanuShalz</div></div><span id="60199"></span><div id="comment-60199" class="comment"><div id="post-60199-score" class="comment-score"></div><div class="comment-text"><p>Try changing the security on the file, maybe taking ownership for your own account.</p></div><div id="comment-60199-info" class="comment-info"><span class="comment-age">(20 Mar '17, 07:20)</span> grahamb ♦</div></div><span id="60202"></span><div id="comment-60202" class="comment"><div id="post-60202-score" class="comment-score"></div><div class="comment-text"><p>it didn't workout....! @grahamb</p></div><div id="comment-60202-info" class="comment-info"><span class="comment-age">(20 Mar '17, 08:07)</span> DhanuShalz</div></div></div><div id="comment-tools-60192" class="comment-tools"></div><div class="clear"></div><div id="comment-60192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

