+++
type = "question"
title = "How do I extract buffer values from a ProtoField?"
description = '''Let&#x27;s say I have an packet that looks like this:  [ ETH, IP, myHeader ]  MyHeader is my own protocol which consists of myHeader.x1 (the first three bits) and myHeader.x2 (the next 5 bits).  What I want to do is loop through the whole pcap file to find all the frames, where a condition is fulfilled t...'''
date = "2013-04-18T04:29:00Z"
lastmod = "2013-04-18T22:20:00Z"
weight = 20566
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/20566" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do I extract buffer values from a ProtoField?](/questions/20566/how-do-i-extract-buffer-values-from-a-protofield)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20566-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Let's say I have an packet that looks like this:</p><pre><code>[ ETH, IP, myHeader ]</code></pre><p>MyHeader is my own protocol which consists of <code>myHeader.x1</code> (the first three bits) and <code>myHeader.x2</code> (the next 5 bits).</p><p>What I want to do is loop through the whole pcap file to find all the frames, where a condition is fulfilled that <code>myHeader.x1</code> AND <code>myHeader.x2</code> are of a certain value.</p><p>The place where I am stuck at is the <code>if</code>-statement. I do not know how to retreive the value for x1 and x2. The following snippet:</p><pre><code>local variable = buffer(offset, 1) 
if (variable:uint() == somevalue) 
...</code></pre><p>works, but it gets the whole byte while I am only interested in the first three bits and the other five bits as two separate values. Does anybody know how to do this? I will provide the code for further clarity below. Look at the <code>if</code>-statement.</p><pre><code>-- Initiate and collect data
MYPROTO = Proto (&quot;myproto&quot;, &quot;myheader&quot;)

local Header = MYPROTO.fields
Header.x1 = ProtoField.uint8 (&quot;myproto.x1&quot;, &quot;X1&quot;, base.DEC, nil, 0xE0)
Header.x2 = ProtoField.uint8 (&quot;myproto.x2&quot;, &quot;X2&quot;, base.DEC, nil, 0x1F)

function MYPROTO.dissector (buffer, pinfo, tree)
    local offset = 0
    local subtree = tree:add (MYPROTO, buffer(offset, 2))        
    subtree:add (Header.x1, buffer(offset, 1))
    subtree:add (Header.x2, buffer(offset, 1))
    offset = offset + 1

    if (Header.x1 == 2 AND Header.x2 == 3) then
        print frame.row 
    end
end

-- Register the dissector
udp_table = DissectorTable.get(&quot;ip.proto&quot;)
udp_table:add(0xFFF, MYPROTO)</code></pre><p>Any help is greatly appreciated!</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '13, 04:29</strong></p><img src="https://secure.gravatar.com/avatar/7709c0c87ed4ba426f119187d3f0c705?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harkap&#39;s gravatar image" /><p>harkap<br />
<span class="score" title="5 reputation points">5</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harkap has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Apr '13, 22:24</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-20566" class="comments-container"></div><div id="comment-tools-20566" class="comment-tools"></div><div class="clear"></div><div id="comment-20566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20610"></span>

<div id="answer-container-20610" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20610-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>if (Header.x1 == 2 AND Header.x2 == 3)</code></pre><p>This is a common mistake. The <code>ProtoField</code> cannot be used to extract values in this manner. You have to manipulate the <code>TvbRange</code> (the object of <code>buffer(offset, 1)</code> in your code) to get the bitfields. There are a few ways to do this.</p><h2 id="option-1-tvbrangebitfield">Option 1: <code>TvbRange:bitfield()</code></h2><p>You can use <a href="http://wiki.wireshark.org/LuaAPI/Tvb#tvbrange:bitfield.28.5Boffset.5D.2C_.5Blength.5D.29"><code>TvbRange:bitfield()</code></a> to extract a subset of bits from the buffer.</p><pre><code>-- get first 3 bits starting from bit 0 (leftmost bit);
-- and next 5 bits starting from bit 3
local first3 = buffer(offset,1):bitfield(0,3)
local next5 = buffer(offset,1):bitfield(3,5)

if (first3 == 2) AND (next5 == 3) then
     print &#39;foo&#39;
end</code></pre><h2 id="option-2-lua-bitop">Option 2: Lua <code>bitop</code></h2><p>You can use the built-in Lua <a href="http://bitop.luajit.org/api.html"><code>bitop</code> library</a> to mask and/or shift bits of an integer, extracted from the buffer:</p><pre><code>local byte = buffer(0,1):uint()

-- assume bit 0 is leftmost
-- right-shift 5 bits to get upper 3
local bits0to2 = bit.rshift(byte, 5)

-- mask out upper 3 bits to get lower 5
local bits3to7 = bit.band(byte, 0x1F)</code></pre><h2 id="option-3-8-bit-comparison">Option 3: 8-bit comparison</h2><p>If you always compare the first 3 bits and the last 5, you could probably compare all 8 bits at once:</p><pre><code>-- in your example, you check for `x1 == 2` and `x2 == 3`,
-- which is equal to `0100 0011` (`0x43`)
if buffer(offset, 1):uint() == 0x43 then
    print &#39;foo&#39;
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '13, 22:20</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Apr '13, 22:22</p></div></div><div id="comments-container-20610" class="comments-container"><span id="20623"></span><div id="comment-20623" class="comment"><div id="post-20623-score" class="comment-score"></div><div class="comment-text"><p>Thank you helloworld, you are king =)</p><p>just wish it had been stated somewhere as easily as you just showed here so that I wouldnt have spent so much time on this..</p></div><div id="comment-20623-info" class="comment-info"><span class="comment-age">(19 Apr '13, 06:18)</span> harkap</div></div></div><div id="comment-tools-20610" class="comment-tools"></div><div class="clear"></div><div id="comment-20610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

