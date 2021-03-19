+++
type = "question"
title = "How to tell dissector to read AFTER my protocol?"
description = '''Hi,  I have create a protocol between UDP and RTP, so the packet I want to capture with wireshark looks like this : ( IP, UDP, [my protocol], RTP )  I have written a lua file to include decoding of my protocol. After I decode my protocol I want to call a dissector to decode the RTP part. The problem...'''
date = "2012-11-07T01:03:00Z"
lastmod = "2012-11-08T21:53:00Z"
weight = 15614
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/15614" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to tell dissector to read AFTER my protocol?](/questions/15614/how-to-tell-dissector-to-read-after-my-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15614-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have create a protocol between UDP and RTP, so the packet I want to capture with wireshark looks like this : ( IP, UDP, [my protocol], RTP )</p><p>I have written a lua file to include decoding of my protocol. After I decode my protocol I want to call a dissector to decode the RTP part. The problem is that it thinks it should start reading RTP after the UDP packet, and not after my protocol (which is 20 bytes )</p><p>Here is the code :</p><pre><code>function MYPROTO.dissector (buffer, pinfo, tree)

local subtree = tree:add (MYPROTO, buffer())
local offset = 0    
subtree:add (f.version, buffer (offset, 1)) 
offset = offset + 1 
...
rtp_table = Dissector.get (&quot;rtp&quot;)   
subtree:add (rtp_table, buffer(offset))
tvb=buffer()
rtp_table:call(tvb:tvb(),pinfo,tree)</code></pre><p>So the problem is that the RTP packets thinks the first bytes after UDP are RTP, but those are my protocol bytes. How can I tell the dissector that RTP should start dissecting AFTER my protocol?</p><p>Thank you in advance</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '12, 01:03</strong></p><img src="https://secure.gravatar.com/avatar/7709c0c87ed4ba426f119187d3f0c705?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harkap&#39;s gravatar image" /><p>harkap<br />
<span class="score" title="5 reputation points">5</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harkap has no accepted answers">0%</span></p></div></div><div id="comments-container-15614" class="comments-container"></div><div id="comment-tools-15614" class="comment-tools"></div><div class="clear"></div><div id="comment-15614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="15726"></span>

<div id="answer-container-15726" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15726-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Eh, let's see. Maybe even easier, you could go with:</p><p><code>rtp_table:call(buffer(20):tvb(), pinfo, tree)</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-15726" class="comments-container"></div><div id="comment-tools-15726" class="comment-tools"></div><div class="clear"></div><div id="comment-15726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15755"></span>

<div id="answer-container-15755" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15755-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The last few lines of your code should be:</p><pre><code>rtp_table = Dissector.get (&quot;rtp&quot;)
subtree:add (rtp_table, buffer(offset))
tvb=buffer(20)
rtp_table:call(tvb:tvb(),pinfo,tree)</code></pre><p>You might consider consolidating into one line:</p><pre><code>Dissector.get(&#39;rtp&#39;):call( buffer(20):tvb(), pinfo, tree )</code></pre><p>Also, check out another <a href="http://ask.wireshark.org/questions/10658/how-to-use-lua-to-write-multi-protocol-dissector-plugin">similar question</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 21:53</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-15755" class="comments-container"><span id="15759"></span><div id="comment-15759" class="comment"><div id="post-15759-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Thank you very much that works great!</p><p>Another question : is there an rtp mux dissector?</p><p>Another question : Is there an dissectortable for UDP source port?</p><p>I cannot find the answer to that simple question, generally, WHAT types of dissectors and dissetortables EXISTS that i can use in the code?</p><p>Thank you!</p></div><div id="comment-15759-info" class="comment-info"><span class="comment-age">(09 Nov '12, 00:50)</span> harkap</div></div><span id="15761"></span><div id="comment-15761" class="comment"><div id="post-15761-score" class="comment-score"></div><div class="comment-text"><p>I converted your "answer" to a comment as that's how this site works, and chose the one from @helloworld as it's the highest rated.</p><p>If an answer solves your problem please accept it for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ to find out how this site works.</p><p>As for your new questions, you should start new questions for those as they'll be lost in the comments to an answer.</p></div><div id="comment-15761-info" class="comment-info"><span class="comment-age">(09 Nov '12, 01:26)</span> grahamb ♦</div></div></div><div id="comment-tools-15755" class="comment-tools"></div><div class="clear"></div><div id="comment-15755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15634"></span>

<div id="answer-container-15634" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15634-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use tvb:range(20) to create a sub-TVB, starting from byte 20 of the buffer you get.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '12, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-15634" class="comments-container"><span id="15642"></span><div id="comment-15642" class="comment"><div id="post-15642-score" class="comment-score"></div><div class="comment-text"><p>Could you please provide an code example on how to do this?</p></div><div id="comment-15642-info" class="comment-info"><span class="comment-age">(07 Nov '12, 06:31)</span> harkap</div></div></div><div id="comment-tools-15634" class="comment-tools"></div><div class="clear"></div><div id="comment-15634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

