+++
type = "question"
title = "Wireshark 2.0 Expert Info: error"
description = '''15 TNS: C:&#92;buildbot&#92;wireshark&#92;wireshark-2.0-64&#92;win7x64&#92;build&#92;epan&#92;dissectors&#92;packet-tcp.c:2643: failed assertion &quot;proto_desegment &amp;amp;&amp;amp; pinfo-&amp;gt;can_desegment&quot;'''
date = "2015-11-11T08:53:00Z"
lastmod = "2015-11-12T02:08:00Z"
weight = 47515
keywords = [ "buildbot6164" ]
aliases = [ "/questions/47515" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 2.0 Expert Info: error](/questions/47515/wireshark-20-expert-info-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47515-score" class="post-score" title="current number of votes">0</div><span id="post-47515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>15 TNS: C:\buildbot\wireshark\wireshark-2.0-64\win7x64\build\epan\dissectors\packet-tcp.c:2643: failed assertion "proto_desegment &amp;&amp; pinfo-&gt;can_desegment"</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-buildbot6164" rel="tag" title="see questions tagged &#39;buildbot6164&#39;">buildbot6164</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '15, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/328e4e3c363565d7a50d22167dd1a5b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="philvilla&#39;s gravatar image" /><p><span>philvilla</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="philvilla has no accepted answers">0%</span></p></div></div><div id="comments-container-47515" class="comments-container"><span id="47518"></span><div id="comment-47518" class="comment"><div id="post-47518-score" class="comment-score"></div><div class="comment-text"><p>Can you share the capture that caused that? The appropriate place for that is on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>.</p></div><div id="comment-47518-info" class="comment-info"><span class="comment-age">(11 Nov '15, 09:25)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="47519"></span><div id="comment-47519" class="comment"><div id="post-47519-score" class="comment-score"></div><div class="comment-text"><p>I am really sorry it has proprietary information in it so I am unable too.</p></div><div id="comment-47519-info" class="comment-info"><span class="comment-age">(11 Nov '15, 09:39)</span> <span class="comment-user userinfo">philvilla</span></div></div><span id="47523"></span><div id="comment-47523" class="comment"><div id="post-47523-score" class="comment-score"></div><div class="comment-text"><p>Are you using a proprietary dissector? Because this assertion usually means that a dissector on top of TCP one is misusing the API.</p></div><div id="comment-47523-info" class="comment-info"><span class="comment-age">(11 Nov '15, 10:52)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-47515" class="comment-tools"></div><div class="clear"></div><div id="comment-47515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47536"></span>

<div id="answer-container-47536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47536-score" class="post-score" title="current number of votes">0</div><span id="post-47536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The assertion you mentioned is reported in this part of packet-tcp.c:</p><pre><code>    plen = (*get_pdu_len)(pinfo, tvb, offset, dissector_data);
    if (plen == 0) {
        /*
         * Support protocols which have a variable length which cannot
         * always be determined within the given fixed_len.
         */
        DISSECTOR_ASSERT(proto_desegment &amp;&amp; pinfo-&gt;can_desegment);
        pinfo-&gt;desegment_offset = offset;
        pinfo-&gt;desegment_len = DESEGMENT_ONE_MORE_SEGMENT;
        return;
    }</code></pre><p>This assertion was added in <a href="https://github.com/wireshark/wireshark/commit/4ca3dbae">v1.99.4rc0-5-g4ca3dba</a> and when tripped, it means that your dissector routine has requested desegmentation (because the "PDU length" is 0), but it is not supported by the layer above it (maybe you have disabled the "Allow subdissector to reassemble TCP streams" preference for the TCP protocol).</p><p>If you are the author of the dissector, check:</p><ul><li>Whether you really want the new behavior introduced by above commit. Before that commit, the value 0 would typically cause a bounds error (Dissector error / "Malformed Packet").</li><li>If you actually want to activate desegmentation, check whether the parent protocol supports it. If there is an extra layer between TCP and your protocol (for example, a HTTP proxy tunnel), check that desegmentation functionality is preserved. The desegmentation functionality can be preserved by incrementing <code>pinfo-&gt;can_desegment</code> before calling another dissector. There was a bug that broke HTTP2 desegmentation, fixed in <a href="https://github.com/wireshark/wireshark/commit/d67e20a9">this commit</a></li></ul><p>If you are a user, please include these details in a bug report:</p><ul><li>A packet capture reproducing the issue. If it is proprietary, you can mark a capture as private such that only Wireshark core developers can see it.</li><li>If you are unable to provide the full capture, at least post the single packet (and/ or the textual dissection from <code>tshark -r your.pcap -V -Y frame.number==123</code>). This should hopefully make it possible to find out what protocols are involved.</li><li>The Wireshark version you are using (see About -&gt; Version or <code>tshark -version</code>).</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '15, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-47536" class="comments-container"></div><div id="comment-tools-47536" class="comment-tools"></div><div class="clear"></div><div id="comment-47536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

