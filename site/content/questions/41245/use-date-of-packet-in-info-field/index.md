+++
type = "question"
title = "Use date of packet in INFO field"
description = '''When I wireshark the packets do not always arrive at the server in the sequence in which they were generated. This means that if I filter by the date of arrival at the server, I may also get older packets that I do not want and miss new packets that are required.  I could use the information in the ...'''
date = "2015-04-07T03:59:00Z"
lastmod = "2015-04-08T08:38:00Z"
weight = 41245
keywords = [ "info" ]
aliases = [ "/questions/41245" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Use date of packet in INFO field](/questions/41245/use-date-of-packet-in-info-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41245-score" class="post-score" title="current number of votes">0</div><span id="post-41245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I wireshark the packets do not always arrive at the server in the sequence in which they were generated.</p><p>This means that if I filter by the date of arrival at the server, I may also get older packets that I do not want and miss new packets that are required.<br />
</p><p>I could use the information in the info field to get the correct sequence of packets but don't know how to do this.</p><p>Is there a method to extract time text from the data payload and use it to filter, (similar to <em>frame.time</em>) ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-info" rel="tag" title="see questions tagged &#39;info&#39;">info</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '15, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/009aba7d1bbe621134e3a5cc1582e91e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seanj&#39;s gravatar image" /><p><span>seanj</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seanj has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-41245" class="comments-container"></div><div id="comment-tools-41245" class="comment-tools"></div><div class="clear"></div><div id="comment-41245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41270"></span>

<div id="answer-container-41270" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41270-score" class="post-score" title="current number of votes">0</div><span id="post-41270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a method to extract time text from the data payload</p></blockquote><p>In general, no, as most packets do <em>not</em> have the time the packet was sent as part of the packet data, as most protocols do not include that in the packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '15, 20:43</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-41270" class="comments-container"><span id="41285"></span><div id="comment-41285" class="comment"><div id="post-41285-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guy, however the packets I am interested in, all have a date in the data payload. I have performed this operation to some degree using a high level programming language but it would be handier if I could just filter the info i need in wireshark. If it can't be done, it can't be done...</p></div><div id="comment-41285-info" class="comment-info"><span class="comment-age">(08 Apr '15, 07:04)</span> <span class="comment-user userinfo">seanj</span></div></div><span id="41291"></span><div id="comment-41291" class="comment"><div id="post-41291-score" class="comment-score"></div><div class="comment-text"><p>If you know your protocol you could write a LUA dissector that hands you this information you can filter on.</p></div><div id="comment-41291-info" class="comment-info"><span class="comment-age">(08 Apr '15, 08:36)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="41292"></span><div id="comment-41292" class="comment"><div id="post-41292-score" class="comment-score"></div><div class="comment-text"><p>That would be a dissector then. You can create a plain text (<a href="http://wsgd.free.fr/">WSGD</a>), <a href="https://wiki.wireshark.org/Lua">Lua</a> or a traditional <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html">C dissector</a>.</p></div><div id="comment-41292-info" class="comment-info"><span class="comment-age">(08 Apr '15, 08:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-41270" class="comment-tools"></div><div class="clear"></div><div id="comment-41270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

