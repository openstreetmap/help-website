+++
type = "question"
title = "Compile a Dissector on OS X"
description = '''I am on step 9.2.1 here. My question is on how to build the dissector on my Mac. I&#x27;m vaguely running into ideas about using automake/autoconf. Is this necessary? If so, premade plugins like gryphon don&#x27;t allow me to build them as well. There seems to be a need for much more than just a Makefile.am f...'''
date = "2015-01-29T04:22:00Z"
lastmod = "2015-01-29T05:06:00Z"
weight = 39475
keywords = [ "macosx", "dissector", "autotools" ]
aliases = [ "/questions/39475" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Compile a Dissector on OS X](/questions/39475/compile-a-dissector-on-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39475-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am on step 9.2.1 <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html">here</a>. My question is on how to build the dissector on my Mac. I'm vaguely running into ideas about using automake/autoconf. Is this necessary? If so, premade plugins like gryphon don't allow me to build them as well. There seems to be a need for much more than just a Makefile.am file.</p></div><div id="question-tags" class="tags-container tags">macosx dissector autotools</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '15, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/e1281ae119e0fd394d058e6d97b0a660?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Erronsing&#39;s gravatar image" /><p>Erronsing<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Erronsing has no accepted answers">0%</span></p></div></div><div id="comments-container-39475" class="comments-container"></div><div id="comment-tools-39475" class="comment-tools"></div><div class="clear"></div><div id="comment-39475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39476"></span>

<div id="answer-container-39476" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39476-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you completed the first part of the Development Guide e.g. <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSrcBuildFirstTime.html#_building_on_unix">Sec 3.5.1</a> which discusses using configure to create Makefile from the Makefile.am templates.</p><p>If you haven't worked your way through Sect 2 &amp; 3, then you need to do so first to create\prove your build environment before attempting to add your own dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '15, 05:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39476" class="comments-container"><span id="39544"></span><div id="comment-39544" class="comment"><div id="post-39544-score" class="comment-score"></div><div class="comment-text"><p>Hello. Trying to run ./autogen.sh grants me this mesage: Useless use of /d modifier in transliteration operator at /usr/local/share/automake-1.9/Automake/Wrap.pm line 60. aclocal -I ./aclocal-fallback -I /usr/local/pkg-config/share/aclocal configure.ac:2975: file `plugins/Custom.m4' does not exist</p></div><div id="comment-39544-info" class="comment-info"><span class="comment-age">(02 Feb '15, 03:14)</span> Erronsing</div></div><span id="39556"></span><div id="comment-39556" class="comment"><div id="post-39556-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark are you trying to build? Are you building from a tarball? do you have a file plugins/Custom.m4?</p></div><div id="comment-39556-info" class="comment-info"><span class="comment-age">(02 Feb '15, 07:28)</span> Anders ♦</div></div><span id="39663"></span><div id="comment-39663" class="comment"><div id="post-39663-score" class="comment-score"></div><div class="comment-text"><p>The wireshark version was cloned from <a href="https://code.wireshark.org/review/wireshark.">https://code.wireshark.org/review/wireshark.</a> It's just a folder, not a tarball.I have a file plugins/Custom.m4.example. Is this something I should look into and/or rename to Custom.m4?Simply removing .example gives me file `asn1/Custom.m4' does not exist. I'm going to try to just add this file whereever this message pops up.</p></div><div id="comment-39663-info" class="comment-info"><span class="comment-age">(05 Feb '15, 05:37)</span> Erronsing</div></div></div><div id="comment-tools-39476" class="comment-tools"></div><div class="clear"></div><div id="comment-39476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

