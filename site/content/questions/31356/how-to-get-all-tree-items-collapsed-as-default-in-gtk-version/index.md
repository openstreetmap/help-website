+++
type = "question"
title = "How to get all tree items collapsed as default in GTK+ version"
description = '''I&#x27;m running on the nightly build. I noticed that for Qt version (either Mac or Windows), when I click on the part of the tree that I have written a dissector for, the tree is collapsed as default and you can expand it as you wish. However, for the GTK+ version (Windows), once you click on my protoco...'''
date = "2014-04-01T10:09:00Z"
lastmod = "2015-06-27T19:21:00Z"
weight = 31356
keywords = [ "lua", "gtk+" ]
aliases = [ "/questions/31356" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to get all tree items collapsed as default in GTK+ version](/questions/31356/how-to-get-all-tree-items-collapsed-as-default-in-gtk-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31356-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31356-score" class="post-score" title="current number of votes">0</div><span id="post-31356-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running on the nightly build. I noticed that for Qt version (either Mac or Windows), when I click on the part of the tree that I have written a dissector for, the tree is collapsed as default and you can expand it as you wish. However, for the GTK+ version (Windows), once you click on my protocol, it expands to the deepest level, which is a bit annoying. I haven't found out a way to change this. Is there a way I can make this all collapsed at the start?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-gtk+" rel="tag" title="see questions tagged &#39;gtk+&#39;">gtk+</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '14, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p><span>YXI</span><br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Apr '14, 17:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-31356" class="comments-container"><span id="31363"></span><div id="comment-31363" class="comment"><div id="post-31363-score" class="comment-score"></div><div class="comment-text"><p>Do you mean when you click on the + to expand a tree (in Gtk+) it automatically expands all subtrees?</p><p>Or do you mean that after doing that and then moving to another frame that contains your protocol all the subtrees are expanded?</p></div><div id="comment-31363-info" class="comment-info"><span class="comment-age">(01 Apr '14, 17:59)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="31390"></span><div id="comment-31390" class="comment"><div id="post-31390-score" class="comment-score"></div><div class="comment-text"><p>I mean when you click on the + to expand a tree (in GTK+), instead of expanding one step down, just to the children level, it expands to children, grandchildren, great-grandchildren, all the way to the leave level of the entire subtree you clicked on.</p></div><div id="comment-31390-info" class="comment-info"><span class="comment-age">(02 Apr '14, 07:33)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="31438"></span><div id="comment-31438" class="comment"><div id="post-31438-score" class="comment-score"></div><div class="comment-text"><p>That's very odd. I don't see that behavior here. I'm on Linux and I tried with both Gtk2 and Gtk3.</p><p>Does it happen for other protocols as well or just yours?</p><p>What about the stable (1.10.x) version?</p></div><div id="comment-31438-info" class="comment-info"><span class="comment-age">(02 Apr '14, 14:08)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="31445"></span><div id="comment-31445" class="comment"><div id="post-31445-score" class="comment-score"></div><div class="comment-text"><p>Seems just to happen for my own protocol which is dissected by my script. Haven't tried on a 1.10.x version.</p></div><div id="comment-31445-info" class="comment-info"><span class="comment-age">(02 Apr '14, 15:43)</span> <span class="comment-user userinfo">YXI</span></div></div></div><div id="comment-tools-31356" class="comment-tools"></div><div class="clear"></div><div id="comment-31356-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31450"></span>

<div id="answer-container-31450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31450-score" class="post-score" title="current number of votes">3</div><span id="post-31450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're getting this behavior when using a Lua script, I think this will happen if you use <code>tree:add()</code> where the first argument is <em>not</em> a <code>ProtoField</code>. In some of your other posts you've had a Lua script use <code>tree:add()</code> with a <code>TvbRange</code> object for the first argument.</p><p>That's not illegal/wrong, but this is the behavior you'll get with that for the reason Bill Meier cited: internally the wireshark C-code needs a registered <code>ett</code> value, and the internal Lua binding code gets the <code>ett</code> either from the registered <code>ProtoField</code> given in the first argument, or if one isn't given in the first argument then it uses a single, generic <code>ett</code> registered for all of Lua; so expanding one of that "type" will expand all of that type. The same thing happens if you do a <code>tree:add("foo")</code> with just text as a subtree parent, for example.</p><p>To avoid this behavior, simply create and register <code>ProtoFields</code> for your subtree parents, and use the <code>ProtoField</code> as the first argument for <code>tree:add()</code>.</p><p>[Qt should have given the same behavior - if it doesn't that's a bug I think.]</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 19:51</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-31450" class="comments-container"><span id="31484"></span><div id="comment-31484" class="comment"><div id="post-31484-score" class="comment-score"></div><div class="comment-text"><p>You guys hit the nail on the head! Yes, I'm using the TvbRange as the first argument in tree:add() I do need to change to using ProtoField as the first argument as that will make my value filterable as well.<br />
Thanks.</p></div><div id="comment-31484-info" class="comment-info"><span class="comment-age">(03 Apr '14, 07:30)</span> <span class="comment-user userinfo">YXI</span></div></div></div><div id="comment-tools-31450" class="comment-tools"></div><div class="clear"></div><div id="comment-31450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31449"></span>

<div id="answer-container-31449" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31449-score" class="post-score" title="current number of votes">1</div><span id="post-31449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you using the same 'ett' variable for each level (subtree) ?</p><p>If so, that will give exactly the effect you describe (at least using GTK).</p><p>If this is the problem, it would appear that there's something different (from GTK Wireshark) about the Wireshark implementation of trees when using QT (which might possibly be a bug).</p><p>(An ett variable keeps track of whether the associated sub-tree is expanded or not; if only a single variable is used for all the sub-trees, then expanding one sub-tree effectively expands all the sub-trees).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 19:33</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span> </br></p></div></div><div id="comments-container-31449" class="comments-container"><span id="42525"></span><div id="comment-42525" class="comment"><div id="post-42525-score" class="comment-score"></div><div class="comment-text"><p>Hello guys as per above answers and comments my below script should work and show only level_1 children only but behaves same as older one</p><pre><code>-- New Protocol and  fields
p_mynewproto  = Proto (&quot;MyProtocol&quot;, &quot;Test&quot;)

-- Define Header fields
local protoHeader = p_mynewproto.fields
protoHeader.rxId        = ProtoField.uint16(&#39;protoHeader.rxId&#39;      , &#39;Rx ID &#39; , base.HEX, nil)
protoHeader.txId        = ProtoField.uint16(&#39;protoHeader.txId&#39;      , &#39;Tx ID &#39; , base.HEX, nil)
protoHeader.timeHour    = ProtoField.uint16(&#39;protoHeader.timeHour&#39;  , &#39;Hour  &#39; , base.HEX, nil)
protoHeader.timeMinute  = ProtoField.uint16(&#39;protoHeader.timeMinute&#39;, &#39;Minute&#39; , base.HEX, nil)
protoHeader.timeSecond  = ProtoField.uint16(&#39;protoHeader.timeSecond&#39;, &#39;Second&#39; , base.HEX, nil)

-- mynewproto dissector function
function p_mynewproto.dissector (buf, pkt, root)

-- Check the packet length
if buf:len() == 0 then return end
pkt.cols.protocol = p_mynewproto.name

-- start from offset 0
local offset = 0

-- create subtree for mynewproto
subtreeA = root:add(p_mynewproto, buf(offset,buf:len())):append_text(&quot; [My Protocol Header]&quot;)

-- Rx ID
subtreeA:add(protoHeader.rxId , buf(offset,2))

-- Tx ID
subtreeA:add(protoHeader.txId , buf(offset+2,2))

-- Time
subtreeB = subtreeA:add(p_mynewproto, buf(offset+4,2),&quot;[TIME]&quot;)
-- Time Hour
subtreeB:add(protoHeader.timeHour , buf(offset+4,2))
subtreeC = subtreeB:add(p_mynewproto, buf(offset+6,4),&quot;[minute and second]&quot;)
-- Time Minute
subtreeC:add(protoHeader.timeMinute , buf(offset+6,2))
-- Time Second
subtreeC:add(protoHeader.timeSecond , buf(offset+8,2))
end

-- Initialization function
function p_mynewproto.init()
end

-- Register a chained dissector for port 11111
tcp_table = DissectorTable.get(&quot;tcp.port&quot;)
-- register our protocol to handle udp port 7777
tcp_table:add(8443,p_mynewproto)</code></pre></div><div id="comment-42525-info" class="comment-info"><span class="comment-age">(18 May '15, 23:38)</span> <span class="comment-user userinfo">ankit</span></div></div><span id="42535"></span><div id="comment-42535" class="comment"><div id="post-42535-score" class="comment-score"></div><div class="comment-text"><p>I don't know why ankit has posted my code <a href="https://ask.wireshark.org/questions/42404/lua-dissector-tree-collapse">https://ask.wireshark.org/questions/42404/lua-dissector-tree-collapse</a> What's the scope of his answer :O ?</p></div><div id="comment-42535-info" class="comment-info"><span class="comment-age">(19 May '15, 04:18)</span> <span class="comment-user userinfo">Peter1969</span></div></div><span id="42547"></span><div id="comment-42547" class="comment"><div id="post-42547-score" class="comment-score"></div><div class="comment-text"><p>Hi peter I have also the same doubt. I have developed one plugin using lua ans same problem has occured as you have mentioned in your question. I have just reused your code to ask doubt nothing else let's see what answer will be given??!!</p></div><div id="comment-42547-info" class="comment-info"><span class="comment-age">(19 May '15, 08:32)</span> <span class="comment-user userinfo">ankit</span></div></div><span id="42586"></span><div id="comment-42586" class="comment"><div id="post-42586-score" class="comment-score"></div><div class="comment-text"><p><span>@Hadriel</span> can you look into this?</p></div><div id="comment-42586-info" class="comment-info"><span class="comment-age">(20 May '15, 09:44)</span> <span class="comment-user userinfo">ankit</span></div></div><span id="43618"></span><div id="comment-43618" class="comment"><div id="post-43618-score" class="comment-score"></div><div class="comment-text"><p>Answered in <a href="https://ask.wireshark.org/questions/42404/lua-dissector-tree-collapse">the original question</a>.</p></div><div id="comment-43618-info" class="comment-info"><span class="comment-age">(27 Jun '15, 19:21)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-31449" class="comment-tools"></div><div class="clear"></div><div id="comment-31449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

