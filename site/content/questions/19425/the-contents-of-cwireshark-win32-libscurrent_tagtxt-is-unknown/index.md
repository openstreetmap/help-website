+++
type = "question"
title = "The contents of C:&#92;wireshark-win32-libs&#92;current_tag.txt is (unknown)"
description = '''hi all,after proper installation as mentioned in developer guide,and running this command in cmd prompt: C:&#92;wireshark&amp;gt; nmake -f Makefile.nmake verify_tools,i get this error.. Microsoft (R) Program Maintenance Utility Version 10.00.40219.01 Copyright (C) Microsoft Corporation. All rights reserved....'''
date = "2013-03-13T01:09:00Z"
lastmod = "2013-03-13T02:47:00Z"
weight = 19425
keywords = [ "makefile.nmake", "windows", "build" ]
aliases = [ "/questions/19425" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [The contents of C:\\wireshark-win32-libs\\current\_tag.txt is (unknown)](/questions/19425/the-contents-of-cwireshark-win32-libscurrent_tagtxt-is-unknown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19425-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all,after proper installation as mentioned in developer guide,and running this command in cmd prompt: C:\wireshark&gt; nmake -f Makefile.nmake verify_tools,i get this error..</p><pre><code>Microsoft (R) Program Maintenance Utility Version 10.00.40219.01
Copyright (C) Microsoft Corporation.  All rights reserved.

ERROR: The contents of C:\wireshark-win32-libs\current_tag.txt is (unknown).
It should be 2013-02-19.

Checking for required applications:
        cl: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/BIN/cl
        link: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/BIN/link
        nmake: nmake
        bash: /usr/bin/bash
        bison: /usr/bin/bison
        flex: /usr/bin/flex
        env: /usr/bin/env
        grep: /usr/bin/grep
        /usr/bin/find: /usr/bin/find
        perl: /usr/bin/perl
        C:\Python27\python.exe: /cygdrive/c/Python27/python.exe
        sed: /usr/bin/sed
        unzip: /usr/bin/unzip
        wget: /usr/bin/wget</code></pre><p>p.s:i am getting the path of nmake as nmake which might be causing problem.help..!!</p></div><div id="question-tags" class="tags-container tags">makefile.nmake windows build</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '13, 01:09</strong></p><img src="https://secure.gravatar.com/avatar/afa04deca78e2ac8df31ecc4deea5bde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajain&#39;s gravatar image" /><p>ajain<br />
<span class="score" title="14 reputation points">14</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajain has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Mar '13, 02:59</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-19425" class="comments-container"><span id="19430"></span><div id="comment-19430" class="comment"><div id="post-19430-score" class="comment-score"></div><div class="comment-text"><p>i could not find the file C:\wireshark-win32-libs\current_tag.txt.i have followed all steps correctly.i could not download WS sources through svn,i just downloaded locally and put it in the c:\wireshark.what am i missing?</p></div><div id="comment-19430-info" class="comment-info"><span class="comment-age">(13 Mar '13, 02:10)</span> ajain</div></div><span id="19437"></span><div id="comment-19437" class="comment"><div id="post-19437-score" class="comment-score"></div><div class="comment-text"><p>The path to nmake is odd. I suspect you've managed to create a file called nmake in the current directory. The fact that verify_tools produces good output shows that nmake is working though.</p></div><div id="comment-19437-info" class="comment-info"><span class="comment-age">(13 Mar '13, 03:05)</span> grahamb ♦</div></div><span id="19438"></span><div id="comment-19438" class="comment"><div id="post-19438-score" class="comment-score"></div><div class="comment-text"><p>makefile.nmake and config.nmake are the only two files in c:\wireshark.what to do?getting the same error with :nmake -f Makefile.nmake setup..</p></div><div id="comment-19438-info" class="comment-info"><span class="comment-age">(13 Mar '13, 04:00)</span> ajain</div></div><span id="19439"></span><div id="comment-19439" class="comment"><div id="post-19439-score" class="comment-score"></div><div class="comment-text"><p>If the error is simply the path to nmake I think you can ignore it. If I create a file nmake in the top level directory and verify_tools then I get the same output as you, but the build still works.</p><p>The setup step attempts to download all the 3rd party libraries using http. Are you blocked from doing that? What error do you get from the setup step?</p></div><div id="comment-19439-info" class="comment-info"><span class="comment-age">(13 Mar '13, 04:18)</span> grahamb ♦</div></div></div><div id="comment-tools-19425" class="comment-tools"></div><div class="clear"></div><div id="comment-19425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19434"></span>

<div id="answer-container-19434" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19434-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Proceed to the next step "Install Libraries", because this happens on a pristine developer machine. Next time you run verify_tools it checks if your libraries are still up to date.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 02:47</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19434" class="comments-container"><span id="19515"></span><div id="comment-19515" class="comment"><div id="post-19515-score" class="comment-score"></div><div class="comment-text"><p>The "install libraries"step gives</p><p>ERROR: The contents of C:\wireshark-win32-libs\current_tag.txt is (unknown). It should be 2013-02-19.</p><p>then,it tries to connect to server(anonsvn.ireshark.org)but fails to connect(even using a proxy site as explained in guide fails). system may be behind company's firewall but i can go to this site through browser.can't i download the libraries directly and put them in the required directory?if yes,plz mention the links to the libraries and location to store them.also,i am working on 32bit windows xp?</p></div><div id="comment-19515-info" class="comment-info"><span class="comment-age">(14 Mar '13, 10:10)</span> ajain</div></div><span id="19516"></span><div id="comment-19516" class="comment"><div id="post-19516-score" class="comment-score"></div><div class="comment-text"><p>The libraries needed are specified in Makefile.nmake and depend on the options set in config.nmake. The actual libraries themselves can be found at <code>http://anonsvn.wireshark.org/wireshark-win32-libs/trunk-1.8/packages/</code> adjust the <code>trunk-1.8</code> part for the version you are building.</p><p>All the files should be placed in your wireshark libs directory which seems to be <code>C:\wireshark-win32-libs</code>.</p><p>If you do this, then run setup again it will find the files and not try to download them.</p></div><div id="comment-19516-info" class="comment-info"><span class="comment-age">(14 Mar '13, 10:55)</span> grahamb ♦</div></div><span id="19517"></span><div id="comment-19517" class="comment"><div id="post-19517-score" class="comment-score"></div><div class="comment-text"><p>grahamb,thanx for prompt reply..what exacty u mean by adjusting the trunk 1.8?what i'm doing is downloading those zip files and extracting to C:\wireshark-win32-libs.</p></div><div id="comment-19517-info" class="comment-info"><span class="comment-age">(14 Mar '13, 11:40)</span> ajain</div></div><span id="19519"></span><div id="comment-19519" class="comment"><div id="post-19519-score" class="comment-score"></div><div class="comment-text"><p>There are different sets of libraries for each major version of Wireshark. So if your source is for 1.8.x then use the libraries in trunk-1.8, if you were building 1.6.x then you would use the libraries in trunk-1.6.</p></div><div id="comment-19519-info" class="comment-info"><span class="comment-age">(14 Mar '13, 13:06)</span> grahamb ♦</div></div><span id="19607"></span><div id="comment-19607" class="comment"><div id="post-19607-score" class="comment-score"></div><div class="comment-text"><p>ok..the setup phase worked..but its looking for wiresparkle-0.3-44-g2c8d9d3-win32ws.zip which i don't see in trunk.it could not connect to internet,so could not move forward and extract these pkg findproc,nasm and upx301,gtk+-bundle(rest others are extracted).it ends with NMAKE : fatal error U1077: 'c:\cygwin\bin\bash.EXE' : return code '0x1'.should i move ahead with distclean and build step after extracting these manually and leaving out wiresparkle?i am working on 32 bit winxp.and rgdg version of wireshark source(i downloaded from link in step-up-step guide through tortoisesvn).</p></div><div id="comment-19607-info" class="comment-info"><span class="comment-age">(18 Mar '13, 01:05)</span> ajain</div></div><span id="19608"></span><div id="comment-19608" class="comment not_top_scorer"><div id="post-19608-score" class="comment-score"></div><div class="comment-text"><p>i assume i should be looking for building 32 bit binaries for my system(32 bit xp) but i have installed MV C++ 2010 Service Pack 1 Compiler Update.is anything brewing there?reason i am saying this because the error i was getting earlier "moonmade architecture"win32" confuse us is mentioned in config.nmake for platform setting.i am using intel xeon cpu 5160,btw?</p></div><div id="comment-19608-info" class="comment-info"><span class="comment-age">(18 Mar '13, 01:20)</span> ajain</div></div><span id="19613"></span><div id="comment-19613" class="comment not_top_scorer"><div id="post-19613-score" class="comment-score"></div><div class="comment-text"><p>If your build is looking for winsparkle then your source is for trunk. That means you need the libraries for trunk, found here: <a href="http://anonsvn.wireshark.org/wireshark-win32-libs/trunk/packages/">http://anonsvn.wireshark.org/wireshark-win32-libs/trunk/packages/</a></p></div><div id="comment-19613-info" class="comment-info"><span class="comment-age">(18 Mar '13, 03:38)</span> grahamb ♦</div></div></div><div id="comment-tools-19434" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-19434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

