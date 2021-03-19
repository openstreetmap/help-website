+++
type = "question"
title = "Lua Dissector for the whole Frame"
description = '''Hi  I am new in this community and I understood how to create a dissector for a tcp/udp packet in LUA.  But I want to create a dissector in LUA which dissect the whole frame because I want to handle the MAC address. I have searched in different topics and I didn&#x27;t find what I want or I cannot apply ...'''
date = "2017-05-03T07:55:00Z"
lastmod = "2017-07-08T11:53:00Z"
weight = 61207
keywords = [ "lua", "mac", "dissector", "ethernet" ]
aliases = [ "/questions/61207" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Lua Dissector for the whole Frame](/questions/61207/lua-dissector-for-the-whole-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61207-score" class="post-score" title="current number of votes">0</div><span id="post-61207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am new in this community and I understood how to create a dissector for a tcp/udp packet in LUA. But I want to create a dissector in LUA which dissect the whole frame because I want to handle the MAC address. I have searched in different topics and I didn't find what I want or I cannot apply what I found. May you have an advice to help me ?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '17, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/bfbe4ff8fdfdcc1cd37d87c6bd1df677?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yassbouc&#39;s gravatar image" /><p><span>yassbouc</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yassbouc has no accepted answers">0%</span></p></div></div><div id="comments-container-61207" class="comments-container"></div><div id="comment-tools-61207" class="comment-tools"></div><div class="clear"></div><div id="comment-61207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62618"></span>

<div id="answer-container-62618" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62618-score" class="post-score" title="current number of votes">0</div><span id="post-62618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to fetch values from other dissectors you can try fetch using a Field. For MAC addresses maybe something like this:</p><pre><code>eth_src_f = Field.new(&quot;eth.src&quot;)
eth_dst_f = Field.new(&quot;eth.dst&quot;)</code></pre><p>Have a look in the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Field.html">Field</a> documentation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '17, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/193a8e6acdc05d13fb1e59fbe4eaba1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stig&#39;s gravatar image" /><p><span>stig ♦</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stig has no accepted answers">0%</span></p></div></div><div id="comments-container-62618" class="comments-container"></div><div id="comment-tools-62618" class="comment-tools"></div><div class="clear"></div><div id="comment-62618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

