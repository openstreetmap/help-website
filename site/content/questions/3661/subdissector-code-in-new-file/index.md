+++
type = "question"
title = "SubDissector code in new file"
description = '''I am writing a subdissector for an existing protocol. The existing protocol has a bacapp_dissector_table. In a new file, i am writing a subdissector with following functions void proto_register_bacnetsbt(void) {  static hf_register_info hf[] = {  { &amp;amp;hf_bacnet_private_transfer,  { &quot;Private Transf...'''
date = "2011-04-20T13:53:00Z"
lastmod = "2011-08-31T11:27:00Z"
weight = 3661
keywords = [ "node", "tree", "null", "subdissector" ]
aliases = [ "/questions/3661" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [SubDissector code in new file](/questions/3661/subdissector-code-in-new-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3661-score" class="post-score" title="current number of votes">0</div><span id="post-3661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a subdissector for an existing protocol. The existing protocol has a bacapp_dissector_table. In a new file, i am writing a subdissector with following functions void proto_register_bacnetsbt(void) { static hf_register_info hf[] = { { &amp;hf_bacnet_private_transfer, { "Private Transfer", "bacnet.private.transfer", FT_FRAMENUM, BASE_NONE, NULL, 0x00, NULL, HFILL} } }; static gint *ett[] = { &amp;ett_bacnet_sbt, };</p><pre><code>/* Register */</code></pre><p>proto_BACnet_PT_mr = proto_register_protocol("ABC","BACNET-SBT", "bacnetsbt"); register_dissector("ABC", dissect_BACnet_SBT_UCPT_mr, proto_BACnet_PT_mr);<br />
} void proto_reg_handoff_bacnetsbt(void) { data_handle = find_dissector("data");</p><pre><code>proto_BACnet_PT_handle = new_create_dissector_handle(dissect_BACnet_SBT_UCPT_mr, proto_BACnet_PT_mr);
dissector_add_uint(&quot;bacapp.vendor_identifier&quot;, SBT_VENDOR_ID, proto_BACnet_PT_handle);</code></pre><p>}<br />
static int dissect_BACnet_SBT_UCPT_mr(tvbuff_t <em>tvb, packet_info</em> pinfo, proto_tree *tree) { // My code } I have declared all required variables used in these functions. My dissect_BACnet_SBT_UCPT_mr function gets called correctly from BACnet disssector using bacapp.vendor_identifier. but when this function is called, the tree is null. When i debug, the tree is null even in bacapp function from which my subdissector function is called(existing dissector file for standard protocol - not my subdissector)</p><p>If this function in same file as existing bacapp dissector, tree node is not null. Am I missing any registration when i move code to new file?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-tree" rel="tag" title="see questions tagged &#39;tree&#39;">tree</span> <span class="post-tag tag-link-null" rel="tag" title="see questions tagged &#39;null&#39;">null</span> <span class="post-tag tag-link-subdissector" rel="tag" title="see questions tagged &#39;subdissector&#39;">subdissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '11, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/c33cba1d3fea69f74f6c8c0425c16c75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsprabhu4&#39;s gravatar image" /><p><span>dsprabhu4</span><br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsprabhu4 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-3661" class="comments-container"><span id="3679"></span><div id="comment-3679" class="comment"><div id="post-3679-score" class="comment-score"></div><div class="comment-text"><p>Is the tree <code>NULL</code> during every invocation of your dissector, or is it only sometimes <code>NULL</code>? Specifically, is the tree variable <code>NULL</code> when the bacapp dissector has already added details to the protocol tree?</p></div><div id="comment-3679-info" class="comment-info"><span class="comment-age">(21 Apr '11, 07:26)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="3683"></span><div id="comment-3683" class="comment"><div id="post-3683-score" class="comment-score"></div><div class="comment-text"><p>In my code, bacapp functions are called first. then function of my code - new subdissector is called. The tree is null every time. It is null also in bacapp functions. I found out this while debugging. This happens only when i move code to a separate file. if i keep code in same bacapp file, then tree is not null. Do we need to call any specific function when i move code to new file?</p></div><div id="comment-3683-info" class="comment-info"><span class="comment-age">(21 Apr '11, 08:24)</span> <span class="comment-user userinfo">dsprabhu4</span></div></div><span id="3692"></span><div id="comment-3692" class="comment"><div id="post-3692-score" class="comment-score"></div><div class="comment-text"><p>Figured out a way to handle this. Thanks everyone.</p></div><div id="comment-3692-info" class="comment-info"><span class="comment-age">(22 Apr '11, 10:25)</span> <span class="comment-user userinfo">dsprabhu4</span></div></div><span id="3695"></span><div id="comment-3695" class="comment"><div id="post-3695-score" class="comment-score"></div><div class="comment-text"><p>@dsprabhu4: Would you mind posting your solution as an answer in case other developers have this problem in the future?</p></div><div id="comment-3695-info" class="comment-info"><span class="comment-age">(22 Apr '11, 11:51)</span> <span class="comment-user userinfo">multipleinte...</span></div></div></div><div id="comment-tools-3661" class="comment-tools"></div><div class="clear"></div><div id="comment-3661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="3709"></span>

<div id="answer-container-3709" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3709-score" class="post-score" title="current number of votes">0</div><span id="post-3709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I am exactly not sure of the steps for adding a sub-dissector. but i analyzed packet-snmp.c and followed these steps. It worked for me :)</p><p>The protocol which I wanted to enhance supports proprietary services. In existing protocol code file, there</p><p>is a table with vendor ids. I wanted to call a function to analyze the proprietary services.</p><p>I wanted to add a dissector function in new file and add that function in this existing dissector table.</p><p>I created a new file packet-xxx.c</p><p>Add this new file packet-xxx.c epandissectors. Add reference of this c file in epanCMakeLists.txt Add reference of this c file in epandissectorsMakefile.common</p><p>I added two functions and my code in this new packet-xxx.c file.</p><p>• proto_register_xxx – This function creates a sub-dissector for a vendor identifier.</p><p>proto_xxx_PT_mr = proto_register_protocol("XXXProto","XXX", "xxx"); new_register_dissector("XXXPT",dissect_XXX_mr, proto_XXX_PT_mr);<br />
</p><p>The first statement will register sub-dissector. The sub-dissector will be referred by exiting protocol which</p><p>i am enhancing for proprietary information.</p><p>Second code statement creates the sub-dissector. Here dissect_XXX_mr function will be called when this</p><p>sub-dissector will be invoked.</p><p>• proto_reg_handoff_xxx – This function adds the dissector created in above function to the dissector</p><p>table.</p><p>proto_XXX_PT_handle = find_dissector("XXXProto"); dissector_add_uint("table_identifier", XXX_VENDOR_ID, proto_XXX_PT_handle);</p><p>Note : "table_identifier" - this string should match with string used for creating dissector table in</p><p>existing code.</p><p>First code statement finds the dissector handle.</p><p>The second code statement is used to add dissector function handle in dissector_table. This is done using</p><p>table name – “table_identifier";</p><p>XXX_VENDOR_ID should have value which will be present in PrivateTransfer message as vendor id. This should</p><p>exactly match.It can be defined using #define.</p><p>• My proprietary code is in dissect_XXX_mr function.</p><p>I hope that above steps are not confusing because of xxx. I have removed specifics to my customer code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '11, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/c33cba1d3fea69f74f6c8c0425c16c75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsprabhu4&#39;s gravatar image" /><p><span>dsprabhu4</span><br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsprabhu4 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-3709" class="comments-container"></div><div id="comment-tools-3709" class="comment-tools"></div><div class="clear"></div><div id="comment-3709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3710"></span>

<div id="answer-container-3710" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3710-score" class="post-score" title="current number of votes">0</div><span id="post-3710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With this, i am not longer getting buffer null. I do not know what changed that has solved problem of NULL buffer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '11, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/c33cba1d3fea69f74f6c8c0425c16c75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsprabhu4&#39;s gravatar image" /><p><span>dsprabhu4</span><br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsprabhu4 has no accepted answers">0%</span></p></div></div><div id="comments-container-3710" class="comments-container"></div><div id="comment-tools-3710" class="comment-tools"></div><div class="clear"></div><div id="comment-3710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6020"></span>

<div id="answer-container-6020" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6020-score" class="post-score" title="current number of votes">0</div><span id="post-6020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Lori added a method to develop plugins for BACnet PrivateTransfer services (vendor specific code) that doesn't require changes to the existing wirewhark BACnet Application Layer dissector (packet-bacapp.c). Simply create a plugin that implements your dissection rules for PrivateTransfer and register the VendorId with the bacapp dissector.</p><pre><code>my_handle = create_dissector_handle(dissect_mypt, proto_mypt);

/* dissector called from bacapp when a PT service matches our vendor code */
dissector_add(&quot;bacapp.vendor_identifier&quot;, MY_VENDOR, my_handle);</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '11, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/fc5d3d18b5d606c17e87772ec4c036b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skarg&#39;s gravatar image" /><p><span>skarg</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skarg has no accepted answers">0%</span></p></div></div><div id="comments-container-6020" class="comments-container"></div><div id="comment-tools-6020" class="comment-tools"></div><div class="clear"></div><div id="comment-6020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

