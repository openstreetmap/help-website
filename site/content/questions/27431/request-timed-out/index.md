+++
type = "question"
title = "Request Timed Out"
description = '''Hello everyone. I am new to wireshark and i need help figuring some things out. i pinged www.mit.edu and i wrote down the details that appeared. Then i opened Wireshark, went to Analyze-&amp;gt;Display Filters and chose IP ADDRESS option. Then i wrote on &#x27;&#x27;filter string&#x27;&#x27; section the ip adress that appe...'''
date = "2013-11-26T07:16:00Z"
lastmod = "2013-11-26T08:26:00Z"
weight = 27431
keywords = [ "cmd", "ping", "wireshark" ]
aliases = [ "/questions/27431" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Request Timed Out](/questions/27431/request-timed-out)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27431-score" class="post-score" title="current number of votes">0</div><span id="post-27431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone. I am new to wireshark and i need help figuring some things out. i pinged www.mit.edu and i wrote down the details that appeared. Then i opened Wireshark, went to Analyze-&gt;Display Filters and chose IP ADDRESS option. Then i wrote on ''filter string'' section the ip adress that appeared when i pinged www.mit.edu Then i pinged www.mit.edu again and i saw on wireshark the source, destination, protocol used etc. Then i opened my browser and went to www.cnn.com. Then went back to cmd and pinged www.cnn.com but request timed out. My question is why my request timed out? Why i couldnt send packets at all? Thank you for spending time on reading this. I appreciate any kind of help :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cmd" rel="tag" title="see questions tagged &#39;cmd&#39;">cmd</span> <span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '13, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/3781f5a7aebfa7785f7eab05c6b0eb80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jeronimo&#39;s gravatar image" /><p><span>Jeronimo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jeronimo has no accepted answers">0%</span></p></div></div><div id="comments-container-27431" class="comments-container"></div><div id="comment-tools-27431" class="comment-tools"></div><div class="clear"></div><div id="comment-27431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27435"></span>

<div id="answer-container-27435" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27435-score" class="post-score" title="current number of votes">0</div><span id="post-27435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I guess there is a Firewall blocking your ICMP Echo Request packets. It allows HTTP of course, because otherwise you couldn't access their web site, but that is using TCP on port 80, not ICMP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-27435" class="comments-container"></div><div id="comment-tools-27435" class="comment-tools"></div><div class="clear"></div><div id="comment-27435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

