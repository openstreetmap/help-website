+++
type = "question"
title = "Lua: How can I evaluate a ProtoField in an IF-statement?"
description = '''I am writing a Lua script, which I&#x27;ve included in init.lua, to decode some data.  I&#x27;m reading the byte before an RTP header to determine how to decode the header. If the byte is 1, I want to decode it one way; otherwise in another way.  This is the code:   MYPROTO = Proto (&quot;myproto&quot;, &quot;My Protocol&quot;) ...'''
date = "2012-11-06T08:05:00Z"
lastmod = "2012-11-06T08:05:00Z"
weight = 15586
keywords = [ "lua" ]
aliases = [ "/questions/15586" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua: How can I evaluate a ProtoField in an IF-statement?](/questions/15586/lua-how-can-i-evaluate-a-protofield-in-an-if-statement)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15586-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a Lua script, which I've included in <code>init.lua</code>, to decode some data.</p><p>I'm reading the byte before an RTP header to determine how to decode the header. If the byte is <code>1</code>, I want to decode it one way; otherwise in another way.</p><p>This is the code:</p><pre><code>MYPROTO = Proto (&quot;myproto&quot;, &quot;My Protocol&quot;)

local f = MYPROTO.fields
f.compressed = ProtoField.uint8 (&quot;myproto.compressed&quot;, &quot;Compressed&quot;)

if(f.compressed == 1) 
then
   f.compseqno = ProtoField.uint8 (&quot;myproto.compseqno&quot;, &quot;RTP Sequence Number&quot;)
   ....
else
   f.rtpversion = ProtoField.uint8 (&quot;myproto.rtpversion&quot;, &quot;RTP Version&quot;, base.DEC, nil, 0xC0)
   ...
end

function MYPROTO.dissector (buffer, pinfo, tree)
   ...
   if(f.compressed == 1) 
   then
      subtree:add (f.compseqno, buffer(offset, 1))
      offset = offset + 1
   else
      subtree:add (f.rtpversion, buffer(offset, 1))
   end
end</code></pre><p>The problem is that the <code>if</code>-statement doesn't work on this data type, I guess, because even though the field's value is <code>1</code>, the <code>then</code> block does not get executed.</p><p><strong>Note:</strong> I know that there are other ways to do this (dissectors etc), but I would like to do it this particular way. How can I make the <code>if</code>-statement work as shown above?</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '12, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/7709c0c87ed4ba426f119187d3f0c705?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harkap&#39;s gravatar image" /><p>harkap<br />
<span class="score" title="5 reputation points">5</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harkap has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Nov '12, 17:43</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-15586" class="comments-container"></div><div id="comment-tools-15586" class="comment-tools"></div><div class="clear"></div><div id="comment-15586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

