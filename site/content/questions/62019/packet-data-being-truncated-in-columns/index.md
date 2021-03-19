+++
type = "question"
title = "Packet data being truncated in Columns"
description = '''I was looking into doing some post processing work on some wireshark logs I captured containing VMF packets. I noticed that packets I found that the logs outputted from wireshark have a 255 character limit per column and some packet data is being truncated. The issue is present in the summary as wel...'''
date = "2017-06-14T08:32:00Z"
lastmod = "2017-06-14T12:18:00Z"
weight = 62019
keywords = [ "pcapng", "truncated", "dissector", "wireshark" ]
aliases = [ "/questions/62019" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Packet data being truncated in Columns](/questions/62019/packet-data-being-truncated-in-columns)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62019-score" class="post-score" title="current number of votes">0</div><span id="post-62019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was looking into doing some post processing work on some wireshark logs I captured containing VMF packets. I noticed that packets I found that the logs outputted from wireshark have a 255 character limit per column and some packet data is being truncated. The issue is present in the summary as well when I'm doing live data captures. I'm using an older version of wireshark(v1.10.3). Would updating to a newer version of wireshark have a much larger limit?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span> <span class="post-tag tag-link-truncated" rel="tag" title="see questions tagged &#39;truncated&#39;">truncated</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '17, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/c51a9570f366127d1c9d0273826bdf89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MartinGD&#39;s gravatar image" /><p><span>MartinGD</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MartinGD has no accepted answers">0%</span></p></div></div><div id="comments-container-62019" class="comments-container"></div><div id="comment-tools-62019" class="comment-tools"></div><div class="clear"></div><div id="comment-62019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62025"></span>

<div id="answer-container-62025" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62025-score" class="post-score" title="current number of votes">0</div><span id="post-62025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the latest <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/column-info.h;h=4fe638ca0678e765ac626ac65e265be87078e6c3;hb=HEAD#l37">column-info.h</a>:</p><pre><code>#define COL_MAX_LEN 256
#define COL_MAX_INFO_LEN 4096</code></pre><p>As far as I can tell, these are the exact same values that were specified in 1.10 though, so if the column data of interest is anything but the Info column, you'll still be limited to <code>COL_MAX_LEN</code>.</p><p>To avoid truncation, you could try to:</p><ul><li><p>Use <code>tshark</code> instead of Wireshark and specify the fields of interest as the output instead of relying on the column data. For example:</p><p><code>tshark -r foo.pcap -T fields -e proto1.field1 -e proto1.field2 -e proto2.field1 ...</code></p><p>You can specify as many fields as you wish including any custom columns that might have been truncated. For those columns that were not being truncated, you can use <code>-e _ws.col.Foo</code> where Foo is the name of the column, e.g., <code>-e _ws.col.Info</code>. Refer to the <a href="https://www.wireshark.org/docs/man-pages/tshark.html"><code>tshark</code> man page</a> for more information.</p></li><li><p>Compile Wireshark yourself, but with a larger value for <code>COL_MAX_LEN</code>.</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '17, 10:34</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-62025" class="comments-container"><span id="62026"></span><div id="comment-62026" class="comment"><div id="post-62026-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure if the _ws.col.Foo format is supported in 1.10.</p></div><div id="comment-62026-info" class="comment-info"><span class="comment-age">(14 Jun '17, 10:42)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="62027"></span><div id="comment-62027" class="comment"><div id="post-62027-score" class="comment-score"></div><div class="comment-text"><p>Right, I think it was originally just <code>col.Foo</code> back then. The <code>_ws.</code> prefix was added with the release of <a href="https://www.wireshark.org/news/20140731.html">Wireshark 1.12.0</a>.</p></div><div id="comment-62027-info" class="comment-info"><span class="comment-age">(14 Jun '17, 10:44)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="62030"></span><div id="comment-62030" class="comment"><div id="post-62030-score" class="comment-score"></div><div class="comment-text"><p>Also keep in mind that any given proto item's string representation is limited to 240 chars--I <em>think</em> that will also apply to tshark's <code>-e</code> output.</p><pre><code>/** the maximum length of a protocol field string representation */
#define ITEM_LABEL_LENGTH       240</code></pre></div><div id="comment-62030-info" class="comment-info"><span class="comment-age">(14 Jun '17, 11:11)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="62031"></span><div id="comment-62031" class="comment"><div id="post-62031-score" class="comment-score"></div><div class="comment-text"><p>Ah good point. I suppose the idea won't work without increasing that value too.</p></div><div id="comment-62031-info" class="comment-info"><span class="comment-age">(14 Jun '17, 11:25)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="62032"></span><div id="comment-62032" class="comment"><div id="post-62032-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the input! Editing COL_MAX_LEN and recompiling wireshark seems to of done the trick.</p></div><div id="comment-62032-info" class="comment-info"><span class="comment-age">(14 Jun '17, 12:18)</span> <span class="comment-user userinfo">MartinGD</span></div></div></div><div id="comment-tools-62025" class="comment-tools"></div><div class="clear"></div><div id="comment-62025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

