+++
type = "question"
title = "Getting UUID Name"
description = '''I wonder how getting UUID name works at Wireshark.  I am working with following pcap file:  https://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;amp;do=get&amp;amp;target=dcerpc_witness.pcapng I debug the code, and I think the responsible file is file:   epan&#92;dissectors&#92;packet-dcerpc-epm.c  Respo...'''
date = "2016-05-25T03:47:00Z"
lastmod = "2016-05-25T04:30:00Z"
weight = 52902
keywords = [ "epm", "uuid", "dcerpc" ]
aliases = [ "/questions/52902" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting UUID Name](/questions/52902/getting-uuid-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52902-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wonder how getting UUID name works at Wireshark. I am working with following pcap file:</p><p><a href="https://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=dcerpc_witness.pcapng">https://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=dcerpc_witness.pcapng</a></p><p>I debug the code, and I think the responsible file is file:</p><blockquote><p>epan\dissectors\packet-dcerpc-epm.c</p></blockquote><p>Responsible Line is line 349:</p><pre><code>uuid_name = guids_get_uuid_name(&amp;uuid);</code></pre><p>I check Frame 223: Tower Pointer -&gt; Floor 1 UUID: WITNESS -&gt; UUID: WITNESS</p><p>I don't understand how Line 349 found name of the UUID as "WITNESS"</p><p>For example, let me change this number "ccd8c074-d0e5-4a40-92b4-d074faa6ba28" from "WITNESS" to "SOMETHINGANOTHER" (It is completely an idea, I will not change anything about this UUID)</p><p>How can I do this?</p></div><div id="question-tags" class="tags-container tags">epm uuid dcerpc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '16, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/6257a856e7271c04dd39469c7a5332ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BirolCapa&#39;s gravatar image" /><p>BirolCapa<br />
<span class="score" title="30 reputation points">30</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BirolCapa has no accepted answers">0%</span></p></div></div><div id="comments-container-52902" class="comments-container"></div><div id="comment-tools-52902" class="comment-tools"></div><div class="clear"></div><div id="comment-52902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52903"></span>

<div id="answer-container-52903" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52903-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>guids_get_uuid_name</code> is a macro (in <code>epan/guid-utils.h</code>) that calls <code>guids_get_guid_name</code> which is defined in <code>epan/guid-utils.c</code>.</p><p>That function attempts to look the guid up in the guid name cache built from the capture, and if that fails, on Windows only, attempts to locate the interface name in the registry.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '16, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-52903" class="comments-container"><span id="52904"></span><div id="comment-52904" class="comment"><div id="post-52904-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the answer Graham.</p><p>How is "guid name cache" built?</p><p>Let's look at the file "epan\dissectors\packet-dcerpc-witness.c". As far as I understand, "dcerpc_init_uuid(...)" function adds the name of the UUID to guid name cache by using "proto_dcerpc_witness" parameter. Am I right?</p></div><div id="comment-52904-info" class="comment-info"><span class="comment-age">(25 May '16, 04:45)</span> BirolCapa</div></div><span id="52907"></span><div id="comment-52907" class="comment"><div id="post-52907-score" class="comment-score">1</div><div class="comment-text"><p>I think so, it's the call to <code>guids_add_uuid</code> which is a macro that calls <code>guids_add_guid</code>.</p></div><div id="comment-52907-info" class="comment-info"><span class="comment-age">(25 May '16, 05:31)</span> grahamb ♦</div></div></div><div id="comment-tools-52903" class="comment-tools"></div><div class="clear"></div><div id="comment-52903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

