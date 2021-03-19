+++
type = "question"
title = "read multiple files using tcpdump"
description = '''Hi I wanted to know if I can read multiple files using tcpdump . '''
date = "2012-09-05T13:19:00Z"
lastmod = "2012-09-06T11:21:00Z"
weight = 14064
keywords = [ "filter", "ip", "wireshark", "tcpdump", "multiple-files" ]
aliases = [ "/questions/14064" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [read multiple files using tcpdump](/questions/14064/read-multiple-files-using-tcpdump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14064-score" class="post-score" title="current number of votes">0</div><span id="post-14064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I wanted to know if I can read multiple files using tcpdump .</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-multiple-files" rel="tag" title="see questions tagged &#39;multiple-files&#39;">multiple-files</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '12, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/9b296b0c1a89a6d15e65215e5e6c69b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld0722&#39;s gravatar image" /><p><span>helloworld0722</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld0722 has no accepted answers">0%</span></p></div></div><div id="comments-container-14064" class="comments-container"></div><div id="comment-tools-14064" class="comment-tools"></div><div class="clear"></div><div id="comment-14064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14070"></span>

<div id="answer-container-14070" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14070-score" class="post-score" title="current number of votes">0</div><span id="post-14070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>only one after the other. If that does not work for you, I suggest to use Wiresharks <strong><a href="http://www.wireshark.org/docs/man-pages/mergecap.html">mergecap</a></strong> to merge the files and then either open it with tcpdump or wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Sep '12, 16:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14070" class="comments-container"><span id="14094"></span><div id="comment-14094" class="comment"><div id="post-14094-score" class="comment-score"></div><div class="comment-text"><p>hi kurt , thanks for the reply i wrote a script that would do it after i posted this question . what i wanted to ask is that is it possible to mergecap all files in a directory . for example i have 50 files can i run mergecap once and combine all files into one huge pcap file ???</p></div><div id="comment-14094-info" class="comment-info"><span class="comment-age">(06 Sep '12, 11:21)</span> <span class="comment-user userinfo">helloworld0722</span></div></div></div><div id="comment-tools-14070" class="comment-tools"></div><div class="clear"></div><div id="comment-14070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

