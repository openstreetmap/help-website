+++
type = "question"
title = "How do multiple dissectors work in same plugindll ?"
description = '''Hi all, I am currently trying to write a dissector for my custom protocol. The protocol as most protocols do, has different types of packets which are identified by the first 8 bits of the header. Now i want to display a different structure per each packet. I do realize that we can register multiple...'''
date = "2011-07-14T23:13:00Z"
lastmod = "2011-07-15T07:40:00Z"
weight = 5050
keywords = [ "development", "dissector", "wireshark" ]
aliases = [ "/questions/5050" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do multiple dissectors work in same plugindll ?](/questions/5050/how-do-multiple-dissectors-work-in-same-plugindll)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5050-score" class="post-score" title="current number of votes">0</div><span id="post-5050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am currently trying to write a dissector for my custom protocol. The protocol as most protocols do, has different types of packets which are identified by the first 8 bits of the header. Now i want to display a different structure per each packet. I do realize that we can register multiple dissectors in the plugin.c as in the samples. However i wish to know how to transfer control to a different dissector per different packet once i have deciphered what type of packet it is from the header ? Do we have to return zero or null from one dissector for the next dissector to be called ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '11, 23:13</strong></p><img src="https://secure.gravatar.com/avatar/1977d57c9ec2c3fe14338289c7215da0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Imtiyaz&#39;s gravatar image" /><p><span>Imtiyaz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Imtiyaz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>15 Jul '11, 07:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-5050" class="comments-container"></div><div id="comment-tools-5050" class="comment-tools"></div><div class="clear"></div><div id="comment-5050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5054"></span>

<div id="answer-container-5054" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5054-score" class="post-score" title="current number of votes">1</div><span id="post-5054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's a pretty straightforward process, but it may not be obvious if your are just starting out. Here's one way to do it, using a dissector table. Say you have two dissectors, <code>foo</code>, and <code>subfoo</code>. First, in your main dissector (<code>foo</code>, the one that identifies the type of packet):</p><pre><code>static dissector_table_t foo_dissector_table = NULL; /* declare dissector table */

static void dissect_foo(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    guint8 data_type = 0;
    gboolean subdissector_found = FALSE;
    /* dissection logic goes here */
    data_type = tvb_get_guint8(tvb, 0);
    subdissector_found = dissector_try_port(
        foo_dissector_table,
        data_type,
        tvb, pinfo, tree);
    if(subdissector_found == FALSE)
    {
        /* note that the data is undecoded for the data type */
    }
}

void proto_register_foo(void)
{
    /* Your registration code */
    foo_dissector_table = register_dissector table(
        &quot;foo.data_type&quot;,       /* field filter name, as described in hf_* structure */
        &quot;the data type field&quot;, /* description of field */
        FT_UINT8,              /* data type */
        BASE_DEC               /* display base */
        );
}</code></pre><p>Then, in your other dissectors (<code>subfoo</code>, and any other dissectors that further decode your protocol), register against this table like so:</p><pre><code>void proto_regist_subfoo(void)
{
    /* create a dissector handle for subfoo */
    subfoo_handle = create_dissector_handle(
        dissect_subfoo, /*the dissection function */
        proto_subfoo); /* previously initialized with proto_register_protocol)
}

void proto_reg_handoff_subfoo(void)
{
    /* other reg_handoff tasks */
    dissector_add(&quot;foo.data_type&quot;,
        data_type_value_for_subfoo, /* guint8 value of foo.data_type identifying subfoo */
        subfoo_handle /* initialized in proto_register_subfoo */
        );
}</code></pre><p>You'll probably wan't to provide a subset of <code>tvb</code> rather than the whole thing in <code>dissect_foo</code> when using <code>dissector_try_port</code>, but that is up to you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '11, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jul '11, 07:57</strong> </span></p></div></div><div id="comments-container-5054" class="comments-container"></div><div id="comment-tools-5054" class="comment-tools"></div><div class="clear"></div><div id="comment-5054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

