+++
type = "question"
title = "Record message with wireshark"
description = '''I want to use wireshark to record the messages. But i don&#x27;t need all of them. I want to add some rules, for example: interface: eth1 Network ip: 127.0.0.1 CBTC Base port: 61500 filename: my_record.pcap Is this possible?'''
date = "2012-03-20T03:11:00Z"
lastmod = "2012-03-20T04:37:00Z"
weight = 9626
keywords = [ "recording", "wireshark" ]
aliases = [ "/questions/9626" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Record message with wireshark](/questions/9626/record-message-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9626-score" class="post-score" title="current number of votes">0</div><span id="post-9626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to use wireshark to record the messages. But i don't need all of them. I want to add some rules, for example:</p><p>interface: eth1 Network ip: 127.0.0.1 CBTC Base port: 61500 filename: my_record.pcap</p><p>Is this possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-recording" rel="tag" title="see questions tagged &#39;recording&#39;">recording</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '12, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/4ffb36ec4ee25beb69f3e0fa8969c8b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alice&#39;s gravatar image" /><p><span>Alice</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alice has no accepted answers">0%</span></p></div></div><div id="comments-container-9626" class="comments-container"></div><div id="comment-tools-9626" class="comment-tools"></div><div class="clear"></div><div id="comment-9626-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9629"></span>

<div id="answer-container-9629" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9629-score" class="post-score" title="current number of votes">1</div><span id="post-9629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sure. You're talking about capturing network packets while using a capture filter. Wireshark can do it for you, or you use dumpcap directly. In your case you'd need to specify the NIC and add a capture filter like "host a.b.c.d and tcp port 61500", where a.b.c.d is the IP address you want to filter on. By the way, capturing on localhost might give no or funny results, depending on the OS you're on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '12, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-9629" class="comments-container"><span id="9630"></span><div id="comment-9630" class="comment"><div id="post-9630-score" class="comment-score"></div><div class="comment-text"><p>So i can use the commands like this: tshark -a filesize:1024 -w my_record.pcap -f host 127.0.0.1 and tcp port 61500</p><p>and i can more than one IP addresse?</p><p>Thank you</p></div><div id="comment-9630-info" class="comment-info"><span class="comment-age">(20 Mar '12, 04:05)</span> <span class="comment-user userinfo">Alice</span></div></div><span id="9632"></span><div id="comment-9632" class="comment"><div id="post-9632-score" class="comment-score"></div><div class="comment-text"><p>Yes, you can do -f "host 127.0.0.1 or 192.168.0.1 and tcp port 61500" (as an example). Keep in mind to put the capture filter in quotation marks or the command line will not process the filter like you want it to do.</p><p>(I converted your answer to a comment to keep things simple)</p></div><div id="comment-9632-info" class="comment-info"><span class="comment-age">(20 Mar '12, 04:37)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-9629" class="comment-tools"></div><div class="clear"></div><div id="comment-9629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

