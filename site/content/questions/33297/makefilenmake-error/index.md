+++
type = "question"
title = "[closed] Makefile.nmake error"
description = '''I started building wireshark from scratch following the guide given. I am facing this error C:&#92;Program Files (x86)&#92;Microsoft Visual Studio 10.0&#92;VC&#92;bin&amp;gt;nmake -f Makefile.nma ke Verify_tools Microsoft (R) Program Maintenance Utility Version 10.00.30319.01 Copyright (C) Microsoft Corporation. All ri...'''
date = "2014-06-02T12:28:00Z"
lastmod = "2014-06-02T14:07:00Z"
weight = 33297
keywords = [ "makefile.nmake", "nmake", "wireshark" ]
aliases = [ "/questions/33297" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Makefile.nmake error](/questions/33297/makefilenmake-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33297-score" class="post-score" title="current number of votes">0</div><span id="post-33297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I started building wireshark from scratch following the guide given. I am facing this error C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin&gt;nmake -f Makefile.nma ke Verify_tools</p><p>Microsoft (R) Program Maintenance Utility Version 10.00.30319.01 Copyright (C) Microsoft Corporation. All rights reserved.</p><p>NMAKE : fatal error U1052: file 'Makefile.nmake' not found Stop.</p><p>Where am I going wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-makefile.nmake" rel="tag" title="see questions tagged &#39;makefile.nmake&#39;">makefile.nmake</span> <span class="post-tag tag-link-nmake" rel="tag" title="see questions tagged &#39;nmake&#39;">nmake</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '14, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/a9a254ac482208f766093c0f9c144364?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aman&#39;s gravatar image" /><p><span>aman</span><br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>02 Jun '14, 14:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-33297" class="comments-container"></div><div id="comment-tools-33297" class="comment-tools"></div><div class="clear"></div><div id="comment-33297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by grahamb 02 Jun '14, 14:07

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33301"></span>

<div id="answer-container-33301" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33301-score" class="post-score" title="current number of votes">0</div><span id="post-33301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin</p></blockquote><p>If you start nmake in <strong>that</strong> directory, it won't work, as the Wireshark Makfile is <strong>for sure not located</strong> in the installation directory of the compiler.</p><blockquote><p>Where am I going wrong?</p></blockquote><p>You are not following the developers guide!</p><p>Please <strong>follow</strong> the developers guide <strong>by the word</strong>.</p><p>So,</p><blockquote><p><strong>cd C:\Development\wireshark</strong><br />
nmake -f Makefile.nmake verify_tools<br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '14, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jun '14, 12:38</strong> </span></p></div></div><div id="comments-container-33301" class="comments-container"><span id="33302"></span><div id="comment-33302" class="comment"><div id="post-33302-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt for your reply. Here i get this error: C:\Development\wireshark&gt;nmake -f Makefile.nmake Verify_tools</p><p>Microsoft (R) Program Maintenance Utility Version 10.00.30319.01 Copyright (C) Microsoft Corporation. All rights reserved.</p><p>Makefile.nmake(8) : fatal error U1052: file 'win32.mak' not found Stop.</p></div><div id="comment-33302-info" class="comment-info"><span class="comment-age">(02 Jun '14, 12:40)</span> <span class="comment-user userinfo">aman</span></div></div><span id="33305"></span><div id="comment-33305" class="comment"><div id="post-33305-score" class="comment-score"></div><div class="comment-text"><p>See the answers to the following question</p><blockquote><p><a href="http://ask.wireshark.org/questions/4725/file-win32mak-not-found-stop">http://ask.wireshark.org/questions/4725/file-win32mak-not-found-stop</a></p></blockquote><p>Most certainly, your build environment is not set up properly!</p><p>Did you, really, really, <strong>really</strong>, follow the developers guide <strong>by the word</strong>?</p></div><div id="comment-33305-info" class="comment-info"><span class="comment-age">(02 Jun '14, 12:45)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="33307"></span><div id="comment-33307" class="comment"><div id="post-33307-score" class="comment-score"></div><div class="comment-text"><p>ya I followed as per the guide, but getting strange errors since last week.. really stressed for it..</p></div><div id="comment-33307-info" class="comment-info"><span class="comment-age">(02 Jun '14, 12:47)</span> <span class="comment-user userinfo">aman</span></div></div><span id="33308"></span><div id="comment-33308" class="comment"><div id="post-33308-score" class="comment-score"></div><div class="comment-text"><p>I have win32.mak and I can see that in the folder where it should be.. but its not being called.. I dont know why..</p></div><div id="comment-33308-info" class="comment-info"><span class="comment-age">(02 Jun '14, 12:48)</span> <span class="comment-user userinfo">aman</span></div></div><span id="33309"></span><div id="comment-33309" class="comment"><div id="post-33309-score" class="comment-score"></div><div class="comment-text"><p>what is the output of the following command, if you run it in the DOS box where you tried to run nmake?</p><blockquote><p>set</p></blockquote><p>Please don't post a screenshot of the window. Post the text output!</p><p>Or even beter</p><blockquote><p>set &gt; set.txt</p></blockquote><p>Then post the content of <strong>set.txt</strong></p></div><div id="comment-33309-info" class="comment-info"><span class="comment-age">(02 Jun '14, 12:48)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="33310"></span><div id="comment-33310" class="comment not_top_scorer"><div id="post-33310-score" class="comment-score"></div><div class="comment-text"><p>This is what I get:</p><pre><code>c:\Development\wireshark&gt;set
ALLUSERSPROFILE=C:\ProgramData
APPDATA=C:\Users\saroyaa\AppData\Roaming
CLASSPATH=C:\Program Files (x86)\IBM\RationalSDLC\ClearQuest\cqjni.jar
CLEARCASE_PRIMARY_GROUP=MITEL\ccusers
CLEARQUEST_HOME=C:\Program Files (x86)\IBM\RationalSDLC\ClearQuest
CommonProgramFiles=C:\Program Files\Common Files
CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files
CommonProgramW6432=C:\Program Files\Common Files
COMPUTERNAME=CA626547
ComSpec=C:\Windows\system32\cmd.exe
EMC_AUTOPLAY=C:\Program Files (x86)\Common Files\Roxio Shared\OEM\
FP_NO_HOST_CHECK=NO
HOMEDRIVE=M:
HOMEPATH=\
HOMESHARE=\\ottnfpd02\saroyaa$
IBMLDAP_ALTHOME=C:\Program Files (x86)\IBM\RationalSDLC\common\codeset
JRE_HOME=C:\Program Files (x86)\IBM\RationalSDLC\Common\Java5.0\jre
LOCALAPPDATA=C:\Users\saroyaa\AppData\Local
LOGONSERVER=\\OTTADC02
MITEL_IPA_HOME=C:\Program Files (x86)\Mitel\IP Phone Analyzer (Internal Release)

NUMBER_OF_PROCESSORS=2
OS=Windows_NT
PATH=C:\Python27\;C:\Windows\System32;C:\Program Files (x86)\Microsoft Visual St
udio 10.0\VC\bin;C:\Development\wireshark
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
PROCESSOR_ARCHITECTURE=AMD64
PROCESSOR_IDENTIFIER=Intel64 Family 6 Model 15 Stepping 11, GenuineIntel
PROCESSOR_LEVEL=6
PROCESSOR_REVISION=0f0b
ProgramData=C:\ProgramData
ProgramFiles=C:\Program Files
ProgramFiles(x86)=C:\Program Files (x86)
ProgramW6432=C:\Program Files
PROMPT=$P$G
PSModulePath=C:\Windows\system32\WindowsPowerShell\v1.0\Modules\
PUBLIC=C:\Users\Public
RATIONAL_COMMON=C:\Program Files (x86)\IBM\RationalSDLC\Common
RATIONAL_COMMON_LIB=C:\Program Files (x86)\IBM\RationalSDLC\Common\lib
RATIONAL_HOME=C:\Program Files (x86)\IBM\RationalSDLC
RATIONAL_ICU4J_DIR=C:\Program Files (x86)\IBM\RationalSDLC\common\java\icu
RATIONAL_ICU4J_VERSION=4_8
SESSIONNAME=Console
SystemDrive=C:
SystemRoot=C:\Windows
TEMP=saroyaa\AppData\Local\Temp
TISDIR=C:\Program Files (x86)\IBM\RationalSDLC\common
TMP=C:\Windows\TEMP
USERDNSDOMAIN=MITEL.COM
USERDOMAIN=MITEL
USERNAME=saroyaa
USERPROFILE=C:\Users\saroyaa
VS100COMNTOOLS=C:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\Tools
\
windir=C:\Windows
windows_tracing_flags=3
windows_tracing_logfile=C:\BVTBin\Tests\installpackage\csilogfile.log

c:\Development\wireshark&gt;</code></pre></div><div id="comment-33310-info" class="comment-info"><span class="comment-age">(02 Jun '14, 12:50)</span> <span class="comment-user userinfo">aman</span></div></div><span id="33312"></span><div id="comment-33312" class="comment not_top_scorer"><div id="post-33312-score" class="comment-score"></div><div class="comment-text"><p>Can we solve it using set INCLUDE=%INCLUDE%;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A\Include ?</p></div><div id="comment-33312-info" class="comment-info"><span class="comment-age">(02 Jun '14, 13:02)</span> <span class="comment-user userinfo">aman</span></div></div><span id="33313"></span><div id="comment-33313" class="comment not_top_scorer"><div id="post-33313-score" class="comment-score"></div><div class="comment-text"><blockquote><p>ya I followed as per the guide, but getting strange errors since last week.. really stressed for it..</p></blockquote><p>WIRESHARK_TARGET_PLATFORM is missing. Cygwin path is missing. Some other things are missing.</p><p>Are you <strong>really sure</strong> you followed the developers guide? I doubt it!</p><p>What is the output of the following command, if you run it in the same directory you ran the set command?</p><blockquote><p>nmake -f makefile.nmake verify_tools</p></blockquote></div><div id="comment-33313-info" class="comment-info"><span class="comment-age">(02 Jun '14, 13:09)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="33314"></span><div id="comment-33314" class="comment not_top_scorer"><div id="post-33314-score" class="comment-score"></div><div class="comment-text"><p>I followed the guide, I dont know where I misses any step.. I am not sure, but I followed it.. C:&gt;"C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\vcvars32.bat Setting environment for using Microsoft Visual Studio 2010 x86 tools.</p><p>C:&gt;set WIRESHARK_TARGET_PLATFORM=win32</p><p>C:&gt;cd C:\Development\wireshark</p><p>C:\Development\wireshark&gt;nmake -f Makefile.nmake verify_tools</p><p>Microsoft (R) Program Maintenance Utility Version 10.00.30319.01 Copyright (C) Microsoft Corporation. All rights reserved.</p><p>Makefile.nmake(8) : fatal error U1052: file 'win32.mak' not found Stop.</p><p>C:\Development\wireshark&gt;</p><p>and now I have WIRESHARK_TARGET_PLATFORM in the set.txt but not the cygwin.. where am I going wrong?</p></div><div id="comment-33314-info" class="comment-info"><span class="comment-age">(02 Jun '14, 13:16)</span> <span class="comment-user userinfo">aman</span></div></div><span id="33319"></span><div id="comment-33319" class="comment not_top_scorer"><div id="post-33319-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@aman</span>,</p><p>I'm sorry but this is still a continuation of your other open questions where VS 2010 isn't installed properly.</p><p>If it was installed correctly, running vcvars32.bat would add the following to the environment:</p><p><code> DevEnvDir=C:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\IDE\ Framework35Version=v3.5 FrameworkDir=C:\Windows\Microsoft.NET\Framework\ FrameworkDIR32=C:\Windows\Microsoft.NET\Framework\ FrameworkVersion=v4.0.30319 FrameworkVersion32=v4.0.30319 INCLUDE=c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\INCLUDE;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\ATLMFC\INCLUDE;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A\include; LIB=c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\LIB;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\ATLMFC\LIB;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A\lib; LIBPATH=C:\Windows\Microsoft.NET\Framework\v4.0.30319;C:\Windows\Microsoft.NET\Framework\v3.5;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\LIB;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\ATLMFC\LIB; VCINSTALLDIR=c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\ VSINSTALLDIR=C:\Program Files (x86)\Microsoft Visual Studio 10.0\ WindowsSdkDir=C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A\</code></p><p>along with a few additions to the PATH.</p><p>As you don't have that, we're back to the basic issue of installing VS2010 correctly.</p></div><div id="comment-33319-info" class="comment-info"><span class="comment-age">(02 Jun '14, 14:03)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="33320"></span><div id="comment-33320" class="comment not_top_scorer"><div id="post-33320-score" class="comment-score"></div><div class="comment-text"><p>In my opinion, this is just a restatement of the question <a href="http://ask.wireshark.org/questions/33204/makefilenmake-gives-cl-not-found-error">Makefile.nmake gives cl not found error</a>, so I'm closing this one to prevent confusion between the two questions.</p></div><div id="comment-33320-info" class="comment-info"><span class="comment-age">(02 Jun '14, 14:07)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-33301" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-33301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

