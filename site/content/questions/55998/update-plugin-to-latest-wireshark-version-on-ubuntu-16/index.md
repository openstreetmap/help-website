+++
type = "question"
title = "Update plugin to latest wireshark version on ubuntu 16"
description = '''I have a wireshark plugin code which compiles and generates .so files perfectly under Ubuntu 16. This dissector was written for wireshark 1.6 and the plugin runs perfectly under wireshark 1.6. However when I try to use this plugin for wireshark 2(or any wireshark version higher than 1.6) following e...'''
date = "2016-09-30T01:43:00Z"
lastmod = "2016-09-30T02:43:00Z"
weight = 55998
keywords = [ "wireshark", "dissector", "update", "plugin", "ubuntu" ]
aliases = [ "/questions/55998" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Update plugin to latest wireshark version on ubuntu 16](/questions/55998/update-plugin-to-latest-wireshark-version-on-ubuntu-16)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55998-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a wireshark plugin code which compiles and generates .so files perfectly under Ubuntu 16. This dissector was written for wireshark 1.6 and the plugin runs perfectly under wireshark 1.6.</p><p>However when I try to use this plugin for wireshark 2(or any wireshark version higher than 1.6) following errors show -</p><pre><code>&gt; Couldn&#39;t load module
&gt; /home/th89ct/.config/wireshark/plugins/plugin-1_0_0.so:
&gt; /home/th89ct/.config/wireshark/plugins/plugin-1_0_0.so:
&gt; undefined symbol: tvb_length Couldn&#39;t
&gt; load module
&gt; /home/th89ct/.config/wireshark/plugins/plugin--1_0_0.so:
&gt; /home/th89ct/.config/wireshark/plugins/plugin--1_0_0.so:
&gt; undefined symbol: check_col</code></pre><p>so I wanted to edit the code by replacing the methods - as after googling I've found that these methods do not belong to the new wireshark API.</p><p>but the problem is every time I edit the code - even by only putting a space in a blank space - following error appears -</p><pre><code>&gt; gcc -c -DHAVE_CONFIG_H
&gt; -I/usr/include/wireshark -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include
&gt; -DINET6 -D_U_=attribute((unused)) -Wall -Wpointer-arith -g -DXTHREADS -D_REENTRANT -DXUSE_MTSAFE_API -fPIC -DPIC packet-ife.c -o packet-ife.o packet-ife.c:105:23: fatal error:
&gt; epan/emem.h: No such file or directory
&gt; #include ^ compilation terminated. Makefile.linux:28: recipe for target
&gt; &#39;packet-ife.o&#39; failed make: **
&gt; [packet-ife.o] Error 1*</code></pre><p>what should I do? I am in bad need for help. I have no idea what to do!!!! Thanks in advance</p></div><div id="question-tags" class="tags-container tags">wireshark dissector update plugin ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '16, 01:43</strong></p><img src="https://secure.gravatar.com/avatar/a908c48c60a3ba8f08a762a9cb58268f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xaheen&#39;s gravatar image" /><p>xaheen<br />
<span class="score" title="71 reputation points">71</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xaheen has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Sep '16, 02:38</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-55998" class="comments-container"></div><div id="comment-tools-55998" class="comment-tools"></div><div class="clear"></div><div id="comment-55998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55999"></span>

<div id="answer-container-55999" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55999-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The binary interface between Wireshark and plugins has changed considerably between 1.6 and 2.0, so coding changes will have to be made in the plug-in. Your options are:</p><ol><li>Make the code changes yourself, which you seem to have run into difficulties with.</li><li>Post the code somewhere public and ask for help to fix the issues, which would then allow the dissector to be moved into and distributed with Wireshark.</li><li>If you are unwilling to release the dissector code publically you can hire someone to fix it under some form of NDA, as long as you observe the GPL licence that Wireshark is distributed under (basically if you distribute the plugin to anyone other than your company, then you must also make the source code available).</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '16, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-55999" class="comments-container"><span id="56000"></span><div id="comment-56000" class="comment"><div id="post-56000-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your responce. Sadly I can't make the code public as I have aggrement with my Company. I have been trying to edit the old code, but as I've said, it's showing Errors even if I put a blank space at the end of the code... Why do you think this is occuring???</p></div><div id="comment-56000-info" class="comment-info"><span class="comment-age">(30 Sep '16, 02:48)</span> xaheen</div></div><span id="56001"></span><div id="comment-56001" class="comment"><div id="post-56001-score" class="comment-score">1</div><div class="comment-text"><p>Because the Wireshark interface with plugins has changed, you must make the appropriate changes in the plugin to allow it to compile.</p><p>Unfortunately it's pretty much impossible for anyone to help without seeing the plugin code.</p><p>What you can do is look at each error, look back at the release notes for each major change, i.e. 1.6 -&gt; 1.8, 1.8 &gt; 1.10 etc. to determine what has changed and how to fix it.</p><p>For the error you show <code>packet-ife.c:105:23: fatal error: emem.h: No such file or directory</code>, that is caused by a change in the memory manager used by Wireshark from emem to wmem in Wireshark 2.0, see the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=doc/README.wmem">README.wmem</a> file in the doc directory of the sources for more info.</p><p>I suspect that you'll have a lot of other changes to do though.</p></div><div id="comment-56001-info" class="comment-info"><span class="comment-age">(30 Sep '16, 03:03)</span> grahamb ♦</div></div><span id="56006"></span><div id="comment-56006" class="comment"><div id="post-56006-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your time and answer :) I think i have a lot of work to do :/</p></div><div id="comment-56006-info" class="comment-info"><span class="comment-age">(30 Sep '16, 05:02)</span> xaheen</div></div><span id="56009"></span><div id="comment-56009" class="comment"><div id="post-56009-score" class="comment-score"></div><div class="comment-text"><p>do you know about any wireshark online course for wireshark development?</p></div><div id="comment-56009-info" class="comment-info"><span class="comment-age">(30 Sep '16, 05:38)</span> xaheen</div></div><span id="56011"></span><div id="comment-56011" class="comment"><div id="post-56011-score" class="comment-score">1</div><div class="comment-text"><p>I do a <a href="https://sharkfest.wireshark.org/assets/presentations16/03.7z">presentation</a> about how to start writing dissectors at SharkFest, but it's very basic and won't answer any of your questions. I'm not aware of any on-line courses on dissector implementation, although there are a few articles\blog posts that are mostly out of date.</p><p>The resources I know of are the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/">Developers Guide</a> and the documents in the sources <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=tree;f=doc">doc</a> directory and the 1300+ dissector source files as examples in the Wireshark sources (epan/dissectors/packet-xxx.c)</p></div><div id="comment-56011-info" class="comment-info"><span class="comment-age">(30 Sep '16, 05:53)</span> grahamb ♦</div></div><span id="56178"></span><div id="comment-56178" class="comment not_top_scorer"><div id="post-56178-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your elaborate and resourceful answer. I will try my best to make the best out of it. I wish there were some tutorial for updating the old code!</p></div><div id="comment-56178-info" class="comment-info"><span class="comment-age">(06 Oct '16, 01:39)</span> xaheen</div></div><span id="56180"></span><div id="comment-56180" class="comment not_top_scorer"><div id="post-56180-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately that's one of the costs of keeping your dissector private, you have to maintain it yourself.</p><p>One way to sensibly keep up to date is to setup a continuous build system that compiles your plugin frequently and then you'll know when breaking changes have been made and you can easily see which commits caused the issues.</p><p>Leaving the dissector fallow for many major version releases, i.e. 1.6 -&gt; 1.8 -&gt; 1.10 -&gt; 1.12 -&gt; 2.0 -&gt; 2.2 is quite likely to have lots of issues to be fixed up.</p></div><div id="comment-56180-info" class="comment-info"><span class="comment-age">(06 Oct '16, 02:29)</span> grahamb ♦</div></div></div><div id="comment-tools-55999" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-55999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

