+++
type = "question"
title = "Problem in displaying some info in the tree of S1AP (using modified packet-s1ap.c)"
description = '''Hello, I have edited the S1AP dissector to fit my own needs to display few info in the tree. The problem which I am facing is that I am getting the info of the previous packet. Hence, please do tell me how to correct this so that the correct info is displayed at correct place. I am attaching the scr...'''
date = "2014-05-06T04:22:00Z"
lastmod = "2014-05-12T23:21:00Z"
weight = 32546
keywords = [ "s1ap" ]
aliases = [ "/questions/32546" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Problem in displaying some info in the tree of S1AP (using modified packet-s1ap.c)](/questions/32546/problem-in-displaying-some-info-in-the-tree-of-s1ap-using-modified-packet-s1apc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32546-score" class="post-score" title="current number of votes">1</div><span id="post-32546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have edited the S1AP dissector to fit my own needs to display few info in the tree. The problem which I am facing is that I am getting the info of the previous packet. Hence, please do tell me how to correct this so that the correct info is displayed at correct place.</p><p>I am attaching the screen shot alongwith and also the following snippet contains the edited dissect_s1ap():</p><pre><code>static void dissect_s1ap(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree){  
    proto_item *s1ap_item = NULL;
    proto_tree *s1ap_tree = NULL;

/* make entry in the Protocol column on summary display */
col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;S1AP&quot;);

/* create the s1ap protocol tree */
s1ap_item = proto_tree_add_protocol_format(tree, proto_s1ap, tvb, 0, -1,&quot;S1 Application Protocol-Dev, Event-Message:%s ,Result:%s, Cause:%s &quot;,val_to_str_ext(ProcedureCode, &amp;s1ap_ProcedureCode_vals_ext,
                        &quot;unknown message&quot;),val_to_str(S1AP_PDU,s1ap_S1AP_PDU_vals, &quot;unknown&quot;),val_to_str(Cause,s1ap_Cause_vals, &quot;unknown&quot;));
//s1ap_item = proto_tree_add_item(tree, proto_s1ap, tvb, 0, -1, ENC_NA);
s1ap_tree = proto_item_add_subtree(s1ap_item, ett_s1ap);

dissect_S1AP_PDU_PDU(tvb, pinfo, s1ap_tree, NULL);}</code></pre><p>Screen-Shot link: <a href="http://postimg.org/image/56t7fkuxv/">http://postimg.org/image/56t7fkuxv/</a></p><p><img src="http://postimg.org/image/56t7fkuxv/" alt="alt text" /></p><p>Regards, Ankur</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-s1ap" rel="tag" title="see questions tagged &#39;s1ap&#39;">s1ap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '14, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/5de132d51e4e183bf230804f938b987c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankur92&#39;s gravatar image" /><p><span>ankur92</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankur92 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 May '14, 04:47</strong> </span></p></div></div><div id="comments-container-32546" class="comments-container"></div><div id="comment-tools-32546" class="comment-tools"></div><div class="clear"></div><div id="comment-32546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32547"></span>

<div id="answer-container-32547" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32547-score" class="post-score" title="current number of votes">2</div><span id="post-32547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ankur92 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your code cannot work as you try to use globals that have not been populated with the current dissection yet (dissect_S1AP_PDU_PDU() function has not been called). Instead they contain the data of the previous packet (as you saw). The right way to do it would be something like:</p><pre><code>    /* create the s1ap protocol tree */
s1ap_item = proto_tree_add_item(tree, proto_s1ap, tvb, 0, -1, ENC_NA);
s1ap_tree = proto_item_add_subtree(s1ap_item, ett_s1ap);

dissect_S1AP_PDU_PDU(tvb, pinfo, s1ap_tree, NULL);
proto_item_append_text(s1ap_item, &quot;, Event-Message:%s ,Result:%s, Cause:%s &quot;,val_to_str_ext(ProcedureCode, &amp;s1ap_ProcedureCode_vals_ext,
                    &quot;unknown message&quot;),val_to_str(S1AP_PDU,s1ap_S1AP_PDU_vals, &quot;unknown&quot;),val_to_str(Cause,s1ap_Cause_vals, &quot;unknown&quot;));</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '14, 06:38</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-32547" class="comments-container"><span id="32581"></span><div id="comment-32581" class="comment"><div id="post-32581-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal,</p><p>Thanks for the resolving the issue.</p><p>Now I face one more: I want to display the cause(in detail) for the failure of an event and also the possible way to resolve it. I want to store these info in a string corresponding to each and every S1AP failures separately.</p><p>For this I need to do one more thing of identifying the failure apart from unsucessfulOutcomes which are like "Attach Reject" so for this type of failure in the cause section of the previously stated code I would like to display the "EMM Cause" for this which is "IMSI unknown in HSS".</p><p>So, can you assist me the way in which I can do it.</p><p>Regards, Ankur</p></div><div id="comment-32581-info" class="comment-info"><span class="comment-age">(07 May '14, 02:54)</span> <span class="comment-user userinfo">ankur92</span></div></div><span id="32612"></span><div id="comment-32612" class="comment"><div id="post-32612-score" class="comment-score"></div><div class="comment-text"><p>For the EMM Cause, something like this (untested) ? Can't just paste the patch, so here is a description:</p><p>in de_emm_cause(), get the cause byte using tvb_get_guint8(tvb, curr_offset). Then do col_append_fstr(pinfo-&gt;cinfo, COL_INFO, " (%s)", val_to_str_ext_const(cause, &amp;nas_eps_emm_cause_values_ext, "Unknown"));</p></div><div id="comment-32612-info" class="comment-info"><span class="comment-age">(07 May '14, 10:55)</span> <span class="comment-user userinfo">MartinM</span></div></div><span id="32745"></span><div id="comment-32745" class="comment"><div id="post-32745-score" class="comment-score"></div><div class="comment-text"><p><span>@MartinM</span>: Thanks for the help, it worked. But I want this info beside S1 Application Protocol tree like the one which I am getting using the below function in packet-s1ap.c</p><p>Also, is there any way to access the EMM cause parameter in the packet-s1ap.c file</p><p>proto_item_append_text(s1ap_item, ", Event-Message:%s ,Result:%s, Cause:%s ",val_to_str_ext(ProcedureCode, &amp;s1ap_ProcedureCode_vals_ext, "unknown message"),val_to_str(S1AP_PDU,s1ap_S1AP_PDU_vals, "unknown"),val_to_str(Cause,s1ap_Cause_vals, "unknown"));</p></div><div id="comment-32745-info" class="comment-info"><span class="comment-age">(12 May '14, 23:21)</span> <span class="comment-user userinfo">ankur92</span></div></div></div><div id="comment-tools-32547" class="comment-tools"></div><div class="clear"></div><div id="comment-32547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

