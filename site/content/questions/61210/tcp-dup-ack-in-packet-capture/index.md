+++
type = "question"
title = "TCP Dup ACK in packet capture"
description = '''Hi  I have captured two wireshark file captures through wireless and wired connections from same source desktop to a destination file server. Wireless capture works fine and download time is within 20seconds. Same file while downloading from wired connections i am getting below errors. TCP ACKEDunse...'''
date = "2017-05-03T09:01:00Z"
lastmod = "2017-05-03T10:07:00Z"
weight = 61210
keywords = [ "tcppackets" ]
aliases = [ "/questions/61210" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Dup ACK in packet capture](/questions/61210/tcp-dup-ack-in-packet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61210-score" class="post-score" title="current number of votes">0</div><span id="post-61210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have captured two wireshark file captures through wireless and wired connections from same source desktop to a destination file server. Wireless capture works fine and download time is within 20seconds. Same file while downloading from wired connections i am getting below errors. TCP ACKEDunseen segment TCP Dup ACK 852#1</p><p>Above errors are receiving multiple times from destination server and not able to get the issue. The duplex settings are correct on both wired and wireless connetcions (full duplex 1000M)</p><p>Can you please help to understand the exact issue?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcppackets" rel="tag" title="see questions tagged &#39;tcppackets&#39;">tcppackets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '17, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/3f75fb97190df824fb967d7c3e1277ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gokulkurunthasalam&#39;s gravatar image" /><p><span>gokulkurunth...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gokulkurunthasalam has no accepted answers">0%</span></p></div></div><div id="comments-container-61210" class="comments-container"></div><div id="comment-tools-61210" class="comment-tools"></div><div class="clear"></div><div id="comment-61210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61211"></span>

<div id="answer-container-61211" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61211-score" class="post-score" title="current number of votes">0</div><span id="post-61211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"TCP ACKed unseen segment" is not an error in your environment, it means that Wireshark has seen an acknowledgement packet for TCP data that it didn't see. So a data packet was sent and acknowledged, but Wireshark only saw the acknowledgement - this means that your capture PC was too slow to capture the data as well.</p><p>Dup ACKs happen every once in a while, usually for packet loss - but they're not always bad. Sometimes you see them for out-of-order arrivals. So I wouldn't worry about the expert messages you see, they're probably harmless.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '17, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61211" class="comments-container"><span id="61212"></span><div id="comment-61212" class="comment"><div id="post-61212-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I have attached the wireshark captured file fom source system. can you please analyze the issue and advise me? Destination - 10.168.136.117 please give me url to attach the file</p></div><div id="comment-61212-info" class="comment-info"><span class="comment-age">(03 May '17, 09:27)</span> <span class="comment-user userinfo">gokulkurunth...</span></div></div><span id="61213"></span><div id="comment-61213" class="comment"><div id="post-61213-score" class="comment-score"></div><div class="comment-text"><p>You can share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox etc.</p></div><div id="comment-61213-info" class="comment-info"><span class="comment-age">(03 May '17, 10:07)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-61211" class="comment-tools"></div><div class="clear"></div><div id="comment-61211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

