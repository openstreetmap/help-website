+++
type = "question"
title = "wireshark timestamp"
description = '''The Tcp packet in wireshark has a timestamp option, TSval and TSecr, after googling for a while i understand that TSval is the value of the tcp clock of the sender, right? ...now if i am tracing the packets in wireshark in order to calculate the time between sending a packet and receiving the acknow...'''
date = "2015-05-05T08:14:00Z"
lastmod = "2015-05-05T09:00:00Z"
weight = 42089
keywords = [ "timestamp", "pcap", "tcp", "wireshark" ]
aliases = [ "/questions/42089" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark timestamp](/questions/42089/wireshark-timestamp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42089-score" class="post-score" title="current number of votes">0</div><span id="post-42089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The Tcp packet in wireshark has a timestamp option, TSval and TSecr, after googling for a while i understand that TSval is the value of the tcp clock of the sender, right? ...now if i am tracing the packets in wireshark in order to calculate the time between sending a packet and receiving the acknowledgement between each 2 packets, i need the time at which the packet was sent and the time at which the next packet(the ack pkt) was received ..at the same node .. how do i calculate that?? and is the time at which the pkt was sent = TSval ? .. if so, then how do i get the time at which i received the ack packet??</p><p>noting that i'm doing this capture and calculation on one computer (the client) thinking it'll be easier, but if i will need to include the receiving computer let me know.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '15, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p><span>yas1234</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></div></div><div id="comments-container-42089" class="comments-container"></div><div id="comment-tools-42089" class="comment-tools"></div><div class="clear"></div><div id="comment-42089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42092"></span>

<div id="answer-container-42092" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42092-score" class="post-score" title="current number of votes">0</div><span id="post-42092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the "Time" column in Wireshark to display the times at which the capture mechanism used on your OS recorded the transmission of the request and the ack of packet.</p><p>You can also set the request packet as a "Time Reference" by right clicking the packet in the packet list and selecting "Set Time Reference", accepting the change of time format if Wireshark asks, and then the Time column will directly show the response time for the ack relative to the request.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '15, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-42092" class="comments-container"><span id="42094"></span><div id="comment-42094" class="comment"><div id="post-42094-score" class="comment-score"></div><div class="comment-text"><p>do you mean the pcap file record timestamp if i'm capturing near the sender side ?</p></div><div id="comment-42094-info" class="comment-info"><span class="comment-age">(05 May '15, 08:58)</span> <span class="comment-user userinfo">yas1234</span></div></div><span id="42095"></span><div id="comment-42095" class="comment"><div id="post-42095-score" class="comment-score"></div><div class="comment-text"><p>Yes that's correct. Note that it's only as accurate as the capture mechanism used.</p></div><div id="comment-42095-info" class="comment-info"><span class="comment-age">(05 May '15, 09:00)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-42092" class="comment-tools"></div><div class="clear"></div><div id="comment-42092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

