+++
type = "question"
title = "capturing data from tcp stream"
description = '''Hi I want to extract only binary data from entire conversation. How to do it ? I want pure binary data without HTTP headers.  thx in advance for any help'''
date = "2011-01-05T05:32:00Z"
lastmod = "2011-01-10T08:44:00Z"
weight = 1632
keywords = [ "tcp", "stream" ]
aliases = [ "/questions/1632" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [capturing data from tcp stream](/questions/1632/capturing-data-from-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1632-score" class="post-score" title="current number of votes">0</div><span id="post-1632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I want to extract only binary data from entire conversation. How to do it ? I want pure binary data without HTTP headers.</p><p>thx in advance for any help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '11, 05:32</strong></p><img src="https://secure.gravatar.com/avatar/e00f29ecffe643b0ebf3d1dd8d8562aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="borisTheBlade&#39;s gravatar image" /><p><span>borisTheBlade</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="borisTheBlade has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jan '11, 05:33</strong> </span></p></div></div><div id="comments-container-1632" class="comments-container"></div><div id="comment-tools-1632" class="comment-tools"></div><div class="clear"></div><div id="comment-1632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="1633"></span>

<div id="answer-container-1633" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1633-score" class="post-score" title="current number of votes">1</div><span id="post-1633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you try exporting the content you want? If you select File -&gt; Export -&gt; Objects -&gt; HTTP Wireshark will scan the trace and list all objects that have been transfered via HTTP and allow you to save them into files. You should make sure you have the TCP option "Allow subdisector to reassemble TCP streams" enabled (which it is by default), otherwise you will only get the payload of the first packet of each object.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '11, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1633" class="comments-container"></div><div id="comment-tools-1633" class="comment-tools"></div><div class="clear"></div><div id="comment-1633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1640"></span>

<div id="answer-container-1640" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1640-score" class="post-score" title="current number of votes">1</div><span id="post-1640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For UDP/TCP (and for decrypted SSL sessions) you can use "Follow XXX stream" to display only the content. You can then save as Raw to save the content (without the eth/ip/XXX headers.</p><p>You will have to do this for every single stream individually. So if the protocol is HTTP, you are better of with Jasper's suggestion to use the export options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '11, 15:11</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1640" class="comments-container"></div><div id="comment-tools-1640" class="comment-tools"></div><div class="clear"></div><div id="comment-1640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1690"></span>

<div id="answer-container-1690" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1690-score" class="post-score" title="current number of votes">0</div><span id="post-1690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thx for answers. Now 2nd question - im looking for scrpit, which will capture data from 6000 streams, is there any ? I thought about using tcpflow, but it has disadvantage - all signs from captured data, that cannot be printend are changed to "."</p><p>thx for any help</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '11, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/e00f29ecffe643b0ebf3d1dd8d8562aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="borisTheBlade&#39;s gravatar image" /><p><span>borisTheBlade</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="borisTheBlade has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Jan '11, 02:13</strong> </span></p></div></div><div id="comments-container-1690" class="comments-container"><span id="1694"></span><div id="comment-1694" class="comment"><div id="post-1694-score" class="comment-score"></div><div class="comment-text"><p>Then you must have used the -s parameter:</p><p>-s: strip non-printable characters (change to '.')</p><p>I just checked and my version of tcpflow (0.21) nicely outputs the binary data of an SSL session.</p></div><div id="comment-1694-info" class="comment-info"><span class="comment-age">(10 Jan '11, 08:44)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-1690" class="comment-tools"></div><div class="clear"></div><div id="comment-1690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

