+++
type = "question"
title = "Inspecting file upload"
description = '''How can I inspect the contents of a file, that I upload over wifi from my local computer to a website? So far when I upload, I see that some packets are generated in wire shark, but after inspecting them it seems like they don&#x27;t contain any data matching what was in the file encrypted or otherwise?'''
date = "2016-07-01T08:54:00Z"
lastmod = "2016-07-02T08:05:00Z"
weight = 53773
keywords = [ "inspect", "upload", "wifi" ]
aliases = [ "/questions/53773" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Inspecting file upload](/questions/53773/inspecting-file-upload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53773-score" class="post-score" title="current number of votes">0</div><span id="post-53773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I inspect the contents of a file, that I upload over wifi from my local computer to a website? So far when I upload, I see that some packets are generated in wire shark, but after inspecting them it seems like they don't contain any data matching what was in the file encrypted or otherwise?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-inspect" rel="tag" title="see questions tagged &#39;inspect&#39;">inspect</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '16, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/594dc31defd9778fa37f40bd399df0f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Strawstack&#39;s gravatar image" /><p><span>Strawstack</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Strawstack has no accepted answers">0%</span></p></div></div><div id="comments-container-53773" class="comments-container"></div><div id="comment-tools-53773" class="comment-tools"></div><div class="clear"></div><div id="comment-53773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53782"></span>

<div id="answer-container-53782" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53782-score" class="post-score" title="current number of votes">1</div><span id="post-53782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Strawstack has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Depending on the type of traffic you are looking at you may need to setup parameters to decrypt the communications in order to get back at the original contents of the file, just as the web server has to do.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '16, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53782" class="comments-container"><span id="53785"></span><div id="comment-53785" class="comment"><div id="post-53785-score" class="comment-score"></div><div class="comment-text"><p>How about when uploading / importing a set of data points (in csv format) to this site: <a href="http://atlas.gc.ca/toporama/en/index.html">http://atlas.gc.ca/toporama/en/index.html</a> ?</p></div><div id="comment-53785-info" class="comment-info"><span class="comment-age">(02 Jul '16, 06:42)</span> <span class="comment-user userinfo">Strawstack</span></div></div><span id="53787"></span><div id="comment-53787" class="comment"><div id="post-53787-score" class="comment-score"></div><div class="comment-text"><p>Well, if we had such a CSV file we could have a try...</p></div><div id="comment-53787-info" class="comment-info"><span class="comment-age">(02 Jul '16, 08:05)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-53782" class="comment-tools"></div><div class="clear"></div><div id="comment-53782-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

