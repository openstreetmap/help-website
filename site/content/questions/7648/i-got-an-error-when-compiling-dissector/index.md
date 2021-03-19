+++
type = "question"
title = "I got an error when compiling dissector."
description = '''Hi, I had followed the examples (9.1,9.2 and 9.3) given in the following link &quot;http://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html&quot; to dissect my protocol but i got error when i compiling it on my windows.My protocol name is &quot;TLV&quot;. Please Help me to fix this error.  error:  packet-tlv....'''
date = "2011-11-26T06:04:00Z"
lastmod = "2011-11-26T06:21:00Z"
weight = 7648
keywords = [ "dissector", "plugin" ]
aliases = [ "/questions/7648" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I got an error when compiling dissector.](/questions/7648/i-got-an-error-when-compiling-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7648-score" class="post-score" title="current number of votes">0</div><span id="post-7648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I had followed the examples (9.1,9.2 and 9.3) given in the following link "<a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html">http://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html</a>" to dissect my protocol but i got error when i compiling it on my windows.My protocol name is "TLV".</p><p>Please Help me to fix this error.</p><hr /><p>error:</p><hr /><p>packet-tlv.c(29) : error C2065: 'dissect_tlv' : undeclared identifier</p><p>packet-tlv.c(29) : warning C4047: 'function' : 'dissector_t' differs in levels o f indirection from 'int'</p><p>packet-tlv.c(29) : warning C4024: 'create_dissector_handle' : different types fo r formal and actual parameter 1</p><p>packet-tlv.c(30) : warning C4013: 'dissector_add_unit' undefined; assuming exter n returning int</p><p>plugin.c</p><p>Generating Code... NMAKE : fatal error U1077: '"C:Program FilesMicrosoft Visual Studio 9.0VCBIN cl.EXE"' : return code '0x2' Stop.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '11, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/01febacc45af8ecf743c4f575d428326?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JK7&#39;s gravatar image" /><p><span>JK7</span><br />
<span class="score" title="31 reputation points">31</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JK7 has no accepted answers">0%</span></p></div></div><div id="comments-container-7648" class="comments-container"></div><div id="comment-tools-7648" class="comment-tools"></div><div class="clear"></div><div id="comment-7648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7649"></span>

<div id="answer-container-7649" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7649-score" class="post-score" title="current number of votes">1</div><span id="post-7649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The errors look like simple errors in your source which you'll need to track down and fix. :)</p><p>For example: I expect <code>dissector_add_unit</code> should probably be <code>dissector_add_uint</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '11, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-7649" class="comments-container"></div><div id="comment-tools-7649" class="comment-tools"></div><div class="clear"></div><div id="comment-7649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

