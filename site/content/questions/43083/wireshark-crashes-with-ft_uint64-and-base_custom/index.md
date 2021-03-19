+++
type = "question"
title = "Wireshark crashes with FT_UINT64 and BASE_CUSTOM"
description = '''Hello, I try to add a UINT64 field with the following definition: { &amp;amp;hf_boxinfo_softwarerelease,  { &quot;SoftwareRelease&quot;, &quot;boxinfo.swRelease&quot;,  FT_UINT32, BASE_CUSTOM,  displayVersion48, 0x0,  &quot;SoftwareRelease&quot;, HFILL } }  This field contains 6 bytes, which I want to display as a version (e.g. 03.4...'''
date = "2015-06-11T08:51:00Z"
lastmod = "2015-06-11T09:36:00Z"
weight = 43083
keywords = [ "base_custom", "crash", "ft_uint64", "plugin" ]
aliases = [ "/questions/43083" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashes with FT\_UINT64 and BASE\_CUSTOM](/questions/43083/wireshark-crashes-with-ft_uint64-and-base_custom)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43083-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I try to add a UINT64 field with the following definition:</p><pre><code>{ &amp;hf_boxinfo_softwarerelease,
            { &quot;SoftwareRelease&quot;, &quot;boxinfo.swRelease&quot;,
            FT_UINT32, BASE_CUSTOM,
            displayVersion48, 0x0,
            &quot;SoftwareRelease&quot;, HFILL }
}</code></pre><p>This field contains 6 bytes, which I want to display as a version (e.g. 03.45.32 so 2 bytes per element) The problem is that Wireshark crashes when I click on the protocol item. I have another simular field with a FT_UINT32 which without troubles. Here is the function's source:</p><pre><code>void displayVersion48(gchar *strptr, guint64 value){
     g_snprintf(strptr,15,&quot;TEST&quot;);
}</code></pre><p>Thank you for help.</p><p>lal12</p></div><div id="question-tags" class="tags-container tags">base_custom crash ft_uint64 plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '15, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/cc56ba9bd225bd68cea09a404ecc0b6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lal12&#39;s gravatar image" /><p>lal12<br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lal12 has 2 accepted answers">33%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jun '15, 08:52</p></div></div><div id="comments-container-43083" class="comments-container"></div><div id="comment-tools-43083" class="comment-tools"></div><div class="clear"></div><div id="comment-43083-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43084"></span>

<div id="answer-container-43084" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43084-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Support for 64bits and BASE_CUSTOM was added in master branch. So please consider using this one and declare your entry as:</p><pre><code>{ &amp;hf_boxinfo_softwarerelease,
        { &quot;SoftwareRelease&quot;, &quot;boxinfo.swRelease&quot;,
        FT_UINT64, BASE_CUSTOM,
        CF_FUNC(displayVersion48), 0x0,
        &quot;SoftwareRelease&quot;, HFILL }
}</code></pre><p>where displayVersion48 has the following signature:</p><pre><code>typedef void (*custom_fmt_func_64_t)(gchar *, guint64);</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '15, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jun '15, 09:36</p></div></div><div id="comments-container-43084" class="comments-container"><span id="43095"></span><div id="comment-43095" class="comment"><div id="post-43095-score" class="comment-score"></div><div class="comment-text"><p>If I switch to the master branch, will the plugins work on the normal wireshark installations from the website. If not your solution, won't work for me, cause my plugin needs to work on this versions.</p><p>I think just declaring a FT_UINT32 works, even if the value is longer.</p></div><div id="comment-43095-info" class="comment-info"><span class="comment-age">(12 Jun '15, 05:47)</span> lal12</div></div><span id="43096"></span><div id="comment-43096" class="comment"><div id="post-43096-score" class="comment-score">1</div><div class="comment-text"><p>The plugin are only compatible with the branches for which they are compiled.</p><p>As Wireshark 1.99.6 is distributed on Wireshark web site it should be OK I guess.</p><p>I do not see how you expect to get a guint64 out of a guint32 value... So no it will not work. BASE_CUSTOM simply cannot be used with a 64 bits long number with Wireshark 1.12.x. What you could use instead if proto_tree_add_uint64_format_value() function.</p></div><div id="comment-43096-info" class="comment-info"><span class="comment-age">(12 Jun '15, 06:00)</span> Pascal Quantin</div></div></div><div id="comment-tools-43084" class="comment-tools"></div><div class="clear"></div><div id="comment-43084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

