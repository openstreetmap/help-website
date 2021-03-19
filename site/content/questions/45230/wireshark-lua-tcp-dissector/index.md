+++
type = "question"
title = "Wireshark Lua TCP dissector"
description = '''I have written several UDP dissectors and they all work fine. I am struggling in creating my 1st TCP dissector for a custom protocol. No matter how I register the protocol wireshark seems to either ignore or override my dissector and use a standard decoder on the packet. The custom protocol port num...'''
date = "2015-08-19T00:50:00Z"
lastmod = "2015-08-19T06:22:00Z"
weight = 45230
keywords = [ "lua", "tcp", "dissectors" ]
aliases = [ "/questions/45230" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Lua TCP dissector](/questions/45230/wireshark-lua-tcp-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45230-score" class="post-score" title="current number of votes">0</div><span id="post-45230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have written several UDP dissectors and they all work fine. I am struggling in creating my 1st TCP dissector for a custom protocol. No matter how I register the protocol wireshark seems to either ignore or override my dissector and use a standard decoder on the packet. The custom protocol port number is 8501 and it is always decoded as cmtp-mgt.</p><p>Any suggestions on what I am doing wrong would be appreciated.</p><pre><code>local new_proto_tcp = Proto(&quot;new_traffic&quot;,&quot;new TCP Protocol&quot;)       
local ft =  new_proto_tcp.fields
ft.source_ip = ProtoField.ipv4 (&quot;new.src_ip&quot;,  &quot;Source IP address&quot;)
ft.source_port = ProtoField.uint16 (&quot;new.src_port&quot;,  &quot;Source Port&quot;)
ft.destination_ip = ProtoField.ipv4 (&quot;new.dst_ip&quot;,  &quot;Destination IP address&quot;)
ft.destination_port = ProtoField.uint16 (&quot;new.dst_port&quot;,  &quot;Destination Port&quot;)
function new_proto_tcp.dissector(tvbuffer,pinfo,tree)
    local new_tr = tree:add(new_proto_tcp,tvbuffer(),&quot;new Protocol Data&quot;)
    Packet_content = 0
    new_tr:add(ft.source_ip, tvbuffer(Packet_content+0, 4))
    new_tr:add(ft.destination_ip, tvbuffer(Packet_content+4, 4))    
end

do
    tcp_table = DissectorTable.get(&quot;tcp.port&quot;)
    tcp_table:add(8501,new_proto_tcp)
end</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-dissectors" rel="tag" title="see questions tagged &#39;dissectors&#39;">dissectors</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '15, 00:50</strong></p><img src="https://secure.gravatar.com/avatar/da01c9170269aed91c3b302bc1530e62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karlmj&#39;s gravatar image" /><p><span>karlmj</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karlmj has no accepted answers">0%</span></p></div></div><div id="comments-container-45230" class="comments-container"><span id="45238"></span><div id="comment-45238" class="comment"><div id="post-45238-score" class="comment-score"></div><div class="comment-text"><p>I can now see, the dissector is working on the TCP packets, The confusion has arisen due to the fact the initial set-up packets, syn and syn ack are being labelled as cmpt-mgt by wireshark. How can I make sure these packets are labelled correctly?</p></div><div id="comment-45238-info" class="comment-info"><span class="comment-age">(19 Aug '15, 05:25)</span> <span class="comment-user userinfo">karlmj</span></div></div></div><div id="comment-tools-45230" class="comment-tools"></div><div class="clear"></div><div id="comment-45230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45241"></span>

<div id="answer-container-45241" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45241-score" class="post-score" title="current number of votes">0</div><span id="post-45241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For the SYN and SYN ACK there is no protocol involved, the description of the port comes from the "services" file that is either in the global or personal profile or maybe your OS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '15, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45241" class="comments-container"></div><div id="comment-tools-45241" class="comment-tools"></div><div class="clear"></div><div id="comment-45241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

