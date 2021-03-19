+++
type = "question"
title = "lua help: private header"
description = '''Hi, I am new to Lua. I need to parse packets like below ETHERNET HEADER + PRIVATE HEADER (14 bytes) + ETHERNET HEADER + PAYLOAD I have a lua script to parse the PRIVATE HEADER, but don&#x27;t know how to parse the remaining... Can someone please help? Here is my script. foo_proto = Proto(&quot;foo&quot;,&quot;foo Proto...'''
date = "2016-01-29T22:18:00Z"
lastmod = "2016-01-30T01:38:00Z"
weight = 49642
keywords = [ "lua" ]
aliases = [ "/questions/49642" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [lua help: private header](/questions/49642/lua-help-private-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49642-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am new to Lua. I need to parse packets like below</p><p>ETHERNET HEADER + PRIVATE HEADER (14 bytes) + ETHERNET HEADER + PAYLOAD</p><p>I have a lua script to parse the PRIVATE HEADER, but don't know how to parse the remaining... Can someone please help?</p><p>Here is my script.</p><pre><code>foo_proto = Proto(&quot;foo&quot;,&quot;foo Protocol&quot;)
function foo_proto.dissector(buffer,pinfo,tree)
    pinfo.cols.protocol = &quot;foo&quot;
    local subtree = tree:add(foo_proto,buffer(),&quot;foo Header&quot;)
    subtree:add(buffer(0,2),&quot;index: &quot; .. buffer(0,2):uint())
    subtree:add(buffer(2,2),&quot;vr:&quot; .. buffer(2,2):uint())
    subtree:add(buffer(4,2),&quot;cmd: &quot; .. buffer(4,2):uint())
    subtree:add(buffer(6,4),&quot;cmd_1: &quot; .. buffer(6,4):uint())
    subtree:add(buffer(10,4),&quot;cmd_2: &quot; .. buffer(10,4):uint())
end
ether_table = DissectorTable.get(&quot;ethertype&quot;)
ether_table:add(2048,foo_proto)</code></pre></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '16, 22:18</strong></p><img src="https://secure.gravatar.com/avatar/b7590de43adb375f2d9c6ba1f98b72cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yacare&#39;s gravatar image" /><p>yacare<br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yacare has no accepted answers">0%</span></p></div></div><div id="comments-container-49642" class="comments-container"></div><div id="comment-tools-49642" class="comment-tools"></div><div class="clear"></div><div id="comment-49642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49643"></span>

<div id="answer-container-49643" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49643-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What exactly is unclear <a href="https://wiki.wireshark.org/LuaAPI/Dissector">in this part of Lua API description</a>?</p><p>The first pass of eth dissector processes the first ethernet header and calls your dissector for the payload because you've hooked your dissector into the ethertype table, handing over to you the rest of the packet in the tvb parameter (referred to as <code>buffer</code> in your Lua <code>foo_proto.dissector</code> function).</p><p>Your dissector processes your private header and invokes the eth dissector, handing the rest of the packet to it in the <code>tvb</code> parameter, the packet info table in the <code>pinfo</code> parameter, and the node in the dissection tree where it should hook itself as <code>tree</code> - exactly the same parameters you expect to get when you're invoked yourself.</p><p>So the result would be:</p><pre><code>...
    subtree:add(buffer(10,4),&quot;cmd_2: &quot; .. buffer(10,4):uint())
    Dissector.get(&quot;eth&quot;):call(buffer:range(14):tvb(),pinfo,tree)
end
...</code></pre><p>You may also want to define the individual proto.fields rather than just place the text names of the fields and their values into the dissection tree; if you do so, you can use the field names as display filters, e.g. <code>foo.index == 7</code></p><p>To do so, you would just add the definition of the protocol fields next to your Proto definition:</p><pre><code>foo_proto = Proto(&quot;foo&quot;,&quot;foo Protocol&quot;)
index = ProtoField.new(&quot;Index&quot;,&quot;foo.index&quot;,ftypes.UINT16)
foo_proto.fields = {index}
...</code></pre><p>And then, you would replace</p><pre><code>subtree:add(buffer(0,2),&quot;index: &quot; .. buffer(0,2):uint())</code></pre><p>by</p><pre><code>subtree:add(index,buffer:range(0,2))</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '16, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jan '16, 06:29</p></div></div><div id="comments-container-49643" class="comments-container"><span id="49648"></span><div id="comment-49648" class="comment"><div id="post-49648-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sindy. This really helps.</p><p>Running into another issue. The script works fine when the inner eth-type is not 0x0800. When the inner ethernet frame has 0x0800, it carries the normal IP payload. For instance,</p><pre><code>dst_mac + src_mac + eth-type(0x0800) + private-header(14 bytes) + dst_mac + src_mac + eth-type(0x0800) + IP-header + IP payload</code></pre><p>The scripts interpret the IP-header as private header. I know this is expected, but wonder any way to handle such scenario. Note that private-header is never present in the inner ethernet frames.</p><p>Thanks!</p></div><div id="comment-49648-info" class="comment-info"><span class="comment-age">(30 Jan '16, 18:25)</span> yacare</div></div><span id="49652"></span><div id="comment-49652" class="comment"><div id="post-49652-score" class="comment-score"></div><div class="comment-text"><p>Well, I was hoping that the <code>ether_table:add(2048,foo_proto)</code> was just a bad example, not that you really misuse the ethertype value assigned to IP for your private header. Have you given a thought to what happens if, by mistake, someone connects your equipment sending such packets to a network which interprets this ethertype the normal way?</p><p>From the point of view of Lua dissector it is not that complex, though. As you have told the eth dissector to invoke your one when(ever) it finds ethertype 2048, it is then your dissector's responsibility to choose between "foo" and "ip" dissection, through keeping track about how many times it has already been invoked on that particular frame. You also have to bear in mind that the same frame may get dissected several times in a row.</p><p>So your code might look as follows:</p><pre><code>foo_proto = Proto(&quot;foo&quot;,&quot;foo Protocol&quot;)
index = ProtoField.new(&quot;Index&quot;,&quot;foo.index&quot;,ftypes.UINT16)
...
foo_proto.fields = {index, ... }

local dis_eth = Dissector.get(&quot;eth&quot;) -- fetch the pointer just once,
                                     -- during initialization
local depth = 0
local frame_num = 0                  -- frames are counted from 1 so
                                     -- 0 will be different from any
                                     -- real frame number

function foo_proto.dissector(buffer,pinfo,tree)
    if pinfo.number ~= frame_num then  -- accessing this frame
                                       -- for the first time
        depth = 0
        frame_num = pinfo.number
    end
    depth = depth + 1                -- track the number of recursions
    if depth &gt; 1 then
        dis_orig:call(buffer,pinfo,tree)
    else
        pinfo.cols.protocol = &quot;foo&quot;
        local subtree = tree:add(foo_proto,buffer(),&quot;foo Header&quot;)
        subtree:add(index,buffer:range(0,2))
        ... 
        dis_eth:call(buffer:range(14):tvb(),pinfo,tree)
    end
    depth = depth - 1                -- track the number of recursions
end

ether_table = DissectorTable.get(&quot;ethertype&quot;)
dis_orig = ether_table:get_dissector(2048) -- save the pointer to
                                           -- the original dissector
ether_table:add(2048,foo_proto)</code></pre></div><div id="comment-49652-info" class="comment-info"><span class="comment-age">(31 Jan '16, 00:54)</span> sindy</div></div><span id="49654"></span><div id="comment-49654" class="comment"><div id="post-49654-score" class="comment-score"></div><div class="comment-text"><p>Another method to stop the recursion might be to check some values in the pinfo argument, although I'm not sure what's exposed to Lua, e.g. the curr_layer_num member of pinfo shows how "deep" in the packet tree you are.</p></div><div id="comment-49654-info" class="comment-info"><span class="comment-age">(31 Jan '16, 01:08)</span> grahamb ♦</div></div><span id="49655"></span><div id="comment-49655" class="comment"><div id="post-49655-score" class="comment-score"></div><div class="comment-text"><p>Also, the line <code>pinfo.cols.protocol = "foo"</code>, if used alone, only has a practical effect on the <code>Protocol</code> column in the packet list if <code>foo</code> is the highest layer available in the frame. The reason is that normally <em>each</em> dissector sets this column to its own value - the goal is that always only the highest-layer protocol is shown. This is usually not an issue because by using <code>foo</code> in your display filter, you can visualize only packets which do contain the "foo" layer.</p><p>If you would really insist to see "foo" in the <code>Protocol</code> column although there is more data in the frame after "foo", you would have to use</p><pre><code>pinfo.cols.protocol:fence()</code></pre><p>after setting the value. However, it does not prevent the subsequent dissectors from adding their own texts; it only keeps your one in front of them.</p></div><div id="comment-49655-info" class="comment-info"><span class="comment-age">(31 Jan '16, 01:18)</span> sindy</div></div><span id="49657"></span><div id="comment-49657" class="comment"><div id="post-49657-score" class="comment-score"></div><div class="comment-text"><p>@grahamb, as <code>pinfo.curr_layer_num</code> is currently missing in the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Pinfo.html">list of pinfo fields made available to Lua</a>, one might wonder whether it has actually been?</p><p>A quick test on 2.0.1 proves that your doubt was justified as it hasn't:</p><pre><code>tree:add(&quot;Layer: &quot; .. pinfo.curr_layer_num)</code></pre><p>yields</p><p><code>Lua Error: [string "C:\Users\JohnDoe\AppData\Roaming\Wireshark\p..."]:15: No such 'curr_layer_num' getter attribute/field for object type 'Pinfo'</code></p><p>Also, just to make it 100% clear if someone adds the wrapper for Lua in future, does this pinfo attribute indicate a "layer" in terms of how many dissectors have already done their job in the current run over the frame, or "layer" in terms of the OSI model?</p></div><div id="comment-49657-info" class="comment-info"><span class="comment-age">(31 Jan '16, 01:39)</span> sindy</div></div><span id="49659"></span><div id="comment-49659" class="comment not_top_scorer"><div id="post-49659-score" class="comment-score"></div><div class="comment-text"><p>It's the number of times a dissector has indicated it will try to handle the data in the packet. However, dissectors can explicitly ask for the count not to be incremented via the <code>add_pro_name</code> parameter to <code>dissector_try_uint_new()</code> and <code>dissector_try_guid_new()</code>.</p><p>The value <em>should</em> track the number of entries in the pinfo-&gt;layers list, however if the dissector didn't handle any data in the packet its name is removed from the layers list, but the count isn't decremented. This looks like a bug to me.</p><p>The comment for the commit (319bf245) that added <code>curr_layer_num</code> states:</p><blockquote>Add curr_layer_num which can be used to keep track of multiple occurances of the same protocol in a frame.</blockquote></div><div id="comment-49659-info" class="comment-info"><span class="comment-age">(31 Jan '16, 06:42)</span> grahamb ♦</div></div><span id="49671"></span><div id="comment-49671" class="comment not_top_scorer"><div id="post-49671-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sindy and Grahamb.</p><p>I modified my script as below. I want the foo_proto.dissector interpret the foo header only on the outer ethernet frame. However, I got an error saying "attempt to index global 'dis_orig' (a nil value)" at line 30 (that is "dis_orig:call(buffer,pinfo,tree)"). Somehow, we can't get the dissector for 2048 from ether_table....</p><pre><code>foo_proto = Proto(&quot;foo&quot;,&quot;foo Protocol&quot;)
local Command = {
        [0] = &quot;CMD_A&quot;,
        [1] = &quot;CMD_B&quot;,
}

local f_ifindex = ProtoField.uint16(&quot;foo.ifindex&quot;, &quot;IFINDEX&quot;, base.DEC)
local f_vrf = ProtoField.uint16(&quot;foo.vrf&quot;, &quot;Vrf&quot;, base.DEC)
local f_cmd = ProtoField.uint16(&quot;foo.cmd&quot;, &quot;Cmd&quot;, base.HEX,Command)
local f_cmd_p1 = ProtoField.uint32(&quot;foo.cmd_param1&quot;, &quot;Cmd_Param1&quot;, base.DEC_HEX)
local f_cmd_p2 = ProtoField.uint32(&quot;foo.cmd_param1&quot;, &quot;Cmd_Param2&quot;, base.DEC_HEX)

foo_proto.fields = { f_ifindex, f_vrf, f_cmd, f_cmd_p1, f_cmd_p2 }

local dis_eth = Dissector.get(&quot;eth&quot;)
local frame_num = 0

function foo_proto.dissector(buffer,pinfo,tree)
    pinfo.cols.protocol = &quot;foo&quot;
    if pinfo.number ~= frame_num then
        frame_num = pinfo.number
        local subtree = tree:add(foo_proto,buffer(0,14),&quot;foo Header&quot;)
        subtree:add(f_ifindex,buffer:range(0,2))
        subtree:add(f_vrf,buffer:range(2,2))
        subtree:add(f_cmd,buffer:range(4,2))
        subtree:add(f_cmd_p1,buffer:range(6,4))
        subtree:add(f_cmd_p2,buffer:range(10,4))
        dis_eth:call(buffer:range(14):tvb(),pinfo,tree)
    else
        dis_orig:call(buffer,pinfo,tree)
    end
end

-- load the dissector only when ethernet type is 0x0800
ether_table = DissectorTable.get(&quot;ethertype&quot;)
dis_orig = ether_table:get_dissector(2048)
ether_table:add(2048, foo_proto)</code></pre></div><div id="comment-49671-info" class="comment-info"><span class="comment-age">(31 Jan '16, 18:06)</span> yacare</div></div><span id="49672"></span><div id="comment-49672" class="comment not_top_scorer"><div id="post-49672-score" class="comment-score"></div><div class="comment-text"><p>Changed to dis_orig = ether_table:get_dissector(0x0800). Still no luck. As a test, 0x0806 (ARP) made the error go away... dis_orig = ether_table:get_dissector(0x0806)</p><p>I have to use following and it works!</p><p>dis_orig = Dissector.get("ip")</p></div><div id="comment-49672-info" class="comment-info"><span class="comment-age">(31 Jan '16, 18:46)</span> yacare</div></div><span id="49674"></span><div id="comment-49674" class="comment not_top_scorer"><div id="post-49674-score" class="comment-score"></div><div class="comment-text"><blockquote><p>0x0806 (ARP) made the error go away</p></blockquote><p>Of course it did, because the error is reported when the script attempts to <em>use</em> the value, not when it fetches it. So unless there was an ARP payload in the inner Ethernet, the script never needed to use the pointer. So this provides a useful debug information only if you do have packets with ARP payload.</p><blockquote><p>I have to use <code>dis_orig = Dissector.get("ip")</code> and it works</p></blockquote><p>The reason why I've suggested to mine the dissector from the ethertype table rather than directly choose the "ip" one from the dissector table was that this is a Q&amp;A site and someone else reading the answer may not want to replace/augment the dissection of IP but of some other protocol. So my audacious guess (because it does work for me the way I've suggested it) is that you have either disabled dissection of IP at some moment in the past, i.e. removed the row from the ethertype table (try to open a capture file of regular traffic to check that) or that you have two versions of Lua script in place, one of which destroys the pointer before the second one can access it.</p><p>The last point: I haven't introduced the recursion tracking counter just for fun. Try to double-click the packet in the packet list pane, so that it opens in a separate window. In such case, the same packet is dissected twice in a row, so without the recursion counter, the second pass of the dissector uses ip dissection also on the private header. You cannot anticipate in what other use scenario the same packet may be dissected twice in a row, so even if you never open packets in separate windows, you should still stay on the safe side.</p></div><div id="comment-49674-info" class="comment-info"><span class="comment-age">(31 Jan '16, 22:48)</span> sindy</div></div><span id="49692"></span><div id="comment-49692" class="comment not_top_scorer"><div id="post-49692-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sindy. Understand your last point now. It makes perfect sense. Just modified my script accordingly.</p></div><div id="comment-49692-info" class="comment-info"><span class="comment-age">(01 Feb '16, 08:29)</span> yacare</div></div></div><div id="comment-tools-49643" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-49643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

