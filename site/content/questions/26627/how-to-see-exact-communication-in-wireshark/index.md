+++
type = "question"
title = "How to see exact communication in wireshark?"
description = '''We have installed a proxy inbetween host and internet. when i make a request google.com and if i see the communication in wireshark, i can just see the communication to proxy and reply from proxy, since proxy makes the actual request and reply to host. in this case, how do we see the actual communic...'''
date = "2013-11-02T21:45:00Z"
lastmod = "2013-11-03T03:07:00Z"
weight = 26627
keywords = [ "proxy", "wireshark" ]
aliases = [ "/questions/26627" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to see exact communication in wireshark?](/questions/26627/how-to-see-exact-communication-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26627-score" class="post-score" title="current number of votes">0</div><span id="post-26627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have installed a proxy inbetween host and internet. when i make a request google.com and if i see the communication in wireshark, i can just see the communication to proxy and reply from proxy, since proxy makes the actual request and reply to host.</p><p>in this case, how do we see the actual communication even if proxy is in intermediate,</p><p>like communication from host to google.com in wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '13, 21:45</strong></p><img src="https://secure.gravatar.com/avatar/5ac164cc74888385cb1087dd8d0f6c6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mythbuster&#39;s gravatar image" /><p><span>mythbuster</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mythbuster has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Sep '14, 22:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-26627" class="comments-container"></div><div id="comment-tools-26627" class="comment-tools"></div><div class="clear"></div><div id="comment-26627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26631"></span>

<div id="answer-container-26631" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26631-score" class="post-score" title="current number of votes">0</div><span id="post-26631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, the traffic between your host and the proxy will be actual traffic as is it seen on the network. You can not see the traffic on "the other side of the proxy" from your own host.</p><p>If you want to see how the proxy is requesting the information from the website, you need to capture on the public side of the proxy. This can be done either on the proxy itself (choose the internet facing network interface) or you can mirror the traffic on the switch that connects the public interface of the proxy to the rest of the network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '13, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-26631" class="comments-container"></div><div id="comment-tools-26631" class="comment-tools"></div><div class="clear"></div><div id="comment-26631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

