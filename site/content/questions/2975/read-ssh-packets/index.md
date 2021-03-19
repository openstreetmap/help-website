+++
type = "question"
title = "Read SSH packets?"
description = '''Is there any way I can pass the SSH packets through Wireshark in such a way that it can read them? I can imagine using some sort of proxy, pipe or man-in-the-middle attack, but don&#x27;t really know how to go about pulling it off, and google hasn&#x27;t been terribly helpful on the matter. Could anyone offer...'''
date = "2011-03-21T10:45:00Z"
lastmod = "2011-03-21T16:04:00Z"
weight = 2975
keywords = [ "ssh" ]
aliases = [ "/questions/2975" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Read SSH packets?](/questions/2975/read-ssh-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2975-score" class="post-score" title="current number of votes">0</div><span id="post-2975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way I can pass the SSH packets through Wireshark in such a way that it can read them? I can imagine using some sort of proxy, pipe or man-in-the-middle attack, but don't really know how to go about pulling it off, and google hasn't been terribly helpful on the matter. Could anyone offer an insight as to whether this is even possible, and if so, how to approach it? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssh" rel="tag" title="see questions tagged &#39;ssh&#39;">ssh</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '11, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/62ac013c6ba81536df6689a4f8411880?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Biscuit&#39;s gravatar image" /><p><span>Biscuit</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Biscuit has no accepted answers">0%</span></p></div></div><div id="comments-container-2975" class="comments-container"></div><div id="comment-tools-2975" class="comment-tools"></div><div class="clear"></div><div id="comment-2975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2985"></span>

<div id="answer-container-2985" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2985-score" class="post-score" title="current number of votes">0</div><span id="post-2985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll need the RSA (encryption) keys. See the wiki (<a href="http://wiki.wireshark.org/SSL">http://wiki.wireshark.org/SSL</a>) for further info/guidance/details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-2985" class="comments-container"><span id="2988"></span><div id="comment-2988" class="comment"><div id="post-2988-score" class="comment-score">2</div><div class="comment-text"><p>SSL is actually a totally different protocol from SSH. Currently, Wireshark does not do SSH decryption.</p></div><div id="comment-2988-info" class="comment-info"><span class="comment-age">(21 Mar '11, 15:50)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="2990"></span><div id="comment-2990" class="comment"><div id="post-2990-score" class="comment-score"></div><div class="comment-text"><p>That's what I get for reading too quickly - thanks for the correction!</p></div><div id="comment-2990-info" class="comment-info"><span class="comment-age">(21 Mar '11, 16:04)</span> <span class="comment-user userinfo">wesmorgan1</span></div></div></div><div id="comment-tools-2985" class="comment-tools"></div><div class="clear"></div><div id="comment-2985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

