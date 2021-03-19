+++
type = "question"
title = "error in column &#x27;Payload protocol&#x27;: dissector not found"
description = '''I have defined a foo protocol dissector in Wireshark and compiled it successfully, but when I try adding this dissector in Preferences-&amp;gt;Protocols-&amp;gt;DLT_USER-&amp;gt;Encapsulations Table, it shows this error: error in column &#x27;Payload protocol&#x27;: dissector not found  Please advise. EDIT: SOURCE ADDED ...'''
date = "2012-02-04T07:33:00Z"
lastmod = "2012-02-07T22:39:00Z"
weight = 8823
keywords = [ "development", "error" ]
aliases = [ "/questions/8823" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [error in column 'Payload protocol': dissector not found](/questions/8823/error-in-column-payload-protocol-dissector-not-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8823-score" class="post-score" title="current number of votes">0</div><span id="post-8823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have defined a foo protocol dissector in Wireshark and compiled it successfully, but when I try adding this dissector in <strong>Preferences-&gt;Protocols-&gt;DLT_USER-&gt;Encapsulations Table</strong>, it shows this error:</p><pre><code>error in column &#39;Payload protocol&#39;: dissector not found</code></pre><p>Please advise.</p><p><strong>EDIT:</strong> SOURCE ADDED BELOW</p><pre><code>void
proto_register_foo(void)
{
    static hf_register_info hf[] = {
        { &amp;hf_foo_pdu_type,
            { &quot;FOO PDU Type&quot;, &quot;foo.type&quot;,
            FT_UINT8, BASE_DEC,
            NULL, 0x0,
            NULL, HFILL }
        }
    };

    /* Setup protocol subtree array */
    static gint *ett[] = {
        &amp;ett_foo
    };

    proto_foo = proto_register_protocol (
        &quot;FOO Protocol&quot;, /* name       */
        &quot;FOO&quot;,      /* short name */
        &quot;foo&quot;       /* abbrev     */
        );

    proto_register_field_array(proto_foo, hf, array_length(hf));
    proto_register_subtree_array(ett, array_length(ett));
    register_dissector(&quot;foo&quot;,dissect_foo,proto_foo);
}</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '12, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/d221d26845724614e25ab8e51887c4bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashish_goel&#39;s gravatar image" /><p><span>ashish_goel</span><br />
<span class="score" title="15 reputation points">15</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashish_goel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Feb '12, 22:41</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-8823" class="comments-container"></div><div id="comment-tools-8823" class="comment-tools"></div><div class="clear"></div><div id="comment-8823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8824"></span>

<div id="answer-container-8824" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8824-score" class="post-score" title="current number of votes">0</div><span id="post-8824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to register your dissector with name, register_dissector("rtp", dissect_rtp, proto_rtp);</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '12, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-8824" class="comments-container"><span id="8826"></span><div id="comment-8826" class="comment"><div id="post-8826-score" class="comment-score"></div><div class="comment-text"><p>Hi I added the following statement in the function proto_register_foo() function but no use.. Still getting the same error :(</p></div><div id="comment-8826-info" class="comment-info"><span class="comment-age">(04 Feb '12, 11:02)</span> <span class="comment-user userinfo">ashish_goel</span></div></div><span id="8828"></span><div id="comment-8828" class="comment"><div id="post-8828-score" class="comment-score"></div><div class="comment-text"><p>There is no "following statement" in your comment. Presumably you didn't <em>literally</em> add the statement</p><pre><code>register_dissector(&quot;rtp&quot;, dissect_rtp, proto_rtp);</code></pre><p>as that would only work for an RTP dissector, but you instead registered with a name such as "foo" and with names such as <code>dissect_foo</code> and <code>proto_foo</code> as arguments.</p><p>You also need to put it in your dissector's "register" routine (not the "register_handoff" routine).</p></div><div id="comment-8828-info" class="comment-info"><span class="comment-age">(04 Feb '12, 16:14)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="8831"></span><div id="comment-8831" class="comment"><div id="post-8831-score" class="comment-score"></div><div class="comment-text"><p>@ guy harris. I added : <strong>register_dissector("foo",dissect_foo,proto_foo);</strong> function call at the last line of <strong>proto_register_foo()</strong> routine. I guess I have done it right as per your suggestion. but its not working.</p></div><div id="comment-8831-info" class="comment-info"><span class="comment-age">(05 Feb '12, 00:45)</span> <span class="comment-user userinfo">ashish_goel</span></div></div><span id="8835"></span><div id="comment-8835" class="comment"><div id="post-8835-score" class="comment-score"></div><div class="comment-text"><p>I.e., if you open up the preferences for DLT_USER, click the "Edit..." button for "Encapsulations Table", click "New" or select an existing item and click "Edit...", and put "foo" into the "Payload protocol" field, and click "OK", you get that error?</p></div><div id="comment-8835-info" class="comment-info"><span class="comment-age">(05 Feb '12, 11:14)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="8836"></span><div id="comment-8836" class="comment"><div id="post-8836-score" class="comment-score"></div><div class="comment-text"><p>@guy harris. yes, I followed the same steps. And the foo protocol which I have defined is the same one which is there is developer's guide.</p></div><div id="comment-8836-info" class="comment-info"><span class="comment-age">(05 Feb '12, 18:55)</span> <span class="comment-user userinfo">ashish_goel</span></div></div><span id="8837"></span><div id="comment-8837" class="comment not_top_scorer"><div id="post-8837-score" class="comment-score"></div><div class="comment-text"><p>It might help if you edited your question to include your code for <code>proto_register_foo()</code>.</p></div><div id="comment-8837-info" class="comment-info"><span class="comment-age">(05 Feb '12, 19:26)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="8838"></span><div id="comment-8838" class="comment not_top_scorer"><div id="post-8838-score" class="comment-score"></div><div class="comment-text"><p>not having that right now.. will edit it in few hours.. BTW Is there anything not clear?</p></div><div id="comment-8838-info" class="comment-info"><span class="comment-age">(05 Feb '12, 22:50)</span> <span class="comment-user userinfo">ashish_goel</span></div></div><span id="8839"></span><div id="comment-8839" class="comment not_top_scorer"><div id="post-8839-score" class="comment-score"></div><div class="comment-text"><p>No. Adding <code>register_dissector</code> (or <code>new_register_dissector</code>) is <em>supposed</em> to work (and I've confirmed it does for me using the code template from README.developer with the latest source). Maybe there's something in your code that you don't see.</p></div><div id="comment-8839-info" class="comment-info"><span class="comment-age">(05 Feb '12, 23:45)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="8840"></span><div id="comment-8840" class="comment not_top_scorer"><div id="post-8840-score" class="comment-score"></div><div class="comment-text"><p>And to be complete, my <code>proto_register_foo()</code> looks like this:</p><pre><code>void
proto_register_foo(void)
{
    proto_foo = proto_register_protocol(&quot;foo&quot;,&quot;foo&quot;, &quot;foo&quot;);
    new_register_dissector(&quot;foo&quot;, dissect_foo, proto_foo);
}</code></pre></div><div id="comment-8840-info" class="comment-info"><span class="comment-age">(05 Feb '12, 23:51)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="8841"></span><div id="comment-8841" class="comment not_top_scorer"><div id="post-8841-score" class="comment-score"></div><div class="comment-text"><p>I have called register_dissector() function not new_register_dissector().</p><p>BTW I have edited the ques to include the source of my proto_register_foo function.</p></div><div id="comment-8841-info" class="comment-info"><span class="comment-age">(06 Feb '12, 01:34)</span> <span class="comment-user userinfo">ashish_goel</span></div></div><span id="8849"></span><div id="comment-8849" class="comment not_top_scorer"><div id="post-8849-score" class="comment-score"></div><div class="comment-text"><p>any suggestions plz??</p></div><div id="comment-8849-info" class="comment-info"><span class="comment-age">(06 Feb '12, 08:27)</span> <span class="comment-user userinfo">ashish_goel</span></div></div><span id="8862"></span><div id="comment-8862" class="comment not_top_scorer"><div id="post-8862-score" class="comment-score"></div><div class="comment-text"><p>You can use either <code>new_register_dissector</code> or <code>register_dissector</code>, but the latter requires a type-cast on <code>dissect_foo</code> (depending on which source list you added your dissector to).</p><p>Your code works for me (I can add "foo" to the DLT table from prefs). If you type <code>foo</code> into Wireshark's Display Filter textbox, the textbox's background should turn green. Otherwise, your dissector isn't even registered. Is your source actually being compiled?</p></div><div id="comment-8862-info" class="comment-info"><span class="comment-age">(06 Feb '12, 14:53)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="8863"></span><div id="comment-8863" class="comment not_top_scorer"><div id="post-8863-score" class="comment-score"></div><div class="comment-text"><p>My source file is located in:</p><pre><code>${wireshark_src}/epan/dissectors/packet-foo.c</code></pre><p>I added <code>packet-foo.c</code> to the <code>DISSECTOR_SRC</code> list in:</p><pre><code>${wireshark_src}/epan/CMakeLists.txt</code></pre><p>If you're not using CMake (i.e., you're using the <code>autotools</code> build), the file to modify is:</p><pre><code>${wireshark_src}/epan/dissectors/Makefile.common</code></pre></div><div id="comment-8863-info" class="comment-info"><span class="comment-age">(06 Feb '12, 15:03)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="8865"></span><div id="comment-8865" class="comment not_top_scorer"><div id="post-8865-score" class="comment-score"></div><div class="comment-text"><p>the dissector is registered for sure. I can use it in the decode as option. Even the filter text box turns green.</p><p>the new_register_dissector function not working for me. throws an error while compiling.</p></div><div id="comment-8865-info" class="comment-info"><span class="comment-age">(06 Feb '12, 18:44)</span> <span class="comment-user userinfo">ashish_goel</span></div></div><span id="8866"></span><div id="comment-8866" class="comment not_top_scorer"><div id="post-8866-score" class="comment-score"></div><div class="comment-text"><p>I don't have any other suggestions other than for you to step through the code with a debugger (put a breakpoint at <code>uat_fld_chk_proto</code>).</p></div><div id="comment-8866-info" class="comment-info"><span class="comment-age">(06 Feb '12, 22:36)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="8884"></span><div id="comment-8884" class="comment not_top_scorer"><div id="post-8884-score" class="comment-score"></div><div class="comment-text"><p>thanks, for all the help. I had to create a new workspace and it worked. I guess some file was corrupted</p></div><div id="comment-8884-info" class="comment-info"><span class="comment-age">(07 Feb '12, 22:39)</span> <span class="comment-user userinfo">ashish_goel</span></div></div></div><div id="comment-tools-8824" class="comment-tools"><span class="comments-showing"> showing 5 of 16 </span> <a href="#" class="show-all-comments-link">show 11 more comments</a></div><div class="clear"></div><div id="comment-8824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8861"></span>

<div id="answer-container-8861" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8861-score" class="post-score" title="current number of votes">0</div><span id="post-8861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I've seen this when the <code>user_dlts</code> file is malformed or contains a reference to a nonexistent dissector. Try deleting your <code>user_dlts</code> file, or at least check to make sure that each entry looks valid.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '12, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-8861" class="comments-container"><span id="8883"></span><div id="comment-8883" class="comment"><div id="post-8883-score" class="comment-score"></div><div class="comment-text"><p>thanks, it worked.. I had to create a new workspace and it worked. I guess some file was corrupted</p></div><div id="comment-8883-info" class="comment-info"><span class="comment-age">(07 Feb '12, 22:38)</span> <span class="comment-user userinfo">ashish_goel</span></div></div></div><div id="comment-tools-8861" class="comment-tools"></div><div class="clear"></div><div id="comment-8861-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

