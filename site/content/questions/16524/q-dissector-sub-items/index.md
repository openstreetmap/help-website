+++
type = "question"
title = "[Q] Dissector Sub Items"
description = '''Hi Forum, I am trying to write a dissector for a protocol. I cannot figure out how to display a sub tree PLUS box and sub fields.  I have created a simple example of what I have done.  My protocol has UINT16 message length followed FCOD (UNIT8). I want to use this FCODE as a subtree and have a PLUS ...'''
date = "2012-12-04T01:18:00Z"
lastmod = "2012-12-04T01:40:00Z"
weight = 16524
keywords = [ "dissector", "sub-dissector" ]
aliases = [ "/questions/16524" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [\[Q\] Dissector Sub Items](/questions/16524/q-dissector-sub-items)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16524-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Forum,</p><p>I am trying to write a dissector for a protocol. I cannot figure out how to display a sub tree PLUS box and sub fields.<br />
</p><p>I have created a simple example of what I have done.<br />
</p><p>My protocol has UINT16 message length followed FCOD (UNIT8). I want to use this FCODE as a subtree and have a PLUS box and sub fields, but I have been unable to get it to work.</p><p>I am expecting to see</p><pre><code>+FOO Protocol
    Message Length 1234
    +FCODE
        FLAGS</code></pre><p>Thanks</p><p>Stuart</p><pre><code>#ifdef HAVE_CONFIG_H
#include &quot;config.h&quot;
#endif

#include &lt;epan/packet.h&gt;
#define FOO_PORT 2000

static int hf_header_message_length = -1;
static int hf_header_fcode          = -1;

static int hf_fcode_flag            = -1;

static int ett_fooheader = -1;
static int ett_foosegment = -1;

static int proto_foo = -1;

// define protocol names, register structure
void proto_register_foo(void)
{
    static hf_register_info hf[] = {
        { &amp;hf_header_message_length,
            { &quot;Message Length&quot;, &quot;foo.msglength&quot;,
            FT_UINT16, BASE_DEC,
            NULL, 0x0,
            NULL, HFILL }
        },
        { &amp;hf_header_fcode,
            { &quot;Function Code&quot;, &quot;foo.FCode&quot;,
            FT_UINT8, BASE_HEX,
            NULL, 0x0,
            NULL, HFILL }
        },
        { &amp;hf_fcode_flag,
            { &quot;Fcode Flags&quot;, &quot;foo.Fcode.flags&quot;,
            FT_UINT8, BASE_HEX,
            NULL, 0x0,
            NULL, HFILL }
        }
    };

    static int *ett[] = {
        &amp;ett_fooheader,         //foo header
        &amp;ett_foosegment
    };

    proto_foo = proto_register_protocol (
        &quot;FOO Potocol&quot;,      // name
        &quot;FOO&quot;,              // short name
        &quot;foo&quot;               // abb ref
        );

    proto_register_field_array(proto_foo, hf, array_length(hf));
    proto_register_subtree_array(ett, array_length(ett));
}

static void dissect_foo(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree) {

    int offset = 0;
    guint8 fcode  = 0;

    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;FOO&quot;);
    // Clear out stuff in the info column
    col_clear(pinfo-&gt;cinfo,COL_INFO);

    if (tree) { // in case that someone wants to know some details of our protocol
        proto_item *ti = NULL;
        proto_tree *header_tree = NULL;

        ti = proto_tree_add_item(tree, proto_foo, tvb, 0, -1, ENC_NA);  // Grab all the data from the TCP Layer
        header_tree = proto_item_add_subtree(ti, ett_fooheader);

        proto_tree_add_item(header_tree, hf_header_message_length, tvb, offset, 2,  ENC_BIG_ENDIAN);
        offset +=2;

        fcode = tvb_get_guint8(tvb, offset);

        if (fcode = 0x00) {
            proto_tree *sub_tree = NULL;
            sub_tree = proto_item_add_subtree(header_tree, ett_foosegment);
            proto_tree_add_item(sub_tree, hf_fcode_flag, tvb, offset, 1,  ENC_BIG_ENDIAN);
            offset++;
        }
    }
}

void proto_reg_handoff_foo(void) {
    static dissector_handle_t foo_handle;
    foo_handle = create_dissector_handle(dissect_foo, proto_foo);
    dissector_add_uint(&quot;tcp.port&quot;, FOO_PORT, foo_handle);
}</code></pre></div><div id="question-tags" class="tags-container tags">dissector sub-dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '12, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/e12bbe1b488f2a19cdf565465e260d19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StuieNorris&#39;s gravatar image" /><p>StuieNorris<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StuieNorris has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Dec '12, 13:45</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-16524" class="comments-container"><span id="16555"></span><div id="comment-16555" class="comment"><div id="post-16555-score" class="comment-score"></div><div class="comment-text"><p>(Presumably that should be <code>if (fcode == 0x00)</code>, as <code>if (fcode = 0x00)</code> will set <code>fcode</code> to 0 and return 0 as the result, so the test will always fail. Fun with C....)</p></div><div id="comment-16555-info" class="comment-info"><span class="comment-age">(04 Dec '12, 13:48)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-16524" class="comment-tools"></div><div class="clear"></div><div id="comment-16524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16525"></span>

<div id="answer-container-16525" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16525-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to do something like this:</p><pre><code>if (fcode == 0x00) {
        proto_tree *sub_tree = NULL;
        proto_item *sub_item = NULL;
        sub_item = proto_tree_add_item(header_tree, hf_new, ...); /*you need a new field*/
        sub_tree = proto_item_add_subtree(sub_item , ett_foosegment);

        proto_tree_add_item(sub_tree, hf_fcode_flag, tvb, offset, 1,  ENC_BIG_ENDIAN);
        offset++;
    }</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '12, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p>SidR<br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Dec '12, 20:36</p></div></div><div id="comments-container-16525" class="comments-container"></div><div id="comment-tools-16525" class="comment-tools"></div><div class="clear"></div><div id="comment-16525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

