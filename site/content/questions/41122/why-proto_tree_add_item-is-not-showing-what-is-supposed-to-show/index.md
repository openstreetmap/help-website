+++
type = "question"
title = "why proto_tree_add_item() is not showing what is supposed to show?"
description = '''hiii, /*packet-xxxxx.c*/  # include &quot;config.h&quot;  #include &amp;lt;epan/packet.h&amp;gt; #include &quot;packet-xxxxx.h&quot;  void proto_reg_handoff_xxxxx(void); void proto_register_xxxxx(void);  static int proto_xxxxx = -1; static int hf_data=-1; static gint ett_xxxxx = -1; static gint ett_data = -1; static int xxxxx_...'''
date = "2015-04-02T01:42:00Z"
lastmod = "2015-04-10T06:13:00Z"
weight = 41122
keywords = [ "proto_tree_add_item", "dissector" ]
aliases = [ "/questions/41122" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why proto\_tree\_add\_item() is not showing what is supposed to show?](/questions/41122/why-proto_tree_add_item-is-not-showing-what-is-supposed-to-show)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41122-score" class="post-score" title="current number of votes">0</div><span id="post-41122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hiii,</p><pre><code>/*packet-xxxxx.c*/

# include &quot;config.h&quot;

#include &lt;epan/packet.h&gt;
#include &quot;packet-xxxxx.h&quot;

void proto_reg_handoff_xxxxx(void);
void proto_register_xxxxx(void);

static int proto_xxxxx = -1;
static int hf_data=-1;
static gint ett_xxxxx = -1;
static gint ett_data = -1;
static int xxxxx_rtp_payload_type = 96;
static void
dissect_xxxxx(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    proto_item *ti;
    proto_tree *xxxxx_tree;

    guint8 packet_type = tvb_get_guint8(tvb, 0);
    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;xxxxx&quot;);
    col_set_str(pinfo-&gt;cinfo, COL_INFO, &quot;xxxxx message&quot;);

    if (tree) 
    {
        guint32 offset = 0; 
        ti = proto_tree_add_item(tree, proto_xxxxx, tvb, 0, -1, FALSE);
        xxxxx_tree = proto_item_add_subtree(ti, ett_xxxxx);
        proto_tree_add_item(xxxxx_tree, &amp;hf_data,tvb,offset,1, ENC_BIG_ENDIAN);
        offset += 1;
    }
}

void
proto_register_xxxxx(void)
{
    static hf_register_info hf[] = {
        { &amp;hf_data,
        { &quot;data&quot;, &quot;xxxxx.data&quot;, FT_UINT8, BASE_DEC, NULL, 0x0,
        NULL, HFILL }}
    };

    static gint *ett[] = {
        &amp;ett_xxxxx,
        &amp;ett_data
    };

    proto_xxxxx = proto_register_protocol (
        &quot;xxxxxProtocol&quot;, /* name       */
        &quot;xxxxx&quot;,      /* short name */
        &quot;xxxxx&quot;       /* abbrev     */
    );

    proto_register_field_array(proto_xxxxx, hf, array_length(hf));
    proto_register_subtree_array(ett, array_length(ett));
}

void proto_reg_handoff_xxxxx(void)
{
    static gboolean inited = FALSE;
    dissector_handle_t xxxxx_handle;

    if (!inited) {
        xxxxx_handle = new_create_dissector_handle(dissect_xxxxx, proto_xxxxx);
        inited = TRUE;
    }
    else {
        dissector_delete_uint(&quot;rtp.pt&quot;,xxxxx_rtp_payload_type , xxxxx_handle);
    }
    dissector_add_uint(&quot;rtp.pt&quot;,xxxxx_rtp_payload_type , xxxxx_handle);

    inited = TRUE;
}</code></pre><p>i wrote my own dissector code in epan/dissector.i want to decode the rtp payload stream for payload type 96.i was not able to get the field "data" field after the ssrc in rtp packet(Synchronization Source identifier: 0x73ed0101 (1944912129)).I wrote the code by checking in reference with h.264 protocol. If i am not wrong,when i give my xxxxx procol name in filter it is turning into green,which means my dissector is registered right?</p><p>when i click on the rtp packet and give decode as option ,i was not able to see my xxxxx protocol over rtp. Is my dissector_add_unit function correct?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-proto_tree_add_item" rel="tag" title="see questions tagged &#39;proto_tree_add_item&#39;">proto_tree_add_item</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '15, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/4175e12d54c0b11b1d8a5fb592555a63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lucky15&#39;s gravatar image" /><p><span>lucky15</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lucky15 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Apr '15, 05:16</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-41122" class="comments-container"><span id="41126"></span><div id="comment-41126" class="comment"><div id="post-41126-score" class="comment-score">2</div><div class="comment-text"><p>I fixed the formatting of your code, did this code actually compile? I ask as there seems to be an extra "}" in dissect_xxxxx(), maybe there's a missing "{" after the if?</p></div><div id="comment-41126-info" class="comment-info"><span class="comment-age">(02 Apr '15, 02:30)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="41131"></span><div id="comment-41131" class="comment"><div id="post-41131-score" class="comment-score"></div><div class="comment-text"><p>Thanks,</p><pre><code>void proto_reg_handoff_xxxxx(void)
{
    static gboolean inited = FALSE;
    dissector_handle_t xxxxx_handle;
    if (!inited) {
        xxxxx_handle = new_create_dissector_handle(dissect_xxxxx, proto_xxxxx);
        inited = TRUE;
    }</code></pre><p>That was a typo mistake,i had the '}' in my code.No compilation error was there.</p></div><div id="comment-41131-info" class="comment-info"><span class="comment-age">(02 Apr '15, 02:48)</span> <span class="comment-user userinfo">lucky15</span></div></div><span id="41132"></span><div id="comment-41132" class="comment"><div id="post-41132-score" class="comment-score"></div><div class="comment-text"><p>Is my dissector_add_unit function correct?</p></div><div id="comment-41132-info" class="comment-info"><span class="comment-age">(02 Apr '15, 03:02)</span> <span class="comment-user userinfo">lucky15</span></div></div><span id="41133"></span><div id="comment-41133" class="comment"><div id="post-41133-score" class="comment-score"></div><div class="comment-text"><p>should i use prefs_register_xxx_preference function for this in proto_register_xxxxx(void) function?</p></div><div id="comment-41133-info" class="comment-info"><span class="comment-age">(02 Apr '15, 03:07)</span> <span class="comment-user userinfo">lucky15</span></div></div><span id="41137"></span><div id="comment-41137" class="comment"><div id="post-41137-score" class="comment-score"></div><div class="comment-text"><p>The code error I was referring to was around the <code>if(tree)</code> in <code>dissect_xxxxx()</code>, your comment shows code in <code>proto_reg_handoff_xxxxx()</code>.</p><p>You can edit your question to fix the code to prevent confusion.</p><p>The <code>dissector_add_uint()</code> call looks OK.</p><p>Have you tried hooking up a debugger? Much easier then debugging via ascii.</p></div><div id="comment-41137-info" class="comment-info"><span class="comment-age">(02 Apr '15, 03:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="41140"></span><div id="comment-41140" class="comment not_top_scorer"><div id="post-41140-score" class="comment-score"></div><div class="comment-text"><p>i debugged using visual studio.i kept break points at:</p><p>guint8 packet_type = tvb_get_guint8(tvb, 0);</p><p>dissector_add_uint("rtp.pt",xxxxx_rtp_payload_type , xxxxx_handle);</p><p>i was able to get break point at dissector_add_uint.</p><p>but not in dissect_xxxxx function.</p><p>why is it ?</p><p>can u please explian? I am new to this wireshark code.</p><p>your comments are helpful.thank u..</p><p>Is there any other information or value i have to check while dubugging?</p></div><div id="comment-41140-info" class="comment-info"><span class="comment-age">(02 Apr '15, 04:34)</span> <span class="comment-user userinfo">lucky15</span></div></div><span id="41141"></span><div id="comment-41141" class="comment not_top_scorer"><div id="post-41141-score" class="comment-score"></div><div class="comment-text"><p>while i tried the same code on udp.port,i was able to give get the decode as option ,and when clicked on xxxxx protocol i got the following error on wireshark dispaly:</p><p>+User Datagram Protocol, Src Port: 46163 (46163), Dst Port: cap (1026)</p><pre><code>    xxxxxProtocol

+  Expert Info (Error/Malformed): proto.c:1991: failed assertion &quot;(guint)hfindex &lt; gpa_hfinfo.len&quot; (Unregistered hf!)

when i tried to debug it was going into dissect_xxxxx function 
But it did not debug the if (tree)condition block.</code></pre></div><div id="comment-41141-info" class="comment-info"><span class="comment-age">(02 Apr '15, 05:23)</span> <span class="comment-user userinfo">lucky15</span></div></div><span id="41142"></span><div id="comment-41142" class="comment not_top_scorer"><div id="post-41142-score" class="comment-score"></div><div class="comment-text"><p>You are registering your dissector as a sub-dissector for rtp, with a payload type of 96. This is the same as the 2dparityfec dissector, and maybe some other rtp sub-dissectors.</p><p>Check your registration using the menu item Internals -&gt; Dissector tables -&gt; Integer tables -&gt; RTP payload type.</p></div><div id="comment-41142-info" class="comment-info"><span class="comment-age">(02 Apr '15, 05:25)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="41144"></span><div id="comment-41144" class="comment not_top_scorer"><div id="post-41144-score" class="comment-score"></div><div class="comment-text"><p>thanks,</p><p>And i checked that RTP Payload Type : it is showing some junk value for my protocol.why is it?</p></div><div id="comment-41144-info" class="comment-info"><span class="comment-age">(02 Apr '15, 05:36)</span> <span class="comment-user userinfo">lucky15</span></div></div><span id="41147"></span><div id="comment-41147" class="comment not_top_scorer"><div id="post-41147-score" class="comment-score"></div><div class="comment-text"><p>What does the table show?</p></div><div id="comment-41147-info" class="comment-info"><span class="comment-age">(02 Apr '15, 06:21)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="41150"></span><div id="comment-41150" class="comment not_top_scorer"><div id="post-41150-score" class="comment-score"></div><div class="comment-text"><p>RTP payload Type:</p><p>-898487959 xxxxx</p><p>display is coming.</p></div><div id="comment-41150-info" class="comment-info"><span class="comment-age">(02 Apr '15, 08:04)</span> <span class="comment-user userinfo">lucky15</span></div></div><span id="41171"></span><div id="comment-41171" class="comment not_top_scorer"><div id="post-41171-score" class="comment-score"></div><div class="comment-text"><p>hi,</p><p>Already for 96 some other sub dissector is present in the integer table.Is it contradicting because of this?</p></div><div id="comment-41171-info" class="comment-info"><span class="comment-age">(02 Apr '15, 21:53)</span> <span class="comment-user userinfo">lucky15</span></div></div><span id="41239"></span><div id="comment-41239" class="comment not_top_scorer"><div id="post-41239-score" class="comment-score"></div><div class="comment-text"><ol><li>There is a line: "proto_tree_add_item(xxxxx_tree, &amp;hf_data,tvb,offset,1, ENC_BIG_ENDIAN);"</li></ol><p>&amp;hf_data -&gt; hf_data There is no warning about put void* as int?</p><ol><li>"ti = proto_tree_add_item(tree, proto_xxxxx, tvb, 0, -1, FALSE);" FALSE -&gt; ENC_NA</li></ol></div><div id="comment-41239-info" class="comment-info"><span class="comment-age">(06 Apr '15, 22:51)</span> <span class="comment-user userinfo">Michał Łabędzki</span></div></div><span id="41310"></span><div id="comment-41310" class="comment not_top_scorer"><div id="post-41310-score" class="comment-score"></div><div class="comment-text"><p>umm in my current wireshark 1.12.4 there is no dissector for 96 payload in the rtp.payload dissector table!</p></div><div id="comment-41310-info" class="comment-info"><span class="comment-age">(08 Apr '15, 23:04)</span> <span class="comment-user userinfo">koundi</span></div></div><span id="41349"></span><div id="comment-41349" class="comment not_top_scorer"><div id="post-41349-score" class="comment-score"></div><div class="comment-text"><p>I believe that dissector tables can only hold one entry for the key. In that case, the last dissector to call dissector_add_uint() for a particular integer will be the one that is called as the sub-dissector that that table entry.</p><p>I don't understand why you have such an odd value in the table. Can you check that again?</p></div><div id="comment-41349-info" class="comment-info"><span class="comment-age">(10 Apr '15, 06:13)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-41122" class="comment-tools"><span class="comments-showing"> showing 5 of 15 </span> <a href="#" class="show-all-comments-link">show 10 more comments</a></div><div class="clear"></div><div id="comment-41122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

