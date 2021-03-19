+++
type = "question"
title = "[closed] How to format the value_string"
description = '''Hi, Iam developing a dissector  i have used value string   static const value_string fwd_type_vals[]={  {0x00, &quot;undefined&quot; },  { 0x01, &quot; Info&quot; },  { 0, NULL }};   and   { &amp;amp;hf_type,  { &quot;Com Type &quot;, &quot;com_type&quot;,FT_UINT8, BASE_HEX, VALS(fwd_type_vals), 0x80, NULL, HFILL }  },  Iam using Bitmask 0x80...'''
date = "2014-07-04T03:23:00Z"
lastmod = "2014-07-04T03:23:00Z"
weight = 34400
keywords = [ "value_string", "format" ]
aliases = [ "/questions/34400" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to format the value\_string](/questions/34400/how-to-format-the-value_string)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34400-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Iam developing a dissector</p><p>i have used value string</p><pre><code>          static const value_string fwd_type_vals[]={
           {0x00,    &quot;undefined&quot; },
           { 0x01,    &quot; Info&quot; },
            { 0, NULL }};

       and 
         { &amp;hf_type,
    { &quot;Com Type &quot;, &quot;com_type&quot;,FT_UINT8, BASE_HEX, VALS(fwd_type_vals), 0x80, NULL, HFILL }
    },</code></pre><p>Iam using Bitmask 0x80 here and when i use to call this i get the output as</p><pre><code>               1... .... = com Type : 0x01 (info)</code></pre><p>How can i format and display only com Type : 0x01 (info) how to trim/remove this</p><pre><code>              1... ....=</code></pre><p>Please help!</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">value_string format</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '14, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p>umar<br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 04 Jul '14, 03:47</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-34400" class="comments-container"><span id="34402"></span><div id="comment-34402" class="comment"><div id="post-34402-score" class="comment-score"></div><div class="comment-text"><p>This seems to be the same as your other questions:<br />
</p><ul><li><a href="http://ask.wireshark.org/questions/33229/how-to-dissect-bit-by-bit-and-display">http://ask.wireshark.org/questions/33229/how-to-dissect-bit-by-bit-and-display</a></li><li><a href="http://ask.wireshark.org/questions/33335/dissector-tree-display-format">http://ask.wireshark.org/questions/33335/dissector-tree-display-format</a></li></ul><p>Asking the same question multiple times isn't helpful for other users.</p></div><div id="comment-34402-info" class="comment-info"><span class="comment-age">(04 Jul '14, 03:47)</span> grahamb ♦</div></div></div><div id="comment-tools-34400" class="comment-tools"></div><div class="clear"></div><div id="comment-34400-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by grahamb 04 Jul '14, 03:47

</div>

</div>

</div>

