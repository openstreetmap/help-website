+++
type = "question"
title = "offset value from other file"
description = '''Hi Iam developing custom dissector. where in some part i need to pass the tvb to a externl function NAS message from the file packet-gsm_a_dtap.c. SOme times im calculating remaining length by sustracting the step by step length used  example  proto_tree_add_text(bm__subtree, next_tvb, offset_payloa...'''
date = "2014-11-20T02:21:00Z"
lastmod = "2014-11-20T04:02:00Z"
weight = 38008
keywords = [ "value", "offset" ]
aliases = [ "/questions/38008" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [offset value from other file](/questions/38008/offset-value-from-other-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38008-score" class="post-score" title="current number of votes">0</div><span id="post-38008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Iam developing custom dissector. where in some part i need to pass the tvb to a externl function NAS message from the file packet-gsm_a_dtap.c.</p><p>SOme times im calculating remaining length by sustracting the step by step length used</p><p>example</p><pre><code>        proto_tree_add_text(bm__subtree, next_tvb, offset_payload, 1 , &quot;Instances : 0x%02x (%d)&quot;, instances, instances);

        offset_payload+=1;
        payload_length-=1;</code></pre><p>but when i call NAS message process Call dissector</p><pre><code>            call_dissector(NAS_handle, NAS_tvb , pinfo, NASPDU_tree);</code></pre><p>i copuld not get the correct figure of payload length . how can i get this? Any idea?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-value" rel="tag" title="see questions tagged &#39;value&#39;">value</span> <span class="post-tag tag-link-offset" rel="tag" title="see questions tagged &#39;offset&#39;">offset</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '14, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p><span>umar</span><br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div></div><div id="comments-container-38008" class="comments-container"><span id="38014"></span><div id="comment-38014" class="comment"><div id="post-38014-score" class="comment-score">1</div><div class="comment-text"><p>I'm not sure I understand the question. As I understand it the gsm_a_detap dissector is called with a NAS message, it's then distributed to the correct subdissector dependent on the Protocol Discriminator(PD). Are you calling your subdissector if one of the values of PD isn't handled by the dissector or replacing an existing call? Regardles I think that the tvb given to gsm_dtap should be the complete Layer 3 message so it should be enough to check the length of the tvb. But perhaps you should look at changing the dissector calling the DTAP one to call your dissector instead? That dissector should know the length of the layer3 message I would think.</p></div><div id="comment-38014-info" class="comment-info"><span class="comment-age">(20 Nov '14, 04:02)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-38008" class="comment-tools"></div><div class="clear"></div><div id="comment-38008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

