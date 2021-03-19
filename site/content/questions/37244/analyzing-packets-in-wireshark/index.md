+++
type = "question"
title = "Analyzing packets in wireshark"
description = '''In wireshark when we capture the packets for the Wi-Fi interface, we can analyze the packets that are being sent to server side around us. In the packet data we also get the ip address and the server address. We also get the packet sent by the server which is a acknowledgement. Is there any way to o...'''
date = "2014-10-21T09:43:00Z"
lastmod = "2014-10-22T05:04:00Z"
weight = 37244
keywords = [ "analysis", "packet" ]
aliases = [ "/questions/37244" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Analyzing packets in wireshark](/questions/37244/analyzing-packets-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37244-score" class="post-score" title="current number of votes">0</div><span id="post-37244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In wireshark when we capture the packets for the Wi-Fi interface, we can analyze the packets that are being sent to server side around us. In the packet data we also get the ip address and the server address. We also get the packet sent by the server which is a acknowledgement. Is there any way to only get the packets which are forwarded to server. I just dont want to see this acknowledgement packets or packets sent by the server. Is that possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '14, 09:43</strong></p><img src="https://secure.gravatar.com/avatar/e35c18b4fe32a6eb0aa4b21c55dff6d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harish%20Vaibhav&#39;s gravatar image" /><p><span>Harish Vaibhav</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harish Vaibhav has no accepted answers">0%</span></p></div></div><div id="comments-container-37244" class="comments-container"></div><div id="comment-tools-37244" class="comment-tools"></div><div class="clear"></div><div id="comment-37244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37264"></span>

<div id="answer-container-37264" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37264-score" class="post-score" title="current number of votes">0</div><span id="post-37264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use a capture filter for that: <code>src host &lt;interface ip address&gt;</code></p><p>Open the capture options dialog, double click the network interface, add the expression in the capture filter textbox (adding in the IP address of that interface), and watch it turn green. Click Ok and start your capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '14, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-37264" class="comments-container"></div><div id="comment-tools-37264" class="comment-tools"></div><div class="clear"></div><div id="comment-37264-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37271"></span>

<div id="answer-container-37271" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37271-score" class="post-score" title="current number of votes">0</div><span id="post-37271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would use the filter (ip.src==a.a.a.a) &amp;&amp; (ip.dst==x.x.x.x) because it sounds like you're capturing from the client side. (where a = your capture PC's ip and x = your server's IP)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '14, 05:04</strong></p><img src="https://secure.gravatar.com/avatar/eab06dcd69504dc40c68cf8fa84a390e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robotfish1911&#39;s gravatar image" /><p><span>robotfish1911</span><br />
<span class="score" title="17 reputation points">17</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robotfish1911 has no accepted answers">0%</span></p></div></div><div id="comments-container-37271" class="comments-container"></div><div id="comment-tools-37271" class="comment-tools"></div><div class="clear"></div><div id="comment-37271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

