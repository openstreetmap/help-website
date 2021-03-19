+++
type = "question"
title = "Printer skipping 2nd of 3 labels - rst issue?"
description = '''Hello all. The link below is for a partial capture from a customer installation. The printer, 172.40.22.250, is not printing the data sent in frame 12. It correctly prints data in frames 4 and 20. The data in frame 12 has been verified as valid printer code. I&#x27;m no TCP expert but I suspect the RST&#x27;s...'''
date = "2015-03-20T06:42:00Z"
lastmod = "2015-03-20T12:22:00Z"
weight = 40728
keywords = [ "rst", "as400", "printer" ]
aliases = [ "/questions/40728" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Printer skipping 2nd of 3 labels - rst issue?](/questions/40728/printer-skipping-2nd-of-3-labels-rst-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40728-score" class="post-score" title="current number of votes">0</div><span id="post-40728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all. The link below is for a partial capture from a customer installation. The printer, 172.40.22.250, is not printing the data sent in frame 12. It correctly prints data in frames 4 and 20. The data in frame 12 has been verified as valid printer code. I'm no TCP expert but I suspect the RST's have something to do with the skipped print job. The host / sender is an AS400 computer. This happens consistently. Any insight GREATLY appreciated.</p><p><a href="https://www.dropbox.com/s/o20v7t33kggooie/ANC%20Printer%20Capture%203-18.pcapng?dl=0">https://www.dropbox.com/s/o20v7t33kggooie/ANC%20Printer%20Capture%203-18.pcapng?dl=0</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-as400" rel="tag" title="see questions tagged &#39;as400&#39;">as400</span> <span class="post-tag tag-link-printer" rel="tag" title="see questions tagged &#39;printer&#39;">printer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '15, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/31c2d7f388d2f73ee6966ddfc68631e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shoal&#39;s gravatar image" /><p><span>shoal</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shoal has no accepted answers">0%</span></p></div></div><div id="comments-container-40728" class="comments-container"></div><div id="comment-tools-40728" class="comment-tools"></div><div class="clear"></div><div id="comment-40728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="40731"></span>

<div id="answer-container-40731" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40731-score" class="post-score" title="current number of votes">1</div><span id="post-40731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The printer is 10.40.22.250. Packet 12 is in tcp stream 1. You can see the printer sending a RST after the TCP handshake, so it will not print packet 12. What devices are between the host and the printer?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '15, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-40731" class="comments-container"></div><div id="comment-tools-40731" class="comment-tools"></div><div class="clear"></div><div id="comment-40731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40732"></span>

<div id="answer-container-40732" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40732-score" class="post-score" title="current number of votes">1</div><span id="post-40732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My guess is that the printer refuses the new connection with more print data because it's too busy. Packet 12 comes after a Reset packet, which terminates the session. And since it's coming from the printer it's pretty clear it is not going to do anything afterwards. Maybe its because the second of three print jobs (all with their own TCP sessions) is initiated before the first is complete, while the third is on its own again.</p><p>You might want to check if the printer has some kind of utilization statistics or an error log that you can inspect. Otherwise your sending software needs to send the print jobs sequenially I guess.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '15, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40732" class="comments-container"></div><div id="comment-tools-40732" class="comment-tools"></div><div class="clear"></div><div id="comment-40732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40734"></span>

<div id="answer-container-40734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40734-score" class="post-score" title="current number of votes">1</div><span id="post-40734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The client is also sending data after initiating the termination of the TCP stream. Client = 172.16.2.10, initiates the connection Server = 10.40.22.250, the printer in this case</p><p>There are 3 TCP streams. The following are the TCP source ports. 35910 48485 57660 The destination TCP port is always 9100 = printer page description language In your case, TCP stream 48485 is being Reset by the printer and that is why the 2nd label is not printing. However, if we filter on the first TCP stream (Wireshark filter is tcp.port==35910) we see the following: packet #5 = client sends FIN packet #9 = server acknowledges FIN and send ACK</p><p>When the client sends the FIN packet, the client can still receive data from the server but will no longer accept data from its local application to be sent to the server. But packet #18 shows the client trying to send data using the same port number. This is strange? Maybe there is a filter not showing all the packets?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '15, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-40734" class="comments-container"><span id="40738"></span><div id="comment-40738" class="comment"><div id="post-40738-score" class="comment-score"></div><div class="comment-text"><p>No, it doesn't send data. Packet #18 is empty, it's just the ACK to the FIN from the other side, plus a (useless and a little uncommon) PSH flag.</p></div><div id="comment-40738-info" class="comment-info"><span class="comment-age">(20 Mar '15, 08:34)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="40746"></span><div id="comment-40746" class="comment"><div id="post-40746-score" class="comment-score"></div><div class="comment-text"><p>Oops, you are correct Jasper. I was looking at the packet numbering and not the TCP payload size. Sorry for the confusion.</p></div><div id="comment-40746-info" class="comment-info"><span class="comment-age">(20 Mar '15, 11:24)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="40747"></span><div id="comment-40747" class="comment"><div id="post-40747-score" class="comment-score"></div><div class="comment-text"><p>no worries ;-)</p></div><div id="comment-40747-info" class="comment-info"><span class="comment-age">(20 Mar '15, 11:34)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-40734" class="comment-tools"></div><div class="clear"></div><div id="comment-40734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40748"></span>

<div id="answer-container-40748" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40748-score" class="post-score" title="current number of votes">1</div><span id="post-40748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As others have mentioned: Frame #12 does not get printed because the printer RESET the connection.</p><p><strong>However</strong> the question is: Why did the printer RESET the connection?</p><p>I believe, because the printer does not allow multiple connections to port 9100 at the same time. The SYN of TCP stream #1 arrives at the printer while TCP Stream #0 was still active (FIN of client sent). Sounds stupid, but I have seen that in other cases. Why the printer did not RESET the SYN itself? Good question. I guess the support hotline of the vendor should be able to answer that question.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '15, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-40748" class="comments-container"><span id="40751"></span><div id="comment-40751" class="comment"><div id="post-40751-score" class="comment-score"></div><div class="comment-text"><p>That's pretty much what I meant with the first connection not being complete ;-)</p></div><div id="comment-40751-info" class="comment-info"><span class="comment-age">(20 Mar '15, 12:22)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-40748" class="comment-tools"></div><div class="clear"></div><div id="comment-40748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

