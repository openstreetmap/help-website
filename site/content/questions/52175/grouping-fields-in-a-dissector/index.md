+++
type = "question"
title = "Grouping fields in a dissector"
description = '''Hello, I am writing a dissector in LUA and would like to group fields as per this image:  How do I do it?'''
date = "2016-05-03T06:37:00Z"
lastmod = "2016-05-03T06:54:00Z"
weight = 52175
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/52175" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Grouping fields in a dissector](/questions/52175/grouping-fields-in-a-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52175-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am writing a dissector in LUA and would like to group fields as per this image:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_3aJwg4a.JPG" alt="Header grouping in UDP dissector" /></p><p>How do I do it?</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '16, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/280be066f1979e3cdcdf5782d4863850?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnnymnemonic&#39;s gravatar image" /><p>johnnymnemonic<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnnymnemonic has no accepted answers">0%</span></p></img></div></div><div id="comments-container-52175" class="comments-container"></div><div id="comment-tools-52175" class="comment-tools"></div><div class="clear"></div><div id="comment-52175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52176"></span>

<div id="answer-container-52176" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52176-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You would add a named subtree and items into it, as in this simplified excerpt from another dissector:</p><pre><code>my_subtree=tree:add(&#39;User-Name dissection&#39;)
my_subtree:add(user,buffer:range(0,10))
my_subtree:add(host,buffer:range(11))</code></pre><p>The result will then be</p><pre><code>[-] User-Name dissection
      user_field_description: user_field_value
      host_field_description: host_field_value</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '16, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52176" class="comments-container"><span id="52183"></span><div id="comment-52183" class="comment"><div id="post-52183-score" class="comment-score"></div><div class="comment-text"><p>@sindy - thanks, that works. However, wehn I click on such a field ("User-Name dissection" in your example) it doesn't highlight the range that the sub-fields cover.</p></div><div id="comment-52183-info" class="comment-info"><span class="comment-age">(03 May '16, 10:00)</span> johnnymnemonic</div></div><span id="52185"></span><div id="comment-52185" class="comment"><div id="post-52185-score" class="comment-score"></div><div class="comment-text"><p>That's because the field in the original tree in my example is a text item.</p><p>As said, I've used a quote from a dissector I happened to have open in text editor. Like many other methods of the Lua API, <a href="https://wiki.wireshark.org/LuaAPI/TreeItem#treeitem:add.28proto_field_.5B.2Ctvbrange.5D_.5B.2Cvalue_.5B.2Ctext1_.5B.2Ctext2.5D_....5D_.5D.29">treeitem:add</a> can handle several variants of parameters (some of them even not documented at all places), so if you use just a text label as its single parameter, like I did at that place, there is nothing related to that text label in the packet data, so there is nothing to be highlighted in the raw data pane.</p><p>You may definitely declare another protocol field like "emailaddr" which spans the complete portion of the buffer, so the code above would then change to</p><pre><code>my_subtree=tree:add(emailaddr,buffer:range(0))
my_subtree:add(user,buffer:range(0,10))
my_subtree:add(host,buffer:range(11))</code></pre><p>and if <code>emailaddr, user, host</code> have been previously properly defined as protocol fields, like</p><pre><code>local emailaddr = ProtoField.string(&quot;my_proto.e-mail&quot;,&quot;complete e-mail address&quot;)
local user = ProtoField.string(&quot;my_proto.e-mail.user&quot;,&quot;user part&quot;)
local host = ProtoField.string(&quot;my proto.e-mail.host&quot;,&quot;host part&quot;)
my_proto.fields = {emailaddr,user,host}</code></pre><p>then clicking on any of the three items will highlight the corresponding bytes in the raw data pane.</p><p>To say it all, in my original dissector</p><ul><li><p>the ranges for "user" and "host" parts are of course not defined statically like in the example; their sizes are determined by identifying the position of the <code>@</code> symbol in the buffer,</p></li><li><p>I would rather omit the label-only line completely, because the equivalent of "emailaddr" field given above is already provided by lower layer dissector, but it is not possible as I do not have access to the pointer to that tree item so I cannot hook my items below it.</p></li></ul></div><div id="comment-52185-info" class="comment-info"><span class="comment-age">(03 May '16, 12:49)</span> sindy</div></div></div><div id="comment-tools-52176" class="comment-tools"></div><div class="clear"></div><div id="comment-52176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

