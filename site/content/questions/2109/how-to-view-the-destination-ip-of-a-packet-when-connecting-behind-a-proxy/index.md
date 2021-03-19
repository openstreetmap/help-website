+++
type = "question"
title = "How to view the destination IP of a packet when connecting behind a proxy?"
description = '''Hi, I am behind a proxy and all the packets that I send have my proxy: 192.168.1.5 as a destination, I do not know how to see their actual destination (destination&#x27;s IP). Thanks a lot for your help'''
date = "2011-02-02T10:37:00Z"
lastmod = "2011-02-02T10:42:00Z"
weight = 2109
keywords = [ "ip", "behind", "proxy" ]
aliases = [ "/questions/2109" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to view the destination IP of a packet when connecting behind a proxy?](/questions/2109/how-to-view-the-destination-ip-of-a-packet-when-connecting-behind-a-proxy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2109-score" class="post-score" title="current number of votes">0</div><span id="post-2109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am behind a proxy and all the packets that I send have my proxy: 192.168.1.5 as a destination, I do not know how to see their actual destination (destination's IP). Thanks a lot for your help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-behind" rel="tag" title="see questions tagged &#39;behind&#39;">behind</span> <span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '11, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/faf14674299f1d25bb7469ac1c01e3bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="intuition_man&#39;s gravatar image" /><p><span>intuition_man</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="intuition_man has no accepted answers">0%</span></p></div></div><div id="comments-container-2109" class="comments-container"></div><div id="comment-tools-2109" class="comment-tools"></div><div class="clear"></div><div id="comment-2109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2110"></span>

<div id="answer-container-2110" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2110-score" class="post-score" title="current number of votes">2</div><span id="post-2110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On the client side you can't see the IP address that the proxy will connect to. However, you can extract the dns name it will connect to in the Host: header of the HTTP request. You can then do the name resolving yourself, but this is no 100% guarantee that the Proxy uses the same address. This is because it:</p><ul><li>might use a different nameserver that returns a different IP address</li><li>the same name server might respond with a different IP address to different clients</li><li>there might be multiple IP addresses returned and you don't know which one the proxy picked</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '11, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2110" class="comments-container"></div><div id="comment-tools-2110" class="comment-tools"></div><div class="clear"></div><div id="comment-2110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

