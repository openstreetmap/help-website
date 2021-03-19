+++
type = "question"
title = "lua udp reassembly"
description = '''Hi, I am new both to writing dissectors and to lua, but I have anyway managed to write a mostly working set of dissectors for our protocol stack. Thanks a lot for wireshark as a whole and for the lua capabilities. It makes it really easy to work with. My biggest remaining problem (as in &quot;mostly work...'''
date = "2016-09-17T08:50:00Z"
lastmod = "2016-09-22T14:44:00Z"
weight = 55621
keywords = [ "lua", "udp", "multipart", "reassembly" ]
aliases = [ "/questions/55621" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [lua udp reassembly](/questions/55621/lua-udp-reassembly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55621-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am new both to writing dissectors and to lua, but I have anyway managed to write a mostly working set of dissectors for our protocol stack. Thanks a lot for wireshark as a whole and for the lua capabilities. It makes it really easy to work with.</p><p>My biggest remaining problem (as in "mostly working") is that my messages can be segmented into several UDP-packets. I cannot figure out how to save the segments for later use and then, when all segments are received, concatenate them.</p><p>I would appreciate some hints here.</p><p>This could have been my protocol:</p><pre><code>--- dissector
local data_dis = Dissector.get (&quot;data&quot;)

local p_frag = Proto (&quot;frag&quot;, &quot;Frag proto&quot;)

local f_frag_message_index = ProtoField.uint32 (&quot;frag.message_index&quot;,&quot;Message index&quot;)
local f_frag_part_index = ProtoField.uint8 (&quot;frag.part_index&quot;,&quot;Part Index&quot;)
local f_frag_part_length = ProtoField.uint8 (&quot;frag.part_length&quot;,&quot;Part Length&quot;)
local f_frag_part_lastIndicator = ProtoField.uint8 (&quot;frag.last_indicator&quot;,&quot;Last Part Indicator&quot;)

p_frag.fields = {f_frag_message_index,
                 f_frag_part_index,
                 f_frag_part_length,
                 f_frag_part_lastIndicator}

function p_frag.dissector(tvb, pinfo, tree)
   local subtree = tree:add (p_frag, tvb())
   subtree:add (f_frag_message_index, tvb(0,4))
   subtree:add (f_frag_part_index, tvb(4,1))
   subtree:add (f_frag_part_length, tvb(5,1))
   subtree:add (f_frag_part_lastIndicator, tvb(6,1))

-- Actually, here I call one of few other dissectors depending of the
-- value of the next byte, bur for this example it would be nice to
-- send the complete message to the data dissector.
   data_dis:call(tvb(7):tvb(),pinfo,subtree)
end

local udp_encap_table = DissectorTable.get(&quot;udp.port&quot;)
udp_encap_table:add(2900,p_frag)</code></pre><p>--- end of dissector</p><pre><code>## script to generate a few packets
#!/bin/bash
messageIndex=&quot;00000000&quot;
partIndex=&quot;00&quot;
partLength=&quot;05&quot;
lastIndicator=&quot;01&quot;
data=&quot;53686f7274&quot;

packetSender() {
    sudo nping 4.3.2.1 --udp -c 1 --source-ip 1.2.3.4 --source-port 2900 --dest-port 2900 --data &quot;$messageIndex$partIndex$partLength$lastIndicator$data&quot;
}

# First complete packet
packetSender

# Then a fragmented packet
# first fragment of index 1
messageIndex=&quot;00000001&quot;
partIndex=&quot;00&quot;
partLength=&quot;04&quot;
lastIndicator=&quot;00&quot;
data=&quot;4d756368&quot;
packetSender

# Beware, new message!
messageIndex=&quot;00000002&quot;
partIndex=&quot;00&quot;
partLength=&quot;06&quot;
lastIndicator=&quot;01&quot;
data=&quot;426577617265&quot;
packetSender

#second fragment of index 1
messageIndex=&quot;00000001&quot;
partIndex=&quot;01&quot;
partLength=&quot;06&quot;
lastIndicator=&quot;00&quot;
data=&quot;2c206d756368&quot;
packetSender

#third and final fragment of index 1
messageIndex=&quot;00000001&quot;
partIndex=&quot;02&quot;
partLength=&quot;07&quot;
lastIndicator=&quot;01&quot;
data=&quot;206c6f6e676572&quot;
packetSender
## end of packet generating script</code></pre></div><div id="question-tags" class="tags-container tags">lua udp multipart reassembly</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '16, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/9fe9ccf2520bd306efc468b3c4bcea79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mj99&#39;s gravatar image" /><p>mj99<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mj99 has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Sep '16, 14:53</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-55621" class="comments-container"></div><div id="comment-tools-55621" class="comment-tools"></div><div class="clear"></div><div id="comment-55621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55764"></span>

<div id="answer-container-55764" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55764-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In case someone wants to do reassembly in lua - this is what I will be using until someone points out improvements:</p><pre><code>local data_dis = Dissector.get (&quot;data&quot;)

local p_frag = Proto (&quot;frag&quot;, &quot;Frag proto&quot;)

local f_frag_message_index = ProtoField.uint32 (&quot;frag.message_index&quot;,&quot;Message index&quot;)
local f_frag_part_index = ProtoField.uint8 (&quot;frag.part_index&quot;,&quot;Part Index&quot;)
local f_frag_part_length = ProtoField.uint8 (&quot;frag.part_length&quot;,&quot;Part Length&quot;)
local f_frag_part_lastIndicator = ProtoField.uint8 (&quot;frag.last_indicator&quot;,&quot;Last Part Indicator&quot;)

p_frag.fields = {f_frag_message_index,
                 f_frag_part_index,
                 f_frag_part_length,
                 f_frag_part_lastIndicator}

function p_frag.init ()
   -- print (&quot;(re-)initialise&quot;)
   fragments = {}
   concats = {}
end

function p_frag.dissector(tvb, pinfo, tree)
   local subtree = tree:add (p_frag, tvb())

   local messageInd = tvb(0,4):uint()
   subtree:add (f_frag_message_index, tvb(0,4))

   local partInd = tvb(4,1):uint()
   subtree:add (f_frag_part_index, tvb(4,1))
   subtree:add (f_frag_part_length, tvb(5,1))

   local lastFlag = tvb(6,1):uint ()
   subtree:add (f_frag_part_lastIndicator, tvb(6,1))

   if pinfo.visited == false then
      local range = tvb(7)
      local bytes = range:bytes()
      local completeMessage
      local newTvb
      local B = 0
      local F = 1

      if fragments[messageInd] == nil then
         fragments[messageInd] = {}
         -- print (&quot;Creating mess &quot; .. messageInd)
      end

      if fragments[messageInd][partInd] == nil then
         fragments[messageInd][partInd] = {}
         -- print (&quot;Creating mess &quot; .. messageInd .. &quot;, part &quot; .. partInd)
      end

      fragments[messageInd][partInd][B] = bytes
      fragments[messageInd][partInd][F] = lastFlag

      local ind = 0
      completeMessage = ByteArray.new()
      while ind &lt; 8 do -- maximum 8 fragments
         -- print (&quot;Testing ind = &quot; .. ind)
         if fragments[messageInd][ind] ~= nil then
            completeMessage = completeMessage .. fragments[messageInd][ind][B]
         else
            -- print (&quot;No part with that index, break&quot;)
            break
         end
         if fragments[messageInd][ind][F] == 1 then
            -- print (&quot;Flag, break!&quot;)
            if ind &gt; 0 then
               -- print(&quot;pinfo.number = &quot; .. pinfo.number)
               concats[pinfo.number] = completeMessage
               fragments[messageInd] = {}
            end
            break
         end
         ind = ind + 1
      end
   end

   data_dis:call(tvb(7):tvb(),pinfo,subtree)
   if concats[pinfo.number] ~= nil then
      newTvb = ByteArray.tvb(concats[pinfo.number])
      data_dis:call(newTvb(0):tvb(), pinfo, subtree)
   end
end

local udp_encap_table = DissectorTable.get(&quot;udp.port&quot;)
udp_encap_table:add(2900,p_frag)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '16, 14:44</strong></p><img src="https://secure.gravatar.com/avatar/9fe9ccf2520bd306efc468b3c4bcea79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mj99&#39;s gravatar image" /><p>mj99<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mj99 has one accepted answer">50%</span></p></div></div><div id="comments-container-55764" class="comments-container"></div><div id="comment-tools-55764" class="comment-tools"></div><div class="clear"></div><div id="comment-55764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55726"></span>

<div id="answer-container-55726" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55726-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ok, now I can concatenate messages spread over several packets. I can however see some problems with my concatenating technique:</p><ol><li>It will consume quite some memory since all fragments are saved forever.</li><li>I will run into problems when my message indices are reused.</li></ol><p>I would prefer to see the message together with dissection of the last received part of the message.</p><p>Can the fragments be discarded and the concatenated messages be saved somehow associated with the packet that contains the last part of the message? How is this usually handled?</p><pre><code>-- dissector
-- Containing debug prints

fragments = {}

local data_dis = Dissector.get (&quot;data&quot;)

local p_frag = Proto (&quot;frag&quot;, &quot;Frag proto&quot;)

local f_frag_message_index = ProtoField.uint32 (&quot;frag.message_index&quot;,&quot;Message index&quot;)
local f_frag_part_index = ProtoField.uint8 (&quot;frag.part_index&quot;,&quot;Part Index&quot;)
local f_frag_part_length = ProtoField.uint8 (&quot;frag.part_length&quot;,&quot;Part Length&quot;)
local f_frag_part_lastIndicator = ProtoField.uint8 (&quot;frag.last_indicator&quot;,&quot;Last Part Indicator&quot;)

p_frag.fields = {f_frag_message_index,
                 f_frag_part_index,
                 f_frag_part_length,
                 f_frag_part_lastIndicator}

function p_frag.dissector(tvb, pinfo, tree)
   local subtree = tree:add (p_frag, tvb())

   local messageInd = tvb(0,4):uint()
   subtree:add (f_frag_message_index, tvb(0,4))

   local partInd = tvb(4,1):uint()
   subtree:add (f_frag_part_index, tvb(4,1))
   subtree:add (f_frag_part_length, tvb(5,1))

   local lastFlag = tvb(6,1):uint ()
   subtree:add (f_frag_part_lastIndicator, tvb(6,1))

   local range = tvb(7)
   local bytes = range:bytes()
   local completeMessage
   local concatenated = 0
   local newTvb
   local B = 0
   local F = 1

   if fragments[messageInd] == nil then
      fragments[messageInd] = {}
      print (&quot;Creating mess &quot; .. messageInd)
   end

   if fragments[messageInd][partInd] == nil then
      fragments[messageInd][partInd] = {}
      print (&quot;Creating mess &quot; .. messageInd .. &quot;, part &quot; .. partInd)
   end

   fragments[messageInd][partInd][B] = bytes
   fragments[messageInd][partInd][F] = lastFlag

   local ind = 0
   completeMessage = ByteArray.new()
   while ind &lt; 8 do -- maximum 8 fragments
      print (&quot;Testing ind = &quot; .. ind)
      if fragments[messageInd][ind] ~= nil then
         completeMessage = completeMessage .. fragments[messageInd][ind][B]
      else
         print (&quot;No part with that index, break&quot;)
         break
      end
      if fragments[messageInd][ind][F] == 1 then
         print (&quot;Flag, break!&quot;)
         if ind &gt; 0 then
            print (&quot;Concatenated&quot;)
            concatenated = 1
         end
         break
      end
      ind = ind + 1
   end

   data_dis:call(tvb(7):tvb(),pinfo,subtree)
   if concatenated == 1 then
      newTvb = ByteArray.tvb(completeMessage)
      data_dis:call(newTvb(0):tvb(), pinfo, subtree)
   end
end

local udp_encap_table = DissectorTable.get(&quot;udp.port&quot;)
udp_encap_table:add(2900,p_frag)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '16, 13:36</strong></p><img src="https://secure.gravatar.com/avatar/9fe9ccf2520bd306efc468b3c4bcea79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mj99&#39;s gravatar image" /><p>mj99<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mj99 has one accepted answer">50%</span></p></div></div><div id="comments-container-55726" class="comments-container"><span id="55752"></span><div id="comment-55752" class="comment"><div id="post-55752-score" class="comment-score"></div><div class="comment-text"><p>Impressive - you're probably the first to actually do reassembly in Lua. :-)</p><p>[Note that the below is based on my memory of how Wireshark's reassembly code works; I haven't had time to actually review your code.]</p><p>Wireshark's internal reassembly routines (which AFAIK aren't available via the Lua API) store the reassembled data forever (note: once the message is reassembled only the reassembled message is stored; the fragments are freed). That's needed because Wireshark is only guaranteed to make a single pass through the file (while loading it) whereas the user may click around (and thus want a full dissection of whatever packet s/he clicks on) and so that reassembly data has to be available without redissecting the earlier (fragment) packets.</p><p>The reassembled data is stored such that it's only retrieved when the final frame in the PDU is dissected.</p><p>Hope that helps...</p></div><div id="comment-55752-info" class="comment-info"><span class="comment-age">(22 Sep '16, 06:18)</span> JeffMorriss ♦</div></div><span id="55763"></span><div id="comment-55763" class="comment"><div id="post-55763-score" class="comment-score"></div><div class="comment-text"><p>What is impressive is that is possible to do it with so little work. The praise goes to wireshark - or really to all persons involved in creating and maintaining it it.</p></div><div id="comment-55763-info" class="comment-info"><span class="comment-age">(22 Sep '16, 13:47)</span> mj99</div></div></div><div id="comment-tools-55726" class="comment-tools"></div><div class="clear"></div><div id="comment-55726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

