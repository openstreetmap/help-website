+++
type = "question"
title = "Http request"
description = '''After username and password for our intranet website I see communication from Client Seq -1 next relative sequence no - 918 Ack =1 to server Get /webpage .aspx?q=sdfcklasdkcklejklwfjkacklasjcklasjdkcfsjckljsakl Ack from Server wit seq = 1 and ack = 918  after this i don&#x27;t see any communication in th...'''
date = "2012-07-20T23:47:00Z"
lastmod = "2012-07-21T03:00:00Z"
weight = 12891
keywords = [ "http" ]
aliases = [ "/questions/12891" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Http request](/questions/12891/http-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12891-score" class="post-score" title="current number of votes">0</div><span id="post-12891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After username and password for our intranet website I see communication from Client Seq -1 next relative sequence no - 918 Ack =1 to server <strong>Get</strong> /webpage .aspx?q=sdfcklasdkcklejklwfjkacklasjcklasjdkcfsjckljsakl <strong>Ack</strong> from Server wit seq = 1 and ack = 918 after this i don't see any communication in the wire , we have restarted the server and checked no hope and finally i have unpluged n replug the server interface cable in the switch it stared working ..</p><p>wat could be cause of this issue .</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jul '12, 23:47</strong></p><img src="https://secure.gravatar.com/avatar/847f305ac08a3610580532c798daf48c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbee&#39;s gravatar image" /><p><span>newbee</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbee has no accepted answers">0%</span></p></div></div><div id="comments-container-12891" class="comments-container"></div><div id="comment-tools-12891" class="comment-tools"></div><div class="clear"></div><div id="comment-12891-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12892"></span>

<div id="answer-container-12892" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12892-score" class="post-score" title="current number of votes">0</div><span id="post-12892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>we have restarted the server and checked no hope</p></blockquote><p>by 'server' do mean the computer or the web server software?</p><blockquote><p>and finally i have unpluged n replug the server interface cable in the switch it stared working .</p></blockquote><p>sounds like an internal problem in the network adapter or the driver that was fixed by taking down the link (unplug) and enabling again (plug), which initiated a reinitialisation of the adapter.</p><p>HOWER: If you rebooted the computer, at least the driver and some internal state of the network adapter should have been reset as well, hence my question about what you restarted.</p><p>It could have been a <strong>strange mechanical problem</strong> with the RJ45 connector. If it was not fully plugged in, it could have lost contact with some pins (due to minmal vibrations) and thus you lost the connection to the server. I have seen weird things myself caused by not fully pluged-in connectors (only 1 of 3 pings works, up/download speed totally different like 1:10, etc.)</p><p>BTW: Regarding the SEQ/ACK. Are you really sure you have seen exactly that? They don't match the data you reported (GET request). The server should have ACKed the data of the GET request. Can you post the capture file?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '12, 03:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jul '12, 08:58</strong> </span></p></div></div><div id="comments-container-12892" class="comments-container"></div><div id="comment-tools-12892" class="comment-tools"></div><div class="clear"></div><div id="comment-12892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

