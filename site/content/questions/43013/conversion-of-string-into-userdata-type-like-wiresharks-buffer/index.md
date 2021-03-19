+++
type = "question"
title = "conversion of string into userdata type like wireshark&#x27;s buffer"
description = '''Hi, I&#x27;m working on a wireshark dissector and I have a part of my dissector that uses a C#.net dll. The objective is to decipher (this is done by the dll) a part of the frame captured by wireshark and to dissect the deciphered frame. The problem is that all my dissectors functions uses a parameter ca...'''
date = "2015-06-09T06:56:00Z"
lastmod = "2015-06-11T00:54:00Z"
weight = 43013
keywords = [ "lua", "sub-dissector" ]
aliases = [ "/questions/43013" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [conversion of string into userdata type like wireshark's buffer](/questions/43013/conversion-of-string-into-userdata-type-like-wiresharks-buffer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43013-score" class="post-score" title="current number of votes">0</div><span id="post-43013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm working on a wireshark dissector and I have a part of my dissector that uses a C#.net dll. The objective is to decipher (this is done by the dll) a part of the frame captured by wireshark and to dissect the deciphered frame. The problem is that all my dissectors functions uses a parameter called "buffer" which has a "userdata" type coming from Wireshark, and my dll returns a string.</p><p>Example of function :</p><p>function xxx(buf,pkt,tree)</p><pre><code> local apdu = buf(0,1):uint() 
 local pdu_variant = buf(1,1):uint()    
 local t = root:add(proto_dlms,buf(0))  
 t:append_text( string.format(&quot; %u Bytes&quot;, buf:len() ))</code></pre><p>end</p><p>Is there a way to convert the string into a userdata ? So I can use my functions to dissect the string coming from the dll?</p><p>I tried to modify the dll to return a byte[] type (instead of a string) but I was not able to use this variable like "buffer".</p><p>I also tried to send back my string result on the network on localhost using (luasocket) but wireshark doesn't capture the packets in localhost.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-sub-dissector" rel="tag" title="see questions tagged &#39;sub-dissector&#39;">sub-dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '15, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/91c3b4de80a272c387ee6db9accbb6ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SWLuaTest&#39;s gravatar image" /><p><span>SWLuaTest</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SWLuaTest has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>12 Jun '15, 06:27</strong> </span></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span></p></div></div><div id="comments-container-43013" class="comments-container"><span id="43014"></span><div id="comment-43014" class="comment"><div id="post-43014-score" class="comment-score"></div><div class="comment-text"><p>The problem with loopback capture in Windows is a WinPCap issue. Hopefully it will be fixed in future WinPCap updates.</p></div><div id="comment-43014-info" class="comment-info"><span class="comment-age">(09 Jun '15, 07:20)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="43028"></span><div id="comment-43028" class="comment"><div id="post-43028-score" class="comment-score"></div><div class="comment-text"><p>Yes, but before this new version (wich will fix the problem of loopback) : Is there a way to convert a string into a type "buf"?</p></div><div id="comment-43028-info" class="comment-info"><span class="comment-age">(10 Jun '15, 02:36)</span> <span class="comment-user userinfo">SWLuaTest</span></div></div></div><div id="comment-tools-43013" class="comment-tools"></div><div class="clear"></div><div id="comment-43013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43058"></span>

<div id="answer-container-43058" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43058-score" class="post-score" title="current number of votes">0</div><span id="post-43058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SWLuaTest has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For information it's now working :</p><blockquote><p>local b = ByteArray.new(decipheredFrame)<br />
local bufFrame = ByteArray.tvb(b, "My Tvb")</p></blockquote><p>Those 2 lines allows me to convert my string "decipheredFrame" into a wireshark type "buffer".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '15, 00:54</strong></p><img src="https://secure.gravatar.com/avatar/91c3b4de80a272c387ee6db9accbb6ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SWLuaTest&#39;s gravatar image" /><p><span>SWLuaTest</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SWLuaTest has one accepted answer">100%</span> </br></p></div></div><div id="comments-container-43058" class="comments-container"></div><div id="comment-tools-43058" class="comment-tools"></div><div class="clear"></div><div id="comment-43058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

