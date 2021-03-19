+++
type = "question"
title = "Dissection"
description = '''My dissector code is able to detect packets(i can see in protocol column)but its not able to dissect fields of query packet or response packet .Written code taking reference from &quot;foo&quot;. static void dissect_mc(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree) {  char st[]=   gint offset = 0;  int ...'''
date = "2013-05-16T02:26:00Z"
lastmod = "2013-06-04T01:26:00Z"
weight = 21175
keywords = [ "dissector" ]
aliases = [ "/questions/21175" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dissection](/questions/21175/dissection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21175-score" class="post-score" title="current number of votes">0</div><span id="post-21175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My dissector code is able to detect packets(i can see in protocol column)but its not able to dissect fields of query packet or response packet .Written code taking reference from "foo".</p><pre><code>static void dissect_mc(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    char st[]= 
    gint offset = 0;
    int packettype;
    packettype=classify_mc_packet(pinfo);
    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;MC&quot;);
    /* Clear out stuff in the info column */
    col_clear(pinfo-&gt;cinfo,COL_INFO);
    if (packettype==QUERY_PACKET)
    {
     if (tree) 
     {/* we are being asked for details */
        proto_item *ti = NULL;
        proto_tree *mc_tree = NULL;
        ti = proto_tree_add_item(tree, proto_mc, tvb, 0, -1, ENC_NA);
        mc_tree = proto_item_add_subtree(ti, ett_mc);
        proto_tree_add_item(mc_tree, hf_mc_subheader, tvb, offset, 1, ENC_LITTLE_ENDIAN);
        offset += 1;
        proto_tree_add_item(mc_tree, hf_mc_pcnumber, tvb, offset, 1, ENC_LITTLE_ENDIAN);
        offset += 1;
        proto_tree_add_item(mc_tree, hf_mc_monitortimer, tvb, offset, 2, ENC_LITTLE_ENDIAN);
        offset += 2;
        proto_tree_add_item(mc_tree, hf_mc_headdevnumber, tvb, offset, 4, ENC_LITTLE_ENDIAN);
        offset += 4;
        proto_tree_add_item(mc_tree, hf_mc_devicename, tvb, offset, 2, ENC_LITTLE_ENDIAN);
        offset += 2;
        proto_tree_add_item(mc_tree, hf_mc_devicepoints, tvb, offset, 1, ENC_LITTLE_ENDIAN);
        offset += 1;
        proto_tree_add_item(mc_tree, hf_mc_terminator, tvb, offset, 1, ENC_LITTLE_ENDIAN);
        offset += 1;

        }
    }
    else if (packettype==RESPONSE_PACKET)

    {
        if(tree)
        {
        proto_item *ti = NULL;
        proto_tree *mc_tree = NULL;
        ti = proto_tree_add_item(tree, proto_mc, tvb, 0, -1, ENC_NA);
        mc_tree = proto_item_add_subtree(ti, ett_mc);
        proto_tree_add_item(mc_tree, hf_mc_subheader, tvb, offset, 1, ENC_LITTLE_ENDIAN);
        offset += 1;
        proto_tree_add_item(mc_tree, hf_mc_subheader, tvb, offset, 1, ENC_LITTLE_ENDIAN);
        offset += 2;
        }
    else return;
    }</code></pre><p>other functions seem to be right..what is the mistake in this function?Thanx..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '13, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/f48b4f4f35dc1e8a66425e223c958173?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chin12&#39;s gravatar image" /><p><span>chin12</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chin12 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 May '13, 02:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-21175" class="comments-container"></div><div id="comment-tools-21175" class="comment-tools"></div><div class="clear"></div><div id="comment-21175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21178"></span>

<div id="answer-container-21178" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21178-score" class="post-score" title="current number of votes">2</div><span id="post-21178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure your <code>classify_mc_packet()</code> routine is returning a suitable value into packettype? If it doesn't return <code>QUERY_PACKET</code> or <code>RESPONSE_PACKET</code> then nothing will be added to the tree.</p><p>Either run Wireshark under a debugger to inspect the value or add a "default" else branch to the code to indicate an unknown packet type.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '13, 03:39</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-21178" class="comments-container"><span id="21284"></span><div id="comment-21284" class="comment"><div id="post-21284-score" class="comment-score"></div><div class="comment-text"><p>I debugged the code and found control not entering classify_mc_packet(),dissect_mc() though it enters proto_register_mc and proto_reg_handoff_mc mc.The fn is defined as :</p><pre><code>static int
classify_mc_packet(packet_info *pinfo)
{
    if (hf_mc_subheader==00 ||hf_mc_subheader==01||hf_mc_subheader==02||hf_mc_subheader==03||hf_mc_subheader==04)
        return QUERY_PACKET;
    if (hf_mc_subheader==80 ||hf_mc_subheader==81||hf_mc_subheader==82||hf_mc_subheader==83||hf_mc_subheader==84)
        return RESPONSE_PACKET;
    return CANNOT_CLASSIFY;
}</code></pre><p>Has anything gone corrupt? I have written it on lines of foo dissector?plz look at the code and help me figure out where's the fault?plz reply soon..</p></div><div id="comment-21284-info" class="comment-info"><span class="comment-age">(19 May '13, 23:14)</span> <span class="comment-user userinfo">chin12</span></div></div><span id="21285"></span><div id="comment-21285" class="comment"><div id="post-21285-score" class="comment-score">1</div><div class="comment-text"><p>According to the sample code you provided, the classify_mc_packet should be instead:</p><pre><code>static int
classify_mc_packet(tvbuff_t *tvb)
{
    guint8 subheader = tvb_get_guint8(tvb, 0);
    if (subheader ==00 ||subheader ==01||subheader ==02||subheader ==03||subheader ==04)
        return QUERY_PACKET;
    if (subheader ==80 ||subheader ==81||subheader ==82||subheader ==83||subheader ==84)
        return RESPONSE_PACKET;
    return CANNOT_CLASSIFY;
}</code></pre></div><div id="comment-21285-info" class="comment-info"><span class="comment-age">(19 May '13, 23:57)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="21286"></span><div id="comment-21286" class="comment"><div id="post-21286-score" class="comment-score"></div><div class="comment-text"><p>doesn't make any difference..control is not going inside the bracket..btw..why tvbuff_t <em>tvb and why not packet_info</em> pinfo(as in "foo"protocol)?</p></div><div id="comment-21286-info" class="comment-info"><span class="comment-age">(20 May '13, 01:35)</span> <span class="comment-user userinfo">chin12</span></div></div><span id="21287"></span><div id="comment-21287" class="comment"><div id="post-21287-score" class="comment-score"></div><div class="comment-text"><p>Anybody can think of any other reason?The above code had worked once but i modified lateron w/o backup.plzz help soon</p></div><div id="comment-21287-info" class="comment-info"><span class="comment-age">(20 May '13, 02:04)</span> <span class="comment-user userinfo">chin12</span></div></div><span id="21288"></span><div id="comment-21288" class="comment"><div id="post-21288-score" class="comment-score"></div><div class="comment-text"><p>Packet_info contains some information on the context of the current packet, while tvb contains the packet itself (that can be accessed via all the tvb_* functions).</p><p>In your code you were passing the pinfo pointer to classify_mc_packet without even using it. What was the purpose of this?</p><p>It looks like you want to check the subheader value that is in the first byte of the payload. That's why you need the tvb_get_guint8(tvb, 0) call (to retrieve the byte at offset 0). I do not see how classify_mc_packet would not be called <em>IF</em> dissect_mc is being called. As you stated that you can see your "MC" string in the protocol column, it means that dissect_mc is called. If dissect_mc is not called, it means that you did not register your dissector correctly and did not indicate Wireshark when to call it (based on a port number for example,... ).</p><p>I highly recommend you to have a read of doc/README.developer document to understand the difference between tvb and packet_info and how to register your dissector.</p></div><div id="comment-21288-info" class="comment-info"><span class="comment-age">(20 May '13, 02:05)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="21289"></span><div id="comment-21289" class="comment not_top_scorer"><div id="post-21289-score" class="comment-score"></div><div class="comment-text"><p>Agreed and made changes but in vain..here's reqd routines: Debugging shows no control flow inside dissect and classify routine."MC" might be displayed in protocol column due to some plugins added with the source code in the beginning.</p><p>void proto_reg_handoff_mc(void) {</p><pre><code>static dissector_handle_t mc_handle;
mc_handle = create_dissector_handle(dissect_mc, proto_mc);
dissector_add_uint(&quot;tcp.port&quot;, MC_PORT, mc_handle);</code></pre><p>} and void proto_register_mc(void) {</p><pre><code>static hf_register_info hf[] = {
    { &amp;hf_mc_subheader,
        { &quot;MC Subheader&quot;, &quot;mc.subheader&quot;,
        FT_UINT8, BASE_DEC,
        NULL, 0x0,
        NULL, HFILL }
    },
    { &amp;hf_mc_pcnumber,
        { &quot;MC PC Number&quot;, &quot;mc.pcn&quot;,
        FT_UINT8, BASE_DEC,
        NULL, 0x0,
        NULL, HFILL }

       :
       :
    { &amp;hf_mc_terminator,
        { &quot;MC  Terminator&quot;, &quot;mc.terminator&quot;,
        FT_UINT8, BASE_DEC,
        NULL, 0x0,
        NULL, HFILL }

    },</code></pre><p>};</p><pre><code>/* Setup protocol subtree array */
static gint *ett[] = {
    &amp;ett_mc
};

proto_mc = proto_register_protocol (
    &quot;MCprotocol&quot;,/* name       */
    &quot;mc&quot; ,   /* short name */
    &quot;mc&quot;       /* abbrev     */
    );
proto_register_field_array(proto_mc,hf, array_length(hf));
proto_register_subtree_array(ett, array_length(ett));</code></pre><p>}</p></div><div id="comment-21289-info" class="comment-info"><span class="comment-age">(20 May '13, 02:47)</span> <span class="comment-user userinfo">chin12</span></div></div><span id="21295"></span><div id="comment-21295" class="comment not_top_scorer"><div id="post-21295-score" class="comment-score"></div><div class="comment-text"><p>someone please help..</p></div><div id="comment-21295-info" class="comment-info"><span class="comment-age">(20 May '13, 03:47)</span> <span class="comment-user userinfo">chin12</span></div></div><span id="21298"></span><div id="comment-21298" class="comment not_top_scorer"><div id="post-21298-score" class="comment-score"></div><div class="comment-text"><p>To help you further please post a) your complete dissector code and b) a sample capture containing your protocol somewhere where others can access them.</p><p>Please also bear in mind that any that do help are effectively debugging your code for free.</p></div><div id="comment-21298-info" class="comment-info"><span class="comment-age">(20 May '13, 04:06)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="21393"></span><div id="comment-21393" class="comment not_top_scorer"><div id="post-21393-score" class="comment-score"></div><div class="comment-text"><p>pascal,you were right..its working..thanks a lot.. Graham,i am really grateful and indebted to people replying here.. Now,i need a litle help.. i am seeing query packet dissections properly but there is no reply packet getting dissected.Morever,the capture does not list any reply packet too..plz check the code above..thanks</p></div><div id="comment-21393-info" class="comment-info"><span class="comment-age">(23 May '13, 01:23)</span> <span class="comment-user userinfo">chin12</span></div></div><span id="21728"></span><div id="comment-21728" class="comment not_top_scorer"><div id="post-21728-score" class="comment-score"></div><div class="comment-text"><p>A/c above code, for devicename field (2 bytes) i am getting ascii value(numerical)value as devicename :3268(space and D) IF i modify that as proto_tree_add_item(mc_tree, hf_mc_devicename, tvb, offset, 1, ENC_LITTLE_ENDIAN); offset += 1; proto_tree_add_item(mc_tree, hf_mc_devicename, tvb, offset, 1, ENC_LITTLE_ENDIAN); offset += 1; i get devicename :32 devicename :68</p><p>but I want to display as devicename : D FOLLOWED BY SPACE ,i mean how to use FT_STRING feature here ..and in FUNCTION proto_reg_mc,i have { &amp;hf_mc_devicename, { "MC Devicename", "mc.devicename", FT_UINT16, BASE_DEC, NULL, 0x0, NULL, HFILL } Do i have to modify/write my proto_tree_add_item function(proto.c)?REgisters i am dealing with has single character and 2 character address format .PLeas reply soon..thanx</p></div><div id="comment-21728-info" class="comment-info"><span class="comment-age">(03 Jun '13, 23:09)</span> <span class="comment-user userinfo">chin12</span></div></div><span id="21732"></span><div id="comment-21732" class="comment not_top_scorer"><div id="post-21732-score" class="comment-score"></div><div class="comment-text"><p>Simply replace { &amp;hf_mc_devicename, { "MC Devicename", "mc.devicename", FT_UINT16, BASE_DEC, NULL, 0x0, NULL, HFILL } by { &amp;hf_mc_devicename, { "MC Devicename", "mc.devicename", FT_STRING, BASE_NONE, NULL, 0x0, NULL, HFILL } and do proto_tree_add_item(mc_tree, hf_mc_devicename, tvb, offset, 2, ENC_ASCII|ENC_NA);</p></div><div id="comment-21732-info" class="comment-info"><span class="comment-age">(04 Jun '13, 01:26)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-21178" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-21178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

