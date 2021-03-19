+++
type = "question"
title = "Piecing Together Multipart UDP messages with Lua Wireshark Dissector"
description = '''I&#x27;m writing a Lua Wireshark Dissector to work with a protocol that I am using that is on top of UDP. My protocol has fields to distinguish when a message is multipart, how many segments make up the message, and what the current segment is. Everything I&#x27;ve seen for putting together multiple messages ...'''
date = "2014-04-09T06:59:00Z"
lastmod = "2014-04-09T10:39:00Z"
weight = 31670
keywords = [ "lua", "udp", "multipart" ]
aliases = [ "/questions/31670" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Piecing Together Multipart UDP messages with Lua Wireshark Dissector](/questions/31670/piecing-together-multipart-udp-messages-with-lua-wireshark-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31670-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a Lua Wireshark Dissector to work with a protocol that I am using that is on top of UDP.</p><p>My protocol has fields to distinguish when a message is multipart, how many segments make up the message, and what the current segment is.</p><p>Everything I've seen for putting together multiple messages in Lua is on top of TCP and uses a length in bytes. So nothing really seems to help with what I need to do.</p><p>Is it possible to piece together my messages? Any ideas on how?</p><p>Thanks for the help!</p></div><div id="question-tags" class="tags-container tags">lua udp multipart</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '14, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/67069e6aafa751257cdc28f55c9afb5e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nclay09&#39;s gravatar image" /><p>nclay09<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nclay09 has no accepted answers">0%</span></p></div></div><div id="comments-container-31670" class="comments-container"></div><div id="comment-tools-31670" class="comment-tools"></div><div class="clear"></div><div id="comment-31670-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31677"></span>

<div id="answer-container-31677" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31677-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There isn't a built-in way of doing it like there is for TCP. But you <em>can</em> write Lua code to do it. The details for how to do that depend on how your protocol is structured and how you want to show the resulting message and fields in the Packet Details view.</p><p>If you can dissect the individual fields in each UDP packet alone, without having to reassemble across UDP packets in order to dissect it, that would make life a lot easier. You can still show which set of UDP packets are related to each other, by using an <code>ftypes.FRAMENUM</code> typed <code>ProtoField</code>.</p><p>But I'm presuming you need to reassemble across UDP packets in order to then dissect some reassembled payload that your protocol is carrying... correct?</p><p>If so, this is going to be hard to explain... it would probably be easier to just write an example script and post it. :)</p><p>The basic concept is you're going to have to save packet protocol payload as <code>ByteArray</code>s, in a Lua table. And then reassemble them in the final packet of a fragment sequence (if all the fragments were received), by concatenating the <code>ByteArray</code>s and creating a new <code>Tvb</code> from the concatenated one; and then calling the appropriate payload dissector on the new <code>Tvb</code>.</p><p>You'd also check the <code>pinfo.visited</code>, to avoid adding to this table after the first sequential run through the capture. And you'd need to set a function into <code>proto.init</code>, to reset the table(s) whenever a capture is restarted or a capture file loaded.</p><p>The details, though, depend a lot on how your protocol is structured; because the first thing you need is something to use for a key in the Lua table that holds these fragments. It would be key'd by some field or combination of fields in your protocol that identifies a single reassembled "message". Usually protocols call this thing a transaction id or message id or some such. That field needs to appear in every UDP packet, be the same value for each fragment of the same message, and be unique per reassembled message. For example, for the IPv4/IPv6 protocol, it's the "identification" field. Do you have such a field in your protocol? Or some combination of fields that can be used to create such a thing? (in fact it will really be a combination... for example, you'd probably want to include the source+dest IP:port in this key, so that the same id value from/to different hosts does not collide)</p><p>Also, if you have a current script and example pcap capture file, it would help a lot if you posted it. You can post the script here, and the pcap file on cloudshark.org; or post them on the wireshark wiki. That would make explaining this stuff go faster I think.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '14, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-31677" class="comments-container"><span id="31678"></span><div id="comment-31678" class="comment"><div id="post-31678-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the help! I do have a key that could be used, which would be the combination of two bytes. Where would the table need to be stored? I think I follow all your logic, though, as to what needs to be done.</p></div><div id="comment-31678-info" class="comment-info"><span class="comment-age">(09 Apr '14, 10:49)</span> nclay09</div></div><span id="31679"></span><div id="comment-31679" class="comment"><div id="post-31679-score" class="comment-score"></div><div class="comment-text"><p>The table would just be local to your whole script - not inside a function or anything. That's why you need to set a function into <code>proto.init</code> to reset it, because wireshark doesn't provide anything to do that for you automatically, afaik.</p></div><div id="comment-31679-info" class="comment-info"><span class="comment-age">(09 Apr '14, 10:53)</span> Hadriel</div></div></div><div id="comment-tools-31677" class="comment-tools"></div><div class="clear"></div><div id="comment-31677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

