+++
type = "question"
title = "lua listener, icmp redirect packets called twice"
description = '''Hi together,  i write a small lua script, that collects connection data via tshark lua api and store this in a csv file. I use this listener function: local tap_ipv4 = create_IPv4_tap()  function tap_ipv4.packet(pinfo, tvb, ip)  some code end   All works fine. But it seems that the tap_ipv4.packet()...'''
date = "2015-11-02T12:51:00Z"
lastmod = "2015-11-03T11:18:00Z"
weight = 47170
keywords = [ "lua", "icmp", "tshark" ]
aliases = [ "/questions/47170" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [lua listener, icmp redirect packets called twice](/questions/47170/lua-listener-icmp-redirect-packets-called-twice)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47170-score" class="post-score" title="current number of votes">0</div><span id="post-47170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi together,<br />
</p><p>i write a small lua script, that collects connection data via tshark lua api and store this in a csv file.</p><p>I use this listener function:</p><pre><code>local tap_ipv4 = create_IPv4_tap()

function tap_ipv4.packet(pinfo, tvb, ip)
   some code
end</code></pre><p><br />
</p><p>All works fine. But it seems that the tap_ipv4.packet() gets called twice for IMCP redircet packets. ICMP echo/reply,TCP/UDP seems normal. I dont know if this is works as designed. Has someone else this problem?</p><p>Here is the a example code:</p><pre><code>-- function to create a IPv4 listener
function create_IPv4_tap()
    local tap = Listener.new(&quot;ip&quot;)
    return(tap)
end

-- let&#39;s create a ipv4 listener
local tap_ipv4 = create_IPv4_tap()

-- will be called once for every IP Header.
function tap_ipv4.packet(pinfo, tvb, ip)
    local packet_number = pinfo.number  -- for debug reasons
    print(&quot;Packet Number:   &quot;, packet_number)
end

function tap_ipv4.draw()
    print(&quot;draw called&quot;)     -- Debug Message
end</code></pre><p>and the Output from a simple capture file that contains 3 ICMP redirects</p><pre><code>&gt; tshark -r test_05.pcapng -X lua_script:test.lua
Packet Number:          1
  1 0.000000000 192.168.0.100 -&gt; 8.8.8.8      ICMP 74 Echo (ping) request  id=0x0001, seq=9/2304, ttl=128
Packet Number:          2
  2 0.026124000      8.8.8.8 -&gt; 192.168.0.100 ICMP 74 Echo (ping) reply    id=0x0001, seq=9/2304, ttl=56 (request in 1)
Packet Number:          3
  3 1.001399000 192.168.0.100 -&gt; 8.8.8.8      ICMP 74 Echo (ping) request  id=0x0001, seq=10/2560, ttl=128
Packet Number:          4
Packet Number:          4
  4 1.002284000  192.168.0.2 -&gt; 192.168.0.100 ICMP 102 Redirect             (Redirect for host)
Packet Number:          5
  5 1.026090000      8.8.8.8 -&gt; 192.168.0.100 ICMP 74 Echo (ping) reply    id=0x0001, seq=10/2560, ttl=56 (request in 3)
Packet Number:          6
  6 2.003533000 192.168.0.100 -&gt; 8.8.8.8      ICMP 74 Echo (ping) request  id=0x0001, seq=11/2816, ttl=128
Packet Number:          7
  7 2.026073000      8.8.8.8 -&gt; 192.168.0.100 ICMP 74 Echo (ping) reply    id=0x0001, seq=11/2816, ttl=56 (request in 6)
Packet Number:          8
  8 3.005648000 192.168.0.100 -&gt; 8.8.8.8      ICMP 74 Echo (ping) request  id=0x0001, seq=12/3072, ttl=128
Packet Number:          9
Packet Number:          9
  9 3.006529000  192.168.0.2 -&gt; 192.168.0.100 ICMP 102 Redirect             (Redirect for host)
Packet Number:          10
 10 3.031055000      8.8.8.8 -&gt; 192.168.0.100 ICMP 74 Echo (ping) reply    id=0x0001, seq=12/3072, ttl=56 (request in 8)
Packet Number:          11
Packet Number:          11
 11 10.449692000  192.168.0.2 -&gt; 192.168.0.100 ICMP 90 Redirect             (Redirect for host)
draw called</code></pre><p>Platform Windows7 64bit (also tested with GNU/Debian Linux 8, same issue) Wireshark v1.12.8-0-g5b6e543 from master-1.12</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '15, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/5f051d406b8e6e493557e1c0e86c01c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="C_N&#39;s gravatar image" /><p><span>C_N</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="C_N has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-47170" class="comments-container"></div><div id="comment-tools-47170" class="comment-tools"></div><div class="clear"></div><div id="comment-47170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47176"></span>

<div id="answer-container-47176" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47176-score" class="post-score" title="current number of votes">1</div><span id="post-47176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But it seems that the tap_ipv4.packet() gets called twice for IMCP redircet packets. ICMP echo/reply,TCP/UDP seems normal. <strong>I dont know if this is works as designed.</strong></p></blockquote><p>As far as I can see in the code (packet-icmp.c), I'd say: yes it works as designed. The ICMP dissector calls the IP dissector for the ICMP payload, which contains the IP header of the packet that triggered the ICMP redirect. You should see the same behavior for ICMP UNREACHABLE, TIMEEXEEDED, SOURCEQUENCH, REDIRECT.</p><p><strong>Possible Solution</strong> (if you want to look at the 'outer' ICMP frame only): Add a table (array/hash) to your code to remember that you've already processed a certain frame number and skip it the second time your tap is called for that frame.</p><p>Please take a look at the code of <span>@izopizo</span> in the following question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/15196/implementing-a-basic-packet-counter-and-incorrect-order-detector-using-dissectors-and-lua">https://ask.wireshark.org/questions/15196/implementing-a-basic-packet-counter-and-incorrect-order-detector-using-dissectors-and-lua</a><br />
</p></blockquote><p>The code stores the packet number in <strong>pkts</strong> and uses <strong>pinfo.visited</strong>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '15, 16:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-47176" class="comments-container"><span id="47188"></span><div id="comment-47188" class="comment"><div id="post-47188-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>thanks for the quick help. Ok that behavior make sense.</p><p>I only need the connection information (srcIP, DstIP, Proto, and length in bytes).<br />
Simply check, if the packet number was already processed works fine for me.</p><p>Here is a example:</p><pre><code>-- function to create a IPv4 listener
function create_IPv4_tap()
    local tap = Listener.new(&quot;ip&quot;)
    return(tap)
end

-- we store the number of a processed packet
local processed_packets = {}

-- let&#39;s create a ipv4 listener
local tap_ipv4 = create_IPv4_tap()

-- will be called once for every IP Header.
function tap_ipv4.packet(pinfo, tvb, ip)
    local packet_number = pinfo.number  -- for debug reasons

    if processed_packets[packet_number] then
        print(&quot;Packet &quot;, packet_number, &quot; already processed&quot;)
    else
        print(&quot;Packet Number:   &quot;, packet_number)
        processed_packets[pinfo.number] = true
    end
end

function tap_ipv4.draw()
    print(&quot;draw called&quot;)     -- Debug Message
end</code></pre></div><div id="comment-47188-info" class="comment-info"><span class="comment-age">(03 Nov '15, 10:55)</span> <span class="comment-user userinfo">C_N</span></div></div><span id="47190"></span><div id="comment-47190" class="comment"><div id="post-47190-score" class="comment-score"></div><div class="comment-text"><p>good!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-47190-info" class="comment-info"><span class="comment-age">(03 Nov '15, 11:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-47176" class="comment-tools"></div><div class="clear"></div><div id="comment-47176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

