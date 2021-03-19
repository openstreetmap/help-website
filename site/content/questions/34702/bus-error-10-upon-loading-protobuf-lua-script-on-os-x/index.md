+++
type = "question"
title = "Bus Error 10 upon loading protobuf-lua script on OS X"
description = '''I compiled protobuf for lua under Mac OS, one of my post-dissector require to load protobuf.lua file. After finish loading wireshark will crash with Bus Error 10 without giving any details.  my lua script run fine without require &quot;protobuf&quot;  here is the protobuf-for-lua repo  https://github.com/sean...'''
date = "2014-07-16T04:01:00Z"
lastmod = "2014-07-16T07:16:00Z"
weight = 34702
keywords = [ "lua" ]
aliases = [ "/questions/34702" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bus Error 10 upon loading protobuf-lua script on OS X](/questions/34702/bus-error-10-upon-loading-protobuf-lua-script-on-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34702-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I compiled protobuf for lua under Mac OS, one of my post-dissector require to load protobuf.lua file. After finish loading wireshark will crash with Bus Error 10 without giving any details.</p><p>my lua script run fine without<br />
<code>require "protobuf"</code></p><p>here is the protobuf-for-lua repo <a href="https://github.com/sean-lin/protoc-gen-lua">https://github.com/sean-lin/protoc-gen-lua</a></p><p>Is there a flag i can use to check the error in detail ?</p><p>alternatively , is there any scripting language i can use other than lua for dissector ? I know there is already protobuf-dissector for wireshark , but it require re-compiling which is hard to do in Mac.</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '14, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/830fc6edeaa3c6ae4b564eb94b51f31d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="24hours&#39;s gravatar image" /><p>24hours<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="24hours has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jul '14, 17:18</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-34702" class="comments-container"></div><div id="comment-tools-34702" class="comment-tools"></div><div class="clear"></div><div id="comment-34702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34706"></span>

<div id="answer-container-34706" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34706-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"<code>Bus Error 10</code>" is a low-level operating system error (related to memory access), so no there's no flag to get more details, other than maybe getting the stack trace and (hopefully) debug symbols.<br />
</p><p>Did you get a stack trace? I.e., when it crashed with the bus error, did a window pop up with details?</p><p>And this doesn't appear to be a Wireshark bug, but rather something in protobuf-for-lua. Are you supposed to be using "<code>require "protobuf"</code>"? The readme for it appears to say you're not - that instead you're supposed to create a <code>.proto</code> file, "compile" it into a new lua file, and then <code>require</code> that new lua file.</p><p>There is no other scripting language for Wireshark other than Lua. What is it you're trying to do exactly? Create a new dissector? Create a tap? Why did you need protobuf-for-lua?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '14, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span> </br></p></div></div><div id="comments-container-34706" class="comments-container"><span id="34707"></span><div id="comment-34707" class="comment"><div id="post-34707-score" class="comment-score"></div><div class="comment-text"><p>Wireshark simply fail with bus error 10 and nothing else.</p><p>Im trying to reverse engineer a client-server model using protobuf (proto file already reversed and obtained ). yes, I used <code>required "myprogram_proto"</code> to parse the udp data. and myprogram_proto.lua require protobuf I tried to load <code>required "myprogram_proto"</code> using lua interpreter and does not encounter any error.</p><p><a href="https://code.google.com/p/protobuf-wireshark/">https://code.google.com/p/protobuf-wireshark/</a> Im trying to replicate the function above without having to recompile wireshark , since compiling in MacOS seems to be a pain.</p><p>protobuf-for-lua require pb.so file which link lua to c implementation, the most likely reason is I compile pb.c and linked to different Lua version with wireshark</p></div><div id="comment-34707-info" class="comment-info"><span class="comment-age">(16 Jul '14, 07:34)</span> 24hours</div></div><span id="34716"></span><div id="comment-34716" class="comment"><div id="post-34716-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Wireshark simply fail with bus error 10 and nothing else.</p></blockquote><p>If you open up the Console application (in the Utilities subfolder of Applications), does it show a crash report for "wireshark-bin" under "User Diagnostic Reports"?</p></div><div id="comment-34716-info" class="comment-info"><span class="comment-age">(16 Jul '14, 17:19)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-34706" class="comment-tools"></div><div class="clear"></div><div id="comment-34706-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

