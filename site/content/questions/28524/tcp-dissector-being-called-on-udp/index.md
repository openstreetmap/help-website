+++
type = "question"
title = "TCP dissector being called on UDP"
description = '''Hi, I have two dissectors specified in different files. One TCP and the other UDP. The protocols I am dissecting both use the same magic, in TCP or in UDP. When opening a cap, during packet dissection it seems both dissectors are called on a UDP packet. In the output I get informations from the UDP ...'''
date = "2014-01-02T03:54:00Z"
lastmod = "2014-01-02T03:54:00Z"
weight = 28524
keywords = [ "udp", "dissector", "tcp" ]
aliases = [ "/questions/28524" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP dissector being called on UDP](/questions/28524/tcp-dissector-being-called-on-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28524-score" class="post-score" title="current number of votes">0</div><span id="post-28524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have two dissectors specified in different files. One TCP and the other UDP. The protocols I am dissecting both use the same magic, in TCP or in UDP. When opening a cap, during packet dissection it seems both dissectors are called on a UDP packet. In the output I get informations from the UDP dissector....and the TCP dissector.</p><p>How is that possible ? Each dissector is registered using the correct udp.port or tcp.port table. How can a dissector be triggered on a packet type it's not registered for ?</p><p>Stripped/Simplified code :</p><pre><code>DISSECTOR_A = Proto (&quot;DISSECTOR_A&quot;, &quot;A udp Protocol&quot;)
-- register to handle udp port range
local function register_udp_port_range(start_port, end_port)
if not start_port or start_port &lt;= 0 or not end_port or end_port &lt;= 0 then
    return
end
udp_port_table = DissectorTable.get(&quot;udp.port&quot;)
for port = start_port,end_port do
    udp_port_table:add(port,DISSECTOR_A)
end
 end    
 register_udp_port_range(7400,65000)
 function DISSECTOR_A.dissector (buffer, pinfo, tree)
  subtree = tree:add (DISSECTOR_A, buffer())
  -- Modify columns
  pinfo.cols.protocol = DISSECTOR_A.name
  pinfo.cols.info = &quot;PROTOCOL A&quot;
  dissection etc etc
end

function DISSECTOR_A.init ()
 packet_counter = 0
end</code></pre><p>Other dissector :</p><pre><code> DISSECTOR_B = Proto (&quot;DISSECTOR_B&quot;, &quot;B tcp Protocol&quot;)

 -- register to handle tcp port range
 local function register_tcp_port_range(start_port, end_port)
    if not start_port or start_port &lt;= 0 or not end_port or end_port &lt;= 0 then
        return
    end
tcp_port_table = DissectorTable.get(&quot;tcp.port&quot;)
 for port = start_port,end_port do
    tcp_port_table:add(port,DISSECTOR_B)
 end
 end    
 register_tcp_port_range(7400,65000)

 function DISSECTOR_B.dissector (buffer, pinfo, tree)
 subtree = tree:add (DISSECTOR_B, buffer())

 -- Modify columns
 pinfo.cols.protocol = DISSECTOR_B.name
 pinfo.cols.info = &quot;PROTOCOL B&quot;
 end

function DISSECTOR_B.init ()
 packet_counter = 0
end</code></pre><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '14, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/e4e8bc4618a9948a893ae407b22e8160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lepolac&#39;s gravatar image" /><p><span>lepolac</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lepolac has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jan '14, 04:01</strong> </span></p></div></div><div id="comments-container-28524" class="comments-container"></div><div id="comment-tools-28524" class="comment-tools"></div><div class="clear"></div><div id="comment-28524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

