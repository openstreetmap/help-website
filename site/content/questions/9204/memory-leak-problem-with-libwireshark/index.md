+++
type = "question"
title = "memory leak problem with libwireshark!"
description = '''i am working on a project: capture and dissect the network packets using libwireshark when i execute my code with valgrind.. i found this report 7,024 bytes in 143 blocks are definitely lost in loss record 25 of 41 ==21679== at 0x4A05809: malloc (vg_replace_malloc.c:149) ==21679== by 0x32D2E33BFA: g...'''
date = "2012-02-25T03:03:00Z"
lastmod = "2012-06-19T07:12:00Z"
weight = 9204
keywords = [ "development", "memory_leak", "valgrind", "libwireshark.lib" ]
aliases = [ "/questions/9204" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [memory leak problem with libwireshark!](/questions/9204/memory-leak-problem-with-libwireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9204-score" class="post-score" title="current number of votes">0</div><span id="post-9204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i am working on a project: capture and dissect the network packets using libwireshark when i execute my code with valgrind.. i found this report</p><p>7,024 bytes in 143 blocks are definitely lost in loss record 25 of 41</p><p>==21679== at 0x4A05809: malloc (vg_replace_malloc.c:149)</p><p>==21679== by 0x32D2E33BFA: g_malloc (in /lib64/libglib-2.0.so.0.1200.3)</p><p>==21679== by 0x32D2E45A7E: g_strdup (in /lib64/libglib-2.0.so.0.1200.3)</p><p>==21679== by 0x5BD2A2E: add_oid (oids.c:145)</p><p>==21679== by 0x5BD2BAA: oid_add_from_string (oids.c:178)</p><p>==21679== by 0x62935D3: proto_reg_handoff_pkixqualified (packet-pkixqualified-dis-tab.c:7)</p><p>==21679== by 0x6339509: register_all_protocol_handoffs (register.c:1593)</p><p>==21679== by 0x5BEBFD1: proto_init (proto.c:416)</p><p>==21679== by 0x5BCC92F: epan_init (epan.c:104)</p><p>==21679== by 0x401FF9: init_libwireshark (trace.c:124)</p><p>==21679== by 0x402AAD: main (trace.c:518)</p><p>is this the problem with libwireshark only ?? how to get rid of this problem. any help!? thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-memory_leak" rel="tag" title="see questions tagged &#39;memory_leak&#39;">memory_leak</span> <span class="post-tag tag-link-valgrind" rel="tag" title="see questions tagged &#39;valgrind&#39;">valgrind</span> <span class="post-tag tag-link-libwireshark.lib" rel="tag" title="see questions tagged &#39;libwireshark.lib&#39;">libwireshark.lib</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '12, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p><span>Sanny_D</span><br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-9204" class="comments-container"></div><div id="comment-tools-9204" class="comment-tools"></div><div class="clear"></div><div id="comment-9204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9205"></span>

<div id="answer-container-9205" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9205-score" class="post-score" title="current number of votes">1</div><span id="post-9205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First: Please note that valgrind may become confused due to various memory optimizations used in libwireshark and Glib.</p><p>To use valgrind with Glib based programs please see :</p><p><a href="http://live.gnome.org/Valgrind">Valgrind and Gnome</a></p><p><a href="http://developer.gnome.org/glib/2.30/glib-running.html">Running GLib</a></p><p>(A Google search finds other discussions on this topic).</p><p>Also: from the Wireshark sources: epan/emem.c</p><pre><code>/*
 * Tools like Valgrind and ElectricFence don&#39;t work well with memchunks.
 * Export the following environment variables to make {ep|se}_alloc() allocate each
 * object individually.
 *
 * WIRESHARK_DEBUG_EP_NO_CHUNKS
 * WIRESHARK_DEBUG_SE_NO_CHUNKS</code></pre><p>Second: At least some of the cases are because Wireshark does certain memory allocations during initialization which are for the lifetime of the program and which are never freed.</p><p>Fixing these hasn't been a priority although I believe there have been efforts from time to time.<br />
Possible cases:</p><pre><code>==21679== by 0x6339509: register_all_protocol_handoffs (register.c:1593)
==21679== by 0x5BEBFD1: proto_init (proto.c:416)
==21679== by 0x5BCC92F: epan_init (epan.c:104)
==21679== by 0x401FF9: init_libwireshark (trace.c:124)</code></pre><p>To get "clean" valgind output, the simplest solution may be to configure valgrind to ignore certain of these memory leaks.</p><p>Third: Other cases may very well be memory leaks which are more "real": e.g., memory allocated during dissection of a frame which is not freed properly when the dissection is complete.</p><p>We gladly accept patches to fix specific instances of memory leaks. :) :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '12, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Feb '12, 06:21</strong> </span></p></div></div><div id="comments-container-9205" class="comments-container"><span id="9254"></span><div id="comment-9254" class="comment"><div id="post-9254-score" class="comment-score"></div><div class="comment-text"><p>And it's not clear it's worth fixing the cases where Wireshark does certain memory allocations during initialization which are for the lifetime of the program and which are never freed - it's faster to free that memory by simply terminating the process with exit() or a return from main() than to manually free it before exiting.</p></div><div id="comment-9254-info" class="comment-info"><span class="comment-age">(27 Feb '12, 12:23)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="12044"></span><div id="comment-12044" class="comment"><div id="post-12044-score" class="comment-score"></div><div class="comment-text"><p>yes. but i want to run the application for a long time on server side, so freeing with exit() or return from main() wont serve the purpose.</p><p>is any other way to remove this unwanted leaks, like cleanup routines.</p><p>thanks!</p></div><div id="comment-12044-info" class="comment-info"><span class="comment-age">(19 Jun '12, 00:34)</span> <span class="comment-user userinfo">Sanny_D</span></div></div><span id="12045"></span><div id="comment-12045" class="comment"><div id="post-12045-score" class="comment-score"></div><div class="comment-text"><p>There's no way to remove memory allocations that valgrind misidentifies as leaks; there might, as per the links Bill suggests, be ways to get valgrind to stop falsely claiming that they're leaks, so that it identifies only <em>real</em> leaks. From looking at add_oid(), what valgrind is reporting there is unlikely to be a leak unless add_oid() isn't properly updating the tree and therefore losing the stuff it allocates.</p><p>And, no, there's no way to remove allocations of stuff that's <em>intended</em> to be allocated during the entire Wireshark run.</p></div><div id="comment-12045-info" class="comment-info"><span class="comment-age">(19 Jun '12, 01:05)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="12048"></span><div id="comment-12048" class="comment"><div id="post-12048-score" class="comment-score"></div><div class="comment-text"><pre><code>6,552 bytes in 273 blocks are definitely lost in loss record 49,162 of 49,380
==25873==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==25873==    by 0x32D2E33BFA: g_malloc (in /lib64/libglib-2.0.so.0.1200.3)
==25873==    by 0x32D2E10AF1: g_array_sized_new (in /lib64/libglib-2.0.so.0.1200.3)
==25873==    by 0x5D97344: proto_register_diameter (packet-diameter.c:1482)
==25873==    by 0x634036E: register_all_protocols (register.c:234)
==25873==    by 0x5BECF25: proto_init (proto.c:395)
==25873==    by 0x5BCD92F: epan_init (epan.c:104)
==25873==    by 0x392DCB48: init_libwireshark (trace_23rdfb.c:36)
==25873==    by 0x392DDA46: init_trace (trace_23rdfb.c:582)</code></pre><p>this is the report after turning off the glib optimization.. now what could be wrong?</p></div><div id="comment-12048-info" class="comment-info"><span class="comment-age">(19 Jun '12, 01:18)</span> <span class="comment-user userinfo">Sanny_D</span></div></div><span id="12050"></span><div id="comment-12050" class="comment"><div id="post-12050-score" class="comment-score"></div><div class="comment-text"><p>What's wrong is that</p><p>1) you have Diameter dictionaries</p><p>and</p><p>2) either turning off the glib optimization isn't sufficient to keep valgrind from being confused or somehow the array isn't getting freed (it's probably the build_dict.hf array if this is a <em>recent</em> version of Wireshark, and that array <em>is</em> freed - but its content isn't freed because it's been registered as a set of fields - so the answer is probably "turning off the glib optimization isn't sufficient to keep valgrind from being confused").</p></div><div id="comment-12050-info" class="comment-info"><span class="comment-age">(19 Jun '12, 01:48)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="12055"></span><div id="comment-12055" class="comment not_top_scorer"><div id="post-12055-score" class="comment-score"></div><div class="comment-text"><blockquote><p>yes. but i want to run the application for a long time on server side ...</p></blockquote><p>Note well: the code in various dissectors (in libwireshark) accumulates state (using memory) as frames are dissected.</p><p>So, expecting to "run the application for a long time on server side" without memory usage increasing (which seems the implication of your questions) is a non-starter.</p><p>Am I missing something (or incorrect about how you are using libwireshark ?)</p></div><div id="comment-12055-info" class="comment-info"><span class="comment-age">(19 Jun '12, 07:12)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-9205" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-9205-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

