+++
type = "question"
title = "Export HTTP Object - images remain dissected even if I&#x27;ve checked to &quot;Allow sub dissector to reassemble TCP stream&quot;"
description = '''Hi, I&#x27;m new to Wireshark but I&#x27;m studying with some online tutorial and home practice. I&#x27;d found this really could ability of the program &quot;Export Objects&quot;. I&#x27;ve tried to export all the images form an http session, but I see that the png or jpeg file remain dissected and not built up in a single file...'''
date = "2016-04-17T09:25:00Z"
lastmod = "2016-04-17T12:07:00Z"
weight = 51732
keywords = [ "export-http" ]
aliases = [ "/questions/51732" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Export HTTP Object - images remain dissected even if I've checked to "Allow sub dissector to reassemble TCP stream"](/questions/51732/export-http-object-images-remain-dissected-even-if-ive-checked-to-allow-sub-dissector-to-reassemble-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51732-score" class="post-score" title="current number of votes">1</div><span id="post-51732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm new to Wireshark but I'm studying with some online tutorial and home practice.</p><p>I'd found this really could ability of the program "Export Objects". I've tried to export all the images form an http session, but I see that the png or jpeg file remain dissected and not built up in a single file.</p><p>I don't know what I'm doing wrong or missing.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-export-http" rel="tag" title="see questions tagged &#39;export-http&#39;">export-http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '16, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/00e8edc0dc2cb05ff49205edd695a958?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shadowsheep&#39;s gravatar image" /><p><span>shadowsheep</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shadowsheep has no accepted answers">0%</span></p></div></div><div id="comments-container-51732" class="comments-container"></div><div id="comment-tools-51732" class="comment-tools"></div><div class="clear"></div><div id="comment-51732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51733"></span>

<div id="answer-container-51733" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51733-score" class="post-score" title="current number of votes">2</div><span id="post-51733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="shadowsheep has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use version 1.12 or earlier. The export capability is not working properly yet in v2 (currently 2.0.2).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '16, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-51733" class="comments-container"><span id="51735"></span><div id="comment-51735" class="comment"><div id="post-51735-score" class="comment-score"></div><div class="comment-text"><p>Thanks! It's actually right! Version 1.12 works like expected!</p></div><div id="comment-51735-info" class="comment-info"><span class="comment-age">(17 Apr '16, 12:07)</span> <span class="comment-user userinfo">shadowsheep</span></div></div></div><div id="comment-tools-51733" class="comment-tools"></div><div class="clear"></div><div id="comment-51733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

