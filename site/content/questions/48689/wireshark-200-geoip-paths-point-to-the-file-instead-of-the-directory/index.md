+++
type = "question"
title = "Wireshark 2.0.0 GeoIP paths point to the file instead of the directory"
description = '''The settings in Wireshark want you to locate the exact files for GeoIP name resolution, instead of the path. I couldn&#x27;t figure out why the GeoIP paths weren&#x27;t working on my Windows server. I edited the geoip_db_paths file manually to point to the directory instead of the exact path to the file, then...'''
date = "2015-12-23T11:34:00Z"
lastmod = "2015-12-23T23:51:00Z"
weight = 48689
keywords = [ "geoip", "windows2012r2" ]
aliases = [ "/questions/48689" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 2.0.0 GeoIP paths point to the file instead of the directory](/questions/48689/wireshark-200-geoip-paths-point-to-the-file-instead-of-the-directory)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48689-score" class="post-score" title="current number of votes">0</div><span id="post-48689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The settings in Wireshark want you to locate the exact files for GeoIP name resolution, instead of the path. I couldn't figure out why the GeoIP paths weren't working on my Windows server. I edited the geoip_db_paths file manually to point to the directory instead of the exact path to the file, then things worked fine.</p><p>So yeah, maybe this is just an issue specific to the Windows distro.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-geoip" rel="tag" title="see questions tagged &#39;geoip&#39;">geoip</span> <span class="post-tag tag-link-windows2012r2" rel="tag" title="see questions tagged &#39;windows2012r2&#39;">windows2012r2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '15, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/c4d99c2848cb24a3b895360b3977db16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RyzaJr&#39;s gravatar image" /><p><span>RyzaJr</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RyzaJr has no accepted answers">0%</span></p></div></div><div id="comments-container-48689" class="comments-container"><span id="48691"></span><div id="comment-48691" class="comment"><div id="post-48691-score" class="comment-score"></div><div class="comment-text"><p>Was your intention to extend the Q&amp;A with this topic (so it is a self-answered question) or did you actually want to file a bug?</p></div><div id="comment-48691-info" class="comment-info"><span class="comment-age">(23 Dec '15, 12:10)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="48692"></span><div id="comment-48692" class="comment"><div id="post-48692-score" class="comment-score"></div><div class="comment-text"><p>Ah, sorry. A bug report would be fine.</p></div><div id="comment-48692-info" class="comment-info"><span class="comment-age">(23 Dec '15, 12:25)</span> <span class="comment-user userinfo">RyzaJr</span></div></div><span id="48693"></span><div id="comment-48693" class="comment"><div id="post-48693-score" class="comment-score">1</div><div class="comment-text"><p>If you feel like filing the bug yourself, do it <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi?product=Wireshark">here</a>, otherwise let me know and I'll do that. When I had a look at what you were actually talking about I've realized that I've come across the same issue (the file selector not allowing you to choose a directory) when trying to set something else.</p></div><div id="comment-48693-info" class="comment-info"><span class="comment-age">(23 Dec '15, 12:42)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="48694"></span><div id="comment-48694" class="comment"><div id="post-48694-score" class="comment-score"></div><div class="comment-text"><p>Alright, posted it myself. Thanks.</p></div><div id="comment-48694-info" class="comment-info"><span class="comment-age">(23 Dec '15, 13:11)</span> <span class="comment-user userinfo">RyzaJr</span></div></div></div><div id="comment-tools-48689" class="comment-tools"></div><div class="clear"></div><div id="comment-48689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48695"></span>

<div id="answer-container-48695" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48695-score" class="post-score" title="current number of votes">1</div><span id="post-48695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This bug has already been fixed and will be part of the upcoming 2.0.1 release. You can grab a pre release <a href="https://www.wireshark.org/download/automated/">here</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '15, 23:51</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-48695" class="comments-container"></div><div id="comment-tools-48695" class="comment-tools"></div><div class="clear"></div><div id="comment-48695-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

