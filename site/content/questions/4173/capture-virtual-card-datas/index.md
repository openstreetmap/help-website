+++
type = "question"
title = "Capture Virtual card datas"
description = '''Hello My OS is XP, I have installed a Pocket PC emulator, and therefore a virtual card. I want to sniff the traffic between an FTP client, which resides on the emulator, and a ftp server wich is on onother machine. WireShark is on the emulator&#x27;s host machine. I&#x27;m able to sniff the traffic from the e...'''
date = "2011-05-22T09:47:00Z"
lastmod = "2011-05-23T01:17:00Z"
weight = 4173
keywords = [ "xp", "card", "virtual" ]
aliases = [ "/questions/4173" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Virtual card datas](/questions/4173/capture-virtual-card-datas)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4173-score" class="post-score" title="current number of votes">0</div><span id="post-4173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>My OS is XP, I have installed a Pocket PC emulator, and therefore a virtual card.</p><p>I want to sniff the traffic between an FTP client, which resides on the emulator, and a ftp server wich is on onother machine.</p><p>WireShark is on the emulator's host machine.</p><p>I'm able to sniff the traffic from the emulator to the ftp server, but not the return traffic, from the ftp server to the emulator.</p><p>Is there a way to do it ?</p><p>Thank You</p><p>Andre</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xp" rel="tag" title="see questions tagged &#39;xp&#39;">xp</span> <span class="post-tag tag-link-card" rel="tag" title="see questions tagged &#39;card&#39;">card</span> <span class="post-tag tag-link-virtual" rel="tag" title="see questions tagged &#39;virtual&#39;">virtual</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '11, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/a5bfae007baa6af5d7a8911309c43c68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chantme&#39;s gravatar image" /><p><span>Chantme</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chantme has no accepted answers">0%</span></p></div></div><div id="comments-container-4173" class="comments-container"></div><div id="comment-tools-4173" class="comment-tools"></div><div class="clear"></div><div id="comment-4173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4184"></span>

<div id="answer-container-4184" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4184-score" class="post-score" title="current number of votes">1</div><span id="post-4184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It seems the "Pocket PC Emulator" created a virtual NIC in such a way that return traffic is directed to the "Emulated Pocket PC" before libpcap sees the traffic. Therefor I don't think it will be possible to capture traffic on your host.</p><p>However, you can capture on the FTP server (if it is under your control) or else use a HUB or switch with Span-port and connect your host to it. Then you can use a second system to capture the packets.</p><p>See also: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '11, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4184" class="comments-container"></div><div id="comment-tools-4184" class="comment-tools"></div><div class="clear"></div><div id="comment-4184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4176"></span>

<div id="answer-container-4176" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4176-score" class="post-score" title="current number of votes">0</div><span id="post-4176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Since the ftp server is on another machine which rules out traffic missing because of localhost transfers you have a strange situation there. You should see both outgoing and incoming packets. If you don't you should check for</p><ol><li>capture filters refusing one direction</li><li>display filters showing only one direction</li><li>more than one network card in your host machine, where the outgoing traffic travels through a different card than the incoming (don't forget wired/wireless cards being in the same network)</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '11, 13:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4176" class="comments-container"></div><div id="comment-tools-4176" class="comment-tools"></div><div class="clear"></div><div id="comment-4176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

