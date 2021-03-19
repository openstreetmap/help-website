+++
type = "question"
title = "CRC16-TVB checksum custom dissector CRC"
description = '''Hi Iam developing custom dissector using wieshark 1.113 ,  iam trying for CRC tree uusing crc16_ccitt_tvb() (my polynominal is (x16 + x12 + x5 + 1))and i can able to see results correctly. But its showing reverse (eg. my 2 byte CRC is 52 AC my wireshark shows as CRC 0X52AC [CORRECT] but actually i s...'''
date = "2014-05-27T01:31:00Z"
lastmod = "2014-05-27T21:02:00Z"
weight = 33101
keywords = [ "crc16", "tvb" ]
aliases = [ "/questions/33101" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [CRC16-TVB checksum custom dissector CRC](/questions/33101/crc16-tvb-checksum-custom-dissector-crc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33101-score" class="post-score" title="current number of votes">0</div><span id="post-33101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Iam developing custom dissector using wieshark 1.113 , iam trying for CRC tree uusing crc16_ccitt_tvb() (my polynominal is (x16 + x12 + x5 + 1))and i can able to see results correctly.</p><p>But its showing reverse (eg. my 2 byte CRC is 52 AC my wireshark shows as CRC 0X52AC [CORRECT] but actually i suppose to get CRC 0XAC52 [CORRECT] here below my code.</p><pre><code>checksum_offset = reported_length - 2;
checksum = tvb_get_ntohs(tvb, checksum_offset);
checksum_calculated = crc16_ccitt_tvb(tvb, checksum_offset);
checksum_calculated = g_htons(checksum_calculated);
  /* Note: g_htons() macro may eval arg multiple times */

if (checksum == checksum_calculated) {
        checksum_ti = proto_tree_add_uint_format_value(PARENT_tree, hf_PARENT_CRC, tvb, checksum_offset, 2, 0, &quot;0x%04x [correct]&quot;, checksum, ENC_LITTLE_ENDIAN);
        checksum_tree = proto_item_add_subtree(checksum_ti, ett_PARENT_CRC);
        proto_tree_add_boolean(checksum_tree, hf_PARENT_cksum_gd, tvb,checksum_offset, 2, TRUE);
        proto_tree_add_boolean(checksum_tree, hf_PARENT_cksum_bd, tvb, checksum_offset, 2, FALSE);
 } else {
        checksum_ti = proto_tree_add_uint_format_value(PARENT_tree, hf_PARENT_CRC, tvb, checksum_offset, 2, 0, &quot;0x%04x [incorrect, should be 0x%04x]&quot;, checksum, checksum_calculated, ENC_LITTLE_ENDIAN);
        checksum_tree = proto_item_add_subtree(checksum_ti, ett_PARENT_CRC);
        proto_tree_add_boolean(checksum_tree, hf_PARENT_cksum_gd, tvb, checksum_offset, 2, FALSE);
        proto_tree_add_boolean(checksum_tree, hf_PARENT_cksum_bd, tvb, checksum_offset, 2, TRUE);
 }</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-crc16" rel="tag" title="see questions tagged &#39;crc16&#39;">crc16</span> <span class="post-tag tag-link-tvb" rel="tag" title="see questions tagged &#39;tvb&#39;">tvb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '14, 01:31</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p><span>umar</span><br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 May '14, 02:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-33101" class="comments-container"><span id="33104"></span><div id="comment-33104" class="comment"><div id="post-33104-score" class="comment-score"></div><div class="comment-text"><p><span>@mrajsekar</span> I've already fixed the formatting once, if you edit it again please use the "code" button to format code correctly (or use code tags around the code).</p></div><div id="comment-33104-info" class="comment-info"><span class="comment-age">(27 May '14, 02:54)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-33101" class="comment-tools"></div><div class="clear"></div><div id="comment-33101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33113"></span>

<div id="answer-container-33113" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33113-score" class="post-score" title="current number of votes">0</div><span id="post-33113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just a wild guess: Please try <strong>ENC_BIG_ENDIAN</strong> instead of <strong>ENC_LITTLE_ENDIAN</strong>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '14, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-33113" class="comments-container"></div><div id="comment-tools-33113" class="comment-tools"></div><div class="clear"></div><div id="comment-33113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33115"></span>

<div id="answer-container-33115" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33115-score" class="post-score" title="current number of votes">0</div><span id="post-33115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>proto_tree_add_uint_format_value()</code> takes, as the value argument <em>and</em> as arguments to the format string, values in the <em>host</em> byte order, so <em>don't</em> do</p><pre><code>checksum_calculated = g_htons(checksum_calculated);</code></pre><p>Also, all arguments to <code>proto_tree_add_uint_format_value()</code> after the format string are arguments to the format string, and <code>proto_tree_add_uint_format_value()</code> doesn't fetch any values, so leave the <code>ENC_LITTLE_ENDIAN</code> argument out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '14, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-33115" class="comments-container"><span id="33124"></span><div id="comment-33124" class="comment"><div id="post-33124-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>Thanks for the reply</p><p>Found the issue from checksum = tvb_get_ntohs(tvb, checksum_offset);</p><p>This FETCH value in BIG Endian</p><p>I hve used checksum = tvb_get_letohs(tvb, checksum_offset);</p><p>Issue settled. Thanks!:)</p></div><div id="comment-33124-info" class="comment-info"><span class="comment-age">(27 May '14, 21:02)</span> <span class="comment-user userinfo">umar</span></div></div></div><div id="comment-tools-33115" class="comment-tools"></div><div class="clear"></div><div id="comment-33115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

