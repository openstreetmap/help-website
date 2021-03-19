+++
type = "question"
title = "How to Display DSCP Column as a DEC or HEX Value as Needed"
description = '''Keywords: Differentiated Services, DifServ, TOS,  I know how to display the column:  Field Name: ip.dsfield.dscp How do we force that output to display in DEC (decimal) or HEX or even BIN if wanted? William...'''
date = "2014-04-17T08:44:00Z"
lastmod = "2014-04-17T18:26:00Z"
weight = 31934
keywords = [ "services", "tos", "differentiated", "ip.dsfield.dscp", "difserv" ]
aliases = [ "/questions/31934" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to Display DSCP Column as a DEC or HEX Value as Needed](/questions/31934/how-to-display-dscp-column-as-a-dec-or-hex-value-as-needed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31934-score" class="post-score" title="current number of votes">0</div><span id="post-31934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Keywords: Differentiated Services, DifServ, TOS,</p><p>I know how to display the column:</p><p>Field Name: ip.dsfield.dscp</p><p>How do we force that output to display in DEC (decimal) or HEX or even BIN if wanted?</p><p>William...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-services" rel="tag" title="see questions tagged &#39;services&#39;">services</span> <span class="post-tag tag-link-tos" rel="tag" title="see questions tagged &#39;tos&#39;">tos</span> <span class="post-tag tag-link-differentiated" rel="tag" title="see questions tagged &#39;differentiated&#39;">differentiated</span> <span class="post-tag tag-link-ip.dsfield.dscp" rel="tag" title="see questions tagged &#39;ip.dsfield.dscp&#39;">ip.dsfield.dscp</span> <span class="post-tag tag-link-difserv" rel="tag" title="see questions tagged &#39;difserv&#39;">difserv</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '14, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/93b885acdab4ef4d0fd8845b9b457df3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WAudette&#39;s gravatar image" /><p><span>WAudette</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WAudette has no accepted answers">0%</span></p></div></div><div id="comments-container-31934" class="comments-container"><span id="31949"></span><div id="comment-31949" class="comment"><div id="post-31949-score" class="comment-score"></div><div class="comment-text"><p>Hi William,</p><p>That’s a great question and yes, it’s tough to find the answer.</p><p>Essentially, you to add an “IP DSCP Value” column. Remember that there are two ways to add columns – you can right click on the DSCP line in an IP header and choose Apply Column. You can also choose Preferences | Columns. That’s what you want to do to see the IP DSCP value in decimal.</p><p>In the Preferences | Columns area, click Add. Select IP DSCP Value for the field type. Click on the Title column to enter a new name. Click anywhere in the white space before clicking OK (this gets you out of edit mode).</p><p><img src="http://i1362.photobucket.com/albums/r698/WAudette/IPDSCP_zpsfb2cb0fb.png" alt="alt text" /></p><p>Let me know if that doesn’t work for you!</p><p>Laura Chappell</p></div><div id="comment-31949-info" class="comment-info"><span class="comment-age">(17 Apr '14, 14:32)</span> <span class="comment-user userinfo">WAudette</span></div></div></div><div id="comment-tools-31934" class="comment-tools"></div><div class="clear"></div><div id="comment-31934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31958"></span>

<div id="answer-container-31958" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31958-score" class="post-score" title="current number of votes">0</div><span id="post-31958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For changing the value from hex to decimal, I don't believe there's any way to toggle that for a given field type in Wireshark. TOS/DSCP does have a preference for switching between two formats, but not a preference for changing the field from hex to decimal. Personally I'd prefer the IETF notation (AF12, EF, etc.).</p><p>This seems to be controlled around the 2,000 line mark in the packet-ip.c file in Wireshark's source code:</p><pre><code>if (g_ip_dscp_actif) {
  tf = proto_tree_add_uint_format(ip_tree, hf_ip_dsfield, tvb, offset + 1,
    1, iph-&gt;ip_tos, &quot;Differentiated Services Field: 0x%02x &quot;
    &quot;(DSCP 0x%02x: %s; ECN: 0x%02x: %s)&quot;, iph-&gt;ip_tos,
    IPDSFIELD_DSCP(iph-&gt;ip_tos), val_to_str_ext_const(IPDSFIELD_DSCP(iph-&gt;ip_tos),
                                                      &amp;dscp_vals_ext, &quot;Unknown DSCP&quot;),
    IPDSFIELD_ECN(iph-&gt;ip_tos), val_to_str_const(IPDSFIELD_ECN(iph-&gt;ip_tos),
                                                 ecn_vals, &quot;Unknown ECN&quot;));

  field_tree = proto_item_add_subtree(tf, ett_ip_dsfield);
  proto_tree_add_item(field_tree, hf_ip_dsfield_dscp, tvb, offset + 1, 1, ENC_NA);
  proto_tree_add_item(field_tree, hf_ip_dsfield_ecn, tvb, offset + 1, 1, ENC_NA);
}</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '14, 18:26</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Apr '14, 18:27</strong> </span></p></div></div><div id="comments-container-31958" class="comments-container"></div><div id="comment-tools-31958" class="comment-tools"></div><div class="clear"></div><div id="comment-31958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

