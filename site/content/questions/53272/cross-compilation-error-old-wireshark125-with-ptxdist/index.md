+++
type = "question"
title = "Cross Compilation error old wireshark(1.2.5) with ptxdist"
description = '''Hey guys, I&#x27;m trying to compile Wireshark 1.2.5 with ptxdist (version 2011.08.0) on an ubuntu 14.04 64-bit and I am facing compilation error. (target architecture is ARM 32-bit). In one of the stages it tries to run tshark (which is built in a earlier stage) and it fails: make[4]: Entering directory...'''
date = "2016-06-07T04:05:00Z"
lastmod = "2016-06-07T04:05:00Z"
weight = 53272
keywords = [ "wireshark-1.2.5" ]
aliases = [ "/questions/53272" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cross Compilation error old wireshark(1.2.5) with ptxdist](/questions/53272/cross-compilation-error-old-wireshark125-with-ptxdist)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53272-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys, I'm trying to compile Wireshark 1.2.5 with ptxdist (version 2011.08.0) on an ubuntu 14.04 64-bit and I am facing compilation error. (target architecture is ARM 32-bit).</p><p>In one of the stages it tries to run tshark (which is built in a earlier stage) and it fails:</p><pre><code>make[4]: Entering directory &#39;&lt;my-build-path&gt;/wireshark-1.2.5/doc&#39;
WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1 ../tshark -G fields | /usr/bin/perl ./dfilter2pod.pl ./wireshark-filter.pod.template &gt; wireshark-filter.pod
/bin/sh: ../tshark: cannot execute binary file Exec format error</code></pre><p>Any ideas? Thanks.</p><p>Edit: In fact I have no use with the docs, I wouldn't mind to skip them - is that an option?</p></div><div id="question-tags" class="tags-container tags">wireshark-1.2.5</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '16, 04:05</strong></p><img src="https://secure.gravatar.com/avatar/01b9c2ec13dd5bd40f6c076b52019f3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AndyTH&#39;s gravatar image" /><p>AndyTH<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AndyTH has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Jun '16, 05:00</p></div></div><div id="comments-container-53272" class="comments-container"></div><div id="comment-tools-53272" class="comment-tools"></div><div class="clear"></div><div id="comment-53272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

