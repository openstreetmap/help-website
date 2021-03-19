+++
type = "question"
title = "capture filter default"
description = '''Hello, How can I configure wireshark to have custom, default capture filter?  There is option -f for wireshark which lets read custom filter by wireshark, but I could not find how to make this filter in required format (libpcap). Im not programist and I dont know how to play with pcap_compile. Is th...'''
date = "2013-07-03T04:45:00Z"
lastmod = "2013-07-05T05:43:00Z"
weight = 22595
keywords = [ "capture-filter", "pcap_compile", "libpcap" ]
aliases = [ "/questions/22595" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [capture filter default](/questions/22595/capture-filter-default)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22595-score" class="post-score" title="current number of votes">0</div><span id="post-22595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, How can I configure wireshark to have custom, default capture filter? There is option -f for wireshark which lets read custom filter by wireshark, but I could not find how to make this filter in required format (libpcap). Im not programist and I dont know how to play with pcap_compile. Is there an painless way for preparing this filter? Regards, R</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-pcap_compile" rel="tag" title="see questions tagged &#39;pcap_compile&#39;">pcap_compile</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '13, 04:45</strong></p><img src="https://secure.gravatar.com/avatar/78289254d18619fee0476d41ce9b6bc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rafal&#39;s gravatar image" /><p><span>rafal</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rafal has no accepted answers">0%</span></p></div></div><div id="comments-container-22595" class="comments-container"></div><div id="comment-tools-22595" class="comment-tools"></div><div class="clear"></div><div id="comment-22595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22599"></span>

<div id="answer-container-22599" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22599-score" class="post-score" title="current number of votes">0</div><span id="post-22599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but I could not find how to make this filter in required format (libpcap).</p></blockquote><p>I'm not sure if I understand your question, but the <strong>capture</strong> filter format is defined here</p><blockquote><p><a href="http://www.manpagez.com/man/7/pcap-filter/">http://www.manpagez.com/man/7/pcap-filter/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '13, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22599" class="comments-container"><span id="22688"></span><div id="comment-22688" class="comment"><div id="post-22688-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thanks Kurt, I read it already. It finally started working for me. The easiest way to have it in default value is to make shell script or bat file with predefined filter. BR, Rafal</p></div><div id="comment-22688-info" class="comment-info"><span class="comment-age">(05 Jul '13, 05:43)</span> <span class="comment-user userinfo">rafal</span></div></div></div><div id="comment-tools-22599" class="comment-tools"></div><div class="clear"></div><div id="comment-22599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

