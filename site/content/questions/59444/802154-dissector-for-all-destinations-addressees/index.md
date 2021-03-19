+++
type = "question"
title = "802.15.4 Dissector for all Destinations (addressees)"
description = '''I&#x27;m getting started creating a Dissector for an IEEE 802.15.4 packet. I&#x27;m using the TI cc2531 dingle and the python script ccsniffpip to get data into Wireshark and I can see the packets as raw 802.15.4 packets just fine. It seems that Wireshark is designed assuming that the 802.15.4 destination add...'''
date = "2017-02-15T15:26:00Z"
lastmod = "2017-02-17T11:23:00Z"
weight = 59444
keywords = [ "802.15.4", "lua", "dissector" ]
aliases = [ "/questions/59444" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [802.15.4 Dissector for all Destinations (addressees)](/questions/59444/802154-dissector-for-all-destinations-addressees)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59444-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm getting started creating a Dissector for an IEEE 802.15.4 packet. I'm using the TI cc2531 dingle and the python script ccsniffpip to get data into Wireshark and I can see the packets as raw 802.15.4 packets just fine. It seems that Wireshark is designed assuming that the 802.15.4 destination addresses significant in the sense that ports are intended to hint at what the packet type is. For 15.4 that is often just not the case. For 15.4 the destination is more akin to an IP address. I want to decode every 15.4 packet I see. In my case, I have my protocol hiding inside the "data" section of 15.4 packets with the first byte of the data indicating the packet type. I have no problem creating a simple Lua dissector to walk through things and build out some simple trees, but as fas as I can tell, I have to go in by hand in the GUI and tell the program to Decode As "MyProtocol" for each new destination address that becomes allocated. My need to to make my dissector promiscuous to all 15.4 destination addresses. I've fond notes where dissector_add for_decode_as was exposed to Lua ("https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=016769d7e2462c2238364d73c1dde1c4457fa486" )(Wireshark-commits: [Wireshark-commits] master 016769d: Expose dissector_add_for_decode_as() to Lua), but I can't find any examples on how to use it. Also any high level architecture suggestions would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">802.15.4 lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '17, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/b4b7f09942345d067d2c40d60da675cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MountainLogic&#39;s gravatar image" /><p>MountainLogic<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MountainLogic has no accepted answers">0%</span></p></div></div><div id="comments-container-59444" class="comments-container"></div><div id="comment-tools-59444" class="comment-tools"></div><div class="clear"></div><div id="comment-59444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59511"></span>

<div id="answer-container-59511" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59511-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think the best way to solve is to register a heuristic dissector in the wpan table, some example code:</p><pre><code>local my_proto = Proto(&quot;myproto&quot;, &quot;My Protocol&quot;)

local function my_proto_dissector(tvbuffer, pinfo, treeitem)
   local result = false
   -- check if tvbuffer belongs to your protocol, return true if it does ..
   return result
end

my_proto.dissector = my_proto_dissector 
my_proto:register_heuristic(&quot;wpan&quot;, my_proto_dissector)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '17, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/ce127a4716cc9b4c3401c9c47820f336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kim&#39;s gravatar image" /><p>kim<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kim has one accepted answer">50%</span></p></div></div><div id="comments-container-59511" class="comments-container"></div><div id="comment-tools-59511" class="comment-tools"></div><div class="clear"></div><div id="comment-59511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

