+++
type = "question"
title = "Can WSGD understand float NAN, QNAN?"
description = '''Have a packet with float32 values. Some of them are filled with NAN(QNAN). With WSGD Wireshark shows them as 6.90546e-041. How to fix it with .fdesk and .wsgd files only? I cannot edit sources and recompile WSGD at the time. Upd. Sorry, it was my mistake, wrong byte order.'''
date = "2016-01-18T08:20:00Z"
lastmod = "2016-01-18T13:54:00Z"
weight = 49326
keywords = [ "float", "nan", "dissector", "wsgd" ]
aliases = [ "/questions/49326" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can WSGD understand float NAN, QNAN?](/questions/49326/can-wsgd-understand-float-nan-qnan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49326-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Have a packet with <code>float32</code> values. Some of them are filled with <code>NAN(QNAN)</code>. With WSGD Wireshark shows them as <strong><code>6.90546e-041</code></strong>.<br />
How to fix it with <code>.fdesk</code> and <code>.wsgd</code> files only? I cannot edit sources and recompile WSGD at the time.</p><p><strong>Upd.</strong> Sorry, it was my mistake, <strong>wrong byte order</strong>.</p></div><div id="question-tags" class="tags-container tags">float nan dissector wsgd</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '16, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/680680d82143e4d33dc569913e5ef8c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kyb&#39;s gravatar image" /><p>kyb<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kyb has one accepted answer">100%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jan '16, 05:22</p></div></div><div id="comments-container-49326" class="comments-container"></div><div id="comment-tools-49326" class="comment-tools"></div><div class="clear"></div><div id="comment-49326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49335"></span>

<div id="answer-container-49335" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49335-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Relying on <a href="http://www.astro.umass.edu/~weinberg/a732/notes07_01.pdf">http://www.astro.umass.edu/~weinberg/a732/notes07_01.pdf</a> for hexa decimal values of +/-Infinity and Nan.</p><p>The following test :</p><pre><code>  call frame_append_hexa_data (internal_frame, &quot;7f800000&quot;);
  call frame_append_hexa_data (internal_frame, &quot;ff800000&quot;);
  call frame_append_hexa_data (internal_frame, &quot;7fc00000&quot;);
  float32  float32_7f800000_PosInfinity;
  float32  float32_ff800000_NegInfinity;
  float32  float32_7fc00000_NaN;

  call frame_append_hexa_data (internal_frame, &quot;7ff00000 00000000&quot;);
  call frame_append_hexa_data (internal_frame, &quot;fff00000 00000000&quot;);
  call frame_append_hexa_data (internal_frame, &quot;7ff80000 00000000&quot;);
  float64  float64_7ff00000_00000000_PosInfinity;
  float64  float64_fff00000_00000000_NegInfinity;
  float64  float64_7ff80000_00000000_NaN;</code></pre><p>Displays (win64 wireshark 2.0 &amp; 1.12) :</p><pre><code>  float32_7f800000_PosInfinity: 1.#INF
  float32_ff800000_NegInfinity: -1.#INF
  float32_7fc00000_NaN: 1.#QNAN
  float64_7ff00000_00000000_PosInfinity: 1.#INF
  float64_fff00000_00000000_NegInfinity: -1.#INF
  float64_7ff80000_00000000_NaN: 1.#QNAN</code></pre><p>Which seems coherent.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '16, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/f69baac47dbc58c404e4356eb7a3b191?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wsgd&#39;s gravatar image" /><p>wsgd<br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wsgd has 2 accepted answers">100%</span></p></div></div><div id="comments-container-49335" class="comments-container"></div><div id="comment-tools-49335" class="comment-tools"></div><div class="clear"></div><div id="comment-49335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

