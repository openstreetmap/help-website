+++
type = "question"
title = "add error with bignumbers in lua"
description = '''Hi guys, i have a problems doing the operation add with numbers of 64 bits the following code return a incorrect value: report_failure(string.format(&quot;%16x&quot;, ((0xfefefefe * math.pow(2,32))+0xabababab)))  this code should be return a window with the value fefefefeabababab, but return fefefefeababa800 ...'''
date = "2013-11-27T06:24:00Z"
lastmod = "2013-11-27T11:25:00Z"
weight = 27489
keywords = [ "lua", "math", "error" ]
aliases = [ "/questions/27489" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [add error with bignumbers in lua](/questions/27489/add-error-with-bignumbers-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27489-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, i have a problems doing the operation add with numbers of 64 bits</p><p>the following code return a incorrect value:</p><pre><code>report_failure(string.format(&quot;%16x&quot;, ((0xfefefefe * math.pow(2,32))+0xabababab)))</code></pre><p>this code should be return a window with the value <em>fefefefeabababab</em>, but return <em>fefefefeababa800</em></p><p>any idea?</p></div><div id="question-tags" class="tags-container tags">lua math error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '13, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/1b78887a0db6906cea1d126a0a9f2eac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Javier%20Aguinaga&#39;s gravatar image" /><p>Javier Aguinaga<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Javier Aguinaga has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Nov '13, 06:34</p></div></div><div id="comments-container-27489" class="comments-container"></div><div id="comment-tools-27489" class="comment-tools"></div><div class="clear"></div><div id="comment-27489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27507"></span>

<div id="answer-container-27507" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27507-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://lua-users.org/wiki/NumbersTutorial">Lua stores all numbers</a> (internally) as floats (by default double-precision floating point numbers). So you can't do 64-bit math very well in Lua. For some more details see <a href="https://www.wireshark.org/lists/wireshark-bugs/201309/msg00570.html">this email</a> on the wireshark-users mailing list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '13, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-27507" class="comments-container"><span id="27509"></span><div id="comment-27509" class="comment"><div id="post-27509-score" class="comment-score"></div><div class="comment-text"><p>thanks, i'll see the links</p></div><div id="comment-27509-info" class="comment-info"><span class="comment-age">(27 Nov '13, 12:00)</span> Javier Aguinaga</div></div></div><div id="comment-tools-27507" class="comment-tools"></div><div class="clear"></div><div id="comment-27507-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

