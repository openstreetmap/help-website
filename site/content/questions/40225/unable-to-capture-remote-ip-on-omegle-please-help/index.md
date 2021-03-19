+++
type = "question"
title = "Unable to capture remote IP on Omegle, please help"
description = '''Hi! I don&#x27;t know what I&#x27;m doing wrong, I&#x27;m new to Wireshark, I&#x27;ve seen tutorials on Youtube and yet I can&#x27;t capture a remote IP address of a person texting with me over Omegle (so I could see where is the person&#x27;t location - just for fun of course). I select my caputure device (my NIC), I filter UDP...'''
date = "2015-03-03T12:27:00Z"
lastmod = "2015-03-04T16:00:00Z"
weight = 40225
keywords = [ "capture", "cant", "packets", "udp", "omegle" ]
aliases = [ "/questions/40225" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to capture remote IP on Omegle, please help](/questions/40225/unable-to-capture-remote-ip-on-omegle-please-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40225-score" class="post-score" title="current number of votes">0</div><span id="post-40225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I don't know what I'm doing wrong, I'm new to Wireshark, I've seen tutorials on Youtube and yet I can't capture a remote IP address of a person texting with me over Omegle (so I could see where is the person't location - just for fun of course).</p><p>I select my caputure device (my NIC), I filter UDP packets and yet all I get is 192.168.2.1 (my router) and 192.168.2.2 (my computer's local IP). And so if I go under IPv4 Source I can't see anything else but those two IPs.</p><p>Note: I'm texting on Omegle, not video-ing, is that a problems? Note 2: I'm behind 2 routers, but I don't think that could be the problem?</p><p>Please help me, thank oyu!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-cant" rel="tag" title="see questions tagged &#39;cant&#39;">cant</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-omegle" rel="tag" title="see questions tagged &#39;omegle&#39;">omegle</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '15, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/b8799db0617a43c40eea12c727879309?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bellzemos&#39;s gravatar image" /><p><span>Bellzemos</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bellzemos has no accepted answers">0%</span></p></div></div><div id="comments-container-40225" class="comments-container"><span id="40229"></span><div id="comment-40229" class="comment"><div id="post-40229-score" class="comment-score"></div><div class="comment-text"><p>Anyone, please?</p></div><div id="comment-40229-info" class="comment-info"><span class="comment-age">(03 Mar '15, 13:59)</span> <span class="comment-user userinfo">Bellzemos</span></div></div></div><div id="comment-tools-40225" class="comment-tools"></div><div class="clear"></div><div id="comment-40225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40231"></span>

<div id="answer-container-40231" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40231-score" class="post-score" title="current number of votes">0</div><span id="post-40231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Chat tools/app usually don't talk directly to the persons devices, as that won't work (think about private addresses, NAT, proxies, etc.). Instead they use a relay server of the app vendor. So, all you will see is the ip address of the Omegle chat server. There is no way to find the IP address of the chat partner unless Omegle discloses that information in the app itself.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '15, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-40231" class="comments-container"><span id="40236"></span><div id="comment-40236" class="comment"><div id="post-40236-score" class="comment-score"></div><div class="comment-text"><p>Here, it starts happening at about 2 minutes in: <a href="https://www.youtube.com/watch?v=hBcvX6GA5UQ">https://www.youtube.com/watch?v=hBcvX6GA5UQ</a></p><p>There some more videos showing the same trick (but I'm still unable to make it work). It's also possible to get the other person's IP while talking over Skype by using Wireshark - I've seen it done.</p><p>So, how can I do that?</p></div><div id="comment-40236-info" class="comment-info"><span class="comment-age">(03 Mar '15, 15:13)</span> <span class="comment-user userinfo">Bellzemos</span></div></div><span id="40237"></span><div id="comment-40237" class="comment"><div id="post-40237-score" class="comment-score"></div><div class="comment-text"><p>O.K. looks like they are using some form of P2P protocol via UDP to stream the cam videos directly between the clients. Well, in that case you should see the IP address of the other side. Looks like this is only done for Video chats, not text chats (are being relayed via the Omegle servers). Maybe that's the reason why you can't find the IP.</p></div><div id="comment-40237-info" class="comment-info"><span class="comment-age">(03 Mar '15, 15:36)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="40260"></span><div id="comment-40260" class="comment"><div id="post-40260-score" class="comment-score"></div><div class="comment-text"><p>@ Kurt - you were right, I tried the video thing and I was able to get the right coutry from the captured IP but not necesarily the city. Do you know if this would work on Skype as well?</p><p>Also, a bit off topic: does using and having Wireshark installed on a Windows PC pose any kind of security risk?</p><p>Thank you!</p></div><div id="comment-40260-info" class="comment-info"><span class="comment-age">(04 Mar '15, 12:59)</span> <span class="comment-user userinfo">Bellzemos</span></div></div><span id="40261"></span><div id="comment-40261" class="comment"><div id="post-40261-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Do you know if this would work on Skype as well?</p></blockquote><p>maybe. Google will tell you ;-)</p><blockquote><p>Also, a bit off topic: does using and having Wireshark installed on a Windows PC pose any kind of security risk?</p></blockquote><p>maybe not for you :-)</p><p>Well, actually there is a theoretical risk. Wireshark is a piece of software where a few hundred people contributed code to. Nobody will guarantee that there are no security related bugs in Wireshark, especially not for the dissectors.</p><p>So, the honest answer is: Yes running Wireshark <strong>could</strong> pose a risk if you are processing capture data (pcap file or captured on the wire) with traffic that triggers a buffer overflow in one of the dissectors. That would be really bad, even though Wireshark has some privilege separation. Anyway, this is all theoretical and I don't know any proof of concept that shows how to do that.</p><p>So, the good news for you: Go ahead and use Wireshark.</p><p>But, if your computer starts to make strange sounds....</p><pre><code>     RUN !!! </code></pre><p>or even better "<a href="https://www.youtube.com/watch?v=IKqXu-5jw60">Duck and Cover</a>" ;-))</p><blockquote><p><a href="https://www.youtube.com/watch?v=IKqXu-5jw60">https://www.youtube.com/watch?v=IKqXu-5jw60</a></p></blockquote></div><div id="comment-40261-info" class="comment-info"><span class="comment-age">(04 Mar '15, 16:00)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-40231" class="comment-tools"></div><div class="clear"></div><div id="comment-40231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

