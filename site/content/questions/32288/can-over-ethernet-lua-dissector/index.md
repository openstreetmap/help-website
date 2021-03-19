+++
type = "question"
title = "CAN-over-Ethernet LUA dissector"
description = '''Hello, I&#x27;m writing a Lua dissector for a custom simple protocol. My protocol basically wraps CAN frames over ethernet media. Thus, wireshark captures ethernet frames from the ethernet card, and I hooked to them my LUA dissector. I can successfully parse some fields (timestamp and other random flags)...'''
date = "2014-04-29T05:27:00Z"
lastmod = "2014-04-30T11:09:00Z"
weight = 32288
keywords = [ "ethernet", "dissector", "can", "lua" ]
aliases = [ "/questions/32288" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [CAN-over-Ethernet LUA dissector](/questions/32288/can-over-ethernet-lua-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32288-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm writing a Lua dissector for a custom simple protocol. My protocol basically wraps CAN frames over ethernet media.</p><p>Thus, wireshark captures ethernet frames from the ethernet card, and I hooked to them my LUA dissector. I can successfully parse some fields (timestamp and other random flags) and I can extract CAN ID, CAN len, and CAN payload.</p><p>Then I would like to chain to the standard wireshark CAN dissector, but I failed to do this. If I do:</p><p>local can_dis = Dissector.get("can")</p><p>Wireshark complains about not found dissector "bad argument #1 to 'get' (Dissector_get: No such dissector)".</p><p>The "can" dissector should anyway be present in my Wireshark since I used it with socketcan devices successfully, and from menu "Internals-&gt;Supported protocol" it seems "can" is correctly listed. BTW version is 1.10.2 (SVN Rev 51934 from /trunk-1.10) (Linux)</p><p>Any suggestion would be appreciated :)</p><p>Thanks Andrea</p></div><div id="question-tags" class="tags-container tags">ethernet dissector can lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '14, 05:27</strong></p><img src="https://secure.gravatar.com/avatar/96076cb0346f60280e33f1964e316475?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrea&#39;s gravatar image" /><p>Andrea<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrea has no accepted answers">0%</span></p></div></div><div id="comments-container-32288" class="comments-container"><span id="32291"></span><div id="comment-32291" class="comment"><div id="post-32291-score" class="comment-score"></div><div class="comment-text"><p>For that to work I think the can dissector needs to register by name. Check if it does.</p></div><div id="comment-32291-info" class="comment-info"><span class="comment-age">(29 Apr '14, 08:20)</span> Anders ♦</div></div><span id="32306"></span><div id="comment-32306" class="comment"><div id="post-32306-score" class="comment-score"></div><div class="comment-text"><p>Is it possible to register a dissector from LUA script ? Can you please tell me how? Thank you</p></div><div id="comment-32306-info" class="comment-info"><span class="comment-age">(29 Apr '14, 23:46)</span> Andrea</div></div></div><div id="comment-tools-32288" class="comment-tools"></div><div class="clear"></div><div id="comment-32288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32319"></span>

<div id="answer-container-32319" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32319-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What Anders means is: in order for you to call a built-in Wireshark dissector such as the CAN one by using <code>Dissector.get("can")</code>, the CAN dissector needs to have registered itself by name, which it does not do. "CAN" shows up in "Supported Protocols", but those are registered <em>protocols</em> not registered <em>dissectors</em>; it's not a one-to-one relationship for protocols and dissectors.</p><p>There are multiple ways dissectors can register themselves to handle dissecting frames/packets. For the CAN protocol, it registers its dissector in two tables by number: in the "<code>wtap_encap</code>" table, and in the "<code>sll.ltype</code>" table. The "<code>wtap_encap</code>" table is a table used for wiretap encapsulation types, and the CAN dissector is registered for the encapsulation type number defined by "<code>WTAP_ENCAP_SOCKETCAN</code>" in C-code, which is the same as the Lua "<code>wtap_encaps.SOCKETCAN</code>" field in <code>init.lua</code>.</p><p>So that means you can get the CAN dissector by getting that number's entry from the <code>DissectorTable</code> for "<code>wtap_encap</code>", like this:</p><pre><code>local encap_tbl = DissectorTable.get(&quot;wtap_encap&quot;)
local can_dis   = encap_tbl:get_dissector(wtap_encaps.SOCKETCAN)</code></pre><p>or this is quicker:</p><pre><code>local can_dis = DissectorTable.get(&quot;wtap_encap&quot;):get_dissector(wtap_encaps.SOCKETCAN)</code></pre><hr /><p>As an aside... to see what dissectors are registered by name, you can use the Lua <code>Dissector.list()</code> function which was introduced in release <strong>1.11.3</strong>, like so:</p><pre><code>local t = Dissector.list()

for _,name in ipairs(t) do
    print(name)
end</code></pre><p>If you do that, you'll see there is no dissector named "<code>can</code>".</p><p>You can also see what the available <code>DissectorTables</code> are by using the new Lua <code>DissectorTable.list()</code> function as of 1.11.3, like so:</p><pre><code>local dt = DissectorTable.list()

for _,name in ipairs(dt) do
    print(name)
end</code></pre><p>If you do that, you'll see there is one named "<code>wtap_encap</code>", as well as the one named "<code>sll.ltype</code>".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '14, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-32319" class="comments-container"><span id="32321"></span><div id="comment-32321" class="comment"><div id="post-32321-score" class="comment-score"></div><div class="comment-text"><p>You could submit a patch to the can dissector to register by name.</p></div><div id="comment-32321-info" class="comment-info"><span class="comment-age">(30 Apr '14, 14:30)</span> Anders ♦</div></div><span id="32379"></span><div id="comment-32379" class="comment"><div id="post-32379-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your detailed explanation: I appreciate it a lot. And it worked! :)</p><p>About submitting the patch, maybe I will do that also.</p><p>Thanks Andrea</p></div><div id="comment-32379-info" class="comment-info"><span class="comment-age">(01 May '14, 23:15)</span> Andrea</div></div></div><div id="comment-tools-32319" class="comment-tools"></div><div class="clear"></div><div id="comment-32319-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

