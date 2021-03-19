+++
type = "question"
title = "Lua tostring(tvb(offset,8):le_int64()) returns a Big Endian result"
description = '''Hi, I am trying to use lua tvb_range:le_uint64() but it does not return the correct value when converted from userdata to a lua integer? It seems to always return tvb_range:int64() The captured buffer contains; &quot;aa c8 74 91 ba d2 4c 00&quot; local f.my_proto.fields f.my_int64 = ProtoField.int64(&quot;my_proto...'''
date = "2011-11-13T19:48:00Z"
lastmod = "2011-11-13T19:48:00Z"
weight = 7407
keywords = [ "lua", "le_int64" ]
aliases = [ "/questions/7407" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua tostring(tvb(offset,8):le\_int64()) returns a Big Endian result](/questions/7407/lua-tostringtvboffset8le_int64-returns-a-big-endian-result)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7407-score" class="post-score" title="current number of votes">2</div><span id="post-7407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to use lua tvb_range:le_uint64() but it does not return the correct value when converted from userdata to a lua integer? It seems to always return tvb_range:int64()</p><p>The captured buffer contains; "aa c8 74 91 ba d2 4c 00"</p><pre><code>local f.my_proto.fields
f.my_int64 = ProtoField.int64(&quot;my_proto.my_int64&quot;, &quot;My Int 64&quot;, base.Dec)
tree:add_le(f.mt_int64, tvb(0,8))</code></pre><p>This code correctly dissects the bytes and displays</p><p>"My Int 64: 216237969109738"</p><p>Then I try and convert the range from userdata to a lua integer</p><pre><code>print (tvb(0,8):le_int64(), tvb(0,8):int64())
&gt;-6140529922666247168 -6140529922666247168

print (tostring(tvb(0,8):le_int64()), tostring(tvb(0,8):int64()) 
&gt;-6140529922666247168 -6140529922666247168</code></pre><p>But it should return</p><pre><code>print (tvb(0,8):le_int64(), tvb(0,8):int64())
&gt;216237969109738  -6140529922666247168</code></pre><p>Is there a bug in the le_uint64() function? I couldn't find it in Bugzilla.</p><p>Thanks</p><p>OS: Centos 5.3 Wireshark 1.4.1 Lua 5.1</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-le_int64" rel="tag" title="see questions tagged &#39;le_int64&#39;">le_int64</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '11, 19:48</strong></p><img src="https://secure.gravatar.com/avatar/e9a64b38c3c80a882aa3c808b71cccbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrb&#39;s gravatar image" /><p><span>mrb</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrb has no accepted answers">0%</span></p></div></div><div id="comments-container-7407" class="comments-container"></div><div id="comment-tools-7407" class="comment-tools"></div><div class="clear"></div><div id="comment-7407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

