+++
type = "question"
title = "Unable to build wireshark from the source on windows XP"
description = '''Hi, I have successfully compiled wireshark source code on ubunut but while trying to compile wireshark source code on windows XP I am getting stuck with few errors: It would be nice if anyone can let me know where I am going wrong. nmake -f Makefile.nmake verify_tools output is same as the one given...'''
date = "2011-07-05T13:12:00Z"
lastmod = "2011-07-05T13:12:00Z"
weight = 4912
keywords = [ "wireshark" ]
aliases = [ "/questions/4912" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to build wireshark from the source on windows XP](/questions/4912/unable-to-build-wireshark-from-the-source-on-windows-xp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4912-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have successfully compiled wireshark source code on ubunut but while trying to compile wireshark source code on windows XP I am getting stuck with few errors: It would be nice if anyone can let me know where I am going wrong.</p><p>nmake -f Makefile.nmake verify_tools output is same as the one given in win32 installation guide. nmake -f Makefile.nmake setup command did not give any error and the final line said "Wireshark is ready to build".</p><p>But when I run the command nmake -f Makefile.nmake all, I get the below error:</p><pre><code>file_util.c
file_util.c(246) : error C2220: warning treated as error - no object file generated
file_util.c(246) : warning C4133: &#39;function&#39; : incompatible types - from &#39;_stat64 *&#39; to &#39;_stati64 *&#39;
NMAKE : fatal error U1077: &#39;cl&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio .NET\VC7\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre><p>If I run the command as nmake /I -f Makefile.nmake all then I get the below error:</p><pre><code>LINK : fatal error LNK1181: cannot open input file &#39;main.obj&#39;
        cd ..
        cd win32
        nmake /I                  /f Makefile.nmake libui_win32.lib

Microsoft (R) Program Maintenance Utility Version 7.00.9466
Copyright (C) Microsoft Corporation.  All rights reserved.

&#39;libui_win32.lib&#39; is up-to-date
        cd ..
NMAKE : fatal error U1073: don&#39;t know how to make &#39;wsutil\libwsutil.lib&#39;
Stop.</code></pre><p>Can anyone suggest what needs to be checked to resolve this? I am using Microsoft Visual Studio .Net (2002).</p><p>Thanks Anoop</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '11, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/2f2f5ea4c30ed5bc326b2f1c023d831d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anoop&#39;s gravatar image" /><p>Anoop<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anoop has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Jul '11, 00:48</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-4912" class="comments-container"><span id="4913"></span><div id="comment-4913" class="comment"><div id="post-4913-score" class="comment-score">1</div><div class="comment-text"><p>I suggest you try building with a newer VC (say VC 2008) ? VC2002 is a bit old;</p><p>Wireshark is currently built with VC2008.</p><p>The VC 2008 "Express Edition" can be downloaded for free from Microsoft.</p><p>See http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html</p></div><div id="comment-4913-info" class="comment-info"><span class="comment-age">(05 Jul '11, 14:19)</span> Bill Meier ♦♦</div></div><span id="4915"></span><div id="comment-4915" class="comment"><div id="post-4915-score" class="comment-score">2</div><div class="comment-text"><p>Bill's answer is your best bet going forward, but if you MUST use VS 2002, then the issue is probably with the SDK. Are you using the SDK that comes with VS? If so then I would suggest you install a more modern SDK and use a command window initialised using the SDK SetEnv.cmd to set up the paths to the tools. In SetEnv.cmd you can see the required parameters if the defaults don't suit you.</p></div><div id="comment-4915-info" class="comment-info"><span class="comment-age">(05 Jul '11, 14:28)</span> grahamb ♦</div></div><span id="4919"></span><div id="comment-4919" class="comment"><div id="post-4919-score" class="comment-score"></div><div class="comment-text"><p>Hey Graham, I did get a newer SDK but the build still failed. Like Bill suggested I might as well get a more recent release of VC and try out.</p></div><div id="comment-4919-info" class="comment-info"><span class="comment-age">(05 Jul '11, 20:26)</span> Anoop</div></div><span id="4956"></span><div id="comment-4956" class="comment"><div id="post-4956-score" class="comment-score"></div><div class="comment-text"><p>Was able to build it successfully with a newer version. Thanks.</p></div><div id="comment-4956-info" class="comment-info"><span class="comment-age">(08 Jul '11, 08:24)</span> Anoop</div></div></div><div id="comment-tools-4912" class="comment-tools"></div><div class="clear"></div><div id="comment-4912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

