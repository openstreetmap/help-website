+++
type = "question"
title = "LUA: Formatting floating point decimals"
description = '''Hi, I have written a LUA postdissector that outputs some time delta values. I want the values to be in decimal format, but when the value is small (less than say 0.001) Wireshark displays the value in scientific notation.  I&#x27;ve tried adding a string.format call to the code specifying a floating poin...'''
date = "2015-08-11T23:51:00Z"
lastmod = "2015-08-12T05:12:00Z"
weight = 44985
keywords = [ "lua" ]
aliases = [ "/questions/44985" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LUA: Formatting floating point decimals](/questions/44985/lua-formatting-floating-point-decimals)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44985-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have written a LUA postdissector that outputs some time delta values. I want the values to be in decimal format, but when the value is small (less than say 0.001) Wireshark displays the value in scientific notation.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/lua_sn.jpg" alt="alt text" /></p><p>I've tried adding a string.format call to the code specifying a floating point format but Wireshark still displays as scientific notation. The relevant code looks like this:</p><pre><code>  new_item = subtree:add(rte_art_F, string.format(&quot;%.06f&quot;, rte_art))
  new_item:set_generated()</code></pre><p>How can I force Wireshark to always display my value as a floating point decimal?</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '15, 23:51</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></img></div></div><div id="comments-container-44985" class="comments-container"></div><div id="comment-tools-44985" class="comment-tools"></div><div class="clear"></div><div id="comment-44985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44997"></span>

<div id="answer-container-44997" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44997-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately the <code>treeitem:add()</code> function has a complicated API form. When you do this:</p><pre><code>subtree:add(rte_art_F, string.format(&quot;%.06f&quot;, rte_art))</code></pre><p>...you're having wireshark add the <code>ProtoField</code> object <code>rte_art_F</code> to the tree, with the <strong>value</strong> of the second argument. Since <code>rte_art_F</code> is presumably a <code>ftypes.FLOAT</code> <code>ProtoField</code>, wireshark will use the <em>value</em> as a floating point number, and display it however it displays such things. That second argument does not affect how it displays the value.</p><p>What you want to do is control what wireshark displays. So to do that, set the text it displays for that tree item. There are three ways to do that:</p><pre><code>-- as a third argument of that same `treeitem:add()` function call:
new_item = subtree:add(rte_art_F, rte_art, string.format(&quot;%.06f&quot;, rte_art))

-- or using treeitem:set_text():
new_item = subtree:add(rte_art_F, rte_art)
new_item:set_text(string.format(&quot;%.06f&quot;, rte_art))

-- or as a field attribute:
new_item = subtree:add(rte_art_F, rte_art)
new_item.text = string.format(&quot;%.06f&quot;, rte_art)</code></pre><p>I think one or all of those methods might replace the field label in the tree display as well, though I can't recall right now. If they do, you'll have to add that back in too, like:</p><pre><code>new_item = subtree:add(rte_art_F, rte_art, string.format(&quot;APDU Rsp Time: %.06f&quot;, rte_art))</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '15, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-44997" class="comments-container"><span id="45000"></span><div id="comment-45000" class="comment"><div id="post-45000-score" class="comment-score"></div><div class="comment-text"><p>Hi Hadriel,</p><p>Thanks for the prompt response.</p><p>The first two options make no difference. The third option throws an error on the line:</p><p>new_item.text = string.format("%.06f", rte_art)</p><p>The error is:</p><p>attempt to index local 'new_item' (a userdata value)</p><p>This did get me thinking about the way I have defined rte_art_F. I've got:</p><p>rte_art_F = ProtoField.float("transum.art","APDU Rsp Time")</p><p>Is that OK?</p><p>Thanks and regards...Paul</p></div><div id="comment-45000-info" class="comment-info"><span class="comment-age">(12 Aug '15, 06:43)</span> PaulOfford</div></div><span id="45004"></span><div id="comment-45004" class="comment"><div id="post-45004-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by: "The first two options make no difference."? You mean they don't work to change the text?</p><p>Sorry about the third option - I forgot that only became available in 1.99, the current development branch - not in 1.12.</p></div><div id="comment-45004-info" class="comment-info"><span class="comment-age">(12 Aug '15, 07:31)</span> Hadriel</div></div><span id="45005"></span><div id="comment-45005" class="comment"><div id="post-45005-score" class="comment-score"></div><div class="comment-text"><p>Yes - with the first two options the text does not change, I still get scientific notation.</p></div><div id="comment-45005-info" class="comment-info"><span class="comment-age">(12 Aug '15, 08:00)</span> PaulOfford</div></div><span id="45007"></span><div id="comment-45007" class="comment"><div id="post-45007-score" class="comment-score"></div><div class="comment-text"><p>Worked fine for me - what wireshark version are you running?</p><p>I just tried this and it worked fine on wireshark 1.12.6:</p><pre><code>local myproto = Proto.new(&quot;myproto&quot;, &quot;myproto&quot;)

local rte_art_F = ProtoField.float(&quot;myproto.art&quot;,&quot;APDU Rsp Time&quot;)

myproto.fields = { rte_art_F }

function myproto.dissector(tvbuf,pktinfo,root)
    local tree = root:add(myproto, tvbuf(0,tvbuf:len()))

    local rte_art = 0.000001

    local subtree = tree:add(rte_art_F, rte_art)

    subtree:set_text(string.format(&quot;Time = %.06f&quot;, rte_art))
    subtree:set_generated()
end

register_postdissector(myproto)</code></pre></div><div id="comment-45007-info" class="comment-info"><span class="comment-age">(12 Aug '15, 08:35)</span> Hadriel</div></div><span id="45091"></span><div id="comment-45091" class="comment"><div id="post-45091-score" class="comment-score"></div><div class="comment-text"><p>Hi Hadriel,</p><p>I had my trees, subtrees and new_items muddled. Your code does generate a floating point decimal number, but now try right clicking on that number and Apply as Column. You get scientific notation again.</p><p>Is there some way of overriding the format in the column?</p><p>Thanks and regards...Paul</p></div><div id="comment-45091-info" class="comment-info"><span class="comment-age">(14 Aug '15, 00:03)</span> PaulOfford</div></div><span id="45104"></span><div id="comment-45104" class="comment not_top_scorer"><div id="post-45104-score" class="comment-score"></div><div class="comment-text"><p>No there's no way to override the column as far as I know. It's not a Lua thing; the column gets its data from the field's value, all in C-code. It's exactly what would happen if some C-code based dissector set a float field.</p><p>But really why don't you just multiply your values by 1000 or some such - i.e., represent them as milliseconds instead of seconds. No one said your fields have to be based in seconds.</p></div><div id="comment-45104-info" class="comment-info"><span class="comment-age">(14 Aug '15, 03:45)</span> Hadriel</div></div><span id="45130"></span><div id="comment-45130" class="comment not_top_scorer"><div id="post-45130-score" class="comment-score"></div><div class="comment-text"><p>I have tbhought about multiplying by 1000 and I may add that option. I want to keep the information aligned with the way Wireshark represents similar information. So Wireshark will show Time since last frame as 0.000048 and a LUA calculating the same number shows 4.8e-005. It would be great if it were possible to set the format.</p><p>Anyway, thanks for your help.</p></div><div id="comment-45130-info" class="comment-info"><span class="comment-age">(15 Aug '15, 01:03)</span> PaulOfford</div></div></div><div id="comment-tools-44997" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-44997-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

