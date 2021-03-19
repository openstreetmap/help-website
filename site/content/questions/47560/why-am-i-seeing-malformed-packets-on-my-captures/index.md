+++
type = "question"
title = "Why am I seeing malformed packets on my captures?"
description = ''' I get the below error for dns requests and response. I also see UDP Bad lenght greater that IP Payload. Any suggestion or advice ffrom anyone as to cause of this error?'''
date = "2015-11-13T02:26:00Z"
lastmod = "2015-11-13T14:10:00Z"
weight = 47560
keywords = [ "iberty", "dns", "malformed" ]
aliases = [ "/questions/47560" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why am I seeing malformed packets on my captures?](/questions/47560/why-am-i-seeing-malformed-packets-on-my-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47560-score" class="post-score" title="current number of votes">0</div><span id="post-47560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/MALFORMED_PACKET.PNG" alt="alt text" /></p><p>I get the below error for dns requests and response.</p><p>I also see UDP Bad lenght greater that IP Payload.</p><p>Any suggestion or advice ffrom anyone as to cause of this error?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iberty" rel="tag" title="see questions tagged &#39;iberty&#39;">iberty</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span> <span class="post-tag tag-link-malformed" rel="tag" title="see questions tagged &#39;malformed&#39;">malformed</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '15, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/f539aede30bd0b1b4759882bd71d8b96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="olutola&#39;s gravatar image" /><p><span>olutola</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="olutola has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Nov '15, 02:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-47560" class="comments-container"><span id="47568"></span><div id="comment-47568" class="comment"><div id="post-47568-score" class="comment-score"></div><div class="comment-text"><p>Can you share the capture file? From an image it's impossible to tell. You could use cloudshark for that.</p></div><div id="comment-47568-info" class="comment-info"><span class="comment-age">(13 Nov '15, 02:59)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-47560" class="comment-tools"></div><div class="clear"></div><div id="comment-47560-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47590"></span>

<div id="answer-container-47590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47590-score" class="post-score" title="current number of votes">0</div><span id="post-47590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While it's true what <span>@Jaap</span> says regarding the screenshot, I'll to make an assumption. The size of the frames and the uniform length pattern (44, 80, 84) does not match a typical DNS query/answer. So I guess that's traffic where Wireshark only believes it could be DNS, based on the protocol and port (TCP/UDP 53), but in reality it's something totally different, hence the "Malformed Packet".</p><p>As the IP 41.190.6.70 is on the internet (Nigeria), this looks a bit "strange". Could be DNS tunneling software, malware or simply a bug somewhere.</p><p>We will see, as soon as you provide the capture file.<br />
</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '15, 14:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-47590" class="comments-container"></div><div id="comment-tools-47590" class="comment-tools"></div><div class="clear"></div><div id="comment-47590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

