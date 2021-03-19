+++
type = "question"
title = "Use tshark to analyze source and destination IPs from dumpfile?"
description = '''Hi,  If I use wireshark to open a dumpfile I get something like this: No. Time Source Destination Protocol Info  1 0.000000 10.192.128.15 10.192.3.78 UDP Source port: 5482 Destination port: 35218  I need to use tshark (CLI) to read multiple dumpfiles and get the source and destination IPs. Is this p...'''
date = "2011-09-22T05:07:00Z"
lastmod = "2011-09-28T07:38:00Z"
weight = 6488
keywords = [ "tshark" ]
aliases = [ "/questions/6488" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Use tshark to analyze source and destination IPs from dumpfile?](/questions/6488/use-tshark-to-analyze-source-and-destination-ips-from-dumpfile)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6488-score" class="post-score" title="current number of votes">0</div><span id="post-6488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>If I use wireshark to open a dumpfile I get something like this:</p><pre><code>No.     Time        Source                Destination           Protocol Info

1 0.000000    10.192.128.15         10.192.3.78           UDP      Source port: 5482  Destination port: 35218</code></pre><p>I need to use tshark (CLI) to read multiple dumpfiles and get the source and destination IPs.</p><p>Is this possible?</p><p>Cheers.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '11, 05:07</strong></p><img src="https://secure.gravatar.com/avatar/10db31f5f239296235814002a0edd40e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ravendark&#39;s gravatar image" /><p><span>Ravendark</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ravendark has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Sep '11, 15:32</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6488" class="comments-container"><span id="6490"></span><div id="comment-6490" class="comment"><div id="post-6490-score" class="comment-score">1</div><div class="comment-text"><p>Have you checked the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark manual page</a>?</p></div><div id="comment-6490-info" class="comment-info"><span class="comment-age">(22 Sep '11, 06:15)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="6492"></span><div id="comment-6492" class="comment"><div id="post-6492-score" class="comment-score"></div><div class="comment-text"><p>yes I have but I don't understand much</p></div><div id="comment-6492-info" class="comment-info"><span class="comment-age">(22 Sep '11, 11:09)</span> <span class="comment-user userinfo">Ravendark</span></div></div><span id="6493"></span><div id="comment-6493" class="comment"><div id="post-6493-score" class="comment-score"></div><div class="comment-text"><p>Then you'll have to define more specifically what you want.</p></div><div id="comment-6493-info" class="comment-info"><span class="comment-age">(22 Sep '11, 11:23)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-6488" class="comment-tools"></div><div class="clear"></div><div id="comment-6488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6622"></span>

<div id="answer-container-6622" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6622-score" class="post-score" title="current number of votes">1</div><span id="post-6622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How about tshark -T fields -e ip.src -e ip.dst ... for each file ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '11, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-6622" class="comments-container"></div><div id="comment-tools-6622" class="comment-tools"></div><div class="clear"></div><div id="comment-6622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

