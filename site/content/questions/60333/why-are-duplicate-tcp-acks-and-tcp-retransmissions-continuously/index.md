+++
type = "question"
title = "Why are Duplicate TCP Acks and TCP retransmissions continuously"
description = '''Hello. I have a problem with sending data through TCP server from PIC32 custome board (192.168.5.11) to PC (192.168.5.10). Communication works fine when sending small amount of data or at max speed with no other tasks in PIC. Problem is when I try to insert some additional tasks to the PIC uC, an it...'''
date = "2017-03-27T00:23:00Z"
lastmod = "2017-03-28T00:20:00Z"
weight = 60333
keywords = [ "duplicateacks", "retransmission", "tcp" ]
aliases = [ "/questions/60333" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why are Duplicate TCP Acks and TCP retransmissions continuously](/questions/60333/why-are-duplicate-tcp-acks-and-tcp-retransmissions-continuously)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60333-score" class="post-score" title="current number of votes">0</div><span id="post-60333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I have a problem with sending data through TCP server from PIC32 custome board (192.168.5.11) to PC (192.168.5.10). Communication works fine when sending small amount of data or at max speed with no other tasks in PIC. Problem is when I try to insert some additional tasks to the PIC uC, an it looks like this: <img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_iRKwM5R.PNG" alt="alt text" /></p><p>Can someone explain me what can cause that behavior? PS. Sorry for my english :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicateacks" rel="tag" title="see questions tagged &#39;duplicateacks&#39;">duplicateacks</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '17, 00:23</strong></p><img src="https://secure.gravatar.com/avatar/145b078f8ade4804b2f7c643841a4101?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ENRO&#39;s gravatar image" /><p><span>ENRO</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ENRO has no accepted answers">0%</span></p></img></div></div><div id="comments-container-60333" class="comments-container"><span id="60345"></span><div id="comment-60345" class="comment"><div id="post-60345-score" class="comment-score"></div><div class="comment-text"><p>can you please upload the capture?</p></div><div id="comment-60345-info" class="comment-info"><span class="comment-age">(27 Mar '17, 03:39)</span> <span class="comment-user userinfo">soochi</span></div></div><span id="60348"></span><div id="comment-60348" class="comment"><div id="post-60348-score" class="comment-score"></div><div class="comment-text"><p>I's another capture with the same error: <a href="https://www.cloudshark.org/captures/8eb9b677dd97">https://www.cloudshark.org/captures/8eb9b677dd97</a></p></div><div id="comment-60348-info" class="comment-info"><span class="comment-age">(27 Mar '17, 04:10)</span> <span class="comment-user userinfo">ENRO</span></div></div></div><div id="comment-tools-60333" class="comment-tools"></div><div class="clear"></div><div id="comment-60333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60350"></span>

<div id="answer-container-60350" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60350-score" class="post-score" title="current number of votes">1</div><span id="post-60350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ENRO has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's a very interesting capture. The server sends MSS 536 in the SYN/ACK packet, but sends 1460 bytes packets - that doesn't make any sense (if it says it can only do 536, it should only receive and send 536 bytes at max). My guess is that this leads to trouble.</p><p>I would recommend doing a simultaneous capture at client and server at the same time (and not <strong>on</strong> the client or server, but using TAPs or SPAN ports), to check what really happens. It looks like the packets may have been modified in flight - maybe some middle box is messing with the packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '17, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60350" class="comments-container"><span id="60351"></span><div id="comment-60351" class="comment"><div id="post-60351-score" class="comment-score"></div><div class="comment-text"><p>You're right. I didn't noticed that. There is no middle box. The server is implemented on PIC32 embedded processor - it's my modification od Microchip MLA stack. I could make a mistake when porting the code. At least now i know where to start looking for error. Thank you.</p></div><div id="comment-60351-info" class="comment-info"><span class="comment-age">(27 Mar '17, 04:45)</span> <span class="comment-user userinfo">ENRO</span></div></div><span id="60352"></span><div id="comment-60352" class="comment"><div id="post-60352-score" class="comment-score"></div><div class="comment-text"><p>Okay, it was just that the server sends a TTL of 100 which is very unusual - normal start values are 64, 128 or 255. So I guessed there is something in between :-)</p></div><div id="comment-60352-info" class="comment-info"><span class="comment-age">(27 Mar '17, 04:46)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="60353"></span><div id="comment-60353" class="comment"><div id="post-60353-score" class="comment-score"></div><div class="comment-text"><p>TTL = 100 may be unusual, but it should normally work. Changing the MSS didn't work. A have just read that each direction of data flow can use a different MSS. Any other ideas?</p></div><div id="comment-60353-info" class="comment-info"><span class="comment-age">(27 Mar '17, 05:06)</span> <span class="comment-user userinfo">ENRO</span></div></div><span id="60355"></span><div id="comment-60355" class="comment"><div id="post-60355-score" class="comment-score">1</div><div class="comment-text"><p>You're right, TTL 100 is not a problem.</p><p>And while it's true that both directions can advertise different MSS values, it is wise for both to honor the lower of the values - simply because exceeding that value will lead to packets being unable to pass without fragmentation.</p><p>What seems to be a problem is that all of your server packets have incorrect CRCs, and if you captured on the client they should be okay. My guess is that those packets are dropped because the checksum is bad. You need to fix your CRC calculation, is my guess :-)</p></div><div id="comment-60355-info" class="comment-info"><span class="comment-age">(27 Mar '17, 05:39)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="60356"></span><div id="comment-60356" class="comment not_top_scorer"><div id="post-60356-score" class="comment-score"></div><div class="comment-text"><p>Exactly. I just started to writing a comment when saw your message. I also think it is the cause of error. Thank you :)</p></div><div id="comment-60356-info" class="comment-info"><span class="comment-age">(27 Mar '17, 05:43)</span> <span class="comment-user userinfo">ENRO</span></div></div><span id="60382"></span><div id="comment-60382" class="comment"><div id="post-60382-score" class="comment-score">1</div><div class="comment-text"><p>Problem solved :) There was no error with calculating CRC, only with data copy (CRC was calculated for entire package, but I copied max 960 bytes of TCP data). Thanks for help :)</p></div><div id="comment-60382-info" class="comment-info"><span class="comment-age">(28 Mar '17, 00:20)</span> <span class="comment-user userinfo">ENRO</span></div></div></div><div id="comment-tools-60350" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-60350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

