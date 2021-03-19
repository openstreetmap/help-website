+++
type = "question"
title = "How to decode private protocol?"
description = '''Hello, I am debugging our system composed of two TCP/IP stations that use a private protocol over TCP. The protocol message formats are well documented. I would like to &quot;teach&quot; (or customize) wireshark so that it can display these messages according to the message formats. ( I do not know if you cal...'''
date = "2010-11-21T01:46:00Z"
lastmod = "2010-11-21T03:10:00Z"
weight = 1046
keywords = [ "decode", "protocol", "customization", "private" ]
aliases = [ "/questions/1046" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to decode private protocol?](/questions/1046/how-to-decode-private-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1046-score" class="post-score" title="current number of votes">0</div><span id="post-1046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am debugging our system composed of two TCP/IP stations that use a private protocol over TCP. The protocol message formats are well documented. I would like to "teach" (or customize) wireshark so that it can display these messages according to the message formats. ( I do not know if you call it: dissect/decode /parse). Is it possible and how?</p><p>PS: I have successfully used filters by searching specific opcode inside our TCP payload data. But this only allows to filetr our messages from all the network activity. Still the TCP payload data appears as a raw Hexadecimal bytes, while I do have the information of how to interpret it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-customization" rel="tag" title="see questions tagged &#39;customization&#39;">customization</span> <span class="post-tag tag-link-private" rel="tag" title="see questions tagged &#39;private&#39;">private</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '10, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/e1bd5eeb2e465c689960629fc4a5a261?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ShlomoAms&#39;s gravatar image" /><p><span>ShlomoAms</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ShlomoAms has no accepted answers">0%</span></p></div></div><div id="comments-container-1046" class="comments-container"></div><div id="comment-tools-1046" class="comment-tools"></div><div class="clear"></div><div id="comment-1046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1047"></span>

<div id="answer-container-1047" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1047-score" class="post-score" title="current number of votes">1</div><span id="post-1047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can decode your private protocol, you just have to develop your own dissector.</p><p>Best place to start is reading <a href="http://www.wireshark.org/docs/wsdg_html_chunked/">wireshark dev guide</a></p><p>Then, read <em>README</em> documents in <em>./wireshark/doc</em> directory, especially <em>README.developer</em></p><p>Last, look at some protocol dissectors over TCP in <em>./wireshark/epan/dissectors</em> (<em>packet-bgp.c</em> for instance).</p><p>Dissectors are usually written in C, it's also possible to write them in <a href="http://wiki.wireshark.org/Lua">Lua</a> for fast prototyping.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '10, 03:10</strong></p><img src="https://secure.gravatar.com/avatar/2282d6ca42253cbf6aa80c00be6af1b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manux&#39;s gravatar image" /><p><span>manux</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manux has no accepted answers">0%</span></p></div></div><div id="comments-container-1047" class="comments-container"></div><div id="comment-tools-1047" class="comment-tools"></div><div class="clear"></div><div id="comment-1047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

