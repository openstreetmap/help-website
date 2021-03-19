+++
type = "question"
title = "Are Lua dissector fields filterable?"
description = '''I&#x27;m wondering how to get the fields declared in a Lua dissector searchable in the filter bar. When trying to declare fields the same way as in various tutorials/samples, despite the fact that the dissector works fine, packets are recognized and decoded, the fields are unavailable to search. Example ...'''
date = "2013-12-06T06:17:00Z"
lastmod = "2013-12-11T02:02:00Z"
weight = 27868
keywords = [ "lua", "dissector", "fields" ]
aliases = [ "/questions/27868" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Are Lua dissector fields filterable?](/questions/27868/are-lua-dissector-fields-filterable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27868-score" class="post-score" title="current number of votes">0</div><span id="post-27868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm wondering how to get the fields declared in a Lua dissector searchable in the filter bar. When trying to declare fields the same way as in various tutorials/samples, despite the fact that the dissector works fine, packets are recognized and decoded, the fields are unavailable to search.</p><p>Example :</p><pre><code>p_myproto = Proto (&quot;myproto&quot;,&quot;My Protocol&quot;)
local f_command = ProtoField.uint16(&quot;myproto.command&quot;, &quot;Command&quot;, base.HEX)
local f_data = ProtoField.string(&quot;myproto.data&quot;, &quot;Data&quot;, FT_STRING)

p_myproto.fields = {f_command,f_data}

myproto.f_data == in the filter bar gives &quot;myproto.f_data isn&#39;t a valid display filter&quot; &quot;myproto.f_data is neither a field nor a protocol name&quot;</code></pre><p>Are custom fields supposed to be searchable?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '13, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/e4e8bc4618a9948a893ae407b22e8160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lepolac&#39;s gravatar image" /><p><span>lepolac</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lepolac has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Dec '13, 13:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-27868" class="comments-container"></div><div id="comment-tools-27868" class="comment-tools"></div><div class="clear"></div><div id="comment-27868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27880"></span>

<div id="answer-container-27880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27880-score" class="post-score" title="current number of votes">1</div><span id="post-27880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You get the error message "myproto.f_data is neither a field nor a protocol name" because you have used a different string for your field's filter string. Try <code>myproto.data</code> in stead.</p><p>In the line <code>local f_data = ProtoField.string("myproto.data", "Data", FT_STRING)</code>, it is actually the first argument to <code>ProtoField.string</code> that determines the filter string (i.e. <code>"myproto.data"</code>), not the name of the variable into which it is stored (i.e. <code>local f_data</code>).<br />
You could just have easily typed the following, and it would still use <code>myproto.data</code> as the filter string:</p><pre><code>local some_data_field_with_a_long_name = ProtoField.string(&quot;myproto.data&quot;, &quot;Data&quot;, FT_STRING)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '13, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span> </br></p></div></div><div id="comments-container-27880" class="comments-container"><span id="27945"></span><div id="comment-27945" class="comment"><div id="post-27945-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Thanks for answering this. I tried to rename the field but still get the error. Below code for the sake of example :</p><pre><code>p_myproto = Proto (&quot;myproto&quot;,&quot;My Protocol&quot;)
local f_command = ProtoField.uint16(&quot;myproto.command&quot;, &quot;Command&quot;, base.HEX)
local f_data = ProtoField.string(&quot;testdata&quot;, &quot;Data&quot;, FT_STRING)
local f_debug = ProtoField.uint8(&quot;myproto.debug&quot;, &quot;Debug&quot;)

p_myproto.fields = {f_command,f_data,f_debug}

function p_myproto.dissector (buf, pkt, root)

  if buf:len() == 0 then return end
  pkt.cols.protocol = p_myproto.name
  subtree = root:add(p_myproto, buf(0))
  subtree:add(f_command, buf(0,2)):append_text(&quot; [Command text]&quot;)
  subtree:append_text(&quot;, Command details here or in the tree below&quot;)

  if f_debug then
    subtree:add(f_debug, buf:len())
  end
end

function p_myproto.init()
end

local tcp_dissector_table = DissectorTable.get(&quot;tcp.port&quot;)
dissector = tcp_dissector_table:get_dissector(80)
tcp_dissector_table:add(80, p_myproto)</code></pre></div><div id="comment-27945-info" class="comment-info"><span class="comment-age">(09 Dec '13, 03:08)</span> <span class="comment-user userinfo">lepolac</span></div></div><span id="27957"></span><div id="comment-27957" class="comment"><div id="post-27957-score" class="comment-score"></div><div class="comment-text"><p>In this code, you haven't added the <code>f_data</code> field to any part of the tree. You have, however, added the <code>f_command</code> field, so you should be able to filter on <em>myproto.command</em>. Have you looked at the examples at <a href="http://wiki.wireshark.org/Lua/Examples">http://wiki.wireshark.org/Lua/Examples</a> ?</p></div><div id="comment-27957-info" class="comment-info"><span class="comment-age">(09 Dec '13, 10:35)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="27996"></span><div id="comment-27996" class="comment"><div id="post-27996-score" class="comment-score"></div><div class="comment-text"><p>Hi, Sorry, didn't catch that one.. This is not my actual dissector, was just trying to quickly give an example. myproto.command doesn't work either, I still get myproto.command isn't a valid display filter. By the way, I tested dozens of various dissectors I found, including the simplest wiki examples, and none of them allow me to access field in the filter. Maybe I'm doing something the wrong way...</p></div><div id="comment-27996-info" class="comment-info"><span class="comment-age">(11 Dec '13, 02:02)</span> <span class="comment-user userinfo">lepolac</span></div></div></div><div id="comment-tools-27880" class="comment-tools"></div><div class="clear"></div><div id="comment-27880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

