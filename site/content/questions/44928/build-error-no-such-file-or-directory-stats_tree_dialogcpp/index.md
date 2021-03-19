+++
type = "question"
title = "Build error &#x27;No such file or directory: &#x27;./stats_tree_dialog.cpp&#x27;&#x27;"
description = '''I build QtShark.pro with Qt5.4 and got the error below: C:&#92;Python27&#92;python.exe ../../tools/make-tap-reg.py . taps stats_tree_dialog.cpp Traceback (most recent call last): File &quot;../../tools/make-tap-reg.py&quot;, line 108, in &amp;lt;module&amp;gt; file = open(filename) IOError: [Errno 2] No such file or director...'''
date = "2015-08-07T18:19:00Z"
lastmod = "2015-08-09T05:21:00Z"
weight = 44928
keywords = [ "build_error" ]
aliases = [ "/questions/44928" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Build error 'No such file or directory: './stats\_tree\_dialog.cpp''](/questions/44928/build-error-no-such-file-or-directory-stats_tree_dialogcpp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44928-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I build QtShark.pro with Qt5.4 and got the error below:</p><p>C:\Python27\python.exe ../../tools/make-tap-reg.py . taps stats_tree_dialog.cpp Traceback (most recent call last): File "../../tools/make-tap-reg.py", line 108, in &lt;module&gt; file = open(filename) IOError: [Errno 2] No such file or directory: './stats_tree_dialog.cpp'</p><p>I google a long time and nothing found. Could anyone give me any suggestion?</p><p>By the way 1. My code directory is C:\Dev\Wireshark 2. The build step seems ok, i use the same step build wireshark successfully.</p></div><div id="question-tags" class="tags-container tags">build_error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '15, 18:19</strong></p><img src="https://secure.gravatar.com/avatar/f297701b92f28ff81d3843b96d7c718c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="1330&#39;s gravatar image" /><p>1330<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="1330 has no accepted answers">0%</span></p></div></div><div id="comments-container-44928" class="comments-container"></div><div id="comment-tools-44928" class="comment-tools"></div><div class="clear"></div><div id="comment-44928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44938"></span>

<div id="answer-container-44938" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44938-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I build QtShark.pro with Qt5.4 and got the error below:</p></blockquote><p>Ok, stop doing that and build using the recommended methods, either nmake for 1.12.x or CMake for the development branch (currently 1.99.x). See the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/">Developers Guide</a> for more info (and README.cmake for CMake).</p><p>Are you building 1.12.x or development (1.99.x)? If its 1.12.x, don't both with the Qt version as it's not supported and rather buggy.</p><p>Are you building using a tarball or git? If from a tarball and it's the dev branch, then you might have got a "bad" one, get a later one, or even better switch to using git and keep your repo up to date.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '15, 05:21</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44938" class="comments-container"></div><div id="comment-tools-44938" class="comment-tools"></div><div class="clear"></div><div id="comment-44938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

