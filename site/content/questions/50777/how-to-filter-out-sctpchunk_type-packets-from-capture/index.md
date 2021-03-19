+++
type = "question"
title = "how to filter out sctp.chunk_type packets from capture"
description = '''hi,  I am unable to filter out sctp.chunk_type packets, which are eating up the space. which is the correct filter format, to be used. I used this filer in my script (and ! sctp.chunk_type == 5 and ! sctp.chunk_type == 4) also used (and not sctp.chunk_type == 5 and not sctp.chunk_type == 4) [root@wi...'''
date = "2016-03-09T00:15:00Z"
lastmod = "2016-03-09T00:34:00Z"
weight = 50777
keywords = [ "sctp.chunk_type", "capture-filter" ]
aliases = [ "/questions/50777" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to filter out sctp.chunk\_type packets from capture](/questions/50777/how-to-filter-out-sctpchunk_type-packets-from-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50777-score" class="post-score" title="current number of votes">0</div><span id="post-50777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, I am unable to filter out sctp.chunk_type packets, which are eating up the space. which is the correct filter format, to be used.</p><p>I used this filer in my script (and ! sctp.chunk_type == 5 and ! sctp.chunk_type == 4) also used (and not sctp.chunk_type == 5 and not sctp.chunk_type == 4)</p><p>[<span class="__cf_email__" data-cfemail="f785989883b7809e8592849f96859cdac6">[email protected]</span> ~]# tshark -q -w /tmp/traces_1.cap -B 10 -i e</p><p>[<span class="__cf_email__" data-cfemail="15677a7a6155627c6770667d74677e3824">[email protected]</span> ~]# Running as user "root" and group "root". This could be dangerous. Capturing on 'em2' tshark: Invalid capture filter "</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sctp.chunk_type" rel="tag" title="see questions tagged &#39;sctp.chunk_type&#39;">sctp.chunk_type</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '16, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/cda0c82a9c0a558b315872288990422d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="murthyvo&#39;s gravatar image" /><p><span>murthyvo</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="murthyvo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Mar '16, 00:29</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-50777" class="comments-container"></div><div id="comment-tools-50777" class="comment-tools"></div><div class="clear"></div><div id="comment-50777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50779"></span>

<div id="answer-container-50779" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50779-score" class="post-score" title="current number of votes">0</div><span id="post-50779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please look at the difference between <em>display filter</em> and <em>capture filter</em> syntax (they differ significantly) and capabilities (which differ significantly too, as the display filters make full use of packet dissection while capture filters are much simpler). In your particular case you can only use the capture filter if the sctp chunk type can be found at a fixed place in the packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '16, 00:34</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50779" class="comments-container"></div><div id="comment-tools-50779" class="comment-tools"></div><div class="clear"></div><div id="comment-50779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

