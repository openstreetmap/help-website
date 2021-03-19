+++
type = "question"
title = "error in heuristic dissector"
description = '''I get this error when i run wireshark.I have built a heuristic dissector 17:29:46 Err file packet.c: line 1542 (heur_dissector_add): assertion failed: (sub_dissectors != NULL) Aborted'''
date = "2011-03-17T05:01:00Z"
lastmod = "2011-03-17T06:47:00Z"
weight = 2896
keywords = [ "heuristics" ]
aliases = [ "/questions/2896" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [error in heuristic dissector](/questions/2896/error-in-heuristic-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2896-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I get this error when i run wireshark.I have built a heuristic dissector 17:29:46 Err file packet.c: line 1542 (heur_dissector_add): assertion failed: (sub_dissectors != NULL) Aborted</p></div><div id="question-tags" class="tags-container tags">heuristics</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '11, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/46023e482c60329a251a137848f8f5f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="niks3089&#39;s gravatar image" /><p>niks3089<br />
<span class="score" title="21 reputation points">21</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="niks3089 has no accepted answers">0%</span></p></div></div><div id="comments-container-2896" class="comments-container"></div><div id="comment-tools-2896" class="comment-tools"></div><div class="clear"></div><div id="comment-2896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2902"></span>

<div id="answer-container-2902" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2902-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The "name" field (the 1st parameter) in your heur_dissector_add() call is not valid. Or I suppose it may be valid but you're calling heur_dissector_add() before the other protocol has been registered (are you calling heur_dissector_add() in your reg_handoff routine?).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '11, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-2902" class="comments-container"><span id="2906"></span><div id="comment-2906" class="comment"><div id="post-2906-score" class="comment-score"></div><div class="comment-text"><p>void proto_reg_handoff_arr(void)</p><p>{</p><pre><code>static gboolean initialized=FALSE;

if (!initialized) {

arr_handle = new_create_dissector_handle(dissect_arr, proto_arr);</code></pre><p>dissector_add_handle("tcp", arr_handle);</p><pre><code>    heur_dissector_add(&quot;tcp&quot;, dissect_arr_heur, proto_arr);

}</code></pre><p>}</p><p>this is the code</p></div><div id="comment-2906-info" class="comment-info"><span class="comment-age">(17 Mar '11, 10:42)</span> niks3089</div></div></div><div id="comment-tools-2902" class="comment-tools"></div><div class="clear"></div><div id="comment-2902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

