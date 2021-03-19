+++
type = "question"
title = "Source code cannot be compiled successfully"
description = '''Source code can no be compiled successful in linux,the error is in the following, who can help me to deal with it,and ido not know what the reason is.thanks! mate_runtime.c: In function &#x27;destroy_mate_pdus&#x27;: mate_runtime.c:64: warning: implicit declaration of function &#x27;g_slice_free&#x27; mate_runtime.c:64...'''
date = "2012-04-23T02:50:00Z"
lastmod = "2012-04-23T11:44:00Z"
weight = 10396
keywords = [ "tshark" ]
aliases = [ "/questions/10396" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Source code cannot be compiled successfully](/questions/10396/source-code-cannot-be-compiled-successfully)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10396-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Source code can no be compiled successful in linux,the error is in the following, who can help me to deal with it,and ido not know what the reason is.thanks!</p><pre><code>mate_runtime.c: In function &#39;destroy_mate_pdus&#39;:
mate_runtime.c:64: warning: implicit declaration of function &#39;g_slice_free&#39;
mate_runtime.c:64: error: expected expression before &#39;mate_max_size&#39;
mate_runtime.c: In function &#39;destroy_mate_gops&#39;:
mate_runtime.c:81: error: expected expression before &#39;mate_max_size&#39;
mate_runtime.c: In function &#39;destroy_mate_gogs&#39;:
mate_runtime.c:99: error: expected expression before &#39;mate_max_size&#39;
mate_runtime.c: In function &#39;new_gop&#39;:
mate_runtime.c:175: warning: implicit declaration of function &#39;g_slice_new&#39;
mate_runtime.c:175: error: expected expression before &#39;mate_max_size&#39;
mate_runtime.c:175: warning: cast to pointer from integer of different size
mate_runtime.c: In function &#39;new_gog&#39;:
mate_runtime.c:239: error: expected expression before &#39;mate_max_size&#39;
mate_runtime.c:239: warning: cast to pointer from integer of different size
mate_runtime.c: In function &#39;new_pdu&#39;:
mate_runtime.c:710: error: expected expression before &#39;mate_max_size&#39;
mate_runtime.c:710: warning: cast to pointer from integer of different size
mate_runtime.c: In function &#39;mate_analyze_frame&#39;:
mate_runtime.c:881: error: expected expression before &#39;mate_max_size&#39;
mate_runtime.c:892: error: expected expression before &#39;mate_max_size&#39;
make[3]: *** [mate_runtime.lo] Error 1
make[3]: Leaving directory `/data/webroot/tshark/wireshark-1.6.7/plugins/mate&#39;
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory `/data/webroot/tshark/wireshark-1.6.7/plugins&#39;
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/data/webroot/tshark/wireshark-1.6.7&#39;
make: *** [all] Error 2</code></pre></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '12, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/36c3e48ead01673b3c3c0149cdfe2562?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kurokyli&#39;s gravatar image" /><p>kurokyli<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kurokyli has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Apr '12, 02:02</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-10396" class="comments-container"></div><div id="comment-tools-10396" class="comment-tools"></div><div class="clear"></div><div id="comment-10396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10406"></span>

<div id="answer-container-10406" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10406-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark 1.6 and later require a version of GLib that supports "memory slices", which means it requires GLib 2.10 or later; you probably have an older version of GLib.</p><p>There's a bug in 1.6's configure script, in that it doesn't check to make sure you have GLib 2.10 or later, it checks for GLib 2.4 or later.</p><p>You would either have to upgrade the GLib (and GTK+) on your system, or try building Wireshark 1.4.12 instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '12, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10406" class="comments-container"><span id="11182"></span><div id="comment-11182" class="comment"><div id="post-11182-score" class="comment-score"></div><div class="comment-text"><p>I requested that the change which requires glib 2.10 or later be reverted from the 1.6 branch; with luck it'll make the 1.6.8 release.</p></div><div id="comment-11182-info" class="comment-info"><span class="comment-age">(21 May '12, 08:24)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-10406" class="comment-tools"></div><div class="clear"></div><div id="comment-10406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

