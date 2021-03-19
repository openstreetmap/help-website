+++
type = "question"
title = "64-bit installer"
description = '''Is there one installer that will work for both 64-bit and 32-bit OS?'''
date = "2011-09-22T16:25:00Z"
lastmod = "2011-09-22T22:52:00Z"
weight = 6497
keywords = [ "installer", "compatibility", "64-bit" ]
aliases = [ "/questions/6497" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [64-bit installer](/questions/6497/64-bit-installer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6497-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there one installer that will work for both 64-bit and 32-bit OS?</p></div><div id="question-tags" class="tags-container tags">installer compatibility 64-bit</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '11, 16:25</strong></p><img src="https://secure.gravatar.com/avatar/c6b210f20ae8fc2a9972f9ea5724785c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Averyb&#39;s gravatar image" /><p>Averyb<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Averyb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Sep '11, 15:31</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6497" class="comments-container"></div><div id="comment-tools-6497" class="comment-tools"></div><div class="clear"></div><div id="comment-6497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6498"></span>

<div id="answer-container-6498" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6498-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The 32-bit installer will work on both. Get the latest version from the <a href="http://www.wireshark.org/download.html">download</a> page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '11, 17:53</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-6498" class="comments-container"></div><div id="comment-tools-6498" class="comment-tools"></div><div class="clear"></div><div id="comment-6498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6501"></span>

<div id="answer-container-6501" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6501-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is, as far as I know, no Windows installer that will install a 32-bit version of Wireshark on a 32-bit system and a 64-bit version of Wireshark on a 64-bit system. However, as Chris Maynard notes, the 32-bit installer will install a 32-bit version of Wireshark on a 32-bit or 64-bit system, and the 32-bit version will work on a 64-bit system, albeit with a smaller address space, so it won't be able to read as large files as the 64-bit version can.</p><p>If you're not talking about Windows:</p><ul><li><p>For Mac OS X, we don't have any "fat" package that includes both 32-bit and 64-bit binaries.</p></li><li><p>We have no other binary installers; I don't know what third-party installer packages do on other OSes, but I suspect they have separate packages for separate instruction sets, and treat 32-bit and 64-bit instruction sets as separate.</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '11, 22:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-6501" class="comments-container"><span id="6504"></span><div id="comment-6504" class="comment"><div id="post-6504-score" class="comment-score"></div><div class="comment-text"><p>Indeed, looking at the Debian package for instance, it provides individual packages for the following architectures:</p><ul><li>amd64</li><li>armel</li><li>i386</li><li>ia64</li><li>kfreebsd-amd64</li><li>kfreebsd-i386</li><li>mips</li><li>mipsel</li><li>powerpc</li><li>s390</li><li>sparc</li></ul><p>with Ubuntu limiting itself to i368 and ia64.</p></div><div id="comment-6504-info" class="comment-info"><span class="comment-age">(23 Sep '11, 01:32)</span> Jaap ♦</div></div></div><div id="comment-tools-6501" class="comment-tools"></div><div class="clear"></div><div id="comment-6501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

