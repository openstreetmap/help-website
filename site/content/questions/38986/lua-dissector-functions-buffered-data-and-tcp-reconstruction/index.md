+++
type = "question"
title = "Lua - Dissector Functions, Buffered Data, and TCP Reconstruction"
description = '''I&#x27;m starting out creating a wireshark dissector (in lua) for my game-in-development&#x27;s multiplayer protocol to help with debugging, and have so far been dissapointed by the lack of good documentation on the subject. This protocol runs on top of TCP because I can&#x27;t be bothered to implement a real solu...'''
date = "2015-01-08T23:25:00Z"
lastmod = "2015-01-09T16:33:00Z"
weight = 38986
keywords = [ "buffer", "lua", "dissector", "tcp" ]
aliases = [ "/questions/38986" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Lua - Dissector Functions, Buffered Data, and TCP Reconstruction](/questions/38986/lua-dissector-functions-buffered-data-and-tcp-reconstruction)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38986-score" class="post-score" title="current number of votes">1</div><span id="post-38986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm starting out creating a wireshark dissector (in lua) for my game-in-development's multiplayer protocol to help with debugging, and have so far been dissapointed by the lack of good documentation on the subject. This protocol runs on top of TCP because I can't be bothered to implement a real solution, and TCP is good enough for me. I've found dissector.lua, which seems to be a very valuable resource, but this leaves me wondering:</p><ul><li>How often is this dissector function called?</li><li>How full is the buffer when it's called?</li><li>How can I let the buffer fill up a bit more, if it's running low?</li><li>How can I use TCP reconstruction with my dissector? There is a stunning lack of documentation on this subject specifically</li></ul><p>I'd love to have my dissector be a loop running in a coroutine that can call something like "stream.read(16)" to read 16 bits and that would do a coroutine.yield until I receive more data, and then once I get all my data I can just post some of it to the network dump file like so:</p><pre><code>while(true) do
  stream.read(32)
  --construct tree from data
  dump.put(tree)
end</code></pre><p>Unfortunately, I don't believe that Wireshark works like this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-buffer" rel="tag" title="see questions tagged &#39;buffer&#39;">buffer</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '15, 23:25</strong></p><img src="https://secure.gravatar.com/avatar/576aef9c5cd87830048b24f8de08c76b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Xenotoad&#39;s gravatar image" /><p><span>Xenotoad</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Xenotoad has no accepted answers">0%</span></p></div></div><div id="comments-container-38986" class="comments-container"></div><div id="comment-tools-38986" class="comment-tools"></div><div class="clear"></div><div id="comment-38986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39005"></span>

<div id="answer-container-39005" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39005-score" class="post-score" title="current number of votes">1</div><span id="post-39005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Xenotoad has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How often is this dissector function called?</p></blockquote><p>Potentially multiple times:</p><ol><li>For both Wireshark and tshark: it's called once for every packet when the capture file is loaded or the packet is captured live.</li><li>For Wireshark: I believe it's called a second time for when the GUI packet list gets drawn.</li><li>In Wireshark: it's called again whenever the user selects the packet in the GUI packet list window pane.</li><li>In Wireshark: it's called again once per packet whenever the user applies a new display filter, or for certain statistics/graphs or preference changes, decode-as being chosen, etc.</li><li>In tshark: it's called once per packet a second time if the user used the <code>'-2'</code> command line switch, or used the <code>'-Y'</code> display filter command line option.</li></ol><blockquote><p>How full is the buffer when it's called?</p></blockquote><p>The <code>Tvb</code> contains the contents of the captured packet/frame, starting at wherever the previous layer's dissector finished. So if your dissector is registered into the TCP dissectors table, then your dissector will be given a <code>Tvb</code> buffer of the TCP segment's payload (i.e., not including IP/TCP headers) for that one packet/frame. So it may contain only a portion of your application's message, or it may contain multiple of your application's messages, or it may contain exactly one full message.</p><blockquote><p>How can I let the buffer fill up a bit more, if it's running low? How can I use TCP reconstruction with my dissector? There is a stunning lack of documentation on this subject specifically</p></blockquote><p>See the "<strong>TCP reassembly</strong>" section of <a href="http://wiki.wireshark.org/Lua/Dissectors">http://wiki.wireshark.org/Lua/Dissectors</a>. There is indeed a lack of documentation for TCP-based dissection, but if you ask your questions here (in new topics, not in this topic), then we can use that to help build some documentation for the wiki.</p><blockquote><p>Unfortunately, I don't believe that Wireshark works like this.</p></blockquote><p>Right - a Lua plugin doesn't "drive" Wireshark... Wireshark controls everything and just invokes Lua callbacks. There is an open bug in this area (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9851">bug 9851</a>), and when that gets addressed there may be something to make TCP dissection easier, but only if your protocol has a length field somewhere early in its message format. If, on the other hand, your protocol is more like HTTP where you don't know the length of the message until you're done with it, then the <code>DESEGMENT_ONE_MORE_SEGMENT</code> method is the only one. Does your protocol have a length field?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '15, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Jan '15, 09:36</strong> </span></p></div></div><div id="comments-container-39005" class="comments-container"><span id="39012"></span><div id="comment-39012" class="comment"><div id="post-39012-score" class="comment-score"></div><div class="comment-text"><p>I can read the first few bytes of the message to calculate the total length of the message. Thanks for the great answer, it's pretty close to what I was looking for!</p></div><div id="comment-39012-info" class="comment-info"><span class="comment-age">(09 Jan '15, 15:22)</span> <span class="comment-user userinfo">Xenotoad</span></div></div><span id="39013"></span><div id="comment-39013" class="comment"><div id="post-39013-score" class="comment-score"></div><div class="comment-text"><p>If I return DESEGMENT_ONE_MORE_SEGMENT, will the next call's tvb argument still contain the data from the last call?</p><p>Example:</p><p>Call #1 Buffer: {0, 0, 5, 6, 7} --Returns DESEGMENT_ONE_MORE_SEGMENT</p><p>Will Call #2's buffer be {0, 0, 5, 6, 7, 3 , 5} or {3, 5}?</p></div><div id="comment-39013-info" class="comment-info"><span class="comment-age">(09 Jan '15, 15:37)</span> <span class="comment-user userinfo">Xenotoad</span></div></div><span id="39014"></span><div id="comment-39014" class="comment"><div id="post-39014-score" class="comment-score"></div><div class="comment-text"><p>I believe it depends on what you set <code>pinfo.desegment_offset</code> to: if you leave it at 0, and set <code>pinfo.desegment_len</code> to <code>DESEGMENT_ONE_MORE_SEGMENT</code>, then yes you'll get all the previous Tvb bytes as well as the new ones on the next call to <code>dissect()</code> - i.e., you'll get <code>{0, 0, 5, 6, 7, 3, 5}</code>. If you set <code>pinfo.desegment_offset</code> to 1, then you'll get <code>{0, 5, 6, 7, 3, 5}</code>, and so on.</p></div><div id="comment-39014-info" class="comment-info"><span class="comment-age">(09 Jan '15, 16:33)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-39005" class="comment-tools"></div><div class="clear"></div><div id="comment-39005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

