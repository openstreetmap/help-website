+++
type = "question"
title = "Windows &quot;Build errors&quot;"
description = '''Hello, I am trying to set up a Build environment for Wireshark on Windows7 using VS2013 and CMake. But when I try to build Wireshark from its sources I still got some errors. Does anybody know what the cause of these errors is: Build FAILED.  &quot;C:&#92;Development&#92;wsbuild32&#92;Wireshark.sln&quot; (default target)...'''
date = "2017-07-13T14:25:00Z"
lastmod = "2017-07-14T05:35:00Z"
weight = 62763
keywords = [ "development", "windows7", "msbuild", "build" ]
aliases = [ "/questions/62763" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Windows "Build errors"](/questions/62763/windows-build-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62763-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am trying to set up a Build environment for Wireshark on Windows7 using VS2013 and CMake. But when I try to build Wireshark from its sources I still got some errors. Does anybody know what the cause of these errors is:</p><p>Build FAILED.</p><pre><code>   &quot;C:\Development\wsbuild32\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\Development\wsbuild32\androiddump.vcxproj.metaproj&quot; (default target) (4) -&gt;
   &quot;C:\Development\wsbuild32\ui\ui.vcxproj.metaproj&quot; (default target) (35) -&gt;
   &quot;C:\Development\wsbuild32\ui\ui.vcxproj&quot; (default target) (101) -&gt;
   (CustomBuild target) -&gt; 
     C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\wsbuild32\ui\ui.vcxproj]


   &quot;C:\Development\wsbuild32\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\Development\wsbuild32\epan\dfilter\dfilter.vcxproj.metaproj&quot; (default target) (17) -&gt;
   &quot;C:\Development\wsbuild32\epan\dfilter\dfilter.vcxproj&quot; (default target) (104) -&gt;
     C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\wsbuild32\epan\dfilter\dfilter.vcxproj]


   &quot;C:\Development\wsbuild32\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\Development\wsbuild32\androiddump.vcxproj.metaproj&quot; (default target) (4) -&gt;
   &quot;C:\Development\wsbuild32\wiretap\wiretap.vcxproj.metaproj&quot; (default target) (36) -&gt;
   &quot;C:\Development\wsbuild32\wiretap\wiretap.vcxproj&quot; (default target) (109) -&gt;
     C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\wsbuild32\wiretap\wiretap.vcxproj]


   &quot;C:\Development\wsbuild32\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\Development\wsbuild32\ALL_BUILD.vcxproj.metaproj&quot; (default target) (2) -&gt;
   &quot;C:\Development\wsbuild32\text2pcap.vcxproj.metaproj&quot; (default target) (69) -&gt;
   &quot;C:\Development\wsbuild32\text2pcap.vcxproj&quot; (default target) (114) -&gt;
     C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\wsbuild32\text2pcap.vcxproj]

0 Warning(s)
4 Error(s)</code></pre></div><div id="question-tags" class="tags-container tags">development windows7 msbuild build</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '17, 14:25</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-62763" class="comments-container"><span id="62765"></span><div id="comment-62765" class="comment"><div id="post-62765-score" class="comment-score"></div><div class="comment-text"><p>We need to see the full context of the errors. Can you redirect the msbuild output to a file and post the file (or a link to it)?</p><p>e.g.</p><pre><code>msbuild /p:Configuration=RelWithDebInfo Wireshark.sln 2&gt;&amp;1 &gt;build.txt</code></pre><p>If you turn off parallel builds by dropping the <code>/m</code> then the output is easier to follow.</p></div><div id="comment-62765-info" class="comment-info"><span class="comment-age">(13 Jul '17, 14:43)</span> grahamb ♦</div></div><span id="62766"></span><div id="comment-62766" class="comment"><div id="post-62766-score" class="comment-score"></div><div class="comment-text"><p>I will prepare it tomorrow!</p></div><div id="comment-62766-info" class="comment-info"><span class="comment-age">(13 Jul '17, 15:21)</span> Christian_R</div></div><span id="62767"></span><div id="comment-62767" class="comment"><div id="post-62767-score" class="comment-score"></div><div class="comment-text"><p>Also, don't forget that you can always check the buildbot <code>stdio</code> logs and compare the buildbot's environment, etc. with your own. There are logs for each step by each buidbot, so look at those that are relevant to you. See: <a href="https://buildbot.wireshark.org/wireshark-master/waterfall">https://buildbot.wireshark.org/wireshark-master/waterfall</a></p></div><div id="comment-62767-info" class="comment-info"><span class="comment-age">(13 Jul '17, 17:20)</span> cmaynard ♦♦</div></div><span id="62776"></span><div id="comment-62776" class="comment"><div id="post-62776-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/402/cmaynard"></a><a href="https://ask.wireshark.org/users/402/cmaynard">@cmaynard</a> Thank you for the interesting link. Didn´t know that, before.</p><p><a href="https://ask.wireshark.org/users/1225/grahamb"></a><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a> I have uploaded the build.txt herre: <a href="https://crnetworking-my.sharepoint.com/personal/creusch_crnetworks_de/_layouts/15/guestaccess.aspx?docid=0441d1f830c9146ee858ecd4f840861cc&amp;authkey=AfYwpO9ozoRugIdDzNKmI2U&amp;expiration=2017-07-20T22%3a00%3a00.000Z">build.txt</a></p></div><div id="comment-62776-info" class="comment-info"><span class="comment-age">(14 Jul '17, 04:34)</span> Christian_R</div></div></div><div id="comment-tools-62763" class="comment-tools"></div><div class="clear"></div><div id="comment-62763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62777"></span>

<div id="answer-container-62777" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62777-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have an "odd" version of flex in your path:</p><pre><code>Generating text_import_scanner.c, text_import_scanner_lex.h
C:\Users\xxxx\Downloads\UnxUtils\usr\local\wbin\flex.exe: unknown flag &#39;-&#39;.  For usage, try C:\Users\xxxx\Downloads\UnxUtils\usr\local\wbin\flex.exe --help
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\wsbuild32\ui\ui.vcxproj]</code></pre><p>I would ensure that the element <code>C:\Users\xxxx\Downloads\UnxUtils\usr\local\wbin</code> is NOT on your path when building Wireshark.</p><p>When building Wireshark you have to be careful about what's on your path, that's why I recommend building in a VM so that it's easier to control.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '17, 05:35</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jul '17, 07:32</p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span></p></div></div><div id="comments-container-62777" class="comments-container"><span id="62779"></span><div id="comment-62779" class="comment"><div id="post-62779-score" class="comment-score"></div><div class="comment-text"><p>Thought it night be the problem, too. I will try to disable it.</p></div><div id="comment-62779-info" class="comment-info"><span class="comment-age">(14 Jul '17, 07:30)</span> Christian_R</div></div><span id="62795"></span><div id="comment-62795" class="comment"><div id="post-62795-score" class="comment-score"></div><div class="comment-text"><p>Thank you or showing me how to read the build messages.</p></div><div id="comment-62795-info" class="comment-info"><span class="comment-age">(15 Jul '17, 00:48)</span> Christian_R</div></div></div><div id="comment-tools-62777" class="comment-tools"></div><div class="clear"></div><div id="comment-62777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

