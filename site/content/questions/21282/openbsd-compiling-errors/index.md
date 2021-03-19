+++
type = "question"
title = "openbsd compiling errors"
description = '''During the gmake process while attempting to compile ver 1.8.7 of wireshark on an OpenBSD 5.3 platform I get the following errors: cc1: out of memory allocating 4072 bytes after a total of 0 bytes gmake[5]: *** [packet-parlay.lo] Error 1 gmake[5]: Leaving directory &#x27;/home/..../wireshark-1.8.7/epan/d...'''
date = "2013-05-19T19:31:00Z"
lastmod = "2013-05-20T07:15:00Z"
weight = 21282
keywords = [ "compiling", "openbsd", "errors" ]
aliases = [ "/questions/21282" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [openbsd compiling errors](/questions/21282/openbsd-compiling-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21282-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>During the gmake process while attempting to compile ver 1.8.7 of wireshark on an OpenBSD 5.3 platform I get the following errors:</p><pre><code>cc1: out of memory allocating 4072 bytes after a total of 0 bytes
gmake[5]: *** [packet-parlay.lo] Error 1
gmake[5]: Leaving directory &#39;/home/..../wireshark-1.8.7/epan/dissectors
gmake[5]: *** [all-recursive] Error 1
gmake[5]: Leaving directory &#39;/home/..../wireshark-1.8.7/epan/dissectors
gmake[5]: *** [all] Error 2</code></pre><p>Any thoughts?</p></div><div id="question-tags" class="tags-container tags">compiling openbsd errors</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '13, 19:31</strong></p><img src="https://secure.gravatar.com/avatar/5d3a9a7be31e1f4ed2a88105ebfb3774?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="junebug&#39;s gravatar image" /><p>junebug<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="junebug has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 May '13, 23:01</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-21282" class="comments-container"></div><div id="comment-tools-21282" class="comment-tools"></div><div class="clear"></div><div id="comment-21282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21283"></span>

<div id="answer-container-21283" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21283-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>If you don't care about the <a href="http://en.wikipedia.org/wiki/Parlay_Group">Parlay protocol</a> (if you don't know what it is, you probably don't care about it), edit <code>epan/dissectors/Makefile.common</code> and remove <code>packet-parlay.c</code> from the list in which it appears.</li><li>Repartition your disk to have a significantly larger swap partition and hope that's enough.</li><li>Buy a lot more memory and hope that's enough.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '13, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-21283" class="comments-container"></div><div id="comment-tools-21283" class="comment-tools"></div><div class="clear"></div><div id="comment-21283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21308"></span>

<div id="answer-container-21308" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21308-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>4) Upgrade to 1.10.0rc1 or a development release. The Parlay dissector has 35% lines of code in those versions ("only" 68,000). That <em>might</em> help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '13, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 May '13, 07:15</p></div></div><div id="comments-container-21308" class="comments-container"></div><div id="comment-tools-21308" class="comment-tools"></div><div class="clear"></div><div id="comment-21308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

