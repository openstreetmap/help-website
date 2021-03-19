+++
type = "question"
title = "Dissector for rtp payload independent from port"
description = '''Hey guys, I wanna dissect data from rtp body. I tried this first with adding my defined protocol to the UDP table like that: function myProto.dissector(buffer, pinfo, tree)  -- some code here for dissection end local udp_dissector_table = DissectorTable.get(&quot;udp.port&quot;) udp_dissector_table:add(5010, ...'''
date = "2017-03-13T23:19:00Z"
lastmod = "2017-03-14T09:50:00Z"
weight = 60046
keywords = [ "rtp.payload", "rtp", "postdissector", "offset" ]
aliases = [ "/questions/60046" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Dissector for rtp payload independent from port](/questions/60046/dissector-for-rtp-payload-independent-from-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60046-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys, I wanna dissect data from rtp body.</p><p>I tried this first with adding my defined protocol to the UDP table like that:</p><pre><code>function myProto.dissector(buffer, pinfo, tree)
  -- some code here for dissection
end
local udp_dissector_table = DissectorTable.get(&quot;udp.port&quot;)
udp_dissector_table:add(5010, myProto)</code></pre><p>The dissection works fine but unfortunately just for the specified Port <code>5010</code>. The dissection of the bytes inside of the function <code>myProto.dissector(buffer, pinfo, tree)</code> starts with the beginning ot the udp packet. So <code>buffer()</code> has now the length of the whole RTP content (including header). The problem is now that the RTP can be in UDP packets with differnt ports.</p><p>I tried another way which seems to be the better one because in this case it is independent from the UDP port. I registered a postdissector for checking againnst each packet:</p><pre><code>function myProto.dissector(buffer, pinfo, tree)
  -- some code here for dissection
end

register_postdissector(myProto)</code></pre><p>Now the buffer has the lnegth of the whole frame (ethernet header + ip header + udp header + rtp header + rtp content). So for each of my fields I have to add the offset length of e.g. 42 Bytes (14 + 20 + 8). My problem is now that ethernet frame as well as the ip packets having not everytime a static lnegth.</p><p>Is there a way to check if the buffer contains a rtp packet and to check the header length of ethernet / IP? Or is there mybe a way to use my first option but without any fixed port?</p><p>Thanks in advance.</p><p>Best regards, Danny</p></div><div id="question-tags" class="tags-container tags">rtp.payload rtp postdissector offset</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '17, 23:19</strong></p><img src="https://secure.gravatar.com/avatar/be2ebed82ed399218b89e90abd5bdcc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Danny%20Koppenhagen&#39;s gravatar image" /><p>Danny Koppen...<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Danny Koppenhagen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Mar '17, 23:35</p></div></div><div id="comments-container-60046" class="comments-container"></div><div id="comment-tools-60046" class="comment-tools"></div><div class="clear"></div><div id="comment-60046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60066"></span>

<div id="answer-container-60066" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60066-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should look into registering for <code>rtp.pt</code> or <code>rtp_dyn_payload_type</code>. Have a look into the RTP dissector (<code>epan/dissectors/packet-rtp.c</code>) what that brings you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '17, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-60066" class="comments-container"><span id="60087"></span><div id="comment-60087" class="comment"><div id="post-60087-score" class="comment-score"></div><div class="comment-text"><p>Thank you, this info helps me a lot. I found a solution which looks basically like this: <a href="https://github.com/FOXNEOAdvancedTechnology/RFC4175-dissector/blob/master/RFC-4175.lua">https://github.com/FOXNEOAdvancedTechnology/RFC4175-dissector/blob/master/RFC-4175.lua</a></p><p>Best regards, Danny</p></div><div id="comment-60087-info" class="comment-info"><span class="comment-age">(15 Mar '17, 05:16)</span> Danny Koppen...</div></div></div><div id="comment-tools-60066" class="comment-tools"></div><div class="clear"></div><div id="comment-60066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

