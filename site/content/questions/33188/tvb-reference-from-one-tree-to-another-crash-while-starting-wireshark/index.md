+++
type = "question"
title = "TVB  reference from one tree to another CRASH while starting Wireshark"
description = '''Hi iam trying to build custom protocol and i need to have 2 trees.  [-] Tree1  [-] subtree1   [-] subtree2 [-] Tree 2 (This tree&#x27;s data is from tree1 &#x27;s Subtree 2 )  [-] subtree1 i have used tvb reference and my code not working and facing runtime crash (i can Build, i have tried distclean and compl...'''
date = "2014-05-30T00:16:00Z"
lastmod = "2014-05-30T21:53:00Z"
weight = 33188
keywords = [ "passing", "dissector", "tree", "tvb" ]
aliases = [ "/questions/33188" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TVB reference from one tree to another CRASH while starting Wireshark](/questions/33188/tvb-reference-from-one-tree-to-another-crash-while-starting-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33188-score" class="post-score" title="current number of votes">0</div><span id="post-33188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi iam trying to build custom protocol and i need to have 2 trees.</p><p>[-] Tree1 [-] subtree1 [-] subtree2</p><p>[-] Tree 2 (This tree's data is from tree1 's Subtree 2 ) [-] subtree1</p><p>i have used tvb reference and my code not working and facing runtime crash (i can Build, i have tried distclean and complete setup , distclean, all , still runtime crash ) can anyone help me whats wrong in my code. Advance Thanks!</p><pre><code> #define proto1_PORT XXX
 #define PROTO_TAG_proto1   &quot;proto2&quot;

 static int registration_request_msg =0;

 static int proto_proto1 = -1;
 static int proto_proto2 = -1;
 static dissector_handle_t data_handle;
 static dissector_handle_t proto1_handle;

 static dissector_handle_t proto2_handle;
 static gint hf_proto1 = -1;
 static gint hf_proto2 = -1;

 tvbuff_t *next_tvb;

 static gint ett_proto1 = -1;

 static gint ett_proto2 = -1;

 static gint *ett[] = {

 &amp;ett_proto1,
    ...
    ...
  };

  static gint *ett1[] = {

  &amp;ett_proto2,
    ...
    ...

 };

  void proto_register_proto1(void);
  void proto_reg_handoff_proto1(void);
  void proto_register_proto2(void);
  void proto_reg_handoff_proto2(void);
  void dissect_proto1(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree);
  void dissect_proto2(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree);

  void proto_reg_handoff_proto1(void)
  {
  static dissector_handle_t proto1_handle;
  proto1_handle = find_dissector(&quot;proto1&quot;);
  proto1_handle = create_dissector_handle (dissect_proto1, proto_proto1);
  // sub_dissector_handle (dissect_proto2, proto_proto2);
  dissector_add_uint (&quot;udp.port&quot;, proto1_PORT, proto1_handle);
  }

  void proto_reg_handoff_proto2(void)
  {
  static dissector_handle_t proto2_handle;
  proto2_handle = find_dissector(&quot;proto2&quot;);
  proto2_handle = create_dissector_handle (dissect_proto2, proto_proto2);

  }

   void proto_register_proto1 (void)
  {

   static hf_register_info hf[] = {
  { &amp;hf_proto1,
  { &quot;proto1 &quot;, &quot;proto1.data&quot;, FT_NONE, BASE_NONE, NULL, 0x0,&quot;proto1&quot;, HFILL }},
     ...
     ...
   };

  proto_proto1 = proto_register_protocol (&quot;proto1 &quot;, &quot;proto1&quot;, &quot;bplt&quot;);

  proto_register_field_array (proto_proto1, hf, array_length (hf));
  proto_register_subtree_array (ett, array_length (ett));
  register_dissector(&quot;proto1&quot;, dissect_proto1, proto_proto1);

  }

  static void dissect_proto1(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
  {

  proto_item *proto1_item = NULL;
  proto_item *proto1_sub_item = NULL;
  proto_tree *proto1_tree = NULL;
  proto_tree *proto1_sub_tree = NULL;
  proto_tree *proto1_header_tree = NULL;

   if (tree) { /* we are being asked for details */
   guint offset=0;
   proto_tree    *checksum_tree;
   proto_item    *checksum_ti; 
   guint16    checksum, checksum_calculated; 
   guint     checksum_offset=0;

   guint len=0;
   //guint available_length=0;
   guint length=0;
   guint reported_length=0;
   guint  available_length=0;
   guint length_new=0;

   col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, PROTO_TAG_proto1);
   col_clear(pinfo-&gt;cinfo,COL_INFO);

   proto1_item = proto_tree_add_item(tree, proto_proto1, tvb, 0, -1, FALSE);
   proto1_tree = proto_item_add_subtree(proto1_item, ett_proto1);
   proto1_header_tree = proto_item_add_subtree(proto1_item, ett_proto1);

   tvb_get_guint8( tvb, offset );      
   len = tvb_length(tvb) -offset ;
   len=len-2;

   proto_tree_add_item(proto1_sub_tree, hf_proto1_lesp_data, tvb, offset, len, ENC_LITTLE_ENDIAN);
   offset += len;
   length = tvb_length(tvb);
   reported_length = tvb_reported_length(tvb);

   next_tvb = tvb_new_subset(tvb, offset, len, -1);

   call_dissector(proto2_handle, next_tvb, pinfo, tree);

     }

     }

     void proto_register_proto2 (void)
    {

    static hf_register_info hf[] = {
    { &amp;hf_proto2,
    { &quot;proto2 (Rx 2) &quot;, &quot;proto2.proto1&quot;,FT_NONE, BASE_NONE, NULL, 0x0, NULL, HFILL }
    },
    { &amp;hf_SUBTREE,
    { &quot;SUBTREE) &quot;, &quot;subtree1&quot;,FT_UINT8, BASE_HEX_DEC , NULL, 0x0, NULL, HFILL}
    }

    };

     proto_proto2 = proto_register_protocol (&quot;proto2&quot;, &quot;proto2&quot;, &quot;proto_name&quot;);

     proto_register_field_array (proto_proto2, hf, array_length (hf));
     proto_register_subtree_array (ett1, array_length (ett1));

     }

     static void dissect_proto2(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
     {
     proto_item *proto2_item = NULL;
     proto_item *proto2_sub_item = NULL;
     proto_tree *proto2_tree = NULL;
     proto_tree *proto2_sub_tree = NULL;
     proto_tree *proto2_header_tree = NULL;

     if (tree) { /* we are being asked for details */

     proto2_item = proto_tree_add_item(tree, proto_proto2, tvb, 0, -1, FALSE);
     proto2_tree = proto_item_add_subtree(proto2_item, ett_proto2);
     proto2_header_tree = proto_item_add_subtree(proto2_item, ett_proto2);

     }

     }</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-passing" rel="tag" title="see questions tagged &#39;passing&#39;">passing</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tree" rel="tag" title="see questions tagged &#39;tree&#39;">tree</span> <span class="post-tag tag-link-tvb" rel="tag" title="see questions tagged &#39;tvb&#39;">tvb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '14, 00:16</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p><span>umar</span><br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Sep '14, 23:29</strong> </span></p></div></div><div id="comments-container-33188" class="comments-container"><span id="33191"></span><div id="comment-33191" class="comment"><div id="post-33191-score" class="comment-score"></div><div class="comment-text"><p>Where is the crash occurring? Have you attached a debugger to get a stack backtrace so you can determine where it is going wrong?</p><p>What OS are you using?</p></div><div id="comment-33191-info" class="comment-info"><span class="comment-age">(30 May '14, 02:49)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="33228"></span><div id="comment-33228" class="comment"><div id="post-33228-score" class="comment-score"></div><div class="comment-text"><p>Hi grahamb, Its working now. Iam using Winxp wireshark GTK 1.113.. Thanks for your time :)</p></div><div id="comment-33228-info" class="comment-info"><span class="comment-age">(30 May '14, 21:53)</span> <span class="comment-user userinfo">umar</span></div></div></div><div id="comment-tools-33188" class="comment-tools"></div><div class="clear"></div><div id="comment-33188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33197"></span>

<div id="answer-container-33197" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33197-score" class="post-score" title="current number of votes">1</div><span id="post-33197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="umar has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First this:</p><pre><code>if (tree) { /* we are being asked for details */</code></pre><p>It stops the dissector from setting the column info and it prevents the calling of subdissectors. It should only be applied to statements that work on trees and tree items, and even that doesn't help much because these calls first check the 'tree' parameter anyway.</p><p>Then this module variable:</p><pre><code> tvbuff_t *next_tvb;</code></pre><p>It must be put in the dissection function itself. It may not be shared like this, nor be persistent across frames.</p><pre><code>len = tvb_length(tvb) - offset;</code></pre><p>This is tvb_length_remaining(), but could fail if captured frames are cut short. Watch out for possible negative values!</p><pre><code>next_tvb = tvb_new_subset(tvb, offset, len, -1);</code></pre><p>At this point offset is already beyond len, at the end of the TVB, so you are passing what along?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '14, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-33197" class="comments-container"><span id="33227"></span><div id="comment-33227" class="comment"><div id="post-33227-score" class="comment-score"></div><div class="comment-text"><p>Hi jaap, i could able to solve the problem. I have Moved next_tvb to above the level of my subtree. Its works now. many thanks for your support :)</p></div><div id="comment-33227-info" class="comment-info"><span class="comment-age">(30 May '14, 21:52)</span> <span class="comment-user userinfo">umar</span></div></div></div><div id="comment-tools-33197" class="comment-tools"></div><div class="clear"></div><div id="comment-33197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

