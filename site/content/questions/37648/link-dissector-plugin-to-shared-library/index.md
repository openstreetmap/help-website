+++
type = "question"
title = "Link dissector plugin to shared library."
description = '''I am writing a dissector for protocol, that has most of its data compressed with lz4 compression. The thing I need to do is to link my plug-in with external lz4 shared library to uncompress the compressed data. (liblz4-dev on Ubuntu)  The problem is that unfortunately I don&#x27;t understand the Wireshar...'''
date = "2014-11-07T05:43:00Z"
lastmod = "2014-11-10T23:54:00Z"
weight = 37648
keywords = [ "development", "dissector", "build", "plugin", "linux" ]
aliases = [ "/questions/37648" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Link dissector plugin to shared library.](/questions/37648/link-dissector-plugin-to-shared-library)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37648-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a dissector for protocol, that has most of its data compressed with lz4 compression. The thing I need to do is to link my plug-in with external lz4 shared library to uncompress the compressed data. (liblz4-dev on Ubuntu)</p><p>The problem is that unfortunately I don't understand the Wireshark Autools build system very well and I can't figure it out how to do it. I always get the following error, when I start the wireshark.</p><pre><code> Couldn&#39;t load module /usr/local/lib/wireshark/plugins/1.99.1/test.so: /usr/local/lib/wireshark/plugins/1.99.1/test.so: undefined symbol: LZ4_decompress_safe</code></pre><p>I have tried to change plugins/plugin_name/Makefile.am without any success. LIBS = -llz4</p><p>I would be very grateful if somebody could explain me how to do it? How do I link plug in with another shared library?</p></div><div id="question-tags" class="tags-container tags">development dissector build plugin linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '14, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/d269dbda83b14ddc1e1d1081d1eff25c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miha87&#39;s gravatar image" /><p>miha87<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miha87 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Nov '14, 00:23</p></div></div><div id="comments-container-37648" class="comments-container"><span id="37682"></span><div id="comment-37682" class="comment"><div id="post-37682-score" class="comment-score"></div><div class="comment-text"><p>What's printed if you run the command</p><pre><code>ldd /usr/local/lib/wireshark/plugins/1.99.1/visionect2.so</code></pre></div><div id="comment-37682-info" class="comment-info"><span class="comment-age">(07 Nov '14, 19:12)</span> Guy Harris ♦♦</div></div><span id="37687"></span><div id="comment-37687" class="comment"><div id="post-37687-score" class="comment-score"></div><div class="comment-text"><p>Nobody has the answer?</p><p>I was sure it is trivial and that it is jut me who can't figure it out. Anyway I'm sure I'm not the first one with this problem and I am not he first one who wants to link his plugin with some external lib.</p></div><div id="comment-37687-info" class="comment-info"><span class="comment-age">(07 Nov '14, 23:58)</span> miha87</div></div><span id="37688"></span><div id="comment-37688" class="comment"><div id="post-37688-score" class="comment-score"></div><div class="comment-text"><p>Perhaps nobody has enough information to give you an answer. You were asked a question; perhaps the answer to the question you were asked will help somebody give you an answer.</p><blockquote><p>I was sure it is trivial</p></blockquote><p>Perhaps it isn't.</p></div><div id="comment-37688-info" class="comment-info"><span class="comment-age">(08 Nov '14, 00:09)</span> Guy Harris ♦♦</div></div><span id="37689"></span><div id="comment-37689" class="comment"><div id="post-37689-score" class="comment-score"></div><div class="comment-text"><p>Sorry I have somehow managed to miss your question. I am sorry again. My mistake. I will post the answer ass soon as I get to may computer. :) Thank you</p></div><div id="comment-37689-info" class="comment-info"><span class="comment-age">(08 Nov '14, 04:22)</span> miha87</div></div></div><div id="comment-tools-37648" class="comment-tools"></div><div class="clear"></div><div id="comment-37648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37744"></span>

<div id="answer-container-37744" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37744-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ok I have found the solution that works for me. Actually the steps are the same as before. I have probably spiked something before and this is the reason I had problems before. If you add dependency you should probably go trough all described steps again.</p><ol><li><p>Add dependency to the plugin/[plugin_name]/Makefile.am LIBS variable. (already exists but is empty)</p><p>LIBS = -llz4</p></li><li><p>run autogen.sh script again.</p><p>$./autogen.sh</p></li><li><p>and then new generated configure script</p><p>$./configure</p></li><li><p>And finally make. I am not sure if running "make -C plugins" is sufficient.</p><p>$make</p></li><li><p>If you want to install</p></li></ol><p>$sudo make install</p><ol><li><p>Once you do this you do not need to go trough all steps again to recompile. Just do.</p><p>$make</p><p>and optimally</p><p>$sudo make install</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '14, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/d269dbda83b14ddc1e1d1081d1eff25c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miha87&#39;s gravatar image" /><p>miha87<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miha87 has no accepted answers">0%</span></p></div></div><div id="comments-container-37744" class="comments-container"></div><div id="comment-tools-37744" class="comment-tools"></div><div class="clear"></div><div id="comment-37744-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

