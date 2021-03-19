+++
type = "question"
title = "Lua TCP reassembly"
description = '''Hi all, I work on a protocol built on top of HTTP on the port 4321 for example. I have Wireshark 1.4.2 First I register the HTTP protocol for the port 4321 but it seems that HTTP messages are very well reassembled. Often http PDU are reassembled but sometimes not. I read that there are bugs to reass...'''
date = "2010-12-15T05:52:00Z"
lastmod = "2010-12-15T05:52:00Z"
weight = 1357
keywords = [ "lua", "dissector", "tcp", "reassembly" ]
aliases = [ "/questions/1357" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua TCP reassembly](/questions/1357/lua-tcp-reassembly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1357-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I work on a protocol built on top of HTTP on the port 4321 for example. I have Wireshark 1.4.2</p><p>First I register the HTTP protocol for the port 4321 but it seems that HTTP messages are very well reassembled. Often http PDU are reassembled but sometimes not. I read that there are bugs to reassemble HTTP message because it is diffcult to calculate their size.</p><p>So, since my HTTP messages are quite simple, I would like to write a dissector that reassemble HTTP messages on the port 4321 and then invoke the original http dissector with the complete message. I tried according to http://wiki.wireshark.org/Lua/Dissectors to write a script that reassemble an HTTP message of size 443. Here is the code:</p><p>http_wrapper_proto = Proto("DPWS", "DPWS")</p><p>function http_wrapper_proto.dissector(buffer, pinfo, tree) pinfo.cols.protocol = "HTTP-Wrapper"</p><pre><code>if (buffer:len() &lt; 443) then
    pinfo.desegment_len = 443 - buffer:len() + 1
    pinfo.desegment_offset = buffer:len()
    return (buffer:len() - 443)
end
    -- Here the message is complete</code></pre><p>end</p><p>But it does not work. I don't keep in the buffer the data of the previous call as explained in the README.developers.</p><p>Anybody can help me to solve the HTTP reassembly bug or the problem in my code?</p><p>Thank you in advance.</p><p>Sandrine Beauche.</p></div><div id="question-tags" class="tags-container tags">lua dissector tcp reassembly</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '10, 05:52</strong></p><img src="https://secure.gravatar.com/avatar/a141a084e9ce66ec32b7f064776798bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sandrine%20Beauche&#39;s gravatar image" /><p>Sandrine Bea...<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sandrine Beauche has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Dec '10, 05:56</p></div></div><div id="comments-container-1357" class="comments-container"><span id="1371"></span><div id="comment-1371" class="comment"><div id="post-1371-score" class="comment-score"></div><div class="comment-text"><p>Anybody have any idea??</p></div><div id="comment-1371-info" class="comment-info"><span class="comment-age">(16 Dec '10, 00:44)</span> Sandrine Bea...</div></div><span id="7302"></span><div id="comment-7302" class="comment"><div id="post-7302-score" class="comment-score"></div><div class="comment-text"><p>have you solved the issue? because I'm experiencing similar problems and this might be wireshark lua api bug</p></div><div id="comment-7302-info" class="comment-info"><span class="comment-age">(08 Nov '11, 16:43)</span> ShomeaX</div></div></div><div id="comment-tools-1357" class="comment-tools"></div><div class="clear"></div><div id="comment-1357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

