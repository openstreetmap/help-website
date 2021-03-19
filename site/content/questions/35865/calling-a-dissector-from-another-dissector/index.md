+++
type = "question"
title = "Calling a dissector from another dissector."
description = '''Hi, im having trouble calling a dissector from another dissector. As a test, im trying to call the foo dissector, from my test dissector. The foo dissector has the following registration proto_foo = proto_register_protocol (  &quot;FOO Protocol&quot;, /* name */  &quot;FOO&quot;, /* short name */  &quot;foo&quot; /* abbrev */  )...'''
date = "2014-08-29T05:40:00Z"
lastmod = "2014-08-29T07:05:00Z"
weight = 35865
keywords = [ "test", "foo", "guide", "dissector", "help" ]
aliases = [ "/questions/35865" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Calling a dissector from another dissector.](/questions/35865/calling-a-dissector-from-another-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35865-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, im having trouble calling a dissector from another dissector. As a test, im trying to call the foo dissector, from my test dissector. The foo dissector has the following registration</p><pre><code>proto_foo = proto_register_protocol (
    &quot;FOO Protocol&quot;, /* name       */
    &quot;FOO&quot;,      /* short name */
    &quot;foo&quot;       /* abbrev     */
    );</code></pre><p>Meaning its abbreviation is "foo". So, in the dissector im programing, im doing the following.</p><p>I have the following global variable</p><pre><code>static gint hf_foo_pdu_type=-1;</code></pre><p>This is my handoff</p><pre><code>void proto_reg_handoff_test(void)
{
    static dissector_handle_t test_handle;
    foo_handle = find_dissector(&quot;foo&quot;);
    test_handle = create_dissector_handle(dissect_test, proto_test);
    dissector_add_uint(&quot;udp.port&quot;, TEST_PORT, test_handle);
}

 The trouble im having is that foo_handle is NULL. My dissector compiles OK, but when I run wireshark, it just doesnt work, and the program shuts down.

This is how im trying to call the dissector

static void
dissect_test(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;Test protocol&quot;);
    /* Clear out stuff in the info column */
    col_clear(pinfo-&gt;cinfo,COL_INFO);

    if (tree)
        { /* we are being asked for details */
            proto_item *ti = NULL;
            proto_tree *test_tree = NULL;
            ti = proto_tree_add_item(tree, proto_test, tvb, 0, -1, ENC_NA);
            test_tree = proto_item_add_subtree(ti, ett_test);
            proto_tree_add_item(test_tree, hf_test_uselessbyte, tvb, 0, 1, ENC_BIG_ENDIAN);
            call_dissector(foo_handle, tvb_new_subset_remaining(tvb, 1), pinfo, test_tree);
        }
}

My test protocol, has only 1 byte at the beggining (uselessbyte), and then, the rest follows my foo template. Im doing this to experiment, and to learn how to use this tools, to later apply them in a real dissector.

I havent found any help on the internet (theres nothing on README.dissector), so could you please tell me what im doing wrong?

Thanks in advance</code></pre></div><div id="question-tags" class="tags-container tags">test foo guide dissector help</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '14, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/3f60a30a327fa363a0166009000c466d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ingcpt&#39;s gravatar image" /><p>ingcpt<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ingcpt has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Aug '14, 09:24</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-35865" class="comments-container"><span id="35866"></span><div id="comment-35866" class="comment"><div id="post-35866-score" class="comment-score"></div><div class="comment-text"><p>If foo_handle is NULL it mean that the dissector does not exist. You can check if your dissector exist by trying to find him in filter. Open Wireshark and write your dissector's name in filter bar, green mean that Wireshark knows your dissector and red mean that he does not.</p></div><div id="comment-35866-info" class="comment-info"><span class="comment-age">(29 Aug '14, 06:51)</span> Afrim</div></div><span id="35867"></span><div id="comment-35867" class="comment"><div id="post-35867-score" class="comment-score"></div><div class="comment-text"><p>foo exists. If i run wireshark, and type foo in the filter, it turns green, yet foo_handle is still null</p></div><div id="comment-35867-info" class="comment-info"><span class="comment-age">(29 Aug '14, 07:03)</span> ingcpt</div></div><span id="35869"></span><div id="comment-35869" class="comment"><div id="post-35869-score" class="comment-score"></div><div class="comment-text"><p>foo exists, and works perfectly. I made it using the guide provided by wireshark</p></div><div id="comment-35869-info" class="comment-info"><span class="comment-age">(29 Aug '14, 07:05)</span> ingcpt</div></div></div><div id="comment-tools-35865" class="comment-tools"></div><div class="clear"></div><div id="comment-35865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35868"></span>

<div id="answer-container-35868" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35868-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In the foo dissector you need to do register_dissector("foo", dissect_foo, proto_foo);</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '14, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-35868" class="comments-container"><span id="35872"></span><div id="comment-35872" class="comment"><div id="post-35872-score" class="comment-score"></div><div class="comment-text"><p>Thanks! That worked like a charm!</p></div><div id="comment-35872-info" class="comment-info"><span class="comment-age">(29 Aug '14, 08:08)</span> ingcpt</div></div><span id="35873"></span><div id="comment-35873" class="comment"><div id="post-35873-score" class="comment-score"></div><div class="comment-text"><p>Finally, i had to add, into foo (the dissector that gets called from another dissector) the line</p><p>register_dissector("foo", dissect_foo, proto_foo);</p></div><div id="comment-35873-info" class="comment-info"><span class="comment-age">(29 Aug '14, 08:15)</span> ingcpt</div></div><span id="35878"></span><div id="comment-35878" class="comment"><div id="post-35878-score" class="comment-score"></div><div class="comment-text"><p>@ingcpt,</p><p>If an answer has solved your issue, don't change the title, simply click the checkmark next to the answer as that's how this site works. Please see the FAQ for more info.</p></div><div id="comment-35878-info" class="comment-info"><span class="comment-age">(29 Aug '14, 09:24)</span> grahamb ♦</div></div></div><div id="comment-tools-35868" class="comment-tools"></div><div class="clear"></div><div id="comment-35868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

