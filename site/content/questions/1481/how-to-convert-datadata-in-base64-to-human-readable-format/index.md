+++
type = "question"
title = "How to convert data.data in Base64 to human readable format?"
description = '''Hello, I know Follow TCP Stream do this, but I use custom columns and need to see human readable text instead of  32:30:30:20:43:6f.... is it possible with Lua/Python or with some patch? nice feature if I could define custom column this way: decode_base64(data.data) tolowcase(data.data) is_base64(da...'''
date = "2010-12-25T17:42:00Z"
lastmod = "2010-12-25T17:42:00Z"
weight = 1481
keywords = [ "field", "custom" ]
aliases = [ "/questions/1481" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to convert data.data in Base64 to human readable format?](/questions/1481/how-to-convert-datadata-in-base64-to-human-readable-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1481-score" class="post-score" title="current number of votes">0</div><span id="post-1481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I know Follow TCP Stream do this, but I use custom columns and need to see human readable text instead of 32:30:30:20:43:6f....</p><p>is it possible with Lua/Python or with some patch?</p><p>nice feature if I could define custom column this way:</p><pre><code>decode_base64(data.data)
tolowcase(data.data)
is_base64(data.data) ? decode_base64(data.data) : data.data
decode_base64(bytes[10-34])</code></pre>etc. you got the idea<p>BR</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Dec '10, 17:42</strong></p><img src="https://secure.gravatar.com/avatar/2e18ecb0d92fe1a6045f5ff7c61b6d4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lostbit&#39;s gravatar image" /><p><span>lostbit</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lostbit has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Dec '10, 18:02</strong> </span></p></div></div><div id="comments-container-1481" class="comments-container"></div><div id="comment-tools-1481" class="comment-tools"></div><div class="clear"></div><div id="comment-1481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

