+++
type = "question"
title = "tcp options dissector"
description = '''void proto_reg_handoff_foo(void) {  static dissector_handle_t foo_handle;   foo_handle = create_dissector_handle(dissect_UDP_1234, proto_foo);  dissector_add_uint(&quot;udp.port&quot;, 1234, foo_handle); }  My dissector function (dissect_UDP_1234) will be called for UDP traffic on port 1234.  (http://www.wire...'''
date = "2011-09-20T23:46:00Z"
lastmod = "2011-09-21T03:04:00Z"
weight = 6473
keywords = [ "options", "tcp" ]
aliases = [ "/questions/6473" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tcp options dissector](/questions/6473/tcp-options-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6473-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>void
proto_reg_handoff_foo(void)
{
    static dissector_handle_t foo_handle;

    foo_handle = create_dissector_handle(dissect_UDP_1234, proto_foo);
    dissector_add_uint(&quot;udp.port&quot;, 1234, foo_handle);
}</code></pre><p>My dissector function (<code>dissect_UDP_1234</code>) will be called for UDP traffic on port 1234. (<a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html">http://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html</a>)</p><p>Is there a similar way to do this: my dissector function (<code>dissect_TCP_OPTIONS_123</code>) will be called, if TCP options 123 is present?</p><p>Can I write something like this:</p><pre><code>dissector_add_uint(&quot;tcp.options&quot;, 123, foo_handle);</code></pre><p>But it did't work for me. :(</p><p>Any suggestion how to do this, other than modifying <code>packet-tcp.c</code> file.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">options tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '11, 23:46</strong></p><img src="https://secure.gravatar.com/avatar/53c5d806ca95207e95aa3287052d708d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vikas&#39;s gravatar image" /><p>Vikas<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vikas has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Sep '11, 03:02</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-6473" class="comments-container"></div><div id="comment-tools-6473" class="comment-tools"></div><div class="clear"></div><div id="comment-6473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6475"></span>

<div id="answer-container-6475" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6475-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Currently there's no <code>tcp.options</code> table to dynamically extend with additional options. For now it will have to be coded in <code>packet-tcp.c</code>. There may already be an wishlist item and/or enhancement bug for this, but I'm not sure.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '11, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6475" class="comments-container"></div><div id="comment-tools-6475" class="comment-tools"></div><div class="clear"></div><div id="comment-6475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

