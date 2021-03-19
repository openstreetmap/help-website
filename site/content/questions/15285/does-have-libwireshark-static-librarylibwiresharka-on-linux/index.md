+++
type = "question"
title = "does have libwireshark static library(libwireshark.a) on linux ?"
description = '''I compiled wireshark on linux successfully, but not found libwireshark static library(libwireshark.a) ,only found libwireshark.so libwireshark_generated.a libwireshark_asmopt.a. secondary development wireshark on linux, there are errors as follows(why?):  undefined symbol: proto_item_fill_label (./s...'''
date = "2012-10-25T18:53:00Z"
lastmod = "2012-10-26T18:24:00Z"
weight = 15285
keywords = [ "symbol", "undefined" ]
aliases = [ "/questions/15285" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [does have libwireshark static library(libwireshark.a) on linux ?](/questions/15285/does-have-libwireshark-static-librarylibwiresharka-on-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15285-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I compiled wireshark on linux successfully, but not found libwireshark static library(libwireshark.a) ,only found <a href="http://libwireshark.so">libwireshark.so</a> libwireshark_generated.a libwireshark_asmopt.a.</p><p>secondary development wireshark on linux, there are errors as follows(why?):</p><pre><code>   undefined symbol: proto_item_fill_label (./scandissectpkt.so)
   undefined symbol: g_sprintf     (./scandissectpkt.so)
   undefined symbol: g_assertion_message_expr      (./scandissectpkt.so)
   undefined symbol: register_all_protocol_handoffs        (./scandissectpkt.so)
   undefined symbol: register_all_protocols        (./scandissectpkt.so)
   undefined symbol: epan_init     (./scandissectpkt.so)
   undefined symbol: epan_dissect_init     (./scandissectpkt.so)
   undefined symbol: frame_data_set_before_dissect (./scandissectpkt.so)
   undefined symbol: epan_dissect_run      (./scandissectpkt.so)
   undefined symbol: epan_dissect_cleanup  (./scandissectpkt.so)
   undefined symbol: g_malloc0     (./scandissectpkt.so)</code></pre></div><div id="question-tags" class="tags-container tags">symbol undefined</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '12, 18:53</strong></p><img src="https://secure.gravatar.com/avatar/a5a3214300b3b17fc46c3b656b7bed01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ylda_ljm0620&#39;s gravatar image" /><p>ylda_ljm0620<br />
<span class="score" title="31 reputation points">31</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ylda_ljm0620 has no accepted answers">0%</span></p></div></div><div id="comments-container-15285" class="comments-container"></div><div id="comment-tools-15285" class="comment-tools"></div><div class="clear"></div><div id="comment-15285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15302"></span>

<div id="answer-container-15302" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15302-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>libtool, by default, sets up the Makefile only to build dynamic libraries. You might try running the configure script with <code>--enable-static</code> and rebuilding (you might need to run <code>make distclean</code> first) and see whether that builds libwireshark.a.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '12, 18:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15302" class="comments-container"><span id="15843"></span><div id="comment-15843" class="comment"><div id="post-15843-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much. just ./configure --enable-static, then make, can build static library.</p></div><div id="comment-15843-info" class="comment-info"><span class="comment-age">(12 Nov '12, 22:25)</span> ylda_ljm0620</div></div></div><div id="comment-tools-15302" class="comment-tools"></div><div class="clear"></div><div id="comment-15302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

