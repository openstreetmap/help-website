+++
type = "question"
title = "Network Very Slow"
description = '''Hi Guys, I&#x27;m a new user to wireshark and was wondering the best way to diagnose a very slow network in our office. Since last week users have been complaining of file transfers to and from the file servers to be very slow. I have personally checked them as well and they take forever to transfer an a...'''
date = "2014-04-14T13:04:00Z"
lastmod = "2014-04-14T14:10:00Z"
weight = 31800
keywords = [ "arp" ]
aliases = [ "/questions/31800" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Network Very Slow](/questions/31800/network-very-slow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31800-score" class="post-score" title="current number of votes">0</div><span id="post-31800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>I'm a new user to wireshark and was wondering the best way to diagnose a very slow network in our office. Since last week users have been complaining of file transfers to and from the file servers to be very slow. I have personally checked them as well and they take forever to transfer an average sized file (less than 10mb)tahe couple of minutes.</p><p>I see a lot of ARP traffic when I run wireshark. The IP indicates our print server. I have tried restarting the server as well.</p><p>Any guidance would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '14, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/7d931e315175badb189ccea982c4f543?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marusiraa&#39;s gravatar image" /><p><span>marusiraa</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marusiraa has no accepted answers">0%</span></p></div></div><div id="comments-container-31800" class="comments-container"><span id="31801"></span><div id="comment-31801" class="comment"><div id="post-31801-score" class="comment-score"></div><div class="comment-text"><p>This is unfortunately a fairly loaded question and would require a lot more in-depth knowledge of TCP and network flow to truly come up with the exact reason. Do you have a sample pcap which might shed some light on the file-transfers? Have you checked things on the server itself, like logs for potential errors? Check the disk I/O related error or failing equipment? It might not be the network at fault.</p></div><div id="comment-31801-info" class="comment-info"><span class="comment-age">(14 Apr '14, 13:19)</span> <span class="comment-user userinfo">mire3212</span></div></div></div><div id="comment-tools-31800" class="comment-tools"></div><div class="clear"></div><div id="comment-31800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31804"></span>

<div id="answer-container-31804" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31804-score" class="post-score" title="current number of votes">0</div><span id="post-31804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There can be a variety of reason for a slow network. Some common reasons are</p><ul><li><p>a loop in the Layer2 architecture (connecting switches to each other to build a circle). If this is the case, you will see a lot of duplicate frames. The ARP frames you mentioned could be first sign for this. If you see the same ARP request in consecutive order in the capture file, with very little delay, you should first check if there is a loop somewhere.</p></li><li><p>a broken device, flooding the network with broken frames</p></li><li>dumb user, trying hacker tools on the coporate network, like ARP flooding tools to capture network traffic, essentially 'converting' your switch into a HUB that forwards frames to all ports.</li></ul><p>I could imagine some other reason, but those are the first that pop up in my mind, based on your description.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '14, 14:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31804" class="comments-container"></div><div id="comment-tools-31804" class="comment-tools"></div><div class="clear"></div><div id="comment-31804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

