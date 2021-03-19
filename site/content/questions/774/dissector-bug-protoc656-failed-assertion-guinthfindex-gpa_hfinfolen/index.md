+++
type = "question"
title = "dissector bug: proto.c:656: failed assertion &quot;(guint)hfindex &lt; gpa_hfinfo.len&quot;"
description = '''I search on Google about this failure. Mostly of them suggested to check whether there were variables that were used without going into the hf array.  But I checked carefully both with checkhf.pl and manually, no variable were used in such way. Another thing is that my dissector was originally built...'''
date = "2010-11-01T23:27:00Z"
lastmod = "2010-11-16T08:59:00Z"
weight = 774
keywords = [ "failed", "dissector", "bug", "assertion" ]
aliases = [ "/questions/774" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [dissector bug: proto.c:656: failed assertion "(guint)hfindex &lt; gpa\_hfinfo.len"](/questions/774/dissector-bug-protoc656-failed-assertion-guinthfindex-gpa_hfinfolen)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-774-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I search on Google about this failure. Mostly of them suggested to check whether there were variables that were used without going into the hf array.</p><p>But I checked carefully both with checkhf.pl and manually, no variable were used in such way.</p><p>Another thing is that my dissector was originally built as a plugin DLL with 0.99.5 wireshark. Now we are using wireshark 1.2.x(for the one I use now is 1.2.11), but in 1.2.x, there was a built-in wireshark dissector for my protocol(FMP) package. The way I tried to solve this problem was I copied the entire plugin source code and modified to build with 1.2.x. The dissector(dll) work with 1.2.x because I changed the protocol register name. I saw my dll recognized most of the packet except two packets, which displyed the error: dissector bug: proto.c:656: failed assertion "(guint)hfindex &lt; gpa_hfinfo.len".</p><p>Any body has any suggestion to what happened or where the problem might be? I can't paste code at this moment because of a lot of reason.</p><p>Thanks in advance for your input.</p></div><div id="question-tags" class="tags-container tags">failed dissector bug assertion</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '10, 23:27</strong></p><img src="https://secure.gravatar.com/avatar/3b8a4663b3a2abf720c614f2eeee2fca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alvan&#39;s gravatar image" /><p>alvan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alvan has no accepted answers">0%</span></p></div></div><div id="comments-container-774" class="comments-container"></div><div id="comment-tools-774" class="comment-tools"></div><div class="clear"></div><div id="comment-774-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="775"></span>

<div id="answer-container-775" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-775-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Load the offending capture, try to work out which of the fields cause the error, then go back to your code to verify that that field has indeed been allocated. Use your debugger to make sure.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '10, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-775" class="comments-container"><span id="776"></span><div id="comment-776" class="comment"><div id="post-776-score" class="comment-score"></div><div class="comment-text"><p>The line with a "*" is the field that cause the error. However, I checked carefully in my code, they are indeed allocated:</p><blockquote><ul><li>offset = dissect_rpc_uint64(tvb, tree, hf_fmp2_blockIndex, offset);</li></ul></blockquote><p>This is the line declaring the variable:</p><blockquote><p>static int hf_fmp2_blockIndex = -1;</p></blockquote><p>This is entry in hf array:</p><blockquote><p>{ &amp;hf_fmp2_blockIndex, { "Block Index", "fmp2.offset", FT_UINT64, BASE_DEC, NULL, 0, "Block Index", HFILL }},</p></blockquote><p>Anything wrong? I really didn't see anything wrong. Sorry, I mean to paste more code, but it's too hard to paste code in the reply text box because it doesn't display code in well format.</p></div><div id="comment-776-info" class="comment-info"><span class="comment-age">(02 Nov '10, 00:20)</span> alvan</div></div><span id="777"></span><div id="comment-777" class="comment"><div id="post-777-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your quick response. See my addition below.</p></div><div id="comment-777-info" class="comment-info"><span class="comment-age">(02 Nov '10, 00:21)</span> alvan</div></div><span id="778"></span><div id="comment-778" class="comment"><div id="post-778-score" class="comment-score"></div><div class="comment-text"><p>By the way, the code(built as dll) worked fine with 0.99.5 wireshark. When porting to 1.2.x, I didn't change anything except some Makefile to adapt to new building process. The whole building process with 1.2.x didn't show any errors.<br />
</p></div><div id="comment-778-info" class="comment-info"><span class="comment-age">(02 Nov '10, 00:30)</span> alvan</div></div></div><div id="comment-tools-775" class="comment-tools"></div><div class="clear"></div><div id="comment-775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="973"></span>

<div id="answer-container-973" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-973-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello,</p><p>I think you know this is a classical error when some hf proto fields are missing in the hf array since you ran the checkhf.pl script.</p><p>I got exactly the same error on my custom dissector when upgrading from version 1.2.x to 1.4.x and it took me days to find out out what was wrong...</p><p>Indeed the error happened in my dissector during UDP reassembling, more precisely when I was running the <em>process_reassembled_data</em> function.</p><p>The cause was that in the <em>fragment_items</em> structure, the <em>hf_xxx_reassembled_length</em> field was missing. It was working fine until version 1.2.x but did not work after version 1.4.x</p><p>I think checkhf.pl script did not catch it because the reassembling hf variables are initialised in another sources files (proto.c).</p><p>Tell me if it helps !</p><p>Regards,</p><p>Emmanuel</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '10, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/2282d6ca42253cbf6aa80c00be6af1b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manux&#39;s gravatar image" /><p>manux<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manux has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Nov '10, 10:33</p></div></div><div id="comments-container-973" class="comments-container"><span id="983"></span><div id="comment-983" class="comment"><div id="post-983-score" class="comment-score"></div><div class="comment-text"><p>Indeed, the root cause was revision 31767 of reassemble.h (2 Feb 2010) : <em>Introduce "Reassembled length" filter element for all protocols doing reassembly.</em></p><pre><code>typedef struct _fragment_items {
    gint    *ett_fragment;
    gint    *ett_fragments;

    int *hf_fragments;
    int *hf_fragment;
    int *hf_fragment_overlap;
    int *hf_fragment_overlap_conflict;
    int *hf_fragment_multiple_tails;
    int *hf_fragment_too_long_fragment;
    int *hf_fragment_error;
    int *hf_reassembled_in;
    int *hf_reassembled_length;

    const char  *tag;
} fragment_items;</code></pre></div><div id="comment-983-info" class="comment-info"><span class="comment-age">(17 Nov '10, 01:57)</span> manux</div></div></div><div id="comment-tools-973" class="comment-tools"></div><div class="clear"></div><div id="comment-973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

