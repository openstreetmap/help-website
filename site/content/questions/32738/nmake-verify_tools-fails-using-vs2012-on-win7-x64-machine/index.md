+++
type = "question"
title = "nmake verify_tools fails using VS2012 on Win7 x64 machine"
description = '''I followed the &quot;Win32/64: Step-by-Step Guide&quot; But i get stuck at the point where i have to call &quot;nmake&quot; with &quot;verify_tools&quot; It gives me following result when i run it: &quot;C:&#92;wireshark&amp;gt;nmake -f makefile.nmake verify_tools&quot; Microsoft (R) Program Maintenance Utility Version 11.00.60610.1 Copyright (C)...'''
date = "2014-05-12T13:51:00Z"
lastmod = "2014-05-14T02:27:00Z"
weight = 32738
keywords = [ "win32-setup.sh", "vs2012", "nmake", "verify_tools" ]
aliases = [ "/questions/32738" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nmake verify\_tools fails using VS2012 on Win7 x64 machine](/questions/32738/nmake-verify_tools-fails-using-vs2012-on-win7-x64-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32738-score" class="post-score" title="current number of votes">0</div><span id="post-32738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I followed the "Win32/64: Step-by-Step Guide" But i get stuck at the point where i have to call "nmake" with "verify_tools"</p><p>It gives me following result when i run it:</p><pre><code>&quot;C:\wireshark&gt;nmake -f makefile.nmake verify_tools&quot;
Microsoft (R) Program Maintenance Utility Version 11.00.60610.1
Copyright (C) Microsoft Corporation.  All rights reserved.
&gt;&lt;  ,tools/win32-setup.sh: line 32: exec: --: invalid option  exec:
usage: exec [-cl] [-a name] [command
[arguments ...]] [redirection ...]
&gt;&lt;  ,tools/win32-setup.sh: line 32:
exec: --: invalid option  exec: usage:
exec [-cl] [-a name] [command
[arguments ...]] [redirection ...]
NMAKE : fatal error U1077:
&#39;C:\Cygwin\bin\bash.EXE&#39; : return code
&#39;0x2&#39;  Stop.</code></pre><p>I inserted a "printf" into the "win32-setup.sh" to see the content of "WIN_SETUP"</p><p>win32-setup.sh looks like this then:</p><pre><code>export DOWNLOAD_TAG=&quot;2014-04-16&quot;
export WIRESHARK_TARGET_PLATFORM=&quot;win32&quot;
WIN_SETUP=`echo $0 | sed -e s/win32/win/`
printf &quot;&gt;%s&lt;\n&quot;, $WIN_SETUP
exec $WIN_SETUP [email protected]</code></pre><p>Up in the result you can see "&gt;&lt;". That means the "WIN_SETUP" is quite empty. Don't know exactly if that is the problem or why is empty.</p><p>I don't know anymore how to fix that after hours of searching and investigating.</p><p>I would really appreciate if someone could help me with that issue.</p><p>Thanks in advance.</p><p>Gerald</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-win32-setup.sh" rel="tag" title="see questions tagged &#39;win32-setup.sh&#39;">win32-setup.sh</span> <span class="post-tag tag-link-vs2012" rel="tag" title="see questions tagged &#39;vs2012&#39;">vs2012</span> <span class="post-tag tag-link-nmake" rel="tag" title="see questions tagged &#39;nmake&#39;">nmake</span> <span class="post-tag tag-link-verify_tools" rel="tag" title="see questions tagged &#39;verify_tools&#39;">verify_tools</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '14, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/c6fccd9e9d8971cce06eb4570192fa06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sessler%20Gerald&#39;s gravatar image" /><p><span>Sessler Gerald</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sessler Gerald has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 May '14, 02:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-32738" class="comments-container"><span id="32743"></span><div id="comment-32743" class="comment"><div id="post-32743-score" class="comment-score"></div><div class="comment-text"><p>First:</p><p>Given that you're running om WIN64, I would have expected that win64-setup.sh would have been called, not win32-setup.sh.</p><p>Are you using the 64-bit compiler (or the 32 bit) ?</p><p>Are you explicitly trying to build a win32 version by doing:</p><pre><code>&quot;C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.Cmd&quot;  /Release /x86  ?</code></pre><p>Please try doing the following (instead of the call to setenv). which I think should automatically set things up to do a win64 (or win32) build (depending upon which compiler you are using).</p><p>64 bit compiler:</p><pre><code>&quot;C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\Vcvarsall.bat x64&quot;</code></pre><p>If you are actually using the 32-bit compiler then replace <code>x64</code> by <code>x86</code>.</p><p>(I'll spend a bit more time tomorrow looking at the instructions in the Developer's Guide to see if any changes are needed...)</p><hr /><p>If you still get the same error, then please do the following (presumably now in the win64-setup.sh)</p><p>Please add the following before the WIN_SETUP=... and let us know the output.</p><pre><code>echo $PATH
sed --version
printf &quot;&gt;%s&lt;&quot; &quot;$0&quot;</code></pre><p>(Note that a ',' should not be put between the format and the arg(s) in the printf).</p><hr /></div><div id="comment-32743-info" class="comment-info"><span class="comment-age">(12 May '14, 19:16)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="32764"></span><div id="comment-32764" class="comment"><div id="post-32764-score" class="comment-score"></div><div class="comment-text"><p>First of all... Thanks a lot for spending your time on my case.</p><p>I had set the compiler to x86 because at the beginning I tried with x64 and didn't work. So i thought it maybe works with x86 but i was wrong.</p><p>The path you mentioned =&gt; "C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.Cmd" doesn't exist on my machine.</p><p>As you recommended, I called again "C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\Vcvarsall.bat x64"</p><p>Now gets called the "win64-setup.sh". I inserted the code you gave me into the "win64-setup.sh" file.</p><p>Now it shows an additional error: Can't find Qt. .....</p><p>Below i copied you the command line output:</p><p><code> C:\wireshark&gt;nmake -f makefile.nmake verify_tools</code></p><p><code></code></p><p><code>Microsoft (R) Program Maintenance Utility Version 11.00.50727.1 Copyright (C) Microsoft Corporation. All rights reserved.</code></p><code></code><p><code>/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Common7/IDE/CommonExtensions/Microsoft/TestWindow :/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/BIN/amd64:/cygdrive/c/Windows/Microsoft.NET/F ramework64/v4.0.30319:/cygdrive/c/Windows/Microsoft.NET/Framework64/v3.5:/cygdrive/c/Program Files (x86)/Micro soft Visual Studio 11.0/VC/VCPackages:/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Common7/IDE :/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Common7/Tools:/cygdrive/c/Program Files (x86)/HT ML Help Workshop:/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Team Tools/Performance Tools/x64 :/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Team Tools/Performance Tools:/cygdrive/c/Program Files (x86)/Windows Kits/8.0/bin/x64:/cygdrive/c/Program Files (x86)/Windows Kits/8.0/bin/x86:/cygdrive/c/Pro gram Files (x86)/Microsoft SDKs/Windows/v8.0A/bin/NETFX 4.0 Tools/x64:/cygdrive/c/Program Files (x86)/Microsof t SDKs/Windows/v7.0A/Bin/x64:/cygdrive/c/Program Files (x86)/Microsoft SDKs/Windows/v8.0A/bin/NETFX 4.0 Tools:</code></p></div><div id="comment-32764-info" class="comment-info"><span class="comment-age">(13 May '14, 13:53)</span> <span class="comment-user userinfo">Sessler Gerald</span></div></div><span id="32766"></span><div id="comment-32766" class="comment"><div id="post-32766-score" class="comment-score"></div><div class="comment-text"><p><code> /cygdrive/c/Program Files (x86)/Microsoft SDKs/Windows/v7.0A/Bin:/cygdrive/c/Program Files (x86)/Microsoft Vis ual Studio 11.0/Common7/IDE/CommonExtensions/Microsoft/TestWindow:/cygdrive/c/Program Files (x86)/Microsoft SD Ks/F#/3.0/Framework/v4.0:/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VSTSDB/Deploy:/cygdrive/ c/Program Files (x86)/Microsoft Visual Studio 11.0/Common7/IDE:/cygdrive/c/Program Files (x86)/Microsoft Visua l Studio 11.0/VC/BIN:/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Common7/Tools:/cygdrive/c/Wi ndows/Microsoft.NET/Framework/v4.0.30319:/cygdrive/c/Windows/Microsoft.NET/Framework/v3.5:/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/VCPackages:/cygdrive/c/Program Files (x86)/HTML Help Workshop:/cyg drive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Team Tools/Performance Tools:/cygdrive/c/Program File s (x86)/Windows Kits/8.0/bin/x86:/cygdrive/c/Program Files (x86)/Microsoft SDKs/Windows/v8.0A/bin/NETFX 4.0 To ols:/cygdrive/c/Program Files (x86)/Microsoft SDKs/Windows/v7.0A/Bin:/cygdrive/c/Python34:/cygdrive/c/Python34 /Scripts:/cygdrive/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/cygdrive/c/Program Files (x86)/Intel /iCLS Client:/cygdrive/c/Program Files/Intel/iCLS Client:/cygdrive/c/Windows/system32:/cygdrive/c/Windows:/cyg drive/c/Windows/System32/Wbem:/cygdrive/c/Windows/System32/WindowsPowerShell/v1.0:/cygdrive/c/Program Files/In tel/Intel(R) Management Engine Components/DAL:/cygdrive/c/Program Files/Intel/Intel(R) Management Engine Compo nents/IPT:/cygdrive/c/Program Files (x86)/Intel/Intel(R) Management Engine Components/DAL:/cygdrive/c/Program Files (x86)/Intel/Intel(R) Management Engine Components/IPT:/cygdrive/c/Program Files (x86)/Intel/OpenCL SDK/2 .0/bin/x86:/cygdrive/c/Program Files (x86)/Intel/OpenCL SDK/2.0/bin/x64:/cygdrive/c/Program Files/Lucidlogix T echnologies/VIRTU MVP:/cygdrive/c/Program Files/Microsoft/Web Platform Installer:/cygdrive/c/Program Files (x8 6)/Microsoft ASP.NET/ASP.NET Web Pages/v1.0:</code></p></div><div id="comment-32766-info" class="comment-info"><span class="comment-age">(13 May '14, 13:59)</span> <span class="comment-user userinfo">Sessler Gerald</span></div></div><span id="32767"></span><div id="comment-32767" class="comment"><div id="post-32767-score" class="comment-score"></div><div class="comment-text"><p><code> /cygdrive/c/Program Files (x86)/Windows Kits/8.0/Windows Performan ce Toolkit:/cygdrive/c/Program Files/Microsoft SQL Server/110/Tools/Binn:/cygdrive/c/Program Files (x86)/Visua lSVN/bin:/cygdrive/c/Program Files (x86)/GtkSharp/2.12/bin:/cygdrive/c/Program Files/TortoiseSVN/bin:/cygdrive /c/Users/The Sky/AppData/Local/Android/android-sdk/tools:/cygdrive/c/Program Files/Microsoft SQL Server/110/DT S/Binn:/cygdrive/c/Program Files (x86)/Microsoft SQL Server/110/Tools/Binn:/cygdrive/c/Program Files (x86)/Mic rosoft SQL Server/110/Tools/Binn/ManagementStudio:/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0 /Common7/IDE/PrivateAssemblies:/cygdrive/c/Program Files (x86)/Microsoft SQL Server/110/DTS/Binn:/cygdrive/c/W indows/System32/WindowsPowerShell/v1.0:/usr/bin:/cygdrive/c/Program Files/TortoiseGit/bin:/cygdrive/c/Program Files (x86)/Microchip/xc32/v1.21/bin:/cygdrive/c/Program Files/smartmontools/bin:/cygdrive/c/cygwin/bin:/cygdr ive/c/cygwin/bin:/cygdrive/c/Wireshark-win64-libs/gtk2/bin:/cygdrive/c/bin:/cygdrive/c/Wireshark-win64-libs/zl ib125</code></p><p>tools/win64-setup.sh&lt;</p><p>tools/win64-setup.sh: line 34: exec: --: invalid option exec: usage: exec [-cl] [-a name] [command [arguments ...]] [redirection ...] Can't find Qt. This will become a problem at some point.</p><p>// I deleted here the second "Echo $Path" result =&gt; to much text</p><p>tools/win64-setup.sh&lt;</p><p>tools/win64-setup.sh: line 34: exec: --: invalid option exec: usage: exec [-cl] [-a name] [command [arguments ...]] [redirection ...] NMAKE : fatal error U1077: 'C:\Cygwin\bin\bash.EXE' : return code '0x2' Stop.</p><p>C:\wireshark&gt;</p><p>.</p><p>Seems it gets called 2 times, so i deleted the second result of "Echo $Path" to prevent posting redundant text because it is quite long.</p><p>Hope you can find out something. Otherwise I'll have to try it on a different machine praying to have more luck there.</p><p>Thanks a lot for your effort.</p><p>Gerald</p></div><div id="comment-32767-info" class="comment-info"><span class="comment-age">(13 May '14, 14:06)</span> <span class="comment-user userinfo">Sessler Gerald</span></div></div></div><div id="comment-tools-32738" class="comment-tools"></div><div class="clear"></div><div id="comment-32738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32788"></span>

<div id="answer-container-32788" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32788-score" class="post-score" title="current number of votes">0</div><span id="post-32788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, I've take the path you posted, split it at the separator ":", and then sorted it. There may be the odd extra space due to formatting, cut and paste etc, but I think it shows you have an extraordinarily complicated path IMHO, with a fair amount of dupes:</p><pre><code>/cygdrive/c/Program Files (x86)/GtkSharp/2.12/bin
/cygdrive/c/Program Files (x86)/HTML Help Workshop
/cygdrive/c/Program Files (x86)/HTML Help Workshop
/cygdrive/c/Program Files (x86)/Intel/Intel(R) Management Engine Components/DAL
/cygdrive/c/Program Files (x86)/Intel/Intel(R) Management Engine Components/IPT
/cygdrive/c/Program Files (x86)/Intel/OpenCL SDK/2 .0/bin/x86
/cygdrive/c/Program Files (x86)/Intel/OpenCL SDK/2.0/bin/x64
/cygdrive/c/Program Files (x86)/Intel/iCLS Client
/cygdrive/c/Program Files (x86)/Microchip/xc32/v1.21/bin
/cygdrive/c/Program Files (x86)/Microsoft ASP.NET/ASP.NET Web Pages/v1.0
/cygdrive/c/Program Files (x86)/Microsoft SD Ks/F#/3.0/Framework/v4.0
/cygdrive/c/Program Files (x86)/Microsoft SDKs/Windows/v7.0A/Bin
/cygdrive/c/Program Files (x86)/Microsoft SDKs/Windows/v7.0A/Bin
/cygdrive/c/Program Files (x86)/Microsoft SDKs/Windows/v7.0A/Bin/x64
/cygdrive/c/Program Files (x86)/Microsoft SDKs/Windows/v8.0A/bin/NETFX 4.0 To ols
/cygdrive/c/Program Files (x86)/Microsoft SDKs/Windows/v8.0A/bin/NETFX 4.0 Tools
/cygdrive/c/Program Files (x86)/Microsoft SDKs/Windows/v8.0A/bin/NETFX 4.0 Tools/x64
/cygdrive/c/Program Files (x86)/Microsoft SQL Server/110/DTS/Binn
/cygdrive/c/Program Files (x86)/Microsoft SQL Server/110/Tools/Binn
/cygdrive/c/Program Files (x86)/Microsoft SQL Server/110/Tools/Binn/ManagementStudio
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0 /Common7/IDE/PrivateAssemblies
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Common7/IDE
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Common7/IDE
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Common7/IDE/CommonExtensions/Microsoft/TestWindow
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Common7/IDE/CommonExtensions/Microsoft/TestWindow
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Common7/Tools
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Common7/Tools
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Team Tools/Performance Tools
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Team Tools/Performance Tools
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/Team Tools/Performance Tools/x64
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/BIN
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/BIN/amd64
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/VCPackages
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/VCPackages
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VSTSDB/Deploy
/cygdrive/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common
/cygdrive/c/Program Files (x86)/VisualSVN/bin
/cygdrive/c/Program Files (x86)/Windows Kits/8.0/Windows Performance Toolkit
/cygdrive/c/Program Files (x86)/Windows Kits/8.0/bin/x64
/cygdrive/c/Program Files (x86)/Windows Kits/8.0/bin/x86
/cygdrive/c/Program Files (x86)/Windows Kits/8.0/bin/x86
/cygdrive/c/Program Files/Intel/Intel(R) Management Engine Compo nents/IPT
/cygdrive/c/Program Files/Intel/Intel(R) Management Engine Components/DAL
/cygdrive/c/Program Files/Intel/iCLS Client
/cygdrive/c/Program Files/Lucidlogix Technologies/VIRTU MVP
/cygdrive/c/Program Files/Microsoft SQL Server/110/DT S/Binn
/cygdrive/c/Program Files/Microsoft SQL Server/110/Tools/Binn
/cygdrive/c/Program Files/Microsoft/Web Platform Installer
/cygdrive/c/Program Files/TortoiseGit/bin
/cygdrive/c/Program Files/TortoiseSVN/bin
/cygdrive/c/Program Files/smartmontools/bin
/cygdrive/c/Python34
/cygdrive/c/Python34/Scripts
/cygdrive/c/Users/The Sky/AppData/Local/Android/android-sdk/tools
/cygdrive/c/Windows
/cygdrive/c/Windows/Microsoft.NET/Framework/v3.5
/cygdrive/c/Windows/Microsoft.NET/Framework/v4.0.30319
/cygdrive/c/Windows/Microsoft.NET/Framework64/v3.5
/cygdrive/c/Windows/Microsoft.NET/Framework64/v4.0.30319
/cygdrive/c/Windows/System32/Wbem
/cygdrive/c/Windows/System32/WindowsPowerShell/v1.0
/cygdrive/c/Windows/System32/WindowsPowerShell/v1.0
/cygdrive/c/Windows/system32
/cygdrive/c/Wireshark-win64-libs/gtk2/bin
/cygdrive/c/Wireshark-win64-libs/zlib125
/cygdrive/c/bin
/cygdrive/c/cygwin/bin
/cygdrive/c/cygwin/bin
/usr/bin</code></pre><p>Can you please open a Visual Studio Command Prompt (found in the Start Menu under Visual Studio), x64 or x86 it doesn't really matter, and then execute `echo %PATH% &gt; %TEMP%\mypath.txt, and then post the contents of that file as a comment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '14, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-32788" class="comments-container"></div><div id="comment-tools-32788" class="comment-tools"></div><div class="clear"></div><div id="comment-32788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

