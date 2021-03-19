+++
type = "question"
title = "Failed at emulating browser&#x27;s packets"
description = '''Hi,  I&#x27;m writing a program with raw-sockets and i&#x27;m trying to emulate my browser&#x27;s &quot;syn&quot; packets to a socks server. My program&#x27;s packets and my browser&#x27;s packets are almost alike, but the socks server answers only my browser&#x27;s packets and not my generated packets. My browser sends 5 or 3 syns (with ...'''
date = "2010-11-20T09:09:00Z"
lastmod = "2010-12-04T13:52:00Z"
weight = 1039
keywords = [ "raw", "socket", "socks", "packet", "wireshark" ]
aliases = [ "/questions/1039" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Failed at emulating browser's packets](/questions/1039/failed-at-emulating-browsers-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1039-score" class="post-score" title="current number of votes">0</div><span id="post-1039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm writing a program with raw-sockets and i'm trying to emulate my browser's "syn" packets to a socks server. My program's packets and my browser's packets are almost alike, but the socks server answers only my browser's packets and not my generated packets. My browser sends 5 or 3 syns (with no or very little delay between each of them), and then the socks server sends the "syn,ack" packet. The only difference between the browsers packets and mine is the timestamp in the TCP layer.</p><p>Can anyone help me with that? I can provide a packet file if necessary. Thanks :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-raw" rel="tag" title="see questions tagged &#39;raw&#39;">raw</span> <span class="post-tag tag-link-socket" rel="tag" title="see questions tagged &#39;socket&#39;">socket</span> <span class="post-tag tag-link-socks" rel="tag" title="see questions tagged &#39;socks&#39;">socks</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '10, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/8bf8f9ab72a617604457de73837315aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="toothpick&#39;s gravatar image" /><p><span>toothpick</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="toothpick has no accepted answers">0%</span></p></div></div><div id="comments-container-1039" class="comments-container"><span id="1045"></span><div id="comment-1045" class="comment"><div id="post-1045-score" class="comment-score"></div><div class="comment-text"><p>I guess you'll have to provide traces for both connections, browser and your raw socket, maybe someone can spot the difference that makes the socks server go stubborn and not answering your SYN packet... Do you have a download location?</p></div><div id="comment-1045-info" class="comment-info"><span class="comment-age">(20 Nov '10, 11:32)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-1039" class="comment-tools"></div><div class="clear"></div><div id="comment-1039-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1245"></span>

<div id="answer-container-1245" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1245-score" class="post-score" title="current number of votes">1</div><span id="post-1245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ok, I compared your traces and the only thing that seems to be "off" in the raw socket version is that the TCP checksum is not correct. This is something that could be a result of TCP Checksum offloading (which is why many people turn off TCP checksum validation in Wireshark), but I think it is the problem in this case. Here's why:</p><ol><li>your browser trace shows that the SYN packets have a <strong>correct</strong> TCP checksum</li><li>your raw socket trace shows that the SYN packets have an <strong>incorrect</strong> TCP checksum</li><li>that means that your checksum is not always incorrect, so probably you do not have TCP checksum offloading trouble</li><li>if we assume your computer is usually sending correct TCP checksums for "normal" browser communication and your raw socket communication doesn't, we can assume (with just some doubt, see last paragraph) that</li><li>your raw socket program calculates the TCP checksum incorrectly and thus</li><li>the incorrect checksum is transmitted to the server which then will</li><li>drop the packet because it has to assume it is damaged and</li><li>not reply with a SYN/ACK</li></ol><p>I hope this makes sense to you. Steps to take are:</p><ol><li>capture your computer's traffic with another passive computer to verify if incorrect checksums are in fact sent out the NIC for your raw socket program</li><li>if it turns out they are, you have to</li><li>fix the raw socket program</li></ol><p>If your raw socket program does in fact calculate correct TCP checksums and Wireshark only says they're wrong because of checksum offloading I can't tell why your packets aren't answered, since everything else looks pretty much the same as the browser's packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '10, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1245" class="comments-container"></div><div id="comment-tools-1245" class="comment-tools"></div><div class="clear"></div><div id="comment-1245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1244"></span>

<div id="answer-container-1244" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1244-score" class="post-score" title="current number of votes">0</div><span id="post-1244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>yes, here are the traces of both my program and the browser.</p><p>http://rapidshare.com/files/434905180/my-packets http://rapidshare.com/files/434905209/browser</p><p>my wireshark saved those files without extension, but I guess they are .cap files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '10, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/8bf8f9ab72a617604457de73837315aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="toothpick&#39;s gravatar image" /><p><span>toothpick</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="toothpick has no accepted answers">0%</span></p></div></div><div id="comments-container-1244" class="comments-container"></div><div id="comment-tools-1244" class="comment-tools"></div><div class="clear"></div><div id="comment-1244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

