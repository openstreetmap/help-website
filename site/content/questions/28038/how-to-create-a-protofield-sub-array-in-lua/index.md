+++
type = "question"
title = "How to create a Protofield sub array in Lua"
description = '''Hi, Given the following example: local f= mycoolprotocol.fields f.Length = ProtoField.uint32(&quot;MCP.Length&quot;,&quot;Length&quot;,base.DEC) f.MsgType = ProtoField.uint16(&quot;MCP.MsgType&quot;,&quot;MsgType&quot;,base.DEC)  I have declared 2 Protofields. But imagine I have a repeating group or an array of items: And the message body...'''
date = "2013-12-12T01:14:00Z"
lastmod = "2013-12-12T06:02:00Z"
weight = 28038
keywords = [ "lua", "dissector", "protofield", "plugin" ]
aliases = [ "/questions/28038" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to create a Protofield sub array in Lua](/questions/28038/how-to-create-a-protofield-sub-array-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28038-score" class="post-score" title="current number of votes">0</div><span id="post-28038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Given the following example:</p><pre><code>local f= mycoolprotocol.fields
f.Length = ProtoField.uint32(&quot;MCP.Length&quot;,&quot;Length&quot;,base.DEC)
f.MsgType = ProtoField.uint16(&quot;MCP.MsgType&quot;,&quot;MsgType&quot;,base.DEC)</code></pre><p>I have declared 2 Protofields. But imagine I have a repeating group or an array of items:</p><p>And the message body looks like so:</p><pre><code>struct person
{
  int16 age;
  string name;
}
person[] p = new person[2];</code></pre><p>Ideally, I would like to create a subtree in Wireshark for that group</p><pre><code>+ Persons
 + Person1
    name
    age
 + Person2
    name
    age</code></pre><p>The problem is I don't know how to structure this in Lua. This declares 2 protofields:</p><pre><code>f.name = Protofield.string(&quot;MCP.name&quot;,&quot;name&quot;,&quot;Text&quot;)
f.age = ProtoField.uint16(&quot;MCP.age&quot;,&quot;age&quot;,base.DEC)</code></pre><p>But I'd like to create a dynamic array of the group instead, so I can do:</p><pre><code>subtree:add_le( f[0].name, buffer(x,y))</code></pre><p>So, is there a <code>Protofield.ProtoFieldArray</code>? Is it possible? Any other ideas are welcome.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-protofield" rel="tag" title="see questions tagged &#39;protofield&#39;">protofield</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '13, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/10ba80b2d73f068e916ba35852a8a436?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lews%20Therin&#39;s gravatar image" /><p><span>Lews Therin</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lews Therin has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Dec '13, 01:15</strong> </span></p></div></div><div id="comments-container-28038" class="comments-container"></div><div id="comment-tools-28038" class="comment-tools"></div><div class="clear"></div><div id="comment-28038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28052"></span>

<div id="answer-container-28052" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28052-score" class="post-score" title="current number of votes">0</div><span id="post-28052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Lews Therin has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It turns out I can reuse the same fields to build the tree.</p><p>So in pseudocode:</p><pre><code>begin loop
  subtree= mainsubtree:add(a,buffer())
  subtree:add(f.name, buffer(x,y))
  subtree:add(f.age, buffer(x+name.length,y))
end</code></pre><p>So <code>f.name</code> <code>f.age</code> doesn't get overwritten by a newer value. I guess it is just a placeholder for the <code>ProtoField</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '13, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/10ba80b2d73f068e916ba35852a8a436?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lews%20Therin&#39;s gravatar image" /><p><span>Lews Therin</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lews Therin has one accepted answer">100%</span></p></div></div><div id="comments-container-28052" class="comments-container"></div><div id="comment-tools-28052" class="comment-tools"></div><div class="clear"></div><div id="comment-28052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

