+++
type = "question"
title = "Wireshark Build for windows 7 64-bit"
description = '''I want to know what changes are required to build wireshark on windows 7 64-bit. Is there any step by step guide other than the one given in the developer&#x27;s guide as it is for 32 bit system? Which visual C++ would be required, 2008 or 2010? A step by step guide would be much preferable. Thanks'''
date = "2011-12-21T00:26:00Z"
lastmod = "2012-07-16T05:46:00Z"
weight = 8065
keywords = [ "development", "windows", "build", "64-bit" ]
aliases = [ "/questions/8065" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Build for windows 7 64-bit](/questions/8065/wireshark-build-for-windows-7-64-bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8065-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to know what changes are required to build wireshark on windows 7 64-bit. Is there any step by step guide other than the one given in the developer's guide as it is for 32 bit system? Which visual C++ would be required, 2008 or 2010? A step by step guide would be much preferable. Thanks</p></div><div id="question-tags" class="tags-container tags">development windows build 64-bit</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '11, 00:26</strong></p><img src="https://secure.gravatar.com/avatar/b7bdcb1b20e2c4bba13948b04439d544?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vish&#39;s gravatar image" /><p>vish<br />
<span class="score" title="0 reputation points">0</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vish has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Dec '11, 05:58</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8065" class="comments-container"></div><div id="comment-tools-8065" class="comment-tools"></div><div class="clear"></div><div id="comment-8065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="8066"></span>

<div id="answer-container-8066" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8066-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Although I haven't built a 64 bit version, as long as you have the 64 bit compilers installed everything should be straightforward. Ensure your command prompt is set up for building 64 bit applications and edit config.nmake to adjust the variable <code>WIRESHARK_TARGET_PLATFORM</code> to be "win64".</p><p>The buildbot and Wireshark releases use 2008.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '11, 00:53</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-8066" class="comments-container"><span id="8067"></span><div id="comment-8067" class="comment"><div id="post-8067-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. do I need to have 64-bit compiler for that or 32-bit compiler would do?</p></div><div id="comment-8067-info" class="comment-info"><span class="comment-age">(21 Dec '11, 02:03)</span> vish</div></div><span id="8068"></span><div id="comment-8068" class="comment"><div id="post-8068-score" class="comment-score"></div><div class="comment-text"><p>I've converted your "answer" to a comment as that is the way this site works.</p><p>Yes, you must have the 64 bit compilers installed to produce a 64 bit version of wireshark.</p></div><div id="comment-8068-info" class="comment-info"><span class="comment-age">(21 Dec '11, 02:37)</span> grahamb ♦</div></div><span id="8069"></span><div id="comment-8069" class="comment"><div id="post-8069-score" class="comment-score"></div><div class="comment-text"><p>Can you give me some link to download visual c++ 64bit compiler as I m not able to find it. Thanks</p></div><div id="comment-8069-info" class="comment-info"><span class="comment-age">(21 Dec '11, 02:48)</span> vish</div></div><span id="8070"></span><div id="comment-8070" class="comment"><div id="post-8070-score" class="comment-score"></div><div class="comment-text"><p>64 bit isn't available in the free Express editions, only the paid for editions (for 2010 at least).</p><p>See <a href="http://msdn.microsoft.com/en-us/library/hs24szh9.aspx">here</a> for edition information.</p></div><div id="comment-8070-info" class="comment-info"><span class="comment-age">(21 Dec '11, 02:58)</span> grahamb ♦</div></div><span id="8076"></span><div id="comment-8076" class="comment"><div id="post-8076-score" class="comment-score"></div><div class="comment-text"><p>Thanks. One more thing, what do u mean by "setting up the command prompt for 64bit"? Does that mean I have to run vcvarsall.bat instead of vcvars_32.bat(in 32bit system)?</p></div><div id="comment-8076-info" class="comment-info"><span class="comment-age">(22 Dec '11, 00:18)</span> vish</div></div><span id="8078"></span><div id="comment-8078" class="comment not_top_scorer"><div id="post-8078-score" class="comment-score"></div><div class="comment-text"><p>I think you need <code>vcvars64.bat</code> out of the VC\bin\amd64 directory.</p><p>I've been poking around and it seems that you can install the 64 bit compilers on a 32 bit OS and "cross compile". In that case you need <code>vcvars86_amd64.bat</code> from the VC\bin\x86_amd64 directory. I haven't tried this though.</p><p>You can also use vcvarsall.bat and pass the appropriate option to set the toolchain to use as explained by the script usage help.</p></div><div id="comment-8078-info" class="comment-info"><span class="comment-age">(22 Dec '11, 03:52)</span> grahamb ♦</div></div><span id="8079"></span><div id="comment-8079" class="comment not_top_scorer"><div id="post-8079-score" class="comment-score"></div><div class="comment-text"><p>This is correct. I have built both 32- and 64-bit versions of Wireshark this way. The process is pretty much the same for either one; just declare your <code>WIRESHARK_TARGET_PLATFORM</code> target as <code>win32</code> or <code>win64</code>, and set up the toolchain as appropriate for your platform.</p></div><div id="comment-8079-info" class="comment-info"><span class="comment-age">(22 Dec '11, 06:55)</span> multipleinte...</div></div></div><div id="comment-tools-8066" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-8066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8084"></span>

<div id="answer-container-8084" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8084-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might want to read some of the answers to the question entitled, <a href="http://ask.wireshark.org/questions/7707/build-was-working-on-windowsxp-but-now-it-fails-to-build-in-win7-x64">Build was working on WindowsXP, but now it fails to build in Win7 x64</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '11, 13:17</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-8084" class="comments-container"><span id="8099"></span><div id="comment-8099" class="comment"><div id="post-8099-score" class="comment-score"></div><div class="comment-text"><p>I m getting this error:</p><p>file_util.obj: module machine type(x86) conflicting with target machine type(x64).</p><p>What might be the problem?</p></div><div id="comment-8099-info" class="comment-info"><span class="comment-age">(22 Dec '11, 23:56)</span> vish</div></div><span id="8102"></span><div id="comment-8102" class="comment"><div id="post-8102-score" class="comment-score"></div><div class="comment-text"><p>Did you previously compile for 32 bit with the same source tree? It sounds as though there is a 32 bit object file left behind and that can't be linked with the newly compiled 64 bit stuff.</p><p>Try <code>nmake -f Makefile.nmake distclean</code> to clean up your source tree.</p></div><div id="comment-8102-info" class="comment-info"><span class="comment-age">(23 Dec '11, 00:52)</span> grahamb ♦</div></div><span id="8106"></span><div id="comment-8106" class="comment"><div id="post-8106-score" class="comment-score"></div><div class="comment-text"><p>Yes I have made a 32-bit version before but have also run "distclean" command.</p></div><div id="comment-8106-info" class="comment-info"><span class="comment-age">(23 Dec '11, 01:36)</span> vish</div></div><span id="8107"></span><div id="comment-8107" class="comment"><div id="post-8107-score" class="comment-score"></div><div class="comment-text"><p>Now I have made the build for 64 bit but I m getting application error when I run the .exe file.</p><p>"The application was unable to start correctly"</p></div><div id="comment-8107-info" class="comment-info"><span class="comment-age">(23 Dec '11, 03:53)</span> vish</div></div><span id="8108"></span><div id="comment-8108" class="comment"><div id="post-8108-score" class="comment-score"></div><div class="comment-text"><p>The error code is 0xc000007b.</p></div><div id="comment-8108-info" class="comment-info"><span class="comment-age">(23 Dec '11, 05:14)</span> vish</div></div><span id="8109"></span><div id="comment-8109" class="comment not_top_scorer"><div id="post-8109-score" class="comment-score"></div><div class="comment-text"><p>@vish: You should edit your question to include this valuable information. Also consider showing us the output of <code>nmake -f Makefile.nmake verify_tools</code> and the exact command you used to build Wireshark.</p></div><div id="comment-8109-info" class="comment-info"><span class="comment-age">(23 Dec '11, 06:58)</span> multipleinte...</div></div><span id="8112"></span><div id="comment-8112" class="comment not_top_scorer"><div id="post-8112-score" class="comment-score"></div><div class="comment-text"><p>I did the following steps:</p><blockquote><ol><li>C:/Microsoft Visual Studio 10.0/VC/bin/amd64/vcvars_64.bat</li><li>I ran<br />
nmake -f Makefile.nmake verify_tools The output was as shown in the developer's guide. All the tools are properly installed.</li><li>Download vcredist_x64.exe and saved it to C:wireshark-win64-libs Then nmake -f Makefile.nmake setup</li><li>nmake -f Makefile.nmake distclean</li><li>nmake -f Makefile.nmake all</li></ol></blockquote><p>The wireshark.exe was made in the folder wireshark-gtk2, but on double clicking it, error is thrown: The application was unable to start correctly 0xc000007b.</p><p>I searched on google and got to know that the dll's should be 64-bit and that's causing the problem. But still dont know the exact cause and the solution.</p></div><div id="comment-8112-info" class="comment-info"><span class="comment-age">(23 Dec '11, 08:39)</span> vish</div></div><span id="8114"></span><div id="comment-8114" class="comment not_top_scorer"><div id="post-8114-score" class="comment-score"></div><div class="comment-text"><p>Did you read the <a href="http://wiki.wireshark.org/Development/Win64">Win64 Development</a> wiki page carefully? In particular, did you set <code>WIRESHARK_TARGET_PLATFORM=win64</code>?</p></div><div id="comment-8114-info" class="comment-info"><span class="comment-age">(23 Dec '11, 09:14)</span> cmaynard ♦♦</div></div><span id="8123"></span><div id="comment-8123" class="comment not_top_scorer"><div id="post-8123-score" class="comment-score"></div><div class="comment-text"><p>Yes I did that change. But I m confused as to which batch file should I run? When I run vcvarsall.bat, then it shows that setting up environment for 32-bit. Is this correct? Then it throws an error, saying module type x86 conflicting with x64.</p></div><div id="comment-8123-info" class="comment-info"><span class="comment-age">(23 Dec '11, 23:14)</span> vish</div></div><span id="8126"></span><div id="comment-8126" class="comment not_top_scorer"><div id="post-8126-score" class="comment-score"></div><div class="comment-text"><p>See my comment to your original question, if you use vcvarsall.bat you must pass the amd64 option to set the environment for 64 bit compilation.</p><p>If you have previously used your source tree to build the 32 bit version, you must ensure that all build artefacts from that version are removed, e.g. by making distclean.</p></div><div id="comment-8126-info" class="comment-info"><span class="comment-age">(24 Dec '11, 02:59)</span> grahamb ♦</div></div></div><div id="comment-tools-8084" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-8084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12753"></span>

<div id="answer-container-12753" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12753-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>Install Microsoft Visual Studio 2010 Express Edition.
Check for and install any updates.
Download vcredist_x64.exe and save it to C:\wireshark-win64-libs\.
Download and install Microsoft SDK.
Download and install cygwin.
Download and install Python (2.7.2).
Download and extract the Wireshark sources.
If you plan to create a Wireshark installer, download and install NSIS (2.4.6).

Edit Wireshark&#39;s config.nmake file, setting:
    MSVC_VARIANT=MSVC2010 (Yes, I know intuitively it should be set to MSVC2010EE, but I found that setting it to MSVC2010EE didn&#39;t work. I don&#39;t know why.)
    MAKENSIS=&quot;$(PROGRAM_FILES) (x86)\NSIS\makensis.exe&quot;
    WIRESHARK_TARGET_PLATFORM=win64 (Alternatively, you can set this as an environment variable.)

call &quot;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\vcvarsall.bat&quot; x86_amd64  (assume you install this directory)

    nmake -f Makefile.nmake setup
    nmake -f Makefile.nmake distclean
    nmake -f Makefile.nmake all
    nmake -f Makefile.nmake packaging
    etc.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '12, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/8b5d11af8b0996d43bd3907ed22b6563?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ltgao&#39;s gravatar image" /><p>ltgao<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ltgao has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-12753" class="comments-container"><span id="12762"></span><div id="comment-12762" class="comment"><div id="post-12762-score" class="comment-score"></div><div class="comment-text"><p>I also found this bit helpful. I went around in a few circles to find my 64-bit compilers with the SDK, and there was a fix:</p><p><a href="http://support.microsoft.com/kb/2519277">http://support.microsoft.com/kb/2519277</a></p><p>I also just launch the command prompts from the Start Menu (either under the MS Visual Studio 2010 Express group or the Microsoft Windows SDK 7.1 group)</p></div><div id="comment-12762-info" class="comment-info"><span class="comment-age">(16 Jul '12, 07:50)</span> rickg421</div></div></div><div id="comment-tools-12753" class="comment-tools"></div><div class="clear"></div><div id="comment-12753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

