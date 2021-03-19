+++
type = "question"
title = "Get user&#x27;s direct intention from &#x27;.pcap&#x27; file."
description = '''Hy everyone, I have a lot of &#x27;.pcap&#x27; files, I want to scan a packets and get a target URL, that mean for example if I run in background Wireshark and i go to www.cnn.com(i get 3000 packets approximately - only for load the home-page), after i click for get one of the article of CNN i get 1500 packet...'''
date = "2014-01-05T22:31:00Z"
lastmod = "2014-01-07T00:30:00Z"
weight = 28594
keywords = [ "pcap", "session", "request" ]
aliases = [ "/questions/28594" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get user's direct intention from '.pcap' file.](/questions/28594/get-users-direct-intention-from-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28594-score" class="post-score" title="current number of votes">0</div><span id="post-28594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hy everyone, I have a lot of '.pcap' files, I want to scan a packets and get a target URL, that mean for example if I run in background Wireshark and i go to www.cnn.com(i get 3000 packets approximately - only for load the home-page), after i click for get one of the article of CNN i get 1500 packets (approximately).</p><p>I want to be capable to find exactly the URL that the user types(www.cnn.com) and the internal URL user go into (click to article into CNN site).</p><p>I try to filter all packets to get all http.request(GET ....), but the problem is when user entering site like CNN we received a lots of internal sessions that create a HTTP Request(for picture, publicity, image, referring to other sites ect...).</p><p>I search a unique raw or word into request or other things int the packet to be sure that user really get to this page(and its not a internal session to publicity, image, referring to other site etc...).</p><p>if its important i passing over packets with python, scapy library. Thanks a lot for any Response Jo.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-session" rel="tag" title="see questions tagged &#39;session&#39;">session</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '14, 22:31</strong></p><img src="https://secure.gravatar.com/avatar/9ebe29cb08c969dfa7913766b8ab6553?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jo%20Smith&#39;s gravatar image" /><p><span>Jo Smith</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jo Smith has no accepted answers">0%</span></p></div></div><div id="comments-container-28594" class="comments-container"></div><div id="comment-tools-28594" class="comment-tools"></div><div class="clear"></div><div id="comment-28594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28613"></span>

<div id="answer-container-28613" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28613-score" class="post-score" title="current number of votes">0</div><span id="post-28613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like a network forensics task. Problem here is that Wireshark has no logic that classifies things like URLs for any given relevance. It's all manual work. If you need something with more logic you need to look for other solutions or code your own.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '14, 00:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28613" class="comments-container"></div><div id="comment-tools-28613" class="comment-tools"></div><div class="clear"></div><div id="comment-28613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

