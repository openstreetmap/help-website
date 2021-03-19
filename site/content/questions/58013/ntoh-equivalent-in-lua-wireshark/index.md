+++
type = "question"
title = "ntoh equivalent in lua wireshark"
description = '''Hi, I am a little new to writing a dissector using lua. So, please bare an amateur. I am trying to implement a dissector for one of our projects. Since my host order(currently) is little Endian, I am using methods like &quot;tree:add_le()&quot;, &quot;tvbuf:range(offset,2):le_uint()&quot;, etc. However, i would want to...'''
date = "2016-12-12T01:48:00Z"
lastmod = "2017-01-10T23:05:00Z"
weight = 58013
keywords = [ "lua", "wireshark" ]
aliases = [ "/questions/58013" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [ntoh equivalent in lua wireshark](/questions/58013/ntoh-equivalent-in-lua-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58013-score" class="post-score" title="current number of votes">0</div><span id="post-58013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am a little new to writing a dissector using lua. So, please bare an amateur.</p><p>I am trying to implement a dissector for one of our projects. Since my host order(currently) is little Endian, I am using methods like "tree:add_le()", "tvbuf:range(offset,2):le_uint()", etc.</p><p>However, i would want to run a command, which is equivalent to "ntohl()"( method used in C/C++) at the beginning itself, which would eliminate any errors with byte ordering during dissection.</p><p>Please help.</p><p>Thanks, Spark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '16, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/6738d87ca3018fb30201f0c478248cc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spark&#39;s gravatar image" /><p><span>spark</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spark has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Dec '16, 23:00</strong> </span></p></div></div><div id="comments-container-58013" class="comments-container"></div><div id="comment-tools-58013" class="comment-tools"></div><div class="clear"></div><div id="comment-58013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58501"></span>

<div id="answer-container-58501" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58501-score" class="post-score" title="current number of votes">1</div><span id="post-58501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="spark has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should be probably just use <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Tree.html#lua_fn_treeitem_add_packet_field_protofield___tvbrange___encoding___label__"><code>treeitem:add_packet_field</code></a> with an encoding of <code>ENC_LITTLE_ENDIAN</code>. If the endianness may change, use a variable for the encoding and set it appropriately (that would allow you to just set it once rather than having to remember to do it for every field).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '17, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-58501" class="comments-container"><span id="58655"></span><div id="comment-58655" class="comment"><div id="post-58655-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff!</p></div><div id="comment-58655-info" class="comment-info"><span class="comment-age">(10 Jan '17, 23:05)</span> <span class="comment-user userinfo">spark</span></div></div></div><div id="comment-tools-58501" class="comment-tools"></div><div class="clear"></div><div id="comment-58501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

