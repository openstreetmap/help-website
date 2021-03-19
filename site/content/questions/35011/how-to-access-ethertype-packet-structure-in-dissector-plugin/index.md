+++
type = "question"
title = "How to access Ethertype packet structure in Dissector plugin ?"
description = '''Hi everyone, I am modifying a dissector plugin which used to work with wireshark version 1.10. But when I try to compile it wireshark 1.12-rc2 source code, it throws error regarding a missing structure element:  pinfo-&amp;gt;ethertype  Figured out that this element is no longer applicable for newer ver...'''
date = "2014-07-30T13:20:00Z"
lastmod = "2014-07-31T06:29:00Z"
weight = 35011
keywords = [ "etype", "ethertype", "dissector", "wireshark-1.12", "pinfo" ]
aliases = [ "/questions/35011" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to access Ethertype packet structure in Dissector plugin ?](/questions/35011/how-to-access-ethertype-packet-structure-in-dissector-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35011-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I am modifying a dissector plugin which used to work with wireshark version 1.10.</p><p>But when I try to compile it wireshark 1.12-rc2 source code, it throws error regarding a missing structure element:</p><pre><code>    pinfo-&gt;ethertype</code></pre><p>Figured out that this element is no longer applicable for newer versions of wireshark. But I need to access the ethernet type from the packet I received. But the problem is, I am given the pointer buffer in the dissector just after the ethernet header. So cant use tvb_get_ptr.</p><p>I used the following 2 functions to add my dissector:</p><pre><code>dissector_add_uint(&quot;ethertype&quot;, 0xABCD, xmax_handle);
dissector_add_uint(&quot;ethertype&quot;, 0xBDEF,_XMAX_UPLINK, xmax_handle);</code></pre><p>My dissector is working properly with the above 2 packet types. But I need to access those 2 packet types (0xABCD and 0xBDEF) to do some internal processing.</p><p>So I went back to packet-ethertype.c to find out whats going on. Seems like this structure contains the packetype:</p><pre><code>   ethertype_data-&gt;etype</code></pre><p>Can I pass this structure element to my dissector? I tried it, but gives segment fault.</p><p>Is there any other way to do it?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">etype ethertype dissector wireshark-1.12 pinfo</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '14, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/c0a8a56588e89a1efbe6c05ff5adc1e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kazi_hasan&#39;s gravatar image" /><p>kazi_hasan<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kazi_hasan has no accepted answers">0%</span></p></div></div><div id="comments-container-35011" class="comments-container"></div><div id="comment-tools-35011" class="comment-tools"></div><div class="clear"></div><div id="comment-35011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35014"></span>

<div id="answer-container-35014" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35014-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Create two handles (one for each of the ethertypes) each pointing to a different function and do <code>dissector_add_uint</code> separately for each ether type using the corresponding handle; Each of the separate functions can then call the common dissector code with a flag indicating the ethertype.</p><p>E.g., xmax_handle_abcd and xmax_handle_bdef</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '14, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jul '14, 13:35</p></div></div><div id="comments-container-35014" class="comments-container"><span id="35015"></span><div id="comment-35015" class="comment"><div id="post-35015-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. Actually I was thinking about this solution, but is there any way to access the packet type from the dissector itself?</p></div><div id="comment-35015-info" class="comment-info"><span class="comment-age">(30 Jul '14, 13:36)</span> kazi_hasan</div></div></div><div id="comment-tools-35014" class="comment-tools"></div><div class="clear"></div><div id="comment-35014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35030"></span>

<div id="answer-container-35030" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35030-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>A better/easier way is to use <code>pinfo-&gt;match_uint</code>. When your dissector is called because it is registered for a particular uint dissector-table value then this field is filled in with the matching value.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '14, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-35030" class="comments-container"></div><div id="comment-tools-35030" class="comment-tools"></div><div class="clear"></div><div id="comment-35030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

