+++
type = "question"
title = "Failed to Build Wireshark due to Microsoft Resource File To COFF Object Conversion Utility has stopped working"
description = '''When I run &quot;nmake -f Makefile.nmake all&quot; to build Wireshark for the very first time I got a pop-up from Windows saying &quot;Microsoft Resource File To COFF Object Conversion Utility ha stopped working&quot;, and so build fails. In the command prompt where I was doing the build I see the following. link -nolo...'''
date = "2012-09-23T12:05:00Z"
lastmod = "2012-09-23T16:58:00Z"
weight = 14463
keywords = [ "win32", "environment", "build", "coff" ]
aliases = [ "/questions/14463" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Failed to Build Wireshark due to Microsoft Resource File To COFF Object Conversion Utility has stopped working](/questions/14463/failed-to-build-wireshark-due-to-microsoft-resource-file-to-coff-object-conversion-utility-has-stopped-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14463-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I run "nmake -f Makefile.nmake all" to build Wireshark for the very first time I got a pop-up from Windows saying "Microsoft Resource File To COFF Object Conversion Utility ha stopped working", and so build fails. In the command prompt where I was doing the build I see the following.</p><p>link -nologo -debug -incremental:no -opt:ref -def:win32/zlib.def -dll -implib:zdll.lib -out:zlib1.dll -base:0x5A4C0000 adler32.obj compress.obj crc32.obj deflate.obj gzclose.obj gzlib.obj gzread.obj gzwrite.obj infback.obj inflate.obj inftrees.obj trees.obj uncompr.obj zutil.obj inffas32.obj match686.obj zlib1.res Creating library zdll.lib and object zdll.exp LINK : fatal error LNK1123: failure during conversion to COFF: file invalid or corrupt NMAKE : fatal error U1077: '"C:\Program Files\Microsoft Visual Studio 10.0\VC\BIN\link.EXE"' : return code '0x463' Stop. NMAKE : fatal error U1077: '"C:\Program Files\Microsoft Visual Studio 10.0\VC\BIN\nmake.exe"' : return code '0x2' Stop.</p><p>I have followed Wireshark Developer's Guide to set up my Win32 build environment. I followed all the instructions to download all the necessary tools, verified the tools, and did a distclean first. I have 32-bit Vista and MSVSC++ 10 Express Edition. I also ran "sfc /scannow" to bring all Windows system files up to date.</p><p>Anyone has seen this problem before? Any known solution? All suggestions are welcomed!</p><p>Thanks,</p><p>Chris</p></div><div id="question-tags" class="tags-container tags">win32 environment build coff</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '12, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/4f856cf3b6e3ad04bb3ce1bf004b935a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris%20Wang&#39;s gravatar image" /><p>Chris Wang<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris Wang has no accepted answers">0%</span></p></div></div><div id="comments-container-14463" class="comments-container"></div><div id="comment-tools-14463" class="comment-tools"></div><div class="clear"></div><div id="comment-14463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14466"></span>

<div id="answer-container-14466" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14466-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Was able to fix the problem. I think the problem was I had Visual Studio Express 2012 before. Since Wireshark Developer's Guide recommends using VC2010 Express Ed instead, so I uninstalled VC2012 first and then I installed VC2010. It looks like VC2012 was uninstalled fine, but it left behind .NET 4.5 and a bunch of other stuff (many SQL 2012 components). It looks like Wireshark woldn't build under .NET 4.5. So I manually uninstalled .NET 4.5 and other modules that VC2012 uninstallation didn't remove and also uninstall VC2010. Once that's done, I reinstalled VC2010 (which installed .NET 4.0) and now I was able to build Wireshark successfully without seeing that "Microsoft Resource File To COFF Object Conversion Utility has stopped working" error again.</p><p>Chris</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '12, 16:58</strong></p><img src="https://secure.gravatar.com/avatar/4f856cf3b6e3ad04bb3ce1bf004b935a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris%20Wang&#39;s gravatar image" /><p>Chris Wang<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris Wang has no accepted answers">0%</span></p></div></div><div id="comments-container-14466" class="comments-container"></div><div id="comment-tools-14466" class="comment-tools"></div><div class="clear"></div><div id="comment-14466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

