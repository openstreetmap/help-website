+++
type = "question"
title = "TZSP dissector"
description = '''Hello, Everyone! We need to capture TZSP traffic from our wifi access points. We create capture filter but i found error in default TZSP dissector in tzsp.wlan.signal field. Our AP&#x27;s send signal strength in 2 byte format field but wireshark decodes it as 1 byte field. Where can i change field size i...'''
date = "2015-04-21T07:06:00Z"
lastmod = "2015-04-21T07:37:00Z"
weight = 41632
keywords = [ "dissector", "tzsp" ]
aliases = [ "/questions/41632" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TZSP dissector](/questions/41632/tzsp-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41632-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Everyone! We need to capture TZSP traffic from our wifi access points. We create capture filter but i found error in default TZSP dissector in tzsp.wlan.signal field. Our AP's send signal strength in 2 byte format field but wireshark decodes it as 1 byte field. Where can i change field size in packet-tzsp.c source file? Wireshark Interpretation: <img src="https://osqa-ask.wireshark.org/upfiles/wireshark_tzsp_MfKUuog.jpg" alt="alt text" /></p><p>Correct Interpretation:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/correct_tzsp.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">dissector tzsp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '15, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/c0acac321ae990cfb91cdd114a90bd23?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael%20Bychkov&#39;s gravatar image" /><p>Michael Bychkov<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael Bychkov has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 21 Apr '15, 07:08</p></div></div><div id="comments-container-41632" class="comments-container"></div><div id="comment-tools-41632" class="comment-tools"></div><div class="clear"></div><div id="comment-41632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41637"></span>

<div id="answer-container-41637" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41637-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>packet-tzsp.c refers to <a href="http://web.archive.org/web/20050404125022/http://www.networkchemistry.com/support/appnotes/an001_tzsp.html">http://web.archive.org/web/20050404125022/http://www.networkchemistry.com/support/appnotes/an001_tzsp.html</a></p><p>Which specify WLAN_RADIO_HDR_SIGNAL 10 Signal strength of the received packet. Signed byte.</p><p>Which seems to imply a one byte value... On the other hand it also says "the tag is followed by one byte containing the length of the value field in bytes"</p><p>If you want to change the code You have to edit these lines</p><p><code>proto_tree_add_item(tag_tree, hf_signal, tvb, pos, 1, ENC_BIG_ENDIAN);</code></p><pre><code>    `{ &amp;hf_signal, {
        &quot;Signal&quot;, &quot;tzsp.wlan.signal&quot;, FT_INT8, BASE_DEC,
        NULL, 0, NULL, HFILL }},`</code></pre><p>to</p><pre><code>`proto_tree_add_item(tag_tree, hf_signal, tvb, pos, length, ENC_BIG_ENDIAN);`
    `{ &amp;hf_signal, {
        &quot;Signal&quot;, &quot;tzsp.wlan.signal&quot;, FT_INT16, BASE_DEC,
        NULL, 0, NULL, HFILL }},`</code></pre><p>Note that this will not work for length &gt; 2</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '15, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></img></div></div><div id="comments-container-41637" class="comments-container"><span id="41638"></span><div id="comment-41638" class="comment"><div id="post-41638-score" class="comment-score"></div><div class="comment-text"><p>And it will not work if the Length is indeed 1 byte. So this cannot be a generic solution.</p></div><div id="comment-41638-info" class="comment-info"><span class="comment-age">(21 Apr '15, 07:47)</span> Jaap ♦</div></div><span id="41639"></span><div id="comment-41639" class="comment"><div id="post-41639-score" class="comment-score"></div><div class="comment-text"><p>Why wouldn't it work with one byte?</p></div><div id="comment-41639-info" class="comment-info"><span class="comment-age">(21 Apr '15, 08:36)</span> Anders ♦</div></div><span id="41640"></span><div id="comment-41640" class="comment"><div id="post-41640-score" class="comment-score"></div><div class="comment-text"><p>Gah because of int type (negative values), ok so use..add_int.. And do lengt check etc before adding the value</p></div><div id="comment-41640-info" class="comment-info"><span class="comment-age">(21 Apr '15, 08:40)</span> Anders ♦</div></div><span id="41641"></span><div id="comment-41641" class="comment"><div id="post-41641-score" class="comment-score"></div><div class="comment-text"><p>Doesn't the description imply a variable length field, in which case you need to read the length and then add the appropriately sized value?</p><p>Having a capture with that packet in would help.</p></div><div id="comment-41641-info" class="comment-info"><span class="comment-age">(21 Apr '15, 08:53)</span> grahamb ♦</div></div><span id="41642"></span><div id="comment-41642" class="comment"><div id="post-41642-score" class="comment-score"></div><div class="comment-text"><p>Juniper's WLA send two bytes in that field.</p></div><div id="comment-41642-info" class="comment-info"><span class="comment-age">(21 Apr '15, 08:55)</span> Michael Bychkov</div></div><span id="41648"></span><div id="comment-41648" class="comment not_top_scorer"><div id="post-41648-score" class="comment-score"></div><div class="comment-text"><p>Please file a bug on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a> and attach a capture to the bug for use when testing the fix.</p></div><div id="comment-41648-info" class="comment-info"><span class="comment-age">(21 Apr '15, 14:16)</span> Guy Harris ♦♦</div></div><span id="41674"></span><div id="comment-41674" class="comment not_top_scorer"><div id="post-41674-score" class="comment-score"></div><div class="comment-text"><p>I tried to change from:</p><pre><code> proto_tree_add_item(tag_tree, hf_signal, tvb, pos, 1, ENC_BIG_ENDIAN);

{ &amp;hf_signal, {
    &quot;Signal&quot;, &quot;tzsp.wlan.signal&quot;, FT_INT8, BASE_DEC,
    NULL, 0, NULL, HFILL }},</code></pre><p>to</p><pre><code>proto_tree_add_item(tag_tree, hf_signal, tvb, pos, length, ENC_BIG_ENDIAN);

{ &amp;hf_signal, {
    &quot;Signal&quot;, &quot;tzsp.wlan.signal&quot;, FT_INT16, BASE_DEC,
    NULL, 0, NULL, HFILL }},</code></pre><p>But it doesn't work also.</p></div><div id="comment-41674-info" class="comment-info"><span class="comment-age">(22 Apr '15, 05:37)</span> Michael Bychkov</div></div><span id="41700"></span><div id="comment-41700" class="comment not_top_scorer"><div id="post-41700-score" class="comment-score"></div><div class="comment-text"><p>What does it do instead of working?</p><p>Note that the "Silence" value also appears to be 2 bytes, so you'd need to change that as well, if by "doesn't work" means "Signal is now OK, but Silence isn't OK".</p></div><div id="comment-41700-info" class="comment-info"><span class="comment-age">(22 Apr '15, 10:51)</span> Guy Harris ♦♦</div></div><span id="41881"></span><div id="comment-41881" class="comment not_top_scorer"><div id="post-41881-score" class="comment-score"></div><div class="comment-text"><p>Ok, How can i put into output file fields in HEX from tcpdump?</p></div><div id="comment-41881-info" class="comment-info"><span class="comment-age">(27 Apr '15, 05:52)</span> Michael Bychkov</div></div></div><div id="comment-tools-41637" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-41637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

