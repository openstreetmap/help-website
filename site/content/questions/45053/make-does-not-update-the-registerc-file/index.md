+++
type = "question"
title = "make does not update the register.c file"
description = '''Every time I hit &#x27;make&#x27;, I get this output: make -k Making register.c Registering 1285 files, 1285 cached Cache hits: 1284, misses: 1 register.c unchanged. make all-recursive  And indeed, my plugin output and its behavior does not change. I need to invoke &quot;./configure; make;&quot; in order to apply my ch...'''
date = "2015-08-13T05:41:00Z"
lastmod = "2015-08-13T05:41:00Z"
weight = 45053
keywords = [ "dissector" ]
aliases = [ "/questions/45053" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [make does not update the register.c file](/questions/45053/make-does-not-update-the-registerc-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45053-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Every time I hit 'make', I get this output:</p><pre><code>make -k
Making register.c
Registering 1285 files, 1285 cached
Cache hits: 1284, misses: 1
register.c unchanged.
make  all-recursive</code></pre><p>And indeed, my plugin output and its behavior does not change. I need to invoke "./configure; make;" in order to apply my changes to the plugin.</p><p>Is there a proper way to do that?</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '15, 05:41</strong></p><img src="https://secure.gravatar.com/avatar/b6ce7a43b172768e46dcbe233f772931?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yves_paris&#39;s gravatar image" /><p>yves_paris<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yves_paris has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Aug '15, 06:08</p></div></div><div id="comments-container-45053" class="comments-container"><span id="45096"></span><div id="comment-45096" class="comment"><div id="post-45096-score" class="comment-score"></div><div class="comment-text"><p>why the '-k' ?</p></div><div id="comment-45096-info" class="comment-info"><span class="comment-age">(14 Aug '15, 01:09)</span> Jaap ♦</div></div><span id="45099"></span><div id="comment-45099" class="comment"><div id="post-45099-score" class="comment-score"></div><div class="comment-text"><p>It's emacs' default command for compiling any project.</p></div><div id="comment-45099-info" class="comment-info"><span class="comment-age">(14 Aug '15, 01:38)</span> yves_paris</div></div><span id="45103"></span><div id="comment-45103" class="comment"><div id="post-45103-score" class="comment-score"></div><div class="comment-text"><p>It does not say how it's making register.c. How old is this Wireshark version you try to build?</p></div><div id="comment-45103-info" class="comment-info"><span class="comment-age">(14 Aug '15, 02:55)</span> Jaap ♦</div></div><span id="45108"></span><div id="comment-45108" class="comment"><div id="post-45108-score" class="comment-score"></div><div class="comment-text"><p>I'm on this git commit now:</p><p>commit 46d6e8c Author: Stig Bjørlykke [email protected] Date: Fri Aug 14 14:48:49 2015 +0200</p><pre><code>Added some missing breaks</code></pre></div><div id="comment-45108-info" class="comment-info"><span class="comment-age">(14 Aug '15, 07:06)</span> yves_paris</div></div><span id="45110"></span><div id="comment-45110" class="comment"><div id="post-45110-score" class="comment-score"></div><div class="comment-text"><p>I am going to try with the 'cmake' approach, and see whether it solves that issue.</p></div><div id="comment-45110-info" class="comment-info"><span class="comment-age">(14 Aug '15, 07:21)</span> yves_paris</div></div><span id="45113"></span><div id="comment-45113" class="comment not_top_scorer"><div id="post-45113-score" class="comment-score"></div><div class="comment-text"><p>Oke, so what do we know. The build (through make) is running, when creating register.c it sees that a file is changed (your dissector I presume) because it says it has 1 cache miss (because it has a new timestamp). Still register.c is unchanged because your dissector hooks for registration are unchanged. This all has nothing to do with your inability to see the new functionality! It either means it is not linked into the final binary/library, or you're running a previous installment. So, make sure you've setup all the changes to the build environment to get you dissector compiled and included; and make sure you're loading the right version when testing.</p></div><div id="comment-45113-info" class="comment-info"><span class="comment-age">(14 Aug '15, 07:57)</span> Jaap ♦</div></div></div><div id="comment-tools-45053" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-45053-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

