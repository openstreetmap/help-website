+++
type = "question"
title = "Can&#x27;t get list of interfaces: The other host terminated the connection"
description = '''Hello everyone...hope someone can help me. I am trying to capture packets from another machine on my network. When I click the &quot;remote&quot; option and type in the ip address and port number I would like to capture, an error message comes up that says &quot;Can&#x27;t get list of interfaces: The other host termina...'''
date = "2011-01-17T07:18:00Z"
lastmod = "2011-03-12T08:45:00Z"
weight = 1771
keywords = [ "packets", "port", "error" ]
aliases = [ "/questions/1771" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can't get list of interfaces: The other host terminated the connection](/questions/1771/cant-get-list-of-interfaces-the-other-host-terminated-the-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1771-score" class="post-score" title="current number of votes">1</div><span id="post-1771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone...hope someone can help me.</p><p>I am trying to capture packets from another machine on my network. When I click the "remote" option and type in the ip address and port number I would like to capture, an error message comes up that says "Can't get list of interfaces: The other host terminated the connection". Also, when I try to use port 80 instead of the port I am getting the other message with, it returns this error message: "Can't get list of interfaces: Is the server properly installed on #.#.#.#? connect() failed: No connection could be made because the target machine actively refused it. (code 10061) "</p><p>I have tried to find any info on this online but have been unsuccessful. Any help is appreciated..</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '11, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/377f2d482f03d6e5aaac688963f7dd9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="atomv&#39;s gravatar image" /><p><span>atomv</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="atomv has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Jan '11, 07:35</strong> </span></p></div></div><div id="comments-container-1771" class="comments-container"></div><div id="comment-tools-1771" class="comment-tools"></div><div class="clear"></div><div id="comment-1771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1772"></span>

<div id="answer-container-1772" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1772-score" class="post-score" title="current number of votes">2</div><span id="post-1772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The remote capture feature is used to capture frames on a remote host running rpcapd. I guess you're having the wrong idea about its purpose. If you want to capture frames of another system you have to do that via monitor session, network tap or other techniques. See the Wireshark Wiki for common ways to capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '11, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1772" class="comments-container"></div><div id="comment-tools-1772" class="comment-tools"></div><div class="clear"></div><div id="comment-1772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2790"></span>

<div id="answer-container-2790" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2790-score" class="post-score" title="current number of votes">1</div><span id="post-2790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Start "remote packets capture service" from services.msc in remote computer</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '11, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/3680991b76bda34d140b65a62efb1560?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="benson4u2c&#39;s gravatar image" /><p><span>benson4u2c</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="benson4u2c has no accepted answers">0%</span></p></div></div><div id="comments-container-2790" class="comments-container"></div><div id="comment-tools-2790" class="comment-tools"></div><div class="clear"></div><div id="comment-2790-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

