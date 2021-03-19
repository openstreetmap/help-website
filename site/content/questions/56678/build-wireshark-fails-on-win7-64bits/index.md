+++
type = "question"
title = "build wireshark fails on Win7 64bits"
description = '''Hi all When I try to setup the wireshark development env on Win7 64bits, there are always errors when build the project with &quot;msbuild /m /p:Configuration=RelWithDebInfo Wireshark.sln&quot;, do you have some suggestion for the following errors? thanks !  Following the user-guide &quot;developer-giuide-us-0923....'''
date = "2016-10-26T03:23:00Z"
lastmod = "2016-10-26T04:07:00Z"
weight = 56678
keywords = [ "win7-64bits", "build", "vs2013" ]
aliases = [ "/questions/56678" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [build wireshark fails on Win7 64bits](/questions/56678/build-wireshark-fails-on-win7-64bits)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56678-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all When I try to setup the wireshark development env on Win7 64bits, there are always errors when build the project with "msbuild /m /p:Configuration=RelWithDebInfo Wireshark.sln", do you have some suggestion for the following errors? thanks !</p><ol><li>Following the user-guide "developer-giuide-us-0923.pdf"</li><li>Software version: Win7-64bits, VS2013, Cygwin64, python2.7, cmake3.7</li><li>error information:</li></ol><pre><code>    ------ Build started: Project: dfilter (Libs\epan\dfilter\dfilter), Configuration: Debug x64 ------
5&gt;  packet-cattp.c
5&gt;  packet-cbor.c
5&gt;  packet-ccsds.c
5&gt;  packet-cdp.c
5&gt;  packet-cell_broadcast.c
16&gt;  Building Custom Rule E:/Development/wireshark/epan/dfilter/CMakeLists.txt
5&gt;  packet-ceph.c
5&gt;  packet-cfdp.c
16&gt;  CMake does not need to re-run because E:\Development\wsbuild64\epan\dfilter\CMakeFiles\generate.stamp is up-to-date.
16&gt;  Generating scanner.c, scanner_lex.h
5&gt;  packet-cfm.c
16&gt;  C:/cygwin64/bin/flex.exe -&gt; /usr/bin/flex.exe
5&gt;  packet-cgmp.c
5&gt;  packet-chargen.c
5&gt;  packet-chdlc.c
5&gt;  packet-cigi.c
5&gt;  packet-cimd.c
5&gt;  packet-cimetrics.c
5&gt;  packet-cip.c
5&gt;  packet-cipmotion.c
5&gt;  packet-cipsafety.c
5&gt;  packet-cisco-erspan.c
5&gt;  packet-cisco-fp-mim.c
16&gt;  flex: could not create --header-file=./_lex.h
16&gt;  /usr/bin/flex.exe failed: exit status 1
16&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. 
... ... 
running a2x with args --format=xhtml --destination-dir=/cygdrive/e/Development/wsbuild64/docbook --asciidoc-opts= --fop --stylesheet=ws.css release-notes.asciidoc
5&gt;  packet-hdcp2.c
5&gt;  packet-hdfs.c
5&gt;  packet-hdfsdata.c
26&gt;  drag_and_drop.c
5&gt;  packet-hdmi.c
5&gt;  packet-hip.c
26&gt;  edit_packet_comment_dlg.c
5&gt;  packet-hiqnet.c
5&gt;  packet-hislip.c
26&gt;  expert_comp_table.c
5&gt;  packet-homeplug-av.c
30&gt;        0 [main] python 9108 fork: child 7096 - died waiting for dll loading, errno 11
30&gt;a2x : error : failed: &quot;/usr/bin/asciidoc.py&quot; --backend docbook -a &quot;a2x-format=xhtml&quot;   --out-file &quot;/cygdrive/e/Development/wsbuild64/docbook/release-notes.xml&quot; &quot;/cygdrive/e/Development/wireshark/docbook/release-notes.asciidoc&quot;: [Errno 11] Resource temporarily unavailable
26&gt;  export_object_dlg.c
5&gt;  packet-homeplug.c</code></pre></div><div id="question-tags" class="tags-container tags">win7-64bits build vs2013</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '16, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/e829c98cee76cf9a5533043b74683f2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scdma&#39;s gravatar image" /><p>scdma<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scdma has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Oct '16, 03:58</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-56678" class="comments-container"></div><div id="comment-tools-56678" class="comment-tools"></div><div class="clear"></div><div id="comment-56678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56682"></span>

<div id="answer-container-56682" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56682-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can see two errors in the output:</p><pre><code>16&gt;  flex: could not create --header-file=./_lex.h
16&gt;  /usr/bin/flex.exe failed: exit status 1</code></pre><p>Something up with the call to flex, not sure why it's trying to create _lex.h</p><p>and:</p><pre><code>30&gt;        0 [main] python 9108 fork: child 7096 - died waiting for dll loading, errno 11
30&gt;a2x : error : failed: &quot;/usr/bin/asciidoc.py&quot; --backend docbook -a &quot;a2x-format=xhtml&quot;   --out-file &quot;/cygdrive/e/Development/wsbuild64/docbook/release-notes.xml&quot; &quot;/cygdrive/e/Development/wireshark/docbook/release-notes.asciidoc&quot;: [Errno 11] Resource temporarily unavailable</code></pre><p>which is something weird with running the python script asciidoc.py</p><p>Normally I'd expect odd things on the path with issues like this, but for the first one at least it seems that the build is using the Cygwin version of flex. Note that we now recommend the use of winflexbison rather than the Cygwin version, see the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupCygwin">last paragraph</a> of setting up Cygwin in the Developers Guide. If you do install this, you'll need to either delete CMakeCache.txt in your build directory and re-run the CMake generation step, or just delete and recreate the build dir entirely.</p><p>When debugging build output it's much better to turn off parallel builds (remove the /m flag given to msbuild) so that project steps are not comingled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '16, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-56682" class="comments-container"><span id="56720"></span><div id="comment-56720" class="comment"><div id="post-56720-score" class="comment-score"></div><div class="comment-text"><p>Hello Mr.Grahamb,</p><p>thanks for your answer, I will try to install the winflexbsion.</p><p>do you have some idea for the second error? actually, I can find the file "release-notes.asciidoc" in the correct folder, I don't know why a2x can not find it.</p><p>thanks very much</p><pre><code>30&gt;a2x : error : failed: &quot;/usr/bin/asciidoc.py&quot; --backend docbook -a &quot;a2x-format=xhtml&quot;   --out-file &quot;/cygdrive/e/Development/wsbuild64/docbook/release-notes.xml&quot; &quot;/cygdrive/e/Development/wireshark/docbook/release-notes.asciidoc&quot;: [Errno 11] Resource temporarily unavailable</code></pre></div><div id="comment-56720-info" class="comment-info"><span class="comment-age">(26 Oct '16, 18:31)</span> scdma</div></div><span id="56722"></span><div id="comment-56722" class="comment"><div id="post-56722-score" class="comment-score"></div><div class="comment-text"><p>Hello Mr.Grahamb, I used the winflexbison to build the wireshark-64bits on Win7-64bits &amp; VS2013, the same error occurs, the error information is as below, would you like have some suggestion for it?</p><pre><code>99&gt;ClCompile:
         byte_view_tab.cpp
         byte_view_text.cpp
         capture_file.cpp
         capture_file_dialog.cpp
   109&gt;CustomBuild:
         flex: could not create --header-file=./_lex.h
         /usr/bin/flex.exe failed: exit status 1
   107&gt;CustomBuild:
         flex: could not create --header-file=./_lex.h
         /usr/bin/flex.exe failed: exit status 1
   109&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1 。 [e:\Development\wsbuild64\wiretap\wiretap.vcxproj]</code></pre></div><div id="comment-56722-info" class="comment-info"><span class="comment-age">(26 Oct '16, 20:51)</span> scdma</div></div><span id="56725"></span><div id="comment-56725" class="comment"><div id="post-56725-score" class="comment-score"></div><div class="comment-text"><p>I think you meant to write the above answer as a comment!</p></div><div id="comment-56725-info" class="comment-info"><span class="comment-age">(26 Oct '16, 22:53)</span> koundi</div></div><span id="56726"></span><div id="comment-56726" class="comment"><div id="post-56726-score" class="comment-score"></div><div class="comment-text"><p>Still not sure what's up with the docbook issue, but for the flex issue it seems that the build hasn't picked up win_flex as it is still using the Cygwin flex.</p><p>Can you please delete and recreate your build directory, rerun the CMake generation step and then try the build again this time removing the <code>/m</code> flag from the msbuild command line.</p></div><div id="comment-56726-info" class="comment-info"><span class="comment-age">(26 Oct '16, 23:18)</span> grahamb ♦</div></div></div><div id="comment-tools-56682" class="comment-tools"></div><div class="clear"></div><div id="comment-56682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

