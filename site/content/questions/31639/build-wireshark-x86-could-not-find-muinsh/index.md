+++
type = "question"
title = "build wireshark x86 could not find: &quot;MUI.nsh&quot;"
description = '''Processing config: D:&#92;Program Files (x86)&#92;NSIS&#92;nsisconf.nsh Processing script file: &quot;uninstall.nsi&quot; (ACP) !include: could not find: &quot;MUI.nsh&quot; Error in script &quot;uninstall.nsi&quot; on line 22 -- aborting creation process NMAKE : fatal error U1077: &#x27;&quot;D:&#92;Program Files (x86)&#92;NSIS&#92;makensis.exe&quot;&#x27; : return  code...'''
date = "2014-04-08T08:25:00Z"
lastmod = "2014-04-08T09:48:00Z"
weight = 31639
keywords = [ "packaging", "x86", "vs2010", "makensis" ]
aliases = [ "/questions/31639" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [build wireshark x86 could not find: "MUI.nsh"](/questions/31639/build-wireshark-x86-could-not-find-muinsh)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31639-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>Processing config: D:\Program Files (x86)\NSIS\nsisconf.nsh
Processing script file: &quot;uninstall.nsi&quot; (ACP)
!include: could not find: &quot;MUI.nsh&quot;
Error in script &quot;uninstall.nsi&quot; on line 22 -- aborting creation process
NMAKE : fatal error U1077: &#39;&quot;D:\Program Files (x86)\NSIS\makensis.exe&quot;&#39; : return
 code &#39;0x1&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;d:\Program Files (x86)\Microsoft Visual Studio 10.0
\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre></div><div id="question-tags" class="tags-container tags">packaging x86 vs2010 makensis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '14, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/44eba4990d2ff634f98b026710105530?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chennqqi&#39;s gravatar image" /><p>chennqqi<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chennqqi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Apr '14, 09:15</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-31639" class="comments-container"></div><div id="comment-tools-31639" class="comment-tools"></div><div class="clear"></div><div id="comment-31639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31641"></span>

<div id="answer-container-31641" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31641-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>On my build machine, that file lives in the NSIS\Include directory. What version are you building, and is it from git or svn or a zip?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '14, 09:48</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-31641" class="comments-container"><span id="31788"></span><div id="comment-31788" class="comment"><div id="post-31788-score" class="comment-score"></div><div class="comment-text"><p>My OS is Win7 x64. My NSIS version is 3.0a2, location: D:\Program Files (x86)\NSIS</p><p>dir show: D:\Program Files (x86)\NSIS\Include 的目录</p><p>2014/04/05 23:11</p><dir>. 2014/04/05 23:11<dir>.. 2007/12/01 19:43 1,858 Colors.nsh 2013/09/07 07:48 40,502 FileFunc.nsh 2013/03/15 06:04 4,838 InstallOptions.nsh 2013/03/16 08:28 4,441 LangFile.nsh 2008/12/20 19:55 20,797 Library.nsh 2010/03/27 01:18 30,139 LogicLib.nsh 2008/03/17 03:42 10,627 Memento.nsh 2013/05/18 03:31 13,354 MultiUser.nsh 2010/05/01 04:17 6,670 Sections.nsh 2013/09/07 07:48 48,146 StrFunc.nsh 2013/09/07 07:48 24,348 TextFunc.nsh 2007/12/01 19:43 4,993 UpgradeDLL.nsh 2008/11/21 09:12 1,750 Util.nsh 2013/05/18 03:31 3,464 VB6RunTime.nsh 2014/04/05 23:11<dir>Win 2013/03/11 07:28 8,948 WinCore.nsh 2012/10/16 17:43 28,718 WinMessages.nsh 2013/09/03 05:19 14,999 WinVer.nsh 2012/09/17 20:37 43,576 WordFunc.nsh 2013/09/07 07:48 1,358 x64.nsh</dir></dir></dir></div><div id="comment-31788-info" class="comment-info"><span class="comment-age">(14 Apr '14, 05:47)</span> chennqqi</div></div><span id="31789"></span><div id="comment-31789" class="comment"><div id="post-31789-score" class="comment-score"></div><div class="comment-text"><p>I switch NSIS version from 3.0a to 2.63. This problem solved.Thank you very much!</p></div><div id="comment-31789-info" class="comment-info"><span class="comment-age">(14 Apr '14, 06:09)</span> chennqqi</div></div></div><div id="comment-tools-31641" class="comment-tools"></div><div class="clear"></div><div id="comment-31641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

