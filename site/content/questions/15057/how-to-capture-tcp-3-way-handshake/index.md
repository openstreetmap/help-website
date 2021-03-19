+++
type = "question"
title = "How to capture tcp 3 way handshake"
description = '''I&#x27;m looking to capture the conversation between 2 hosts that contains the 3 way handshake. I&#x27;m not sure if this would be doable with a capture filter. Or maybe it&#x27;s a display filter. I&#x27;m thinking something like: tcp.flags == 0x02 | tcp.flags == 0x10 But I don&#x27;t know if this is just a display capture...'''
date = "2012-10-17T07:08:00Z"
lastmod = "2016-06-12T00:47:00Z"
weight = 15057
keywords = [ "capture", "3", "handshake", "way", "tcp" ]
aliases = [ "/questions/15057" ]
osqa_answers = 8
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture tcp 3 way handshake](/questions/15057/how-to-capture-tcp-3-way-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15057-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking to capture the conversation between 2 hosts that contains the 3 way handshake. I'm not sure if this would be doable with a capture filter. Or maybe it's a display filter. I'm thinking something like: tcp.flags == 0x02 | tcp.flags == 0x10 But I don't know if this is just a display capture. It doesn't seem to be recognized in capture filter box. Or maybe the concept is to to set a display filter of tcp.flags == 0x02 | tcp.flags == 0x10 and then capture all traffic and only this syn, syn ack, or ack will be displayed.</p></div><div id="question-tags" class="tags-container tags">capture 3 handshake way tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '12, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/a472d068843eefd8a4ef69c4f94e4160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gipper&#39;s gravatar image" /><p>gipper<br />
<span class="score" title="30 reputation points">30</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gipper has no accepted answers">0%</span></p></div></div><div id="comments-container-15057" class="comments-container"></div><div id="comment-tools-15057" class="comment-tools"></div><div class="clear"></div><div id="comment-15057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

8 Answers:

</div>

</div>

<span id="15061"></span>

<div id="answer-container-15061" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15061-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could try "tcp[13] &amp; 2!=0" as a capture filter, which worked fine when I just tested it, at least for SYN and SYN/ACK packets. The third packet (ACK) of the handshake might be a problem because you can't just filter on ack flags - it would give you all further packets because they will probably all carry an ACK flag.</p><p>I think the other filters you mentioned are all display filters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '12, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Oct '12, 10:51</p></div></div><div id="comments-container-15061" class="comments-container"></div><div id="comment-tools-15061" class="comment-tools"></div><div class="clear"></div><div id="comment-15061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15323"></span>

<div id="answer-container-15323" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15323-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I was able to take advantage of what you said Kurt with LUA.</p><p>I think I have it working. Maybe someone can run my LUA script to capture TCP handshake.</p><p>My command to run tshark from DOS:</p><p><code>tshark -X lua_script:dumptofile_ack_packet.lua -i 4 -o tcp.relative_sequence_numbers:TRUE</code></p><p>where my interface number is 4. Run tshark -D to list interfaces.<br />
This needs to be terminated with CTL-C</p><p><code>dumptofile_ack_packet.lua</code> is LUA script as shown below</p><pre><code>-- Create a file named ackpackets.cap (works for tshark only)
-- Dump file is created for all packets captured.
-- Display packets with a capture filter that adheres to display filter syntax 
firsttime = true
firstclose = false
setdumpers = true
dumpers = {}  

dumpfile={}
--Set filter to use as capture filter on next line
filter = &quot;(tcp.flags == 0x02 &amp;&amp; tcp.seq == 0) || (tcp.flags == 0x12 &amp;&amp; tcp.seq == 0) || (tcp.flags == 0x10 &amp;&amp; tcp.seq == 1)&quot;  -- syn ack
-- tcp.flags
-- 0x10 = ack
-- 0x02 = syn
-- 0x12 = syn ack
--first frame
--syn, seq = 0
--tcp.flags = 0x02  tcp.seq = 0
--second frame
--syn ack, seq = 0
--tcp.flags = 0x12
--tcp.seq = 0
--third frame
--ack, seq = 1
--tcp.flags = 0x10
--tcp.seq = 1
-- Run tshark as shown on the following line
-- tshark -X lua_script:dumptofile_ack_packet.lua -i 4 -o tcp.relative_sequence_numbers:TRUE
do

        --local dumpers = {}    
        local function init_listener()
                local tap = Listener.new(&quot;frame&quot;, filter)
                --tap = Listener.new(&quot;frame&quot;, filter)
                --A Listener, is called once for every packet that matches a certain filter or has a certain tap. 
                --It can read the tree, the packet&#39;s Tvb eventually the tapped data but it cannot add elements to the tree. 
                -- Listener.new([tap], [filter])
                -- Creates a new Listener listener
                -- tap (optional)
                --The name of this tap 
                -- filter (optional)
                --A filter that when matches the tap.packet function gets called (use nil to be called for every packet) 
                -- This case I&#39;m filtering for ip
                --Returns
                --The newly created Listener listener object

                -- we will be called once for every IP Header.
                -- If there&#39;s more than one IP header in a given packet we&#39;ll dump the packet once per every header
                function tap.packet(pinfo,tvb,ip)
                --listener.packet
                --A function that will be called once every packet matches the Listener listener filter. 
                --function tap.packet(pinfo,tvb,userdata) ... end 
                --Packet information

                --pinfo.number
                --The number of this packet in the current file
                --tvb
                --The buffer to dissect 
                        -- local means a variable local to this function

                        dumpersindex = &quot;ttt&quot;
                        local filename
                        filename =&quot;ackpackets.cap&quot;
                        --local dumpfile

                       if setdumpers == true then

                        dumpfile = dumpers[dumpersindex]
                        setdumpers = false

                       end

                        -- Saving capture files 
                        -- dumpers
                        --Dumper.new(filename, [filetype], [encap])
                        --Creates a file to write packets. Dumper:new_for_current() will probably be a better choice. 
                        --Arguments
                        --filename
                        --The name of the capture file to be created

                        --filetype (optional)
                        --The type of the file to be created

                        --encap (optional)
                        --The encapsulation to be used in the file to be created

                        -- The case below is just the file name
                        -- where dir is a variable of the directory
                        -- ip_src is a variable which was from
                        -- tap variable ip.src

                            if  firsttime == true then

                                dumpfile = Dumper.new_for_current( filename )
                               firsttime=false

                            end  -- end if  firsttime == true then

                        --dumper:dump_current()
                        --Dumps the current packet as it is

                        dumpfile:dump_current()

                        --dumper:flush()
                        --Writes all unsaved data of a dumper to the disk
                       -- dumpfile:flush()

                        --Now same for destination IP address to a seperate file

                end  -- end function tap.packet(pinfo,tvb,ip)

                --listener.draw
                --A function that will be called once every few seconds to redraw the gui objects in tshark this funtion is 
                --called oly at the very end of the capture file. function tap.draw(userdata) ... end 
                function tap.draw()

                end  -- end function tap.draw()

               function tap.reset()
               --listener.reset
               -- A function that will be called at the end of the capture run. function tap.reset(userdata) ... end

                     --   dumpers = {}
                end  -- end function tap.reset()
        end
        init_listener()

end  -- do loop
dumpfile:flush()
dumper:close()</code></pre><pre><code></code></pre></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '12, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/a472d068843eefd8a4ef69c4f94e4160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gipper&#39;s gravatar image" /><p>gipper<br />
<span class="score" title="30 reputation points">30</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gipper has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jun '16, 06:50</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-15323" class="comments-container"><span id="15330"></span><div id="comment-15330" class="comment"><div id="post-15330-score" class="comment-score"></div><div class="comment-text"><p>are you sure this is the whole script? It really does not do very much. Especially it does not filter on any flags, etc.</p></div><div id="comment-15330-info" class="comment-info"><span class="comment-age">(29 Oct '12, 04:36)</span> Kurt Knochner ♦</div></div><span id="15405"></span><div id="comment-15405" class="comment"><div id="post-15405-score" class="comment-score"></div><div class="comment-text"><p>Try this link for 3 way handshake capture with LUA</p><p><a href="http://pastebin.com/raw/FDRygmuW">http://pastebin.com/raw/FDRygmuW</a></p></div><div id="comment-15405-info" class="comment-info"><span class="comment-age">(30 Oct '12, 17:11)</span> gipper</div></div></div><div id="comment-tools-15323" class="comment-tools"></div><div class="clear"></div><div id="comment-15323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15064"></span>

<div id="answer-container-15064" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15064-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm looking to capture the conversation between 2 hosts that <strong>contains the 3 way handshake</strong>. I'm not sure if this would be doable with a capture filter.</p></blockquote><p>to be specific: it's not possible to capture <strong>only</strong> the <strong>full</strong> 3-way handshake (SYN,SYN-ACK,ACK), as it's impossible to identify the single ACK in the handshake with tcpdump. The best you can achive is what <strong>Jasper</strong> suggested. This will capture the SYN and the SYN-ACK, however <strong>not</strong> the final ACK of the 3-way handshake.</p><p>The same holds true for Wireshark display filters. Even there it is not possible to capture/filter the final ACK of the 3-way handshake, <strong>without</strong> getting the rest of the communication (ACK flag set) as well.</p><p>You could do it with a Listener in Lua, but that would require some programming.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '12, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Oct '12, 11:10</p></div></div><div id="comments-container-15064" class="comments-container"></div><div id="comment-tools-15064" class="comment-tools"></div><div class="clear"></div><div id="comment-15064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15069"></span>

<div id="answer-container-15069" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15069-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't do this with a capture filter. Make sure Wireshark is using relative sequence numbers and then enter the following display filter:</p><p>(tcp.flags.syn==1 ) || (tcp.flags == 0x0010 &amp;&amp; tcp.seq==1 &amp;&amp; tcp.ack==1)</p><p>Update: Further testing shows that this display filter will display what you want most of the time, but it's not perfect. It will miss the third packet of the handshake if that packet contains data and the PSH bit is set, for example. It will also display the first packet in each direction of a TCP stream whose three-way handshake is not present in the trace file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '12, 19:34</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Oct '12, 21:14</p></div></div><div id="comments-container-15069" class="comments-container"></div><div id="comment-tools-15069" class="comment-tools"></div><div class="clear"></div><div id="comment-15069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15085"></span>

<div id="answer-container-15085" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15085-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>How about this one?</p><p>((tcp.flags.syn eq 1) || (tcp.seq eq 1 &amp;&amp; tcp.ack eq 1 &amp;&amp; frame.protocols == "eth:ip:tcp" &amp;&amp; !tcp.flags.fin eq 1))</p><p>Requires "Relative sequence numbers" in TCP Protocol Preferences.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '12, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/c23b8846cec43a35da426aa0657605a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="holmahenkel&#39;s gravatar image" /><p>holmahenkel<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="holmahenkel has no accepted answers">0%</span></p></div></div><div id="comments-container-15085" class="comments-container"></div><div id="comment-tools-15085" class="comment-tools"></div><div class="clear"></div><div id="comment-15085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30254"></span>

<div id="answer-container-30254" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30254-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I managed to come up with a pcap filter expression that captures the whole TCP setup 3-way handshake - it relies on knowing the value for window size that will be set in the 3rd packet of the handshake. For the Linux 3.8.11-ec2 kernel servers I was capturing on, this value is <code>0x01c9</code>.</p><p>The capture expression matches: any packet containing the syn flag set (first two packets of the handshake) and packets that are &lt; 68 bytes long, have only the ack flag set and have the window size set to <code>0x01c9</code> (captures only the third packet).</p><p>The capture filter expression is therefore: "( tcp[tcpflags] &amp; tcp-syn != 0 ) or ( tcp[tcpflags] = tcp-ack and less 68 and tcp[14:2] == 0x01c9 )"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '14, 17:36</strong></p><img src="https://secure.gravatar.com/avatar/f805e760a3d04dcc301cb2163a9431f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="archaelus&#39;s gravatar image" /><p>archaelus<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="archaelus has no accepted answers">0%</span></p></div></div><div id="comments-container-30254" class="comments-container"></div><div id="comment-tools-30254" class="comment-tools"></div><div class="clear"></div><div id="comment-30254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49765"></span>

<div id="answer-container-49765" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49765-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>what about</p><p>tcp.flags==0x2 || tcp.flags==0x12 || tcp.flags==0x10 and tcp.seq&lt;=1 and tcp.ack&lt;=1 and not nbss</p><p>with relative sequence numbers?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '16, 05:37</strong></p><img src="https://secure.gravatar.com/avatar/04e69a0265bca5fc93ee973095e04f00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gian%20Matteo%20Esposito&#39;s gravatar image" /><p>Gian Matteo ...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gian Matteo Esposito has no accepted answers">0%</span></p></div></div><div id="comments-container-49765" class="comments-container"></div><div id="comment-tools-49765" class="comment-tools"></div><div class="clear"></div><div id="comment-49765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53363"></span>

<div id="answer-container-53363" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53363-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This works</p><p>((tcp.flags == 0x0002) &amp;&amp; (tcp.seq == 0)) || ((tcp.flags == 0x0012) &amp;&amp; (tcp.seq == 0)) || ((tcp.flags == 0x0010) &amp;&amp; (tcp.seq == 1))</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '16, 00:47</strong></p><img src="https://secure.gravatar.com/avatar/bb70f80627326b82596e15280925b820?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gopi1828&#39;s gravatar image" /><p>gopi1828<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gopi1828 has no accepted answers">0%</span></p></div></div><div id="comments-container-53363" class="comments-container"><span id="53397"></span><div id="comment-53397" class="comment"><div id="post-53397-score" class="comment-score"></div><div class="comment-text"><p>it seems there are also some ACK-only packets not related to the 3-way handshake</p><p>maybe this should works better</p><p>((tcp.flags == 0x0002 || tcp.flags == 0x0012) &amp;&amp; tcp.seq == 0) || (tcp.flags == 0x0010 &amp;&amp; tcp.seq == 1 &amp;&amp; tcp.ack &lt;=1)</p><p>thanks</p></div><div id="comment-53397-info" class="comment-info"><span class="comment-age">(13 Jun '16, 06:14)</span> Gian Matteo ...</div></div><span id="53408"></span><div id="comment-53408" class="comment"><div id="post-53408-score" class="comment-score"></div><div class="comment-text"><p>Both still give you too many packets in some situations, e.g. FTP data tranfers where the receiver/client doesn't send anything at all.</p><p>Check out <a href="https://blog.packet-foo.com/2015/03/advanced-display-filtering/">https://blog.packet-foo.com/2015/03/advanced-display-filtering/</a></p><p>Also, the original question is about capture filtering, not display filtering.</p></div><div id="comment-53408-info" class="comment-info"><span class="comment-age">(13 Jun '16, 09:47)</span> Jasper ♦♦</div></div></div><div id="comment-tools-53363" class="comment-tools"></div><div class="clear"></div><div id="comment-53363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

