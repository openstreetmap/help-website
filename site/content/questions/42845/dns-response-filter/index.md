+++
type = "question"
title = "DNS Response filter"
description = '''Could someone help me write a filter to select all DNS conversations with response &quot;No such name&quot;. I believe this is a set of Flags value 0x8183, and not an actual text response. Thanks in Advance.'''
date = "2015-06-03T07:42:00Z"
lastmod = "2015-06-04T01:11:00Z"
weight = 42845
keywords = [ "dns", "dnsquery" ]
aliases = [ "/questions/42845" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [DNS Response filter](/questions/42845/dns-response-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42845-score" class="post-score" title="current number of votes">0</div><span id="post-42845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Could someone help me write a filter to select all DNS conversations with response "No such name". I believe this is a set of Flags value 0x8183, and not an actual text response. Thanks in Advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span> <span class="post-tag tag-link-dnsquery" rel="tag" title="see questions tagged &#39;dnsquery&#39;">dnsquery</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '15, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/a329ca8f34fabdfb26806766bc229169?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fixit9660&#39;s gravatar image" /><p><span>fixit9660</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fixit9660 has no accepted answers">0%</span></p></div></div><div id="comments-container-42845" class="comments-container"></div><div id="comment-tools-42845" class="comment-tools"></div><div class="clear"></div><div id="comment-42845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42846"></span>

<div id="answer-container-42846" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42846-score" class="post-score" title="current number of votes">1</div><span id="post-42846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fixit9660 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sure. It's "dns.flags == 0x8183"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '15, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42846" class="comments-container"><span id="42847"></span><div id="comment-42847" class="comment"><div id="post-42847-score" class="comment-score"></div><div class="comment-text"><p>Yes that shows the responses, but I need the whole conversation, to show the actual query too please.</p></div><div id="comment-42847-info" class="comment-info"><span class="comment-age">(03 Jun '15, 07:51)</span> <span class="comment-user userinfo">fixit9660</span></div></div><span id="42848"></span><div id="comment-42848" class="comment"><div id="post-42848-score" class="comment-score"></div><div class="comment-text"><p>Why? the query is repeated in the answer, too. And it's not possible to filter on packet relationships, you can only match on things that exists in a packet.</p></div><div id="comment-42848-info" class="comment-info"><span class="comment-age">(03 Jun '15, 08:01)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="42849"></span><div id="comment-42849" class="comment"><div id="post-42849-score" class="comment-score"></div><div class="comment-text"><p>OK it's in the Queries section but I need to open the packet to see it. I was hoping to see it in the traffic flow on the screen. Unless you can tell me how to save the Queries to a file for further analysis? Otherwise I'll have to open 10,000's of packets manually.</p></div><div id="comment-42849-info" class="comment-info"><span class="comment-age">(03 Jun '15, 08:06)</span> <span class="comment-user userinfo">fixit9660</span></div></div><span id="42850"></span><div id="comment-42850" class="comment"><div id="post-42850-score" class="comment-score"></div><div class="comment-text"><p>Well, you could just add a custom column, displaying "dns.qry.name" to display the query FQDNs in an extra column in the packet list.</p></div><div id="comment-42850-info" class="comment-info"><span class="comment-age">(03 Jun '15, 08:15)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="42872"></span><div id="comment-42872" class="comment"><div id="post-42872-score" class="comment-score"></div><div class="comment-text"><p>That's exactly what I want! Thank you for the prompt and accurate help.</p></div><div id="comment-42872-info" class="comment-info"><span class="comment-age">(04 Jun '15, 01:11)</span> <span class="comment-user userinfo">fixit9660</span></div></div></div><div id="comment-tools-42846" class="comment-tools"></div><div class="clear"></div><div id="comment-42846-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42851"></span>

<div id="answer-container-42851" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42851-score" class="post-score" title="current number of votes">0</div><span id="post-42851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at MATE</p><blockquote><p><a href="https://wiki.wireshark.org/Mate">https://wiki.wireshark.org/Mate</a></p></blockquote><p>You can group request/response with it.</p><p>In the online MATE library you'll find a simple DNS example, which you'll have to extend to match "dns.flags == 0x8183"</p><blockquote><p><a href="https://wiki.wireshark.org/Mate/Library">https://wiki.wireshark.org/Mate/Library</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '15, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-42851" class="comments-container"></div><div id="comment-tools-42851" class="comment-tools"></div><div class="clear"></div><div id="comment-42851-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

