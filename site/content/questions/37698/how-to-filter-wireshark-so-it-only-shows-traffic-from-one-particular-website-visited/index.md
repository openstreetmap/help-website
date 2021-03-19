+++
type = "question"
title = "How to filter Wireshark so it only shows traffic from one particular website visited?"
description = '''I started a capture and visited a couple of websites. I need to use a filter expression to only view traffic from one of the websites visited. I&#x27;m not sure how to do this. Any help?'''
date = "2014-11-08T09:57:00Z"
lastmod = "2014-11-11T06:59:00Z"
weight = 37698
keywords = [ "filter", "traffic", "wireshark" ]
aliases = [ "/questions/37698" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter Wireshark so it only shows traffic from one particular website visited?](/questions/37698/how-to-filter-wireshark-so-it-only-shows-traffic-from-one-particular-website-visited)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37698-score" class="post-score" title="current number of votes">0</div><span id="post-37698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I started a capture and visited a couple of websites.</p><p>I need to use a filter expression to only view traffic from one of the websites visited.</p><p>I'm not sure how to do this.</p><p>Any help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '14, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/14dfc6b2197d20040b7e35229fb5dc16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MacTavish_10&#39;s gravatar image" /><p><span>MacTavish_10</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MacTavish_10 has no accepted answers">0%</span></p></div></div><div id="comments-container-37698" class="comments-container"></div><div id="comment-tools-37698" class="comment-tools"></div><div class="clear"></div><div id="comment-37698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37753"></span>

<div id="answer-container-37753" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37753-score" class="post-score" title="current number of votes">0</div><span id="post-37753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are more ways to do it:</p><ul><li>Get the ip address of the webserver (e.g. 'ping www.wireshark.org') and use the display filter 'ip.addr==looked-up-ip-address' or</li><li>Use the filter 'http.host==www.wireshark.com' to get the POST/GET request followed by 'Follow TCP stream' to get the complete TCP session.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '14, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-37753" class="comments-container"></div><div id="comment-tools-37753" class="comment-tools"></div><div class="clear"></div><div id="comment-37753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

