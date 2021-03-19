+++
type = "question"
title = "Complex Lua TCP Reassembly Problem"
description = '''Hello Wireshark Community! I have been using lua to create various protocol dissectors for quite a while now and I am facing a problem I haven&#x27;t been able to figure out. The way lua handles TCP reassembly is relatively simple however it seems like there is one shortcoming considering the following s...'''
date = "2015-07-10T09:32:00Z"
lastmod = "2015-07-10T14:14:00Z"
weight = 44057
keywords = [ "reassembly", "dissection", "dissector", "tcp", "lua" ]
aliases = [ "/questions/44057" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Complex Lua TCP Reassembly Problem](/questions/44057/complex-lua-tcp-reassembly-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44057-score" class="post-score" title="current number of votes">0</div><span id="post-44057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Wireshark Community!</p><p>I have been using lua to create various protocol dissectors for quite a while now and I am facing a problem I haven't been able to figure out. The way lua handles TCP reassembly is relatively simple however it seems like there is one shortcoming considering the following situation:<br />
</p><ul><li>You are dissecting some streaming protocol FOO where a message unit is N byte long (N &lt; 1500).</li><li>Your capture starts at the beginning of one message unit.</li><li>All the TCP packets you receive contains at least one cut off message (at the end of the packet)</li><li>And this keeps going on for as long as your capture is taken.</li><li>Let's say your whole capture contains 100 packets.</li><li>Let's say when you reassemble all those packets, you have 500 complete messages.</li></ul><p><br />
Now here is where it gets tricky.<br />
<strong>CASE 1</strong> If your last packet actually contains the bytes that complete the message cut off in the previous packet PLUS one complete message (and nothing else) then your Wireshark will display 99 TCP frames and 1 FOO frame. When looking at this FOO frame it will say something like "100 reassembled TCP segments.." with all the packet numbers composing this huge reassembled frame. You'll be able to look at your 500 decoded FOO messages and you'll be happy (so would I be).<br />
<strong>CASE 2</strong> If your last packet also contains the end of the previous message but also contains an incomplete message, then in Wireshark you will see 100 TCP frames marked as "TCP segment of a reassembled PDU" and basically even though your dissector has been able to decode all the messages (but the very last) in all those packets, no decoded FOO frame will be displayed. This is because the dissector "thinks" the dissection is not over because it is expecting the end of the last message in another packet (which is not available because the capture has ended.) <strong>This is a huge problem because it means that even though 499 FOO messages were successfully decoded, none of them will be displayed because the 500th one is incomplete!</strong><br />
<strong>So the question is how can you tell wireshark to just display what it has been able to dissect even if the last message was not complete?</strong> (Disabling dissector reassembly is not a solution because in this scenario you would only decode 1 message out of the hundreds actually available)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-dissection" rel="tag" title="see questions tagged &#39;dissection&#39;">dissection</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '15, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/75e8b57bc655647abd3b12d5735f0de3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarkoPaulo&#39;s gravatar image" /><p><span>MarkoPaulo</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarkoPaulo has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-44057" class="comments-container"><span id="44058"></span><div id="comment-44058" class="comment"><div id="post-44058-score" class="comment-score"></div><div class="comment-text"><p>How are you performing the TCP reassembly in Lua, exactly? There are multiple ways to do it. Can you paste your script here, or something similar to your script?</p></div><div id="comment-44058-info" class="comment-info"><span class="comment-age">(10 Jul '15, 09:50)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="44061"></span><div id="comment-44061" class="comment"><div id="post-44061-score" class="comment-score"></div><div class="comment-text"><p>Hey Hadriel, Thanks for your comment. Well I usually use 2 ways of reassembling my packets, but in this particular case I do something like this:</p><p>function isFooMessage(buf)    <br />
//if header corresponds to FOO header then return (true, expected_length)    <br />
//otherwise return false (heuristic dissection failed)<br />
end</p><p><br />
function dissectFOOMessage(buf, pinfo, rootTree)    <br />
//doing some dissection    <br />
//if successful return true otherwise return false (heuristic dissection)<br />
end</p><p><br />
function p_FOO.dissector(buf, pinfo, rootTree)<br />
   local is_FOO_message, expected_length = isFooMessage(buf);<br />
<br />
   if(~is_FOO_message) then<br />
      //heuristic dissection failed<br />
      return false;<br />
   end<br />
<br />
   local offset = pkt.desegment_offset or 0<br />
   if(expected_length &gt; buf:len()) then<br />
      pinfo.desegment_len = DESEGMENT_ONE_MORE_SEGMENT;<br />
      pinfo.desegment_offset = offset<br />
      return nil<br />
   end<br />
   return dissectFOOMessage(buf, pinfo, rootTree);<br />
end</p><p><br />
<br />
//Makes the dissector heuristic : Dissects only if p_FOO.dissector<br />
//does NOT return false<br />
p_FOO:register_heuristic("tcp", function(...) p_FOO.dissector (...) end)</p></div><div id="comment-44061-info" class="comment-info"><span class="comment-age">(10 Jul '15, 10:35)</span> <span class="comment-user userinfo">MarkoPaulo</span></div></div><span id="44062"></span><div id="comment-44062" class="comment"><div id="post-44062-score" class="comment-score"></div><div class="comment-text"><p>So basically all I do here is check if the message looks like a FOO message, then if it does and it's larger than the packet, I tell wireshark that I'll need another packet to finish decoding. In this dissector I purposely don't handle the case where my capture starts in the middle of a message but it's not in the scope of the scenario I described in my question.</p></div><div id="comment-44062-info" class="comment-info"><span class="comment-age">(10 Jul '15, 10:41)</span> <span class="comment-user userinfo">MarkoPaulo</span></div></div><span id="44064"></span><div id="comment-44064" class="comment"><div id="post-44064-score" class="comment-score"></div><div class="comment-text"><p>That's not really enough detail to figure things out. :)</p><p>But anyway, doing a heuristic dissector with the end for TCP reassembly is quite tricky.</p><p>I'd suggest starting with it <em>not</em> being a heuristic dissector, but instead just add your <code>p_FOO</code> to the TCP port that your capture file has. Then you can work on the logic to make it work even when missing a last segment -which should be able to work, BTW.</p><p>What I don't see in the example script above is a while-loop, handling each of multiple potential messages inside a TCP segment.</p><p>For an example, see the 'fpm.lua' script and its associated capture file 'segmented_fpm.pcap' in the <a href="https://wiki.wireshark.org/Contrib#Protocol_Dissectors">repository of Lua plugins</a>.</p></div><div id="comment-44064-info" class="comment-info"><span class="comment-age">(10 Jul '15, 12:54)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="44065"></span><div id="comment-44065" class="comment"><div id="post-44065-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply Hadriel. This was just a sample of dummy code to keep things short. I also added the proto to the tcp table. I thought that all the heuristic registration did was to "cancel" the dissection if the dissector returns false, meaning that it turns out the packet was not of the expected format. I'm gonna try removing the heuristic part anyways and start from there.</p><p>I am not sure I understand what you mean with the "while loop thing". Are you talking about a while loop that would iterate through all the types of messages defined in the FOO protocol? If so then it would be in the function dissectFOOMessage(buf, pinfo, rootTree), which I did not develop to keep things short. I was putting what I thought was the right amount of code to show you how I handled the reassembly and nothing else.</p><p>I never found the page you linked in your comment, and I think I am going to find it very useful. I will look at your lua scripts there and see if I can get what I want to work.</p><p>I'll get back to you whether I am successful or not :). Thanks again!</p></div><div id="comment-44065-info" class="comment-info"><span class="comment-age">(10 Jul '15, 13:11)</span> <span class="comment-user userinfo">MarkoPaulo</span></div></div><span id="44066"></span><div id="comment-44066" class="comment not_top_scorer"><div id="post-44066-score" class="comment-score"></div><div class="comment-text"><p>There can be multiple of your FOO messages inside a single TCP segment (inside a single <code>Tvb</code> buffer passed into the dissector function). So you need a while-loop to handle dissecting each of them. If the last one is only partial, then you should be setting the <code>pinfo.desegment_offset</code> to the beginning of that last partial one - but the full ones will have already been dissected, so even if your capture file doesn't have another TCP segment to be able to dissect that last partial one, you'll still have the complete messages dissected and in the tree, etc.</p></div><div id="comment-44066-info" class="comment-info"><span class="comment-age">(10 Jul '15, 14:14)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-44057" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-44057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

