+++
type = "question"
title = "Intermittent web server traffic on port TCP 2048"
description = '''Hi All, I do have a server that is running on the TCP port 2048 but connection in intermittent for the clients. Traffic between the server and the client is traversing through the firewall (Palo Alto). Below the pcap from the Palo (capturing the client-server session) but it doesn&#x27;t tell me much.  D...'''
date = "2017-03-08T03:48:00Z"
lastmod = "2017-03-22T09:56:00Z"
weight = 59918
keywords = [ "tcp" ]
aliases = [ "/questions/59918" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Intermittent web server traffic on port TCP 2048](/questions/59918/intermittent-web-server-traffic-on-port-tcp-2048)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59918-score" class="post-score" title="current number of votes">0</div><span id="post-59918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I do have a server that is running on the TCP port 2048 but connection in intermittent for the clients. Traffic between the server and the client is traversing through the firewall (Palo Alto). Below the pcap from the Palo (capturing the client-server session) but it doesn't tell me much. <img src="https://osqa-ask.wireshark.org/upfiles/pa.JPG" alt="alt text" /></p><p>Does anyone have an idea what is going on&gt;</p><p>Thanks all, Myky</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '17, 03:48</strong></p><img src="https://secure.gravatar.com/avatar/bc027ad1ed53177bd22a7ef8bd4cab03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Myky&#39;s gravatar image" /><p><span>Myky</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Myky has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Mar '17, 03:50</strong> </span></p></div></div><div id="comments-container-59918" class="comments-container"><span id="59919"></span><div id="comment-59919" class="comment"><div id="post-59919-score" class="comment-score">1</div><div class="comment-text"><p>I doubt capturing on the Palo Alto is a good idea - you obviously captured identical packets twice, probably on two firewall interfaces at the same time (incoming/outgoing?).</p><p>Troubleshooting connection problems is better performed by capturing with an additional capture device (e.g. a laptop using a SPAN port), because any device in the communication path may be causing the problem. If you capture on them, they may obfuscate what is happening.</p><p>This means that any capture result you work with may lead to wrong results, because the capture process is biased.</p></div><div id="comment-59919-info" class="comment-info"><span class="comment-age">(08 Mar '17, 03:53)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="59949"></span><div id="comment-59949" class="comment"><div id="post-59949-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper. l will give a go.</p></div><div id="comment-59949-info" class="comment-info"><span class="comment-age">(09 Mar '17, 00:55)</span> <span class="comment-user userinfo">Myky</span></div></div></div><div id="comment-tools-59918" class="comment-tools"></div><div class="clear"></div><div id="comment-59918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60021"></span>

<div id="answer-container-60021" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60021-score" class="post-score" title="current number of votes">0</div><span id="post-60021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Myky has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As you only provided a picture of the packets, nothing much can be said about the real issue with any certainty. However, it sure looks like the SSL ClientHello of 192.168.2.25 is not accepted by 192.168.10.100 and this server sends back an SSL alert, the alert is probably giving you the reason for not accepting the ClientHello, but to be able to tell this, we would need to look at the full data. Can you provide the capture file through CloudShark, Dropbox, GoogleDrive or any other sharing mechanism?</p><p>My bet is that the server has restricted the use of SSL protocols and SSL ciphers to a list of non-vulnerable ones and the Client is not using a supported SSL version or does not offer a supported SSL cipher.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '17, 16:28</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-60021" class="comments-container"><span id="60266"></span><div id="comment-60266" class="comment"><div id="post-60266-score" class="comment-score"></div><div class="comment-text"><p>Thanks guys. Changing the web server to the default port solved the problem. Don't know why!</p></div><div id="comment-60266-info" class="comment-info"><span class="comment-age">(22 Mar '17, 09:56)</span> <span class="comment-user userinfo">Myky</span></div></div></div><div id="comment-tools-60021" class="comment-tools"></div><div class="clear"></div><div id="comment-60021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

