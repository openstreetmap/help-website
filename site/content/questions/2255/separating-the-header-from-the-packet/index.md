+++
type = "question"
title = "separating the header from the packet"
description = '''hi, im still gettin my head around the new software and was wondering how i might go about separating the header from the packet. i want to be able to use it externally, but every time i copy it i end up with a series of numbers from the Hex (or bits view) depending on what i have enabled. i want th...'''
date = "2011-02-09T05:42:00Z"
lastmod = "2011-02-09T07:00:00Z"
weight = 2255
keywords = [ "url", "header", "packet", "separate" ]
aliases = [ "/questions/2255" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [separating the header from the packet](/questions/2255/separating-the-header-from-the-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2255-score" class="post-score" title="current number of votes">0</div><span id="post-2255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, im still gettin my head around the new software and was wondering how i might go about separating the header from the packet.</p><p>i want to be able to use it externally, but every time i copy it i end up with a series of numbers from the Hex (or bits view) depending on what i have enabled. i want the http: link, is there a filter i have missed?</p><p>EDIT: pretty much, hope to sniff out the headers that are being run (able to copy) so that i can better maintain my system</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-separate" rel="tag" title="see questions tagged &#39;separate&#39;">separate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '11, 05:42</strong></p><img src="https://secure.gravatar.com/avatar/672ea1c8ea1987f7a1da8ccff298ee10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stephen%20Costigan&#39;s gravatar image" /><p><span>Stephen Cost...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stephen Costigan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Feb '11, 06:25</strong> </span></p></div></div><div id="comments-container-2255" class="comments-container"></div><div id="comment-tools-2255" class="comment-tools"></div><div class="clear"></div><div id="comment-2255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2256"></span>

<div id="answer-container-2256" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2256-score" class="post-score" title="current number of votes">0</div><span id="post-2256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to copy out all the URLs that are being requested you can enter this display filter into the display filter field: <code>http.request.method</code>. That will give you all packets containing an HTTP request.</p><p>Now export the packet list to file: File -&gt; Export -&gt; File -&gt; Select "Displayed" in the Packet Range Box to limit the output to your filter results, and choose "CSV" as your "Save as Type". That way you'll get a comma separated file containing all your requests that you can easily edit with any text editor or - usually even more comfortable - using a spreadsheet program.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '11, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2256" class="comments-container"></div><div id="comment-tools-2256" class="comment-tools"></div><div class="clear"></div><div id="comment-2256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

