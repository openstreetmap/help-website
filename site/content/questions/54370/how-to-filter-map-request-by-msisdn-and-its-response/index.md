+++
type = "question"
title = "How to filter MAP request by msisdn and its response"
description = '''Hi, Currently I am sending AnyTimeInterrogation to the HLR over a MAP link. I would like to monitor specific queries being made for certain users. So I need to filter by msisdn. It gets complicated because the answer to the ATI does not contain the msisdn field. The only way to link the query to the...'''
date = "2016-07-27T08:47:00Z"
lastmod = "2016-07-27T15:52:00Z"
weight = 54370
keywords = [ "tcap", "map", "mate", "hlr" ]
aliases = [ "/questions/54370" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter MAP request by msisdn and its response](/questions/54370/how-to-filter-map-request-by-msisdn-and-its-response)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54370-score" class="post-score" title="current number of votes">0</div><span id="post-54370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Currently I am sending AnyTimeInterrogation to the HLR over a MAP link. I would like to monitor specific queries being made for certain users. So I need to filter by msisdn.</p><p>It gets complicated because the answer to the ATI does not contain the msisdn field. The only way to link the query to the answer is by the dtid field in TCAP layer</p><p>Any pointers as to how i can do this filter?</p><p>A pcap is downloadable from here</p><p><a href="https://drive.google.com/file/d/0B9-7ejADsontcmVSLThyOE5YUzg/view?usp=sharing">https://drive.google.com/file/d/0B9-7ejADsontcmVSLThyOE5YUzg/view?usp=sharing</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcap" rel="tag" title="see questions tagged &#39;tcap&#39;">tcap</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-mate" rel="tag" title="see questions tagged &#39;mate&#39;">mate</span> <span class="post-tag tag-link-hlr" rel="tag" title="see questions tagged &#39;hlr&#39;">hlr</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '16, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/3fa128cb9679b0f80992ec7945c2aa76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mquevedob&#39;s gravatar image" /><p><span>mquevedob</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mquevedob has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jul '16, 14:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-54370" class="comments-container"></div><div id="comment-tools-54370" class="comment-tools"></div><div class="clear"></div><div id="comment-54370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54372"></span>

<div id="answer-container-54372" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54372-score" class="post-score" title="current number of votes">3</div><span id="post-54372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong>&lt; EDIT &gt;</strong><br />
As <span>@JeffMorriss</span>' has pointed out in <a href="https://ask.wireshark.org/questions/55614/in-a-pcap-file-opened-in-wireshark-how-do-you-know-which-response-packet-belongs-to-a-particular-request-packet/55688">his Answer to another Question</a> (many thanks), the TCAP dissector has this as an embedded functionality which, however, is not activated by default. If you activate it, you can filter or find the <code>invoke</code> packet (using a display filter condition like <code>e164.msisdn == "595972123456"</code>), and use a link in the <code>[Stat]</code> part of TCAP dissection to jump to the response (if it is present in the capture).</p><p>Using MATE as described in the original Answer kept below, you can directly filter or find the <code>returnResultLast</code> response up to the msisdn (using a display filter condition <code>tcap_dialog.msisdn == "595972123456"</code>) regardless whether the TCAP ¨dissector's embedded cross-reference functionality is activated or not (because the MATE configuration duplicates it), as MATE adds to packet dissection metafields whose sources are fields of related other packets.</p><p>Either way, it must be possible to recognize that the SCCP calling address of the <code>invoke</code> is the same as the SCCP called address of the <code>returnResultLast</code> - if some Global Title Translation changes the SCCP called address of the response (e.g. from E.164 number alone to point code alone), the tcap transaction id alone is not sufficient to match the <code>invoke</code> with the <code>returnResultLast</code>.<br />
<strong>&lt; /EDIT &gt;</strong></p><p>If you need to filter PDUs by fields which are not directly present in them and the existing dissector does not provide any meta-fields for this purpose, <a href="https://wiki.wireshark.org/Mate/Manual">MATE</a> is your only way out.</p><p>Using MATE, you may group PDUs together by contents of some fields (in your case, the <code>tcap.dtid</code> field), and export values from some other fields (in your case, the <code>gsm_map.msisdn</code>) from the individual PDUs into meta-fields of the group. To avoid confusion, the group meta-fields bear their own names different from those of the source fields in the PDUs. All PDUs which became members of some group can be display-filtered also on the group meta-fields even if the original fields are not directly present in them.</p><p>If you need a pushstart, publish a trace with at least two independent requests and responses.</p><p>Currently, there are some issues with MATE in tshark, but they may not affect you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '16, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Sep '16, 22:35</strong> </span></p></div></div><div id="comments-container-54372" class="comments-container"><span id="54373"></span><div id="comment-54373" class="comment"><div id="post-54373-score" class="comment-score"></div><div class="comment-text"><p>thanks for the answer! Would you give me some pointers as to how i would have to configure mate in order to filter the outgoing package by msisdn and the incoming packet to match the oid field of the outgoing package?</p></div><div id="comment-54373-info" class="comment-info"><span class="comment-age">(27 Jul '16, 09:41)</span> <span class="comment-user userinfo">mquevedob</span></div></div><span id="54374"></span><div id="comment-54374" class="comment"><div id="post-54374-score" class="comment-score"></div><div class="comment-text"><p>There are no pointers other than <a href="https://wiki.wireshark.org/Mate/Manual">the manual already pointed to</a>.</p><p>Or, if it has discouraged you, you can accept my proposal from the answer:</p><blockquote><p>If you need a pushstart, publish a trace with at least two independent requests and responses.</p></blockquote><p>Because I won't spend time creating a <strong>useless</strong> MATE configuration; to put together a useful one, I need the pcap file to debug it.</p></div><div id="comment-54374-info" class="comment-info"><span class="comment-age">(27 Jul '16, 09:52)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="54377"></span><div id="comment-54377" class="comment"><div id="post-54377-score" class="comment-score"></div><div class="comment-text"><p>I have shared a link (on the original post) where you can download the pcap file. Please let me know. And thanks for your support !</p></div><div id="comment-54377-info" class="comment-info"><span class="comment-age">(27 Jul '16, 10:02)</span> <span class="comment-user userinfo">mquevedob</span></div></div><span id="54381"></span><div id="comment-54381" class="comment"><div id="post-54381-score" class="comment-score"></div><div class="comment-text"><p>Here we go:</p><pre><code>Pdu map_pdu Proto gsm_map Transport tcap/sccp {
    Extract trans_id From tcap.otid;
    Extract trans_id From tcap.dtid;
    Extract msisdn From gsm_map.msisdn ;
};

Gop tcap_dialog On map_pdu Match (trans_id) {
    Start(msisdn);
    Extra(msisdn);
};

Done;</code></pre><p>It is really minimalistic - I am not 100% sure what else on top of TCAP transaction ID has to be checked so that the PDUs could be safely considered a matching request and answer. If you would capture somewhere closer to the HLR and multiple GMSCs would query the same HLR, I guess nothing prevents them from incidentally using the same transaction ID, so the GT of the GMSC should also be part of the Gop key. But integrating that requires more effort because while <code>tcap.otid</code> is only present in the <code>invoke</code> and <code>tcap.dtid</code> is only present in the <code>returnResultLast</code>, the calling and called GT is present in both but with swapped roles, which has to be sorted out using <code>Transform</code>. And you cannot use both GTs without filtering because the GT of the HLR as called in the <code>invoke</code> differs from the GT of the VLR as calling in the <code>returnResultLast</code>, so the (gt,gt) AVPL of the <code>invoke</code> and <code>returnResultLast</code> would differ, preventing the PDUs from matching the same GoP key. Plus this analysis completely ignores cases where one of the SCCP (calling, called) would e.g. not contain the GT but just the point code.</p><p>This MATE configuration (<code>Edit-&gt;Preferences-&gt;Protocols-&gt;Mate-&gt;Configuration Filename</code>, followed by <code>OK</code> and starting a new instance of Wireshark), allows you to use a display filter <code>mate.tcap_dialog.msisdn == "91:95:95:17:41:01:10"</code> to filter an invoke/returnResultLast pair by msisdn. Unfortunately, the format is like this and cannot be changed as this is how the gsm_map dissector provides it.</p></div><div id="comment-54381-info" class="comment-info"><span class="comment-age">(27 Jul '16, 14:24)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="54383"></span><div id="comment-54383" class="comment"><div id="post-54383-score" class="comment-score">1</div><div class="comment-text"><p>Wow, as it turned out to be impossible to achieve the goal of <code>Extract</code>ing both SCCP called and SCCP calling into two AVPs of the same name but, depending on presence of other fields allowing to discriminate between <code>invoke</code> and <code>returnResultLast</code>, keeping as part of the Gop key only that one of the two which represented the GMSC using <code>Transform</code>, I've discovered another feature of MATE not explicitly mentioned in the documentation.</p><p>Apparently it is possible to define several MATE Pdus of the same type but with different description, and get all of them created in parallel from the very same source PDU. So together with the possibility to <code>Accept</code> a Pdu depending on an AVPL match, it is possible to <code>Extract</code> a <code>(gmsc_gt, trans_id)</code> AVPL from <code>(sccp.calling.digits, tcap.otid)</code> in one case and from <code>(sccp.called.digits, tcap.dtid)</code> in another, and <code>Accept</code> only the one whose AVPL contains the <code>trans_id</code>. So effectively, for the <code>invoke</code> where only the <code>tcap.otid</code> is present, the value of the <code>gmsc_gt</code> AVP is taken from the <code>sccp.calling.digits</code>, while for the <code>returnResultLast</code>, it is taken from the <code>sccp.called.digits</code> because in that message, only the <code>tcap.dtid</code> is present.</p><p>So the result is as follows:</p><pre><code>Pdu map_msg Proto gsm_map Transport tcap/sccp {
    Extract trans_id From tcap.otid;
    Extract gmsc_gt From sccp.calling.digits;
    Extract msisdn From gsm_map.msisdn;
    Criteria Accept Strict (trans_id);
};

Pdu map_msg Proto gsm_map Transport tcap/sccp {
    Extract trans_id From tcap.dtid;
    Extract gmsc_gt From sccp.called.digits;
    Criteria Accept Strict (trans_id);
};

Gop tcap_dialog On map_msg Match (trans_id,gmsc_gt) {
    Start(msisdn);
    Extra(msisdn);
};

Done;</code></pre><p>I guess I'll have to update the Wiki accordingly soon.</p></div><div id="comment-54383-info" class="comment-info"><span class="comment-age">(27 Jul '16, 15:52)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-54372" class="comment-tools"></div><div class="clear"></div><div id="comment-54372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54371"></span>

<div id="answer-container-54371" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54371-score" class="post-score" title="current number of votes">1</div><span id="post-54371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds like a job for <a href="https://wiki.wireshark.org/Mate">MATE</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '16, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54371" class="comments-container"></div><div id="comment-tools-54371" class="comment-tools"></div><div class="clear"></div><div id="comment-54371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

