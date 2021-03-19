+++
type = "question"
title = "Lua error: &quot;Tvbs can only be created and used in dissectors&quot;"
description = '''I am trying to use lua to dissect my protocol stack. The one problem I cannot solve is this: I can get several messages that are completed in the same packet. I would then like to make tvbs for each of the completed messages and hand them over to a dissector. But if I get more than one extra tvb - a...'''
date = "2016-10-03T14:17:00Z"
lastmod = "2016-10-17T04:09:00Z"
weight = 56110
keywords = [ "lua", "error", "tvb" ]
aliases = [ "/questions/56110" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Lua error: "Tvbs can only be created and used in dissectors"](/questions/56110/lua-error-tvbs-can-only-be-created-and-used-in-dissectors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56110-score" class="post-score" title="current number of votes">1</div><span id="post-56110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to use lua to dissect my protocol stack.</p><p>The one problem I cannot solve is this:</p><p>I can get several messages that are completed in the same packet.</p><p>I would then like to make tvbs for each of the completed messages and hand them over to a dissector. But if I get more than one extra tvb - and a dissector that is not the generic data-dissector - I get this fault message:</p><p>"Tvbs can only be created and used in dissectors"</p><p>What am I doing wrong?</p><p>This is smallest lua file that can reproduce the problem:</p><pre><code>------------- lua dissector
local data_dis = Dissector.get (&quot;data&quot;)

-- mini dissector I would like to use on reassembled messages
local p_foo = Proto (&quot;foo&quot;, &quot;foo proto&quot;)
local f_foo_first_byte = ProtoField.uint8 (&quot;foo.ind&quot;, &quot;Index&quot;)
p_foo.fields = {f_foo_first_byte}

function p_foo.dissector(tvb, pinfo, tree)
   local subtree = tree:add (p_foo, tvb())
   subtree:add (f_foo_first_byte, tvb(0,1))
end

-- the dissector for the udp packets on port 2800
local p_bar = Proto (&quot;bar&quot;, &quot;bar proto&quot;)
local f_bar_ind = ProtoField.uint8 (&quot;bar.ind&quot;, &quot;Index&quot;)
p_bar.fields = {f_bar_ind}

function p_bar.dissector (tvb, pinfo, tree)
   local subtree = tree:add (p_bar, tvb())

   subtree:add (f_bar_ind, tvb(0,1))
   data_dis:call(tvb, pinfo, tree)

   local dissector

   local alt = 0
   -- alt = 1 -- uncomment to see that it does not works with the foo-dissector

   if alt == 0 then
      dissector = Dissector.get (&quot;data&quot;)
   else
      dissector = Dissector.get (&quot;foo&quot;)
   end

   -- The following is just done to fake reassembly
   local range = tvb(0,tvb:len())
   bytes = range:bytes()

   newTvb = ByteArray.tvb(bytes, &quot;first&quot;)
   dissector:call(newTvb, pinfo, tree)

   newTvb1 = ByteArray.tvb(bytes, &quot;second&quot;)
   dissector:call(newTvb1, pinfo, tree)

end

local udp_encap_table = DissectorTable.get(&quot;udp.port&quot;)
udp_encap_table:add(2800,p_bar)</code></pre><p>And here a script that generates a packet to dissect</p><pre><code>#!/bin/bash

port=2800

messageIndex=&quot;00&quot;
data=&quot;00010203040506070809&quot;

packetSender() {
    sudo nping 4.3.2.1 --udp -c 1 --source-ip 1.2.3.4 --source-port $port --dest-port $port --data &quot;$messageIndex$data&quot;
}

packetSender</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-tvb" rel="tag" title="see questions tagged &#39;tvb&#39;">tvb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '16, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/9fe9ccf2520bd306efc468b3c4bcea79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mj99&#39;s gravatar image" /><p><span>mj99</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mj99 has one accepted answer">50%</span></p></div></div><div id="comments-container-56110" class="comments-container"><span id="56114"></span><div id="comment-56114" class="comment"><div id="post-56114-score" class="comment-score">1</div><div class="comment-text"><p>Not that I would understand why, but if you first create both new tvbs and then dissect them, it works:</p><pre><code>newTvb = ByteArray.tvb(bytes, &quot;first&quot;)
newTvb1 = ByteArray.tvb(bytes, &quot;second&quot;)
dissector:call(newTvb, pinfo, tree)
dissector:call(newTvb1, pinfo, tree)</code></pre><p>makes</p><pre><code>Frame 1: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
Ethernet II, Src: Send_00 (20:53:45:4e:44:00), Dst: Receive_00 (20:52:45:43:56:00)
Internet Protocol Version 4, Src: 1.1.1.1, Dst: 2.2.2.2
User Datagram Protocol, Src Port: 2800, Dst Port: 0
bar proto
Data (10 bytes)
    Data: 00010203040506070809
    [Length: 10]
foo proto
    Index: 0
foo proto
    Index: 0</code></pre></div><div id="comment-56114-info" class="comment-info"><span class="comment-age">(03 Oct '16, 22:24)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="56137"></span><div id="comment-56137" class="comment"><div id="post-56137-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for this workaround!</p><p>I will try to use this, but I think I will have to do two passes over the tvb since I do not know how many reassembled tvbs I will get from a packet and I like to have the reassembled messages along with the fragment that made it complete.</p></div><div id="comment-56137-info" class="comment-info"><span class="comment-age">(04 Oct '16, 10:18)</span> <span class="comment-user userinfo">mj99</span></div></div><span id="56146"></span><div id="comment-56146" class="comment"><div id="post-56146-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot, I could make my dissector work based on this.</p><p>It was however quite painful. I got a lot of "expired tvb" errors before I figured out how to juggle it.</p><p>Is it my code in the question that is buggy some way I cannot see, or is it wireshark that does not support doing this with lua?</p></div><div id="comment-56146-info" class="comment-info"><span class="comment-age">(04 Oct '16, 14:55)</span> <span class="comment-user userinfo">mj99</span></div></div><span id="56190"></span><div id="comment-56190" class="comment"><div id="post-56190-score" class="comment-score">1</div><div class="comment-text"><p>I think it's a bug and I think I see where the problem is. Let me see if I can whip together a patch...</p></div><div id="comment-56190-info" class="comment-info"><span class="comment-age">(06 Oct '16, 06:46)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="56447"></span><div id="comment-56447" class="comment"><div id="post-56447-score" class="comment-score"></div><div class="comment-text"><p><span>@mj99</span> Where did you get the idea of using <code>ByteArray.tvb(bytes, "first")</code> instead of <code>bytes:tvb("first")</code>? The former is not supposed to work and might <a href="https://code.wireshark.org/review/18026">break</a> in future versions of Wireshark.</p></div><div id="comment-56447-info" class="comment-info"><span class="comment-age">(17 Oct '16, 03:41)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="56449"></span><div id="comment-56449" class="comment not_top_scorer"><div id="post-56449-score" class="comment-score"></div><div class="comment-text"><p>I'd suppose the OP has copied the idea from the "official" <a href="https://wiki.wireshark.org/LuaAPI/ByteArray">example page</a>.</p></div><div id="comment-56449-info" class="comment-info"><span class="comment-age">(17 Oct '16, 04:09)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-56110" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-56110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56192"></span>

<div id="answer-container-56192" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56192-score" class="post-score" title="current number of votes">2</div><span id="post-56192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mj99 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It seems this is a bug--what <span>@sindy</span> noticed made that much easier to see.</p><p>I've attempted to fix the problem in <a href="https://code.wireshark.org/review/18095">change 18095</a>. I don't have time at the moment to actually test the change--maybe tonight (if you don't beat me to it :-)).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '16, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-56192" class="comments-container"><span id="56205"></span><div id="comment-56205" class="comment"><div id="post-56205-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your work. I am, for the moment, away from my build environment. I will try to build tomorrow CET.</p></div><div id="comment-56205-info" class="comment-info"><span class="comment-age">(06 Oct '16, 14:08)</span> <span class="comment-user userinfo">mj99</span></div></div><span id="56242"></span><div id="comment-56242" class="comment"><div id="post-56242-score" class="comment-score"></div><div class="comment-text"><p>I did not manage to build wireshark with lua support. Can I download a build with the change to test it?</p></div><div id="comment-56242-info" class="comment-info"><span class="comment-age">(08 Oct '16, 15:30)</span> <span class="comment-user userinfo">mj99</span></div></div><span id="56349"></span><div id="comment-56349" class="comment"><div id="post-56349-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I haven't had a chance to do anything more with this yet. Once I can test it then I can merge the change and you'll be able to pick up an automated build. I just need some free time...</p></div><div id="comment-56349-info" class="comment-info"><span class="comment-age">(13 Oct '16, 12:31)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="56367"></span><div id="comment-56367" class="comment"><div id="post-56367-score" class="comment-score"></div><div class="comment-text"><p>It turns out my change was incomplete but I fixed that and now it works well. Just awaiting code-review and merge.</p></div><div id="comment-56367-info" class="comment-info"><span class="comment-age">(13 Oct '16, 18:55)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="56374"></span><div id="comment-56374" class="comment"><div id="post-56374-score" class="comment-score"></div><div class="comment-text"><p>The change was merged about an hour ago. You should be able to pick up an automated build from <a href="https://www.wireshark.org/download/automated/">here</a> fairly soon. Choose a version with the number 1042 or higher (as in "v2.3.0rc0-1042-g3868252").</p></div><div id="comment-56374-info" class="comment-info"><span class="comment-age">(14 Oct '16, 10:57)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="56385"></span><div id="comment-56385" class="comment not_top_scorer"><div id="post-56385-score" class="comment-score"></div><div class="comment-text"><p>The problem occurs in a very specific situation: a Lua dissector calls another Lua dissector, then invokes <code>bytearray:new("source")</code>. Would it be worth backporting it? Otherwise it takes about another 8 months before it is released I guess.</p></div><div id="comment-56385-info" class="comment-info"><span class="comment-age">(14 Oct '16, 14:07)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="56399"></span><div id="comment-56399" class="comment not_top_scorer"><div id="post-56399-score" class="comment-score"></div><div class="comment-text"><p>Yep, just did (actually before I saw your note but...).</p></div><div id="comment-56399-info" class="comment-info"><span class="comment-age">(14 Oct '16, 18:09)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-56192" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-56192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

