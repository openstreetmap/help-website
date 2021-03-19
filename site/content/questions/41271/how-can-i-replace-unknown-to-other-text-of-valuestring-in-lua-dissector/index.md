+++
type = "question"
title = "How can I replace &quot;Unknown&quot; to other text of valuestring in Lua dissector"
description = '''I made dissector in Lua as following. And decorded as &quot;MYPROTO&quot; TCP payload. When the first byte of TCP palyload is 0x02, dissector shows &quot;First byte: Two (2)&quot;. But the first byte is not 0x02 (for example 0x01), dissector shows &quot;First byte: Unknown (1)&quot;. I want to show &quot;First byte: Not two (1)&quot;. How...'''
date = "2015-04-07T20:55:00Z"
lastmod = "2015-04-09T17:03:00Z"
weight = 41271
keywords = [ "lua", "dissector", "unknown" ]
aliases = [ "/questions/41271" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I replace "Unknown" to other text of valuestring in Lua dissector](/questions/41271/how-can-i-replace-unknown-to-other-text-of-valuestring-in-lua-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41271-score" class="post-score" title="current number of votes">0</div><span id="post-41271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I made dissector in Lua as following. And decorded as "MYPROTO" TCP payload. When the first byte of TCP palyload is 0x02, dissector shows "First byte: Two (2)". But the first byte is not 0x02 (for example 0x01), dissector shows "First byte: Unknown (1)". I want to show "First byte: Not two (1)". How can I replace default string ("Unknown") to other string?</p><pre><code>local myproto = Proto(&quot;myproto&quot;, &quot;My Protocol&quot;)
myproto.fields = {ProtoField.uint8(&quot;myproto.firstbyte&quot;, &quot;First byte&quot;, base.DEC, {[2] = &quot;Two&quot;})}
function myproto.dissector (buf, pkt, root)
   local t = root:add(myproto, buf())
   t:add(myproto.fields[1], buf(0, 1))
end
DissectorTable.get(&quot;tcp.port&quot;):add(10000, myproto)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-unknown" rel="tag" title="see questions tagged &#39;unknown&#39;">unknown</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '15, 20:55</strong></p><img src="https://secure.gravatar.com/avatar/9226a7d863f40da740476e5f59e04853?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cosmos&#39;s gravatar image" /><p><span>cosmos</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cosmos has no accepted answers">0%</span></p></div></div><div id="comments-container-41271" class="comments-container"></div><div id="comment-tools-41271" class="comment-tools"></div><div class="clear"></div><div id="comment-41271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41309"></span>

<div id="answer-container-41309" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41309-score" class="post-score" title="current number of votes">1</div><span id="post-41309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can add your own string like this</p><p><code>local myproto = Proto("myproto", "My Protocol") function myproto.dissector (buf, pkt, root)    local t = root:add(myproto, buf())    local s1 = "Mystring"    t:add(buf(0, 1),string.format("First Byte: %s %d",s1,buf(0,1):uint())) end local tcp_table = DissectorTable.get("tcp.port") tcp_table:add(8443, myproto) tcp_table:add(61639, myproto)</code></p><p><code>You can also append the text after buf like this t:add(buf(0, 1),string.format("First Byte: %s %d",s1,buf(0,1):uint())):append_text("Demo")</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '15, 22:49</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p><span>ankit</span><br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></div></div><div id="comments-container-41309" class="comments-container"><span id="41311"></span><div id="comment-41311" class="comment"><div id="post-41311-score" class="comment-score"></div><div class="comment-text"><p>Do you want to say that I should not use valuestring feature of ProtoFiled()?</p></div><div id="comment-41311-info" class="comment-info"><span class="comment-age">(08 Apr '15, 23:22)</span> <span class="comment-user userinfo">cosmos</span></div></div><span id="41319"></span><div id="comment-41319" class="comment"><div id="post-41319-score" class="comment-score">1</div><div class="comment-text"><p>if you want to use valuestring then you have to create each and every entry of first byte of TCP payload of each and every frame in your pcap file. like this myproto.fields = {ProtoField.uint8("myproto.firstbyte","1st byte",base.DEC,{ [0]="zero", [1]="one", [2]="two", })}</p></div><div id="comment-41319-info" class="comment-info"><span class="comment-age">(09 Apr '15, 04:29)</span> <span class="comment-user userinfo">ankit</span></div></div><span id="41336"></span><div id="comment-41336" class="comment"><div id="post-41336-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much. I understand.</p></div><div id="comment-41336-info" class="comment-info"><span class="comment-age">(09 Apr '15, 17:03)</span> <span class="comment-user userinfo">cosmos</span></div></div></div><div id="comment-tools-41309" class="comment-tools"></div><div class="clear"></div><div id="comment-41309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

