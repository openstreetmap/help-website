+++
type = "question"
title = "how to use wireshark library and glib library ?"
description = '''I make myown dynamic library(myown.so) according to libs of wiresahrk and glib. (libglib-2.0.a libglib-2.0.a libgthread-2.0.a libairpdcap.a libdfilter.a libdissectors.a libftypes.a libwireshark.a libwiretap.a libwsutil.a  libwireshark_asmopt.a libwireshark_generated.a libdirtydissectors.a ) include ...'''
date = "2012-11-10T00:03:00Z"
lastmod = "2012-11-12T22:40:00Z"
weight = 15786
keywords = [ "static", "library", "wireshark" ]
aliases = [ "/questions/15786" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to use wireshark library and glib library ?](/questions/15786/how-to-use-wireshark-library-and-glib-library)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15786-score" class="post-score" title="current number of votes">0</div><span id="post-15786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I make myown dynamic library(<a href="http://myown.so">myown.so</a>) according to libs of wiresahrk and glib.</p><p>(libglib-2.0.a libglib-2.0.a libgthread-2.0.a libairpdcap.a libdfilter.a libdissectors.a libftypes.a libwireshark.a libwiretap.a libwsutil.a libwireshark_asmopt.a libwireshark_generated.a libdirtydissectors.a )</p><p>include path(glib-2.0,wireshark,wireshark/epan).</p><p><a href="http://myown.so">myown.so</a> can be made successfully, but loaded fail.</p><p>ldd -r <a href="http://myown.so">myown.so</a>, errors are as follow:</p><p>undefined symbol: proto_item_fill_label (./<a href="http://myown.so">myown.so</a>)</p><p>undefined symbol: g_sprintf (./<a href="http://myown.so">myown.so</a>)</p><p>undefined symbol: g_assertion_message_expr (./<a href="http://myown.so">myown.so</a>)</p><p>undefined symbol: register_all_protocol_handoffs (./<a href="http://myown.so">myown.so</a>)</p><p>undefined symbol: register_all_protocols (./<a href="http://myown.so">myown.so</a>)</p><p>undefined symbol: epan_init (./<a href="http://myown.so">myown.so</a>)</p><p>undefined symbol: epan_dissect_init (./<a href="http://myown.so">myown.so</a>)</p><p>undefined symbol: frame_data_set_before_dissect (./<a href="http://myown.so">myown.so</a>)</p><p>undefined symbol: epan_dissect_run (./<a href="http://myown.so">myown.so</a>)</p><p>undefined symbol: epan_dissect_cleanup (./<a href="http://myown.so">myown.so</a>)</p><p>undefined symbol: g_malloc0 (./<a href="http://myown.so">myown.so</a>)</p><p>what is the reason? someone help me, please. Thank you very much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-static" rel="tag" title="see questions tagged &#39;static&#39;">static</span> <span class="post-tag tag-link-library" rel="tag" title="see questions tagged &#39;library&#39;">library</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '12, 00:03</strong></p><img src="https://secure.gravatar.com/avatar/a5a3214300b3b17fc46c3b656b7bed01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ylda_ljm0620&#39;s gravatar image" /><p><span>ylda_ljm0620</span><br />
<span class="score" title="31 reputation points">31</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ylda_ljm0620 has no accepted answers">0%</span></p></div></div><div id="comments-container-15786" class="comments-container"></div><div id="comment-tools-15786" class="comment-tools"></div><div class="clear"></div><div id="comment-15786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15844"></span>

<div id="answer-container-15844" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15844-score" class="post-score" title="current number of votes">0</div><span id="post-15844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have built <a href="http://myown.so">myown.so</a> and loaded successfully. I use the glib-2.0 which is installed.</p><p>In makefile, there are:</p><p>VPATH = -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include</p><p>GLIB_DIR =/usr/lib</p><p>WIRESHARKLIB_DIR =../wireshark/lib</p><p>ZIPLIB_DIR = ../zip</p><p>LIBS = /usr/lib</p><p>LIBS = -L$(GLIB_DIR) -lgthread-2.0 -lgmodule-2.0 -lglib-2.0 -L$(WIRESHARKLIB_DIR) -lairpdcap -ldfilter -ldissectors -lftypes -lwireshark -lwiretap -lwsutil -lwireshark_asmopt -lwireshark_generated -ldirtydissectors \ -L$(ZIPLIB_DIR) -lz \ -lpthread -ldl -lrt -rdynamic</p><p>CFLAGS = -g -w -DOS_LINUX -DHAVE_CONFIG_H -D_U_</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '12, 22:40</strong></p><img src="https://secure.gravatar.com/avatar/a5a3214300b3b17fc46c3b656b7bed01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ylda_ljm0620&#39;s gravatar image" /><p><span>ylda_ljm0620</span><br />
<span class="score" title="31 reputation points">31</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ylda_ljm0620 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Nov '12, 22:42</strong> </span></p></div></div><div id="comments-container-15844" class="comments-container"></div><div id="comment-tools-15844" class="comment-tools"></div><div class="clear"></div><div id="comment-15844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

