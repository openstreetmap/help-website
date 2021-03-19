+++
type = "question"
title = "Data Parameter and Private_Data"
description = '''I&#x27;m trying not to avoid the pinfo -&amp;gt; private_data as I want to use the data parameter. My questions is which function definition do I change to be able to use the data parameter, in my dissector there is no function that takes a 4th parameter! if (handle-&amp;gt;is_new) {  ret = (*handle-&amp;gt;dissecto...'''
date = "2015-05-13T13:25:00Z"
lastmod = "2015-05-13T14:06:00Z"
weight = 42379
keywords = [ "dissector", "plugin", "wireshark" ]
aliases = [ "/questions/42379" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Data Parameter and Private\_Data](/questions/42379/data-parameter-and-private_data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42379-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying not to avoid the pinfo -&gt; private_data as I want to use the data parameter. My questions is which function definition do I change to be able to use the data parameter, in my dissector there is no function that takes a 4th parameter!</p><pre><code>if (handle-&gt;is_new) {
        ret = (*handle-&gt;dissector.new_d)(tvb, pinfo, tree, data);
    } else {
        pinfo-&gt;private_data = data;     // ADDED!!!!!!!!!!!!!!!!!!!!
        (*handle-&gt;dissector.old)(tvb, pinfo, tree);
        ret = tvb_length(tvb);
        if (ret == 0) {
            ret = 1;
        }
    }</code></pre><p>Could you please explain exactly what happens here:</p><pre><code>ret = (*handle-&gt;dissector.new_d)(tvb, pinfo, tree, data);</code></pre><p>and here</p><pre><code>(*handle-&gt;dissector.old)(tvb, pinfo, tree);</code></pre><p>In my case I have the following:</p><pre><code>X_handle = new_create_dissector_handle(dissect_X, proto_X);
arr_handle = create_dissector_handle(dissect_arr, proto_ZZX);
arr_handle = create_dissector_handle(dissect_arr, proto_XXZ);

heur_dissector_add(&quot;udp&quot;, dissect_X, proto_X);
dissector_add_uint(&quot;tcp.port&quot;, ZZX_PORT, arr_handle);
dissector_add_uint(&quot;tcp.port&quot;, XXZ_PORT, arr_handle);

Function call leading upto where pinfo-&gt;private_data is used:
dissect_X -&gt; dissect_arr_X -&gt; dissect_retransmissions_X -&gt; add_seq
dissect_arr -&gt; dissect_retransmissions -&gt; add_seq

static gboolean add_seq(tvbuff_t *tvb, packet_info *pinfo)</code></pre></div><div id="question-tags" class="tags-container tags">dissector plugin wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '15, 13:25</strong></p><img src="https://secure.gravatar.com/avatar/42f084d62348c04d00bd67b129116cc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="XQW1123&#39;s gravatar image" /><p>XQW1123<br />
<span class="score" title="46 reputation points">46</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="XQW1123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 May '15, 13:59</p></div></div><div id="comments-container-42379" class="comments-container"></div><div id="comment-tools-42379" class="comment-tools"></div><div class="clear"></div><div id="comment-42379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42380"></span>

<div id="answer-container-42380" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42380-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>in my dissector there is no function that takes a 4th parameter!</p></blockquote><p>Then change the dissector so that its main function <em>does</em> take a 4th parameter, which will be a <code>void *</code> pointing to the data passed to it.</p><p>Note that, in the currently-supported versions of Wireshark (1.10.x, 1.12.x, and 1.99.x), if the function <code>dissect_X()</code> does not have 4 parameters:</p><pre><code>int dissect_X(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *data)
{
    ...
}</code></pre><p>then the call to <code>new_create_dissector_handle()</code> in</p><pre><code>X_handle = new_create_dissector_handle(dissect_X, proto_X);</code></pre><p>will get a warning. <strong><em>DO NOT IGNORE THIS WARNING!</em></strong> Instead, fix <code>dissect_X()</code> to take that fourth parameter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '15, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-42380" class="comments-container"></div><div id="comment-tools-42380" class="comment-tools"></div><div class="clear"></div><div id="comment-42380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

