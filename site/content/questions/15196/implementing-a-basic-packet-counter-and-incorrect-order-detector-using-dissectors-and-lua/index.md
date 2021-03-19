+++
type = "question"
title = "Implementing a basic packet counter and incorrect order detector using dissectors and Lua"
description = '''I am trying to implement, using Lua, a dissector which tells me whether the packets sent are arriving or not.  To achieve this, on top of UDP I have implemented a custom protocol with a field &quot;ID&quot; which is auto-incremented by one on each packet. I got the dissector to process the fields, but I am no...'''
date = "2012-10-23T08:31:00Z"
lastmod = "2012-10-31T09:26:00Z"
weight = 15196
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/15196" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Implementing a basic packet counter and incorrect order detector using dissectors and Lua](/questions/15196/implementing-a-basic-packet-counter-and-incorrect-order-detector-using-dissectors-and-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15196-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to implement, using Lua, a dissector which tells me whether the packets sent are arriving or not. To achieve this, on top of UDP I have implemented a custom protocol with a field "ID" which is auto-incremented by one on each packet.</p><p>I got the dissector to process the fields, but I am not able to make it read the <em>previous</em> packet ID and report whether the current packet ID is in the expected order.</p><p>My code:</p><pre><code>packet_counter=0
function ogg.init()
  packet_counter=0
end

function ogg.dissector(buffer, pinfo, tree)
    local index

    --Get the expected index and store it to a global (and unique per packet) variable
    if (not pinfo.private.expected) then
      pinfo.private.expected=packet_counter+1
      --Get the new index (the current packet ID field)
      index=buffer(2,2):uint()
      --Set it as the new expected packet
      packet_counter=index
    end

    if (tree) then
      --Make all the packet processing here. Somewhere among this:
      if (tonumber(pinfo.private.expected) ~= index) then
        pinfo.cols.info = &quot;ID: &quot;..index..&quot; is Invalid! Expected &quot;.. pinfo.private.expected
      end          
    end
end</code></pre><p>I am getting several packets with the information correct, but other packets are getting the <code>packet_counter</code> variable different than what it should be, i.e. the previous packet was 100, current is 101, and it is saying that expected is 154, as if the processing order of the packets weren't sequential.</p><p>What is wrong here?</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '12, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/2ade52d7e2eaa13aed5f7eea25ed6745?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LoPiTaL&#39;s gravatar image" /><p>LoPiTaL<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LoPiTaL has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Oct '12, 18:18</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-15196" class="comments-container"><span id="15205"></span><div id="comment-15205" class="comment"><div id="post-15205-score" class="comment-score"></div><div class="comment-text"><p><em>(Comment only)</em> First, I believe you should be using a <a href="http://wiki.wireshark.org/Lua/Taps">Lua tap</a> for your purposes, not a dissector. A packet can be dissected (and re-dissected) several times in one session (e.g., clicking between packets in the <em>Packet List Pane</em> causes the packet to be dissected), which might be a contributor to your problem. Try a tap instead.</p></div><div id="comment-15205-info" class="comment-info"><span class="comment-age">(23 Oct '12, 18:32)</span> helloworld</div></div><span id="15210"></span><div id="comment-15210" class="comment"><div id="post-15210-score" class="comment-score"></div><div class="comment-text"><p>Hi helloworld! Thanks for your comment. I've been looking for taps, but I am not able to pass info from the tap to the dissector. It seems like the dissector is processed BEFORE the tap, is this right?So at the momment of dissection,there is no information about packet ordering,thus I can't know if it is out of order or not. Also from the tap I haven't got the tree info, nor the GUI columns info, so I cannot print the msg "out of order" anywhere. How can this be made? Note that I want to see the information using the Wireshark GUI, not the command line version. Thanks in advance, LoPiTaL</p></div><div id="comment-15210-info" class="comment-info"><span class="comment-age">(24 Oct '12, 00:48)</span> LoPiTaL</div></div><span id="15213"></span><div id="comment-15213" class="comment"><div id="post-15213-score" class="comment-score"></div><div class="comment-text"><p>I don't know why the</p><pre><code>  if (not pinfo.private.expected) then
      pinfo.private.expected=packet_counter+1
      --Get the new index (the current packet ID field)
      index=buffer(2,2):uint()
      --Set it as the new expected packet
      packet_counter=index
    end</code></pre><p>didn't worked between passes of the dissector. Somebody can help here? Finally I have worked around this with a global array variable in wich I store the same info:</p><pre><code>    if (not out_of_order[index]) then
      if index~=packet_counter+1 then
        out_of_order[index]=packet_counter+1
      else
        out_of_order[index]=-1
      end

      packet_counter=index
    end</code></pre><p>and it worked pretty fine. But I have the feeling that this will be pretty memory consuming... :D Best regards, LoPiTaL</p></div><div id="comment-15213-info" class="comment-info"><span class="comment-age">(24 Oct '12, 01:58)</span> LoPiTaL</div></div><span id="15238"></span><div id="comment-15238" class="comment"><div id="post-15238-score" class="comment-score"></div><div class="comment-text"><blockquote><p>It seems like the dissector is processed BEFORE the tap, is this right?</p></blockquote><p>Yes, a packet is dissected before reaching a tap. The purpose of a tap is to "listen" for packets of interest (defined by a filter), but in order to determine whether a packet is "interesting", Wireshark must first dissect it.</p></div><div id="comment-15238-info" class="comment-info"><span class="comment-age">(24 Oct '12, 21:48)</span> helloworld</div></div><span id="15239"></span><div id="comment-15239" class="comment"><div id="post-15239-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So at the momment of dissection,there is no information about packet ordering,thus I can't know if it is out of order or not.</p></blockquote><p>Based on your dissector code in the question, your packets contain some kind of index (sequence ID) in <code>buffer(2,2):uint()</code>. The buffer is passed to a tap, so you should be able to determine packet sequence.</p></div><div id="comment-15239-info" class="comment-info"><span class="comment-age">(24 Oct '12, 21:49)</span> helloworld</div></div><span id="15240"></span><div id="comment-15240" class="comment not_top_scorer"><div id="post-15240-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Also from the tap I haven't got the tree info, nor the GUI columns info, so I cannot print the msg "out of order" anywhere.</p></blockquote><p>A tap cannot modify the packet's protocol tree (in the <em>Packet Details Pane</em>), but it <em>can</em> change the packet's columns (in the <em>Packet List Pane</em>) via the <code>pinfo.cols</code> table (<code>pinfo</code> is passed to the tap).</p></div><div id="comment-15240-info" class="comment-info"><span class="comment-age">(24 Oct '12, 21:49)</span> helloworld</div></div></div><div id="comment-tools-15196" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-15196-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15423"></span>

<div id="answer-container-15423" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15423-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should be using pinfo.visited as suggested earlier.</p><p>The problem is that dissectors are running twice before your display is constructed when your wireshark opens and then ever time you click on a packet.</p><p>So you think you see pinfo.visited it always as True. Where it's not.</p><p>Have a look at this question of mine - <a href="http://ask.wireshark.org/questions/14936/lua-postdissector-executed-every-time-i-click-on-a-packet">Lua postdissector executed every time I click on a packet</a></p><p>Try below code ( not sure if it will work but you should get the idea )</p><p>I'd suggest keeping data in outside table.</p><pre><code>packet_counter=0

function ogg.init()
  packet_counter=0
end

-- Define a table your data
local pkts = {}

function ogg.dissector(buffer, pinfo, tree)
    local index

    local pkt_no = tostring(pinfo.number)

    if not pinfo.visited then
        if not pkts[pkt_no] then
            pkts[pkt_no] = {}
        end
        -- add the stuff you want to keep into your table
        pkts[pkt_no][&#39;counter&#39;] = packet_counter + 1
    end

    index=buffer(2,2):uint()
    packet_counter=index

    if pkts[pkt_no] then
        pinfo.cols.info = &quot;ID: &quot;..index..&quot; is Invalid! Expected &quot;.. pkts[pkt_no][&#39;counter&#39;]
    end

end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '12, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-15423" class="comments-container"></div><div id="comment-tools-15423" class="comment-tools"></div><div class="clear"></div><div id="comment-15423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15211"></span>

<div id="answer-container-15211" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15211-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have no experience with Lua dissectors, but with C dissectors you can check the flag "pinfo-&gt;fd-&gt;flags.visited" whether it is the first time a frame is dissected (on the first sequential run through the packets).</p><p>You then have to create session and packet states by using conversations and per-packet data. As is described in "doc/README.developer" in paragraphs 2.2 and 2.5.</p><p>I'm sure there is an interface to these in Lua as well, but I have no experience with Lua dissectors myself unfortunately...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '12, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Oct '12, 21:26</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-15211" class="comments-container"><span id="15212"></span><div id="comment-15212" class="comment"><div id="post-15212-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the comment, but I checked the pinfo.visited flag in LUA, and it seems to be always set to True :(, so it does not worked for me. Where can I find the "doc/README.developer" document? In the installation dir of WireShark seems not to be. I am pretty interested with the per-packet data and the conversations information. Best regards, LoPiTaL</p></div><div id="comment-15212-info" class="comment-info"><span class="comment-age">(24 Oct '12, 01:54)</span> LoPiTaL</div></div><span id="15237"></span><div id="comment-15237" class="comment"><div id="post-15237-score" class="comment-score"></div><div class="comment-text"><p><a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.developer"><code>README.developer</code></a> is in the Wireshark source tree (it's not installed). Lua has no specific interface for conversations, but you're welcome to <a href="http://bugs.wireshark.org">submit a bug report</a> that requests this enhancement.</p></div><div id="comment-15237-info" class="comment-info"><span class="comment-age">(24 Oct '12, 21:32)</span> helloworld</div></div></div><div id="comment-tools-15211" class="comment-tools"></div><div class="clear"></div><div id="comment-15211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

