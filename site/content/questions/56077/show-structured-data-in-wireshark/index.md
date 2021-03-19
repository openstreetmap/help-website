+++
type = "question"
title = "show structured data in WireShark"
description = '''I need to show structured data (HTML rich snippets) in WireShark UI (i.e. RDFa, Microdata, JSON-LD and Microformats). How to do parse HTML over HTTP/S to detect rich snippets and show all found in WireShark UI. I was thinking a subdissector for each type found (e.g. hRecipe) but this does not make s...'''
date = "2016-10-02T12:50:00Z"
lastmod = "2016-10-02T13:40:00Z"
weight = 56077
keywords = [ "richsnippets", "subdissector", "http", "https" ]
aliases = [ "/questions/56077" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [show structured data in WireShark](/questions/56077/show-structured-data-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56077-score" class="post-score" title="current number of votes">0</div><span id="post-56077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to show structured data (HTML rich snippets) in WireShark UI (i.e. RDFa, Microdata, JSON-LD and Microformats). How to do parse HTML over HTTP/S to detect rich snippets and show all found in WireShark UI. I was thinking a subdissector for each type found (e.g. hRecipe) but this does not make sense if HTTP has TCP as a subdissector. What is the best approach?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-richsnippets" rel="tag" title="see questions tagged &#39;richsnippets&#39;">richsnippets</span> <span class="post-tag tag-link-subdissector" rel="tag" title="see questions tagged &#39;subdissector&#39;">subdissector</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '16, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/6116b62f0eaf715d6fe35edb91f9a20b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuralsea&#39;s gravatar image" /><p><span>neuralsea</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuralsea has no accepted answers">0%</span></p></div></div><div id="comments-container-56077" class="comments-container"><span id="56079"></span><div id="comment-56079" class="comment"><div id="post-56079-score" class="comment-score"></div><div class="comment-text"><p>It's reverse, http is a subdissector of tcp, i.e. the tcp dissector invokes http dissector if the payload matches the heuristic criteria used to identify http, or if the tcp port matches one of those registered for http. Accordingly, you would have to hook your own dissectors to http dissector's list of heuristic sub-dissectors.</p></div><div id="comment-56079-info" class="comment-info"><span class="comment-age">(02 Oct '16, 13:17)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="56080"></span><div id="comment-56080" class="comment"><div id="post-56080-score" class="comment-score"></div><div class="comment-text"><p>Thank you sindy. This has helped tremendously.</p></div><div id="comment-56080-info" class="comment-info"><span class="comment-age">(02 Oct '16, 13:40)</span> <span class="comment-user userinfo">neuralsea</span></div></div></div><div id="comment-tools-56077" class="comment-tools"></div><div class="clear"></div><div id="comment-56077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

