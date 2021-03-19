+++
type = "question"
title = "How to convert le_nstime() to string in Lua"
description = '''How do I convert TvbRange.le_nstime() to a string? I tried the following Lua: local field_time = ProtoField.absolute_time(&quot;TIME&quot;,&quot;TIME&quot;,base.LOCAL); ... function SCP_proto.dissector (buf, pkt, root){  local value={  [0] =0,  [1] =0,  [2] =0  }  ...  for i=0,2,1 do  ...  local example_subtree = subtr...'''
date = "2012-06-05T03:24:00Z"
lastmod = "2012-06-05T17:08:00Z"
weight = 11654
keywords = [ "lua" ]
aliases = [ "/questions/11654" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to convert le\_nstime() to string in Lua](/questions/11654/how-to-convert-le_nstime-to-string-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11654-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I convert <code>TvbRange.le_nstime()</code> to a string? I tried the following Lua:</p><pre><code>local field_time = ProtoField.absolute_time(&quot;TIME&quot;,&quot;TIME&quot;,base.LOCAL);
...
function SCP_proto.dissector (buf, pkt, root){
 local value={
    [0] =0,
    [1] =0,
    [2] =0
  }
  ...
  for i=0,2,1 do
     ...
     local example_subtree = subtree:add(field_time,buf(offset,8):le_nstime());
     value[i] = tostring(buf(offset,8):le_nstime());
     ...
  end
}</code></pre><p>...but <code>value[i] = tostring(buf(offset,8):le\_nstime())</code> does not work the way I expected. The time format of <code>value[i]</code> is in seconds ("1336188353.000000150") instead of "Month|Day|Year|Time" format ("May 5, 2012 07:25:53.000000150"). However, in the Packet Details Pane, I see "May 5, 2012 07:25:53.000000150" as expected.</p><p>How can I get a formatted time-string from <code>le_nstime()</code> like the one I see in the protocol tree?</p><p>Wireshark 1.7, Win 7, Lua 5.1</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '12, 03:24</strong></p><img src="https://secure.gravatar.com/avatar/3763e1738205d07231e2d6fc4ff01a35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PavelMSTU&#39;s gravatar image" /><p>PavelMSTU<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PavelMSTU has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jun '12, 16:15</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11654" class="comments-container"></div><div id="comment-tools-11654" class="comment-tools"></div><div class="clear"></div><div id="comment-11654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11697"></span>

<div id="answer-container-11697" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11697-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're looking for <a href="http://wiki.wireshark.org/LuaAPI/Utils#format_date.28timestamp.29"><code>format_date</code></a> (or <a href="http://wiki.wireshark.org/LuaAPI/Utils#format_time.28timestamp.29"><code>format_time</code></a>), as in:</p><pre><code>  -- First, convert the NSTime to a string (which yields a decimal number).
  -- Then, convert that string into a Lua number, required by format_date().
  local seconds = tostring(buf(offset,8):le_nstime())
  seconds = tonumber(seconds)
  value[i] = format_date(seconds)</code></pre><p>But I should point out some other things about your sample code above:</p><ol><li><p>There is no <code>base.LOCAL</code> (despite the documentation in the Wireshark user manual...this is a bug). Since it doesn't exist, <code>base.LOCAL</code> is equivalent to <code>nil</code>.</p></li><li><p>You don't need to initialize a table with zeroes. You can simply declare the table with empty brackets, and Lua is smart enough to know what to do when you index into the table with: <code>value[i]</code>. (Or maybe there's omitted code that actually checks these indices for zero...weird.)</p><p><code>local value = {}</code></p></li><li><p>You don't need to convert the <code>TvbRange</code> into an <code>NSTime</code> when adding it to the tree because <code>field_time</code> is a <code>ProtoField.absolute_time</code>, which is inherently an <code>NSTime</code>. The endianness of the buffer is implied by <a href="http://wiki.wireshark.org/LuaAPI/TreeItem#treeitem:add.28proto_field_.5B.2Ctvbrange.5D_.5B.2Cvalue_.5B.2Ctext1_.5B.2Ctext2.5D_....5D_.5D.29"><code>TreeItem.add()</code></a> and <a href="http://wiki.wireshark.org/LuaAPI/TreeItem#treeitem:add_le.28proto_field_.5B.2Ctvbrange.5D_.5B.2Cvalue_.5B.2Ctext1_.5B.2Ctext2.5D_....5D_.5D.29"><code>TreeItem.add_le()</code></a> (you want <code>add_le()</code> in this case).</p><p><code>local example_subtree = subtree:add_le(field_time, buf(offset,8));</code></p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '12, 17:08</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jun '12, 18:40</p></div></div><div id="comments-container-11697" class="comments-container"><span id="11711"></span><div id="comment-11711" class="comment"><div id="post-11711-score" class="comment-score"></div><div class="comment-text"><p>Helloworld, very thenks to you!</p><p>But code:</p><hr /><p>local seconds = tostring(buf(offset,8):le_nstime())</p><p>seconds = tonumber(seconds)</p><p>value[i] = format_date(seconds)</p><hr /><p>don't work. Because tonumber function return nil.</p><p>I think this mistake arises, because 8 byte double can't converted in Lua. This code works correctly:</p><hr /><p>local seconds = tostring( buf(offset,4):le_nstime());</p><p>seconds = string.sub(seconds,0,10); --[[ Return 10 numbers of seconds, from January 1, 1970 ]]--</p><p>seconds = tonumber(seconds);</p><p>value[i] = format_date(seconds);</p><hr /></div><div id="comment-11711-info" class="comment-info"><span class="comment-age">(06 Jun '12, 00:52)</span> PavelMSTU</div></div><span id="11716"></span><div id="comment-11716" class="comment"><div id="post-11716-score" class="comment-score"></div><div class="comment-text"><p>Actually, an <code>NSTime</code> can be <em>either</em> 4 or 8 bytes. You lose precision with 4 bytes. <code>tonumber()</code> only returns <code>nil</code> for non-convertible strings. The <code>tostring()</code> conversion could've returned a non-convertible string (perhaps <code>nil</code>), which would indicate a problem with the buffer contents.</p><p>You don't need to parse out the seconds from the string since <code>tonumber()</code> handles floating-point numbers.</p></div><div id="comment-11716-info" class="comment-info"><span class="comment-age">(06 Jun '12, 07:39)</span> helloworld</div></div></div><div id="comment-tools-11697" class="comment-tools"></div><div class="clear"></div><div id="comment-11697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

