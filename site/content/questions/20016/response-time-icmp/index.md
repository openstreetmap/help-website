+++
type = "question"
title = "Response Time ICMP"
description = '''Hello, I realized that the icmp echo reply messages, wireshark shows a field called &quot;Response Time&quot;. Since the ICMP header field carries no reply such as wireshark can discover time travel package? att'''
date = "2013-04-02T06:17:00Z"
lastmod = "2013-05-30T11:58:00Z"
weight = 20016
keywords = [ "icmp" ]
aliases = [ "/questions/20016" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Response Time ICMP](/questions/20016/response-time-icmp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20016-score" class="post-score" title="current number of votes">0</div><span id="post-20016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I realized that the icmp echo reply messages, wireshark shows a field called "Response Time".</p><p>Since the ICMP header field carries no reply such as wireshark can discover time travel package?</p><p>att</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '13, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/36d0d7a76be452591d61c7e1c745feaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="victorrebli&#39;s gravatar image" /><p><span>victorrebli</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="victorrebli has no accepted answers">0%</span></p></div></div><div id="comments-container-20016" class="comments-container"></div><div id="comment-tools-20016" class="comment-tools"></div><div class="clear"></div><div id="comment-20016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20017"></span>

<div id="answer-container-20017" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20017-score" class="post-score" title="current number of votes">1</div><span id="post-20017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is able to calculate the "response time" based on the time stamp of the echo request and echo response packet.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '13, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20017" class="comments-container"><span id="21591"></span><div id="comment-21591" class="comment"><div id="post-21591-score" class="comment-score"></div><div class="comment-text"><p>HI , Kurt:</p><p>May I know how wireshark calculate the response time based on echo request and response? Or could you help to teach how ICMP calculate the response time by themselves?</p></div><div id="comment-21591-info" class="comment-info"><span class="comment-age">(30 May '13, 01:16)</span> <span class="comment-user userinfo">無敵小呆瓜</span></div></div><span id="21617"></span><div id="comment-21617" class="comment"><div id="post-21617-score" class="comment-score"></div><div class="comment-text"><p>Take a look at the ICMP protocol and the time stamp protocol fields.</p><blockquote><p><a href="http://en.wikipedia.org/wiki/Internet_Control_Message_Protocol">http://en.wikipedia.org/wiki/Internet_Control_Message_Protocol</a></p></blockquote></div><div id="comment-21617-info" class="comment-info"><span class="comment-age">(30 May '13, 11:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20017" class="comment-tools"></div><div class="clear"></div><div id="comment-20017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

