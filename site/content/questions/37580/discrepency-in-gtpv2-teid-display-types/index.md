+++
type = "question"
title = "[closed] discrepency in gtpv2 teid display types."
description = '''Hi, Does someone know the reason for keeping the types as different ? gtpv2.teid displayed value is in decimal for gtpv2.teid however hex for gtpv2.f_teid_gre_key. This is inconvenient while analysing GTP flows.  Can we please make the gtpv2.teid as HEX as well. As a reference, I came across the fol...'''
date = "2014-11-05T02:44:00Z"
lastmod = "2014-11-06T01:51:00Z"
weight = 37580
keywords = [ "gtpv2c" ]
aliases = [ "/questions/37580" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] discrepency in gtpv2 teid display types.](/questions/37580/discrepency-in-gtpv2-teid-display-types)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37580-score" class="post-score" title="current number of votes">0</div><span id="post-37580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Does someone know the reason for keeping the types as different ? gtpv2.teid displayed value is in decimal for gtpv2.teid however hex for gtpv2.f_teid_gre_key.</p><p>This is inconvenient while analysing GTP flows. Can we please make the gtpv2.teid as HEX as well.</p><p>As a reference, I came across the following thread <a href="https://ask.wireshark.org/questions/24221/decode-gtpv2-teid-as-decimal-or-hex">https://ask.wireshark.org/questions/24221/decode-gtpv2-teid-as-decimal-or-hex</a> which accepted the change from decimal to hex but probably did it just for later and not former field.</p><p>5345 { &amp;hf_gtpv2_t, 5346 {"TEID flag (T)", "gtpv2.t", 5347 FT_UINT8, BASE_DEC, NULL, 0x08, 5348 "If TEID field is present or not", HFILL} 5349 }, 5350 { &amp;hf_gtpv2_message_type,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gtpv2c" rel="tag" title="see questions tagged &#39;gtpv2c&#39;">gtpv2c</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '14, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/4612bb024cb13332f1aa189da329339b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PKR&#39;s gravatar image" /><p><span>PKR</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PKR has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>05 Nov '14, 02:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-37580" class="comments-container"><span id="37581"></span><div id="comment-37581" class="comment"><div id="post-37581-score" class="comment-score"></div><div class="comment-text"><p>This is a duplicate of <a href="https://ask.wireshark.org/questions/24221/decode-gtpv2-teid-as-decimal-or-hex">https://ask.wireshark.org/questions/24221/decode-gtpv2-teid-as-decimal-or-hex</a></p></div><div id="comment-37581-info" class="comment-info"><span class="comment-age">(05 Nov '14, 02:55)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37605"></span><div id="comment-37605" class="comment"><div id="post-37605-score" class="comment-score"></div><div class="comment-text"><p>This is not a duplicate of above. Please check <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-gtpv2.c?r1=51789&amp;r2=51788&amp;pathrev=51789">http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-gtpv2.c?r1=51789&amp;r2=51788&amp;pathrev=51789</a></p><p>I am asking that similar change should apply to gtpv2.teid as well.</p></div><div id="comment-37605-info" class="comment-info"><span class="comment-age">(06 Nov '14, 00:57)</span> <span class="comment-user userinfo">PKR</span></div></div><span id="37606"></span><div id="comment-37606" class="comment"><div id="post-37606-score" class="comment-score"></div><div class="comment-text"><p>In the question I quoted you commented:</p><blockquote>Hi, Have been a wireshark + GTP user for quite some time now. Just realized that teid displayed value is in decimal for gtpv2.teid however hex for gtpv2.f_teid_gre_key. This is again inconvenient while trying to analyse /observe GTP flows. Can we please make the gtpv2.teid as HEX.</blockquote><p>i.e. the same as the "new" question posted above.</p><p>Then <span>@Pascal Quantin</span> commented that this has been fixed in development versions, so this entire question is superfluous.</p><p>In addition, the place to make enhancement requests is the Wireshark <a href="https://bugs.wireshark.org">Bugzilla</a>, although asking questions about why things are done they way they are is appropriate for this site.</p></div><div id="comment-37606-info" class="comment-info"><span class="comment-age">(06 Nov '14, 01:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-37580" class="comment-tools"></div><div class="clear"></div><div id="comment-37580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by grahamb 05 Nov '14, 02:55

</div>

</div>

</div>

