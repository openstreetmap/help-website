+++
type = "question"
title = "WS_VAR_IMPORT does not name a type"
description = '''While compiling the dissector on linux i am getting the fallowing error does anybody know the solution to this wireshark-1.4.7/epan/prefs.h:167: error: WS_VAR_IMPORT does not name a type'''
date = "2011-07-17T23:58:00Z"
lastmod = "2011-07-18T01:51:00Z"
weight = 5086
keywords = [ "linux" ]
aliases = [ "/questions/5086" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WS\_VAR\_IMPORT does not name a type](/questions/5086/ws_var_import-does-not-name-a-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5086-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While compiling the dissector on linux i am getting the fallowing error does anybody know the solution to this</p><p><strong>wireshark-1.4.7/epan/prefs.h:167: error: WS_VAR_IMPORT does not name a type</strong></p></div><div id="question-tags" class="tags-container tags">linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '11, 23:58</strong></p><img src="https://secure.gravatar.com/avatar/257c9f9e498193d7ddde57090efe094a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sagu072&#39;s gravatar image" /><p>sagu072<br />
<span class="score" title="35 reputation points">35</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sagu072 has no accepted answers">0%</span></p></div></div><div id="comments-container-5086" class="comments-container"></div><div id="comment-tools-5086" class="comment-tools"></div><div class="clear"></div><div id="comment-5086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5090"></span>

<div id="answer-container-5090" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5090-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Make sure to include config.h before prefs.h in your dissector, like so:</p><pre><code>#ifdef HAVE_CONFIG_H
# include &quot;config.h&quot;
#endif</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '11, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jul '11, 01:52</p></div></div><div id="comments-container-5090" class="comments-container"><span id="5091"></span><div id="comment-5091" class="comment"><div id="post-5091-score" class="comment-score"></div><div class="comment-text"><p>I have included that but still getting the error. my code is in C++, so do i need to use both g++ and gcc compilers ?</p></div><div id="comment-5091-info" class="comment-info"><span class="comment-age">(18 Jul '11, 01:56)</span> sagu072</div></div><span id="5099"></span><div id="comment-5099" class="comment"><div id="post-5099-score" class="comment-score"></div><div class="comment-text"><p>Note Wireshark is a C project, no C++.</p><p>Did you work with namespaces?</p></div><div id="comment-5099-info" class="comment-info"><span class="comment-age">(18 Jul '11, 04:16)</span> Jaap ♦</div></div><span id="5101"></span><div id="comment-5101" class="comment"><div id="post-5101-score" class="comment-score"></div><div class="comment-text"><p>ya i do use namespace and i have included that in source.</p></div><div id="comment-5101-info" class="comment-info"><span class="comment-age">(18 Jul '11, 05:33)</span> sagu072</div></div><span id="5106"></span><div id="comment-5106" class="comment"><div id="post-5106-score" class="comment-score"></div><div class="comment-text"><p>Then you may be doing that wrong. See <a href="http://stackoverflow.com/questions/1761018/does-not-name-a-type-in-c">here</a>.</p></div><div id="comment-5106-info" class="comment-info"><span class="comment-age">(18 Jul '11, 08:20)</span> Jaap ♦</div></div></div><div id="comment-tools-5090" class="comment-tools"></div><div class="clear"></div><div id="comment-5090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

