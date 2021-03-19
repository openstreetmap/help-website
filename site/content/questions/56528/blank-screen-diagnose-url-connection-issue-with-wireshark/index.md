+++
type = "question"
title = "Blank screen - diagnose URL connection issue with wireshark"
description = '''Hi guys I am trying to diagnose a URL connection issue using wire-shark.  We are not blocking planespotters.net on out firewalls / web-sense at all, and we have a route for URL the on firewalls too, but when we go to the URL the page remains blank. I have run a packet capture for this, and i am seei...'''
date = "2016-10-20T03:28:00Z"
lastmod = "2016-10-20T04:11:00Z"
weight = 56528
keywords = [ "url", "ack", "packet-capture", "sniffing", "wireshark" ]
aliases = [ "/questions/56528" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Blank screen - diagnose URL connection issue with wireshark](/questions/56528/blank-screen-diagnose-url-connection-issue-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56528-score" class="post-score" title="current number of votes">0</div><span id="post-56528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys</p><p>I am trying to diagnose a URL connection issue using wire-shark.</p><p>We are not blocking planespotters.net on out firewalls / web-sense at all, and we have a route for URL the on firewalls too, but when we go to the URL the page remains blank.</p><p>I have run a packet capture for this, and i am seeing the application data being sent, followed by all the ACK's, FIN ACK's, and all the usual guys that need to be there for the connection to go through.</p><p>I have also seen only one line stating :</p><p>8919 200.864163 10.55.16.232 104.25.211.5 TLSv1.2 85 Encrypted Alert</p><p>Not sure what that is or if it could be affecting the connection or not.</p><p>But i guess what i am trying to ask is: What specifically should i be looking for in order to see successful connections? Or lack there of would indicate un-successfull connection to the URL?</p><p>Any and all help would be much appreciated, thank you</p><p>Regards,</p><p>Ad</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span> <span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '16, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/9086eb937f774c8e0f841380c36dd12e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="UnConNecTed&#39;s gravatar image" /><p><span>UnConNecTed</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="UnConNecTed has no accepted answers">0%</span></p></div></div><div id="comments-container-56528" class="comments-container"></div><div id="comment-tools-56528" class="comment-tools"></div><div class="clear"></div><div id="comment-56528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56529"></span>

<div id="answer-container-56529" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56529-score" class="post-score" title="current number of votes">0</div><span id="post-56529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But i guess what i am trying to ask is: What specifically should i be looking for in order to see successful connections?</p></blockquote><p>Well, that is a very broad question which could be answered by a book on troubleshooting. In your case where a SSL session towards a website (over a websense proxy) is involved one would see in a trace made on the client, the following:</p><ol><li>Successful 3-way-handshake to the proxy</li><li>Successful SSL handshake to the proxy</li><li>Application data (in SSL) towards the proxy</li><li>Application data (in SSL) from the proxy back to the client</li><li>repeat 3+4 for more objects that are retrieved from the website through the proxy</li><li>Encrypted alert from either the proxy or the client to close down the SSL session</li><li>Encrypted alert from the other side</li><li>FIN/ACK from both sides to close the TCP session</li><li>Acknowledgement of both FIN's (where one FIN could be the ACK of the other FIN)</li></ol><p>Of course this is just a general idea, analyzing why something is not working would involve looking at the packets. Also, being able to receive data from the proxy down not mean it was the correct data or that it was data that the webbrowser could create a webpage from.</p><blockquote><p>Or lack there of would indicate un-successfull connection to the URL?</p></blockquote><p>Again, this is too broad to answer. But missing parts of the above list might indicate an issue...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '16, 04:11</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-56529" class="comments-container"></div><div id="comment-tools-56529" class="comment-tools"></div><div class="clear"></div><div id="comment-56529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

