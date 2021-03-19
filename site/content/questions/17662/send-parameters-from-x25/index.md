+++
type = "question"
title = "send parameters from X.25"
description = '''Hello, I have to dissect some protocols as X.25, sndcp (sndcf)... In X.25 I have the number of circuit VC and the dictionary of compression. In SNDCP, I have the information concerning the compression or not of data and before to dissect the other protocols i have to uncompress the data. To do this,...'''
date = "2013-01-14T06:26:00Z"
lastmod = "2013-01-18T03:09:00Z"
weight = 17662
keywords = [ "x.25", "parameters" ]
aliases = [ "/questions/17662" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [send parameters from X.25](/questions/17662/send-parameters-from-x25)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17662-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have to dissect some protocols as X.25, sndcp (sndcf)... In X.25 I have the number of circuit VC and the dictionary of compression. In SNDCP, I have the information concerning the compression or not of data and before to dissect the other protocols i have to uncompress the data. To do this, i want to send the VC and the dictionary as parameters from X.25 to SNDCP. For info, i'm using the versions 1.6 of wireshark. So, to start, i try to send VC, and i've done these modifications :</p><p>packet.c :</p><pre><code>...
call_dissector_with_data(...., void *data)
...
if(handle-&gt; is_new) {
    ret=(*handle-&gt;dissector.new)(....,  data);</code></pre><p>I modify also the others functions to use the data packet-x.25, in the case NLPID_SNDCF :</p><pre><code>...
call_dissector_with_data (....., &amp;vc);
...</code></pre><p>packet-sndcp.c :</p><p><code>new_register_dissector(....);</code> instead of <code>register_dissector(...)</code>, and</p><pre><code>dissect_sndcp(...., void *data)
{
    guint16 vc =0;
    id(data)
    vc=*((guint16 *)data);
        ...

    col_add_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;SN-DATA N-PDU %d %d, npdu_field1, vc);
}</code></pre><p>In my packet, I have juste one VC=1 but the function</p><pre><code>col_add_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;SN-DATA N-PDU %d %d, npdu_field1, vc)</code></pre><p>displays the value 0 instead of 1 for VC. Can you help me please? did I forget to modify other functions?</p></div><div id="question-tags" class="tags-container tags">x.25 parameters</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '13, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/c511beedf069ff22b3f13e1016920c9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gigi&#39;s gravatar image" /><p>Gigi<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gigi has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jan '13, 20:39</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-17662" class="comments-container"><span id="17736"></span><div id="comment-17736" class="comment"><div id="post-17736-score" class="comment-score"></div><div class="comment-text"><p>If i understand the function call_dissector_with_data or call_dissector allow us to call the function dissect_PROTO. It's true? What is the main function of a dissector? Thank you</p></div><div id="comment-17736-info" class="comment-info"><span class="comment-age">(17 Jan '13, 03:05)</span> Gigi</div></div></div><div id="comment-tools-17662" class="comment-tools"></div><div class="clear"></div><div id="comment-17662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17773"></span>

<div id="answer-container-17773" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17773-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>if that can help someone, i had to modify the function try_circuit_dissector too(..., void *data) (packet circuit.c).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '13, 03:09</strong></p><img src="https://secure.gravatar.com/avatar/c511beedf069ff22b3f13e1016920c9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gigi&#39;s gravatar image" /><p>Gigi<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gigi has one accepted answer">100%</span></p></div></div><div id="comments-container-17773" class="comments-container"><span id="17780"></span><div id="comment-17780" class="comment"><div id="post-17780-score" class="comment-score"></div><div class="comment-text"><p>Yes, there are ways of calling dissectors other than with <code>call_dissector()</code> or <code>call_dissector_with_data()</code>; in order to support passing dissector data, those routines have to be changed. We'll look at doing that in the 1.10 release.</p></div><div id="comment-17780-info" class="comment-info"><span class="comment-age">(18 Jan '13, 10:51)</span> Guy Harris ♦♦</div></div><span id="49636"></span><div id="comment-49636" class="comment"><div id="post-49636-score" class="comment-score"></div><div class="comment-text"><p><code>try_circuit_dissector()</code> now has a <code>void *data</code> argument in the standard version of Wireshark; that was done either in the 1.10 release or the 1.12 release.</p></div><div id="comment-49636-info" class="comment-info"><span class="comment-age">(29 Jan '16, 15:08)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-17773" class="comment-tools"></div><div class="clear"></div><div id="comment-17773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

