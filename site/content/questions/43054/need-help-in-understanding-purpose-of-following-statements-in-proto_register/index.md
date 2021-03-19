+++
type = "question"
title = "Need help in understanding purpose of following statements in proto_register"
description = '''Hello, I am trying to create a script to document structure of protocol which the disector is discecting. I started working with -&amp;gt; epan_dissectors_packet-gtpv2.c , and parsed that file to get tokens, Can some one please explain the significance/ and usage of the following lines of code ie what e...'''
date = "2015-06-10T12:43:00Z"
lastmod = "2015-06-11T05:16:00Z"
weight = 43054
keywords = [ "disector" ]
aliases = [ "/questions/43054" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need help in understanding purpose of following statements in proto\_register](/questions/43054/need-help-in-understanding-purpose-of-following-statements-in-proto_register)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43054-score" class="post-score" title="current number of votes">0</div><span id="post-43054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am trying to create a script to document structure of protocol which the disector is discecting. I started working with -&gt; epan_dissectors_packet-gtpv2.c , and parsed that file to get tokens, Can some one please explain the significance/ and usage of the following lines of code ie what exactly is the code doing. (I got idea about Line1, but will still like experts opinion)</p><p><strong>Line1</strong></p><pre><code>static hf_register_info hf_gtpv2[] = {
    { &amp;hf_gtpv2_spare_half_octet,
      {&quot;Spare half octet&quot;, &quot;gtpv2.spare_half_octet&quot;,
       FT_UINT8, BASE_DEC, NULL, 0x0,
       NULL, HFILL }
    }</code></pre><p><strong>Line2</strong></p><pre><code>/* Generated from convert_proto_tree_add_text.pl */
  { &amp;hf_gtpv2_transparent_container, { &quot;Transparent Container&quot;, &quot;gtpv2.transparent_container&quot;, FT_BYTES, BASE_NONE, NULL, 0x0, NULL, HFILL }},</code></pre><p><strong>Line3</strong></p><pre><code>static ei_register_info ei[] = {
    { &amp;ei_gtpv2_ie_data_not_dissected, { &quot;gtpv2.ie_data_not_dissected&quot;, PI_UNDECODED, PI_NOTE, &quot;IE data not dissected yet&quot;, EXPFILL }},</code></pre><p><strong>Line4</strong></p><pre><code>expert_gtpv2 = expert_register_protocol(proto_gtpv2);
expert_register_field_array(expert_gtpv2, ei, array_length(ei))</code></pre><p><strong>Line5</strong></p><p>dissector_add_uint("diameter.3gpp", 22, new_create_dissector_handle(dissect_diameter_3gpp_uli, proto_gtpv2));</p><p><strong>Line6</strong></p><p>gtpv2_priv_ext_dissector_table = register_dissector_table("gtpv2.priv_ext", "GTPv2 PRIVATE EXT", FT_UINT16, BASE_DEC);</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-disector" rel="tag" title="see questions tagged &#39;disector&#39;">disector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '15, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/3d041dad7dade4fc0aeeb32031c0e191?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhardwaj_rajesh&#39;s gravatar image" /><p><span>bhardwaj_rajesh</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhardwaj_rajesh has no accepted answers">0%</span></p></div></div><div id="comments-container-43054" class="comments-container"></div><div id="comment-tools-43054" class="comment-tools"></div><div class="clear"></div><div id="comment-43054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43069"></span>

<div id="answer-container-43069" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43069-score" class="post-score" title="current number of votes">0</div><span id="post-43069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would suggest getting a copy of the Wireshark source code and study the file doc/README.dissector. It is all explained in there, with even more details to be found in the relevant header files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '15, 04:14</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-43069" class="comments-container"><span id="43071"></span><div id="comment-43071" class="comment"><div id="post-43071-score" class="comment-score"></div><div class="comment-text"><p>As Jaap says the header fields and expert info is explained elswehere I think.</p><blockquote><p>Line5</p></blockquote><p>Adds a callback to the disector table "diameter.3gpp" for "number 22" used to do further dissection of 3GPP AVP 22.</p><blockquote><p>Line6</p></blockquote><p>Create a dissector table where dissectors can register callbaks, in this case to dissect IE GTPv2 PRIVATE EXT. The vendor Id is used as the "number". So when a private IE is dissected in GTPv2 the dissector checks if there is a callback forthis vendor and if one is found the vendor specific dissector is called to dissect this vendor specified IE. No vendor specific dissectors for GTPv2 exists in the GPL version.</p></div><div id="comment-43071-info" class="comment-info"><span class="comment-age">(11 Jun '15, 04:42)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="43076"></span><div id="comment-43076" class="comment"><div id="post-43076-score" class="comment-score"></div><div class="comment-text"><p>README.dissector can be found <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=doc/README.dissector;hb=HEAD">here</a>.</p></div><div id="comment-43076-info" class="comment-info"><span class="comment-age">(11 Jun '15, 05:16)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-43069" class="comment-tools"></div><div class="clear"></div><div id="comment-43069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

