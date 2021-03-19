+++
type = "question"
title = "Error with ./autogen.sh &quot;Custom.m4 does not exist&quot;"
description = '''I&#x27;m trying to add my own plugin to the wireshark build. I followed all the instructions in README.plugins down to a tee.  When I try to run ./autogen.sh I get an error saying:  Checking for python. aclocal -I ./aclocal-fallback configure.in:1761: file `plugins/Custom.m4&#x27; does not exist  Previously w...'''
date = "2011-02-07T09:42:00Z"
lastmod = "2011-02-07T09:55:00Z"
weight = 2198
keywords = [ "custom.m4", "autogen.sh", "plugins" ]
aliases = [ "/questions/2198" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error with ./autogen.sh "Custom.m4 does not exist"](/questions/2198/error-with-autogensh-customm4-does-not-exist)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2198-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to add my own plugin to the wireshark build. I followed all the instructions in README.plugins down to a tee.</p><p>When I try to run ./autogen.sh I get an error saying:</p><blockquote><p>Checking for python. aclocal -I ./aclocal-fallback configure.in:1761: file `plugins/Custom.m4' does not exist</p></blockquote><p>Previously when I got the error(when I wasn't trying to add a plugin) I just skipped that one and went with ./configure and the build worked. However if I do that now the configure doesn't create a plugins/xxx/Makefile for my plugin.</p><p>What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags">custom.m4 autogen.sh plugins</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '11, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/3d3535b19a6debac9e2b855465a2027b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rodayo&#39;s gravatar image" /><p>Rodayo<br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rodayo has no accepted answers">0%</span></p></div></div><div id="comments-container-2198" class="comments-container"></div><div id="comment-tools-2198" class="comment-tools"></div><div class="clear"></div><div id="comment-2198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2201"></span>

<div id="answer-container-2201" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2201-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>So I tried to combat that issue, by going into configure and manually adding my own entries for my plugin. I just followed the format it used for the other plugins.</p><p>Now ./configure creates the makefile but when I run 'make' I get this error:</p><blockquote><p>cd . &amp;&amp; /bin/bash /home/negrabee/Downloads/wireshark-1.4.3/missing --run aclocal-1.9 <code>./aclocal-flags</code> configure.in:1761: file `plugins/Custom.m4' does not exist make: *** [aclocal.m4] Error 1</p></blockquote></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '11, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/3d3535b19a6debac9e2b855465a2027b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rodayo&#39;s gravatar image" /><p>Rodayo<br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rodayo has no accepted answers">0%</span></p></div></div><div id="comments-container-2201" class="comments-container"></div><div id="comment-tools-2201" class="comment-tools"></div><div class="clear"></div><div id="comment-2201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

