+++
type = "question"
title = "FT_FRAMENUM is not working"
description = '''#include &quot;config.h&quot;  #include &amp;lt;epan/packet.h&amp;gt;  #define TMP_PORT 80  static int proto_tmp_test = -1;  static int hf_tmp_test_pdu_type = -1; static int hf_tmp_test_tmp = -1;  static int ett_tmp_test = -1;  static int dissect_tmp_test (tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *da...'''
date = "2017-01-12T02:10:00Z"
lastmod = "2017-01-13T06:01:00Z"
weight = 58694
keywords = [ "headers", "ftypes", "plugins", "dissectors" ]
aliases = [ "/questions/58694" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [FT\_FRAMENUM is not working](/questions/58694/ft_framenum-is-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58694-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>#include &quot;config.h&quot;

#include &lt;epan/packet.h&gt;

#define TMP_PORT 80

static int proto_tmp_test = -1;

static int hf_tmp_test_pdu_type = -1;
static int hf_tmp_test_tmp = -1;

static int ett_tmp_test = -1;

static int dissect_tmp_test (tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *data)
{
    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;tmp&quot;);
    /* Clear out stuff in the info column */
    col_clear(pinfo-&gt;cinfo,COL_INFO);

    proto_item *ti = proto_tree_add_item(tree, proto_tmp_test, tvb, 0, -1, ENC_NA);

    // just an example - this has no meaning
    proto_tree_add_uint(tree, hf_tmp_test_tmp, tvb, 0, 0, 12);

    return tvb_captured_length(tvb);
}

void
proto_register_tmp_test(void)
{
    static hf_register_info hf[] = {
        { &amp;hf_tmp_test_pdu_type,
            { &quot;tmp PDU type&quot;, &quot;tmp.type&quot;,
            FT_UINT8, BASE_DEC,
            NULL, 0x0,
            NULL, HFILL }
        },
        { &amp;hf_tmp_test_tmp,
            { &quot;tmp Tmp frame number&quot;, &quot;tmp.tmp&quot;,
            FT_FRAMENUM, BASE_NONE,
            NULL, 0x0,
            NULL, HFILL }
        }
    };

    /* Setup protocol subtree array */
    static gint *ett[] = {
        &amp;ett_tmp_test
    };

    proto_tmp_test = proto_register_protocol (
        &quot;tmp Test Protocol&quot;, /* name       */
        &quot;tmp&quot;,      /* short name */
        &quot;tmp&quot;       /* abbrev     */
        );

    proto_register_field_array(proto_tmp_test, hf, array_length(hf));
    proto_register_subtree_array(ett, array_length(ett));
}

void
proto_reg_handoff_tmp_test(void)
{
    static dissector_handle_t tmp_test_handle;

    tmp_test_handle = create_dissector_handle(dissect_tmp_test, proto_tmp_test);
    dissector_add_uint(&quot;tcp.port&quot;, TMP_PORT, tmp_test_handle);
}</code></pre><p>I want to add FT_FRAMENUM for the direct link to frame. But it seems for some reason wireshark is not recognizing the hfinfo and throwing exception DISSECTOR_ASSERT_NOT_REACHED from proto_tree_add_uint. From my analysis I found wireshark is not recognizing hf_tmp_test_tmp in the above code.</p><p>Please help me with this.</p></div><div id="question-tags" class="tags-container tags">headers ftypes plugins dissectors</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '17, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/54b13e716c5802540b3b28701372e876?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chirag&#39;s gravatar image" /><p>chirag<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chirag has no accepted answers">0%</span></p></div></div><div id="comments-container-58694" class="comments-container"><span id="58701"></span><div id="comment-58701" class="comment"><div id="post-58701-score" class="comment-score"></div><div class="comment-text"><p>What is the <em>exact</em> assertion you're getting? And what version are you using?</p></div><div id="comment-58701-info" class="comment-info"><span class="comment-age">(12 Jan '17, 07:11)</span> JeffMorriss ♦</div></div><span id="58731"></span><div id="comment-58731" class="comment"><div id="post-58731-score" class="comment-score"></div><div class="comment-text"><p>I am using version 2.2.3 and I am getting Assertion: DISSECTOR_ASSERT_NOT_REACHED.</p></div><div id="comment-58731-info" class="comment-info"><span class="comment-age">(13 Jan '17, 05:17)</span> chirag</div></div><span id="58732"></span><div id="comment-58732" class="comment"><div id="post-58732-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I meant exactly which <code>DISSECTOR_ASSERT_NOT_REACHED</code>? Usually when an assertion fires it gives you a file and line number.</p></div><div id="comment-58732-info" class="comment-info"><span class="comment-age">(13 Jan '17, 05:51)</span> JeffMorriss ♦</div></div><span id="58801"></span><div id="comment-58801" class="comment"><div id="post-58801-score" class="comment-score"></div><div class="comment-text"><p>Hi Jeff it is not showing which dissector and the line number...it just shows DISSECTOR_ASSERT_NOT_REACHED.</p></div><div id="comment-58801-info" class="comment-info"><span class="comment-age">(16 Jan '17, 02:56)</span> chirag</div></div><span id="58802"></span><div id="comment-58802" class="comment"><div id="post-58802-score" class="comment-score"></div><div class="comment-text"><p>One more thing when I replaced FT_FRAMENUM with FT_UINT56, BASE_DEC then it shows the number but as it is just integer link is not there.</p></div><div id="comment-58802-info" class="comment-info"><span class="comment-age">(16 Jan '17, 02:58)</span> chirag</div></div></div><div id="comment-tools-58694" class="comment-tools"></div><div class="clear"></div><div id="comment-58694-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58733"></span>

<div id="answer-container-58733" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58733-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can run your sample code without any issue with Wireshark 2.2.3.</p><p>Are you developing an internal dissector, or a plugin?</p><p>If it is a plugin, are you compiling it against Wireshark 2.2.3 source code? The ftenum enumeration found in epan/ftypes/ftypes.h changes between Wireshark major releases, so FT_FRAMENUM will not have the same value depending on the branch used.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '17, 06:01</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-58733" class="comments-container"><span id="58804"></span><div id="comment-58804" class="comment"><div id="post-58804-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal, I am developing plugin. I am compiling it using the latest wireshark libraries (source code git cloned). currently I am using it one a 32-bit wireshark 2.2.3 version for windows.</p></div><div id="comment-58804-info" class="comment-info"><span class="comment-age">(16 Jan '17, 03:01)</span> chirag</div></div><span id="58807"></span><div id="comment-58807" class="comment"><div id="post-58807-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal, It seems you are right, the ftypes which is used by the wireshark I downloaded from the internet is different then the one I am compiling with . I calculated the offset and instead of FT_FRAMENUM i had put FT_IPXNET which is right after it, and it worked as FT_FRAMENUM.</p><p>Any idea on how to check the installed wireshark ftypes.h file?</p></div><div id="comment-58807-info" class="comment-info"><span class="comment-age">(16 Jan '17, 04:43)</span> chirag</div></div><span id="58808"></span><div id="comment-58808" class="comment"><div id="post-58808-score" class="comment-score"></div><div class="comment-text"><p>What you should do is ensure you are compiling against the Wireshark version you intend to use.</p><p>So if you want to run Wireshark 2.2.X stable release, you need to clone master-2.2 branch and not master branch (that corresponds to Wireshark 2.3.0 development builds). Wireshark internal APIs are not stable between major releases and you will face many weird issues if you do not follow my advice. Then compile your plugin source code as usual.</p></div><div id="comment-58808-info" class="comment-info"><span class="comment-age">(16 Jan '17, 06:00)</span> Pascal Quantin</div></div><span id="58809"></span><div id="comment-58809" class="comment"><div id="post-58809-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal, thanks a lot for the help, I changed the libraries to match with the installed versions and all problems are gone.</p></div><div id="comment-58809-info" class="comment-info"><span class="comment-age">(16 Jan '17, 06:18)</span> chirag</div></div><span id="58810"></span><div id="comment-58810" class="comment"><div id="post-58810-score" class="comment-score"></div><div class="comment-text"><p>As the problem is solved, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer.</p></div><div id="comment-58810-info" class="comment-info"><span class="comment-age">(16 Jan '17, 06:32)</span> Pascal Quantin</div></div></div><div id="comment-tools-58733" class="comment-tools"></div><div class="clear"></div><div id="comment-58733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

