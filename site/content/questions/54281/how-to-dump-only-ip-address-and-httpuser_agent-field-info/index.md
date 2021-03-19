+++
type = "question"
title = "How to dump only IP address and http.user_agent field info?"
description = '''If the packet doesn&#x27;t have a http.user_agent field, don&#x27;t dump any data. If the packet does have a http.user_agent field, dump the IP address and the http.user_agent field information as follows: tshark -r -w File1.pcapng -T fields -e ip.src -e http.user_agent -w File1.pcapng But it&#x27;s not doing what...'''
date = "2016-07-24T22:38:00Z"
lastmod = "2016-07-26T19:15:00Z"
weight = 54281
keywords = [ "filter", "http.user_agent" ]
aliases = [ "/questions/54281" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to dump only IP address and http.user\_agent field info?](/questions/54281/how-to-dump-only-ip-address-and-httpuser_agent-field-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54281-score" class="post-score" title="current number of votes">0</div><span id="post-54281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If the packet doesn't have a http.user_agent field, don't dump any data.</p><p>If the packet does have a http.user_agent field, dump the IP address and the http.user_agent field information as follows:</p><p>tshark -r -w File1.pcapng -T fields -e ip.src -e http.user_agent -w File1.pcapng</p><p>But it's not doing what I want.</p><p>Any suggestions as to how to get it to work.</p><p>FWIW</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-http.user_agent" rel="tag" title="see questions tagged &#39;http.user_agent&#39;">http.user_agent</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '16, 22:38</strong></p><img src="https://secure.gravatar.com/avatar/6c8f0de8cb4ef9ad7093eefe24030e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbenton&#39;s gravatar image" /><p><span>wbenton</span><br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbenton has no accepted answers">0%</span></p></div></div><div id="comments-container-54281" class="comments-container"><span id="54282"></span><div id="comment-54282" class="comment"><div id="post-54282-score" class="comment-score"></div><div class="comment-text"><p>For starters remove the first '-W File1.pcapng' and replace with the filename you intend to read (not being File1.pcapng).</p></div><div id="comment-54282-info" class="comment-info"><span class="comment-age">(24 Jul '16, 23:43)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="54319"></span><div id="comment-54319" class="comment"><div id="post-54319-score" class="comment-score"></div><div class="comment-text"><p>Sorry about that, when I renamed the actual file with a temporary filename, I guess I replaced too much.</p><p>The following is actually what I was trying:</p><p>tshark -r File1.pcapng -T fields -e ip.src -e http.user_agent -w File1.txt</p><p>But it outputs IP source for fields which don't have any http.user_agent field in it as well.</p><p>I only want output for fields which have the http.user_agent field in them... not for every single packet.</p><p>Any advice on how to do that?</p></div><div id="comment-54319-info" class="comment-info"><span class="comment-age">(25 Jul '16, 17:00)</span> <span class="comment-user userinfo">wbenton</span></div></div></div><div id="comment-tools-54281" class="comment-tools"></div><div class="clear"></div><div id="comment-54281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54327"></span>

<div id="answer-container-54327" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54327-score" class="post-score" title="current number of votes">2</div><span id="post-54327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wbenton has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Add <code>-Y http.user_agent</code> to tshark parameters and replace the last <code>-w</code> with <code>&gt;</code>. The expression folowing the <code>-Y</code> is a display filter; the <code>-w</code> instructs tshark to write the complete filtered packets into a new capture file, while the <code>&gt;</code> tells the shell to write tshark's stdout into a (text) file.</p><p>The protocol fields specified using <code>-e</code> are printed independently from each other, i.e. if one of them is not present in a particular frame but the rest is, the rest is printed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '16, 22:30</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-54327" class="comments-container"><span id="54360"></span><div id="comment-54360" class="comment"><div id="post-54360-score" class="comment-score"></div><div class="comment-text"><p>That did it...</p><p>Thanks!</p></div><div id="comment-54360-info" class="comment-info"><span class="comment-age">(26 Jul '16, 19:15)</span> <span class="comment-user userinfo">wbenton</span></div></div></div><div id="comment-tools-54327" class="comment-tools"></div><div class="clear"></div><div id="comment-54327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

