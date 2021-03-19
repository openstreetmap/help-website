+++
type = "question"
title = "How can I add in one tree information field, the information of a subfield in lua?"
description = '''For example :  In this picture the type &quot;UPDATE Message&quot; is also included in the Border Gateway Protocol tree description an it is a field below it.'''
date = "2016-05-12T04:01:00Z"
lastmod = "2016-05-15T03:31:00Z"
weight = 52464
keywords = [ "fields", "lua" ]
aliases = [ "/questions/52464" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How can I add in one tree information field, the information of a subfield in lua?](/questions/52464/how-can-i-add-in-one-tree-information-field-the-information-of-a-subfield-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52464-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For example : <img src="https://osqa-ask.wireshark.org/upfiles/1_riVIoEb.png" alt="alt text" /> In this picture the type "UPDATE Message" is also included in the Border Gateway Protocol tree description an it is a field below it.</p></div><div id="question-tags" class="tags-container tags">fields lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '16, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/0164b3a0b6fca8e2931eb42defb1ebfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="javiguembe&#39;s gravatar image" /><p>javiguembe<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="javiguembe has no accepted answers">0%</span></p></img></div></div><div id="comments-container-52464" class="comments-container"></div><div id="comment-tools-52464" class="comment-tools"></div><div class="clear"></div><div id="comment-52464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52587"></span>

<div id="answer-container-52587" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52587-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your screenshot is an example of taking an important (distinctive) value from the protocol data and using it as part of the subtree title. So algorithmically, you first parse the tvb at least until you get the value of such parameter (or, if it has a fixed format, fetch it directly from a known position), and only then you compose the description for the tree item at level N, use tree:add to apply that label and hook in a subtree, and then add the subtree items, including the parameter whose value you've already used for the subtree title.</p><p>But that seems so obvious to me that I'm afraid I've actually misunderstood what you've asked.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '16, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52587" class="comments-container"><span id="52607"></span><div id="comment-52607" class="comment"><div id="post-52607-score" class="comment-score"></div><div class="comment-text"><p>I have this to dissect BGP:</p><pre><code>p_mybgp = Proto (&quot;mybgp&quot;,&quot;MyBorder Gateway Protocol&quot;)

local BGP_types = {
  [1] = &quot;OPEN message&quot;,
  [2] = &quot;UPDATE message&quot;,
  [3] = &quot;NOTIFICATION message&quot;,
  [4] = &quot;KEEPALIVE message&quot;
}
function p_mybgp.dissector (buf, pkt, root)

local f_marker = ProtoField.bytes(&quot;mybgp.marker&quot;, &quot;Marker&quot;)
local f_length_field = ProtoField.uint64(&quot;mybgp.length&quot;, &quot;Length&quot;, base.DEC)
local f_type = ProtoField.uint8(&quot;mybgp.type&quot;, &quot;Type&quot;, base.DEC, BGP_types)
local f_data = ProtoField.string(&quot;typroto.data&quot;, &quot;Data&quot;, FT_STRING)
local f_open_version = ProtoField.uint64(&quot;mybgp.version&quot;, &quot;Version&quot;, base.DEC)
local f_my_as = ProtoField.uint64(&quot;mybgp.myas&quot;, &quot;My AS&quot;, base.DEC)
local f_holdtime = ProtoField.uint64(&quot;mybgp.timehold&quot;,&quot;Hold Time&quot;,base.DEC)
local f_bgp_id = ProtoField.ipv4(&quot;mybgp.bgpid&quot;,&quot;BGP Identifier&quot;)

  if buf:len() == 0 then return end
  pkt.cols.protocol = p_mybgp.name --Ponemos el nombre a la columna
   --DESCRIPTION FIELDS:
  offset = 0
  local subtree = root:add(p_mybgp, buf(offset)) **&lt;&lt;&lt;&lt;&lt; I want to add here type value**
  subtree:add(f_marker, buf(offset,16))
  offset = offset +16
  subtree:add(f_length_field, buf(offset,2))
  offset = offset +2
  local type_value  = buf(offset,1):uint()
  subtree:add(f_type,buf(offset,1))
  offset = offset +1</code></pre><p>My problem is that I don´t know how can I add syntactically in the same subtree 2 Protofields. Concatenating with ".." return error (obviusly?).</p></div><div id="comment-52607-info" class="comment-info"><span class="comment-age">(16 May '16, 00:01)</span> javiguembe</div></div><span id="52610"></span><div id="comment-52610" class="comment"><div id="post-52610-score" class="comment-score">1</div><div class="comment-text"><p>I've converted your previous post from an Answer to your original Question (which it clearly wasn't) to a Comment to my Answer. See site FAQ for details.</p><p>To the subject:</p><blockquote><p>My problem is that I don´t know how can I add syntactically in the same subtree 2 Protofields. Concatenating with ".." return error (obviusly?).</p></blockquote><p>You've got it right: you cannot hook two distinct protocol fields (as <code>ProtoField</code> objects) as a single item to the tree.</p><p>But you can describe the tree item using only a reference to a tvb range (spanning even several protocol fields), extract the values from just some (even completely unrelated to that range) bytes of the tvb as text, and use that text as a label of that treeitem, which is what most likely what the original dissector does. So unless ProtoField has recently become a mandatory parameter of <code>treeitem:add</code>, the following should work:</p><pre><code>local subtree = root:add(buf:range(0),&quot;Message type: &quot; .. BGP_types[buf(0,1):uint8])</code></pre><p>Look <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Tree.html">here</a> for details of the highly flexible syntax of <code>treeitem:add</code>.</p></div><div id="comment-52610-info" class="comment-info"><span class="comment-age">(16 May '16, 01:55)</span> sindy</div></div><span id="52654"></span><div id="comment-52654" class="comment"><div id="post-52654-score" class="comment-score">1</div><div class="comment-text"><p>See also section <strong>11.7.1.5. treeitem:append_text(text)</strong>. This allows you to append more information to the tree item so you don't necessarily have to construct it all at once.</p></div><div id="comment-52654-info" class="comment-info"><span class="comment-age">(16 May '16, 15:00)</span> cmaynard ♦♦</div></div><span id="53666"></span><div id="comment-53666" class="comment"><div id="post-53666-score" class="comment-score"></div><div class="comment-text"><p>Thanks sindy and cmaynard! Both methods works!</p></div><div id="comment-53666-info" class="comment-info"><span class="comment-age">(27 Jun '16, 02:28)</span> javiguembe</div></div></div><div id="comment-tools-52587" class="comment-tools"></div><div class="clear"></div><div id="comment-52587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

