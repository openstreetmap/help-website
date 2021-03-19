+++
type = "question"
title = "Using Dissectors and Subdissectors"
description = '''Hi all, I have to write a Protcol-Analyzer, basing on TCP. The first Level is a company-specific Protocol which encapsulates several other company-specific protocols. The first Level I have already implemented and it works. That means. The Data from TCP (lets call it Proto_One) I can analyze and mak...'''
date = "2011-10-25T07:57:00Z"
lastmod = "2011-10-26T02:40:00Z"
weight = 7060
keywords = [ "dissector", "sub-dissector", "wireshark" ]
aliases = [ "/questions/7060" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Using Dissectors and Subdissectors](/questions/7060/using-dissectors-and-subdissectors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7060-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I have to write a Protcol-Analyzer, basing on TCP. The first Level is a company-specific Protocol which encapsulates several other company-specific protocols.</p><p>The first Level I have already implemented and it works. That means. The Data from TCP (lets call it Proto_One) I can analyze and make them viewable in the Tree. But next Step is to make the Data from (lets call it Proto_Two and Proto_Three) available for next dissector. Here is my Code which is not completely working:</p><p>File: packet-proton.c</p><pre><code>void proto_reg_handoff_protone(void)
{
    dissector_handle_t protone_handle;

    protone_handle = find_dissector(&quot;protone&quot;);
    dissector_add_uint(&quot;tcp.port&quot;, global_protone_port, protone_handle);

    data_handle = find_dissector(&quot;data&quot;);
}</code></pre><p><br />
<br />
File: packet-prottwo.c</p><pre><code>void proto_reg_handoff_prottwo(void)
{
    dissector_handle_t prottwo_handle;

    prottwo_handle = find_dissector(&quot;protone&quot;);
    dissector_add(&quot;protone.protid&quot;, 4710, prottwo_handle);

    data_handle = find_dissector(&quot;data&quot;);
}</code></pre><p><br />
<br />
When I startup the WireShark on my Windows XP, I get the Error:<br />
<strong>Runtime Error!<br />
Program: C:\Programme\System\Wireshark\Wireshark.exe<br />
This application has requestes the Runtime to terminate it in an unusual way.<br />
Please contact the application's support team for more information.</strong><br />
<br />
Best Regards<br />
tjmaker<br />
<br />
<br />
<br />
By the Way: I was trying to make the System debugable with my MSVS 2008 but it didn't get it work.</p></div><div id="question-tags" class="tags-container tags">dissector sub-dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '11, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/5ead9ea8c711ef226028510b0810cde3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tjamaker&#39;s gravatar image" /><p>tjamaker<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tjamaker has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '12, 21:30</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></br></p></div></div><div id="comments-container-7060" class="comments-container"></div><div id="comment-tools-7060" class="comment-tools"></div><div class="clear"></div><div id="comment-7060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7065"></span>

<div id="answer-container-7065" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7065-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'll have to create a sub dissector table in <code>proto_register_protone()</code>, like so:</p><p><code>register_dissector_table("protone.protid", .... </code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '11, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-7065" class="comments-container"><span id="7071"></span><div id="comment-7071" class="comment"><div id="post-7071-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer. No I got WireShark started. But the dissection still doesn't work.</p><p>I made these changes in packet-proton.c:</p><pre><code>void proto_register_protone (void)
{
    ...

    static hf_register_info hf[] =
    {
        ...

        { &amp;hf_protone_protId,
              { &quot;Protocol Identifier&quot;, &quot;protone.protId&quot;, 
                    FT_UINT16, BASE_HEX, VALS(protocolIdTypeNames), 
                    0x0, &quot;Protocol Identifier&quot;, HFILL } },

        ...
    };

    /* subdissector code */
    subdissector_table = register_dissector_table(&quot;protone.protid&quot;,
        &quot;Protocol Identifier&quot;, FT_UINT16, BASE_HEX);
    register_heur_dissector_list(&quot;protone&quot;, &amp;heur_subdissector_list);

    ...
}</code></pre><p>Do I really need the line with <strong>register_heur_dissector_list</strong>?<br />
<br />
<br />
And these changes I made in packet-prottwo.c:</p><pre><code>void proto_reg_handoff_prottwo(void)
{
    dissector_handle_t prottwo_handle;

    prottwo_handle = find_dissector(&quot;protone&quot;);
    dissector_add(&quot;protone.protid&quot;, 0x1266, prottwo_handle);

    data_handle = find_dissector(&quot;data&quot;);
}</code></pre><p><br />
Is there something else, I have to configure?<br />
Is it working with 0x1266 or do I have to use 4710?<br />
<br />
Best Regards<br />
tjamaker</p></div><div id="comment-7071-info" class="comment-info"><span class="comment-age">(25 Oct '11, 22:45)</span> tjamaker</div></div><span id="7077"></span><div id="comment-7077" class="comment"><div id="post-7077-score" class="comment-score"></div><div class="comment-text"><p>Do I really need the line with register_heur_dissector_list? Answer: No</p><p>prottwo_handle = find_dissector("protone"); should be find_dissector("prottwo");</p></div><div id="comment-7077-info" class="comment-info"><span class="comment-age">(26 Oct '11, 04:47)</span> Jaap ♦</div></div></div><div id="comment-tools-7065" class="comment-tools"></div><div class="clear"></div><div id="comment-7065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7075"></span>

<div id="answer-container-7075" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7075-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, now I got the MSVC++ 2088 EE running to be able to debug the code. And now I can detect, that in my dissect_protone the call_dissector is called but it never appears in dissect_prottwo.</p><pre><code>static void dissect_wagosp(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    ...

    if (length_remaining != 0) 
    {
        tvbuff_t *next_tvb;
        next_tvb = tvb_new_subset_remaining(tvb, offset);

        call_dissector(data_handle, next_tvb, pinfo, tree);
    }

    ...

}</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '11, 02:40</strong></p><img src="https://secure.gravatar.com/avatar/5ead9ea8c711ef226028510b0810cde3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tjamaker&#39;s gravatar image" /><p>tjamaker<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tjamaker has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-7075" class="comments-container"><span id="7078"></span><div id="comment-7078" class="comment"><div id="post-7078-score" class="comment-score"></div><div class="comment-text"><p>This won't call your prottwo dissector. Use:</p><p><code>dissector_try_uint(subdissector_table, protid, next_tvb, pinfo, tree));</code></p><p>if protid == 0x1266 then it will be called.</p></div><div id="comment-7078-info" class="comment-info"><span class="comment-age">(26 Oct '11, 04:49)</span> Jaap ♦</div></div><span id="7079"></span><div id="comment-7079" class="comment"><div id="post-7079-score" class="comment-score"></div><div class="comment-text"><p>THX, now it works !!!</p></div><div id="comment-7079-info" class="comment-info"><span class="comment-age">(26 Oct '11, 04:55)</span> tjamaker</div></div></div><div id="comment-tools-7075" class="comment-tools"></div><div class="clear"></div><div id="comment-7075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

