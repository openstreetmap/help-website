+++
type = "question"
title = "Dissector handle"
description = '''I&#x27;m trying to develop my own dissector for some protocol I&#x27;ve analysed. I took skeleton dissector from README.developer and filled it. Now that I&#x27;m trying to compile it I get following error, and cannot figure out what&#x27;s wrong: /home/andrey/grive/wireshark-dissector-template/packet-intl.c: In functi...'''
date = "2013-07-03T02:25:00Z"
lastmod = "2013-07-03T02:42:00Z"
weight = 22590
keywords = [ "compile", "dissector", "1.10.0", "plugin" ]
aliases = [ "/questions/22590" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Dissector handle](/questions/22590/dissector-handle)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22590-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to develop my own dissector for some protocol I've analysed. I took skeleton dissector from README.developer and filled it. Now that I'm trying to compile it I get following error, and cannot figure out what's wrong:</p><pre><code>/home/andrey/grive/wireshark-dissector-template/packet-intl.c: In function     ‘proto_reg_handoff_intl’:
/home/andrey/grive/wireshark-dissector-template/packet-intl.c:370:58: warning: passing argument 1 of ‘new_create_dissector_handle’ from incompatible pointer type [enabled by default]
                                                      proto_intl);
                                                      ^
In file included from /home/andrey/grive/wireshark-dissector-template/packet-intl.c:46:0:
/usr/include/wireshark/epan/packet.h:322:34: note: expected ‘new_dissector_t’ but argument is of type ‘int (*)(struct tvbuff_t *, struct packet_info *, struct proto_tree *)’
WS_DLL_PUBLIC dissector_handle_t new_create_dissector_handle(new_dissector_t dissector,</code></pre></div><div id="question-tags" class="tags-container tags">compile dissector 1.10.0 plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '13, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/c9aa1d36ff8501f13272de4dafa34854?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrey&#39;s gravatar image" /><p>Andrey<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrey has one accepted answer">50%</span></p></div></div><div id="comments-container-22590" class="comments-container"></div><div id="comment-tools-22590" class="comment-tools"></div><div class="clear"></div><div id="comment-22590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22592"></span>

<div id="answer-container-22592" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22592-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Presumably you're building from trunk, the dissector function now has four parameters which the skeleton code hasn't caught up with yet.</p><p>You'll need to append a <code>void *</code> to the parameter list for your dissector function, the usual format is <code>void *data _U_</code>. The signature of a dissector function is defined in epan\packet.h as:</p><p><code>typedef int (*new_dissector_t)(tvbuff_t *, packet_info *, proto_tree *, void *);</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '13, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22592" class="comments-container"><span id="22593"></span><div id="comment-22593" class="comment"><div id="post-22593-score" class="comment-score"></div><div class="comment-text"><p>Thanks, it helped</p></div><div id="comment-22593-info" class="comment-info"><span class="comment-age">(03 Jul '13, 03:47)</span> Andrey</div></div></div><div id="comment-tools-22592" class="comment-tools"></div><div class="clear"></div><div id="comment-22592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

