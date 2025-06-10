+++
type = "question"
title = "Why is the PBF StringTable defined to use byte"
description = '''The protocol buffer specified for StringTable states that it stores repeated bytes. message StringTable {  repeated bytes s = 1; }  To the best of my knowledge this could easily be stated as message StringTable {  repeated string s = 1; }  As ProtocolBuffer already defines string to be a utf-8 or eq...'''
date = "2013-07-26T06:32:00Z"
lastmod = "2013-07-28T08:01:00Z"
weight = 24589
keywords = [ "pbf", "encoding" ]
aliases = [ "/questions/24589" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why is the PBF StringTable defined to use byte](/questions/24589/why-is-the-pbf-stringtable-defined-to-use-byte)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24589-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The protocol buffer specified for StringTable states that it stores repeated bytes.</p>
<pre><code>message StringTable {
   repeated bytes s = 1;
}</code></pre>
<p>To the best of my knowledge this could easily be stated as</p>
<pre><code>message StringTable {
   repeated string s = 1;
}</code></pre>
<p>As ProtocolBuffer already defines string to be a utf-8 or equivalent ASCII subset. In its current state I don't see any definition on how strings should be encoded (in PBF), and that is very bad.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-encoding" rel="tag" title="see questions tagged &#39;encoding&#39;">encoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jul '13, 06:32</strong></p>
<img src="https://secure.gravatar.com/avatar/7e77c05737bf455a5bf99c0f17ac19d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="he_the_great&#39;s gravatar image" />
<p><span>he_the_great</span><br />
<span class="score" title="1175 reputation points"><span>1.2k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="he_the_great has 3 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jul '13, 06:33</strong> </span></p>
</div>
</div>
<div id="comments-container-24589" class="comments-container">
<span id="24593"></span>
<div id="comment-24593" class="comment">
<div id="post-24593-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is a very technical question and you are more likely to hear answers to this on the dev list (lists.openstreetmap.org/listinfo/dev).</p>
</div>
<div id="comment-24593-info" class="comment-info">
<span class="comment-age">(26 Jul '13, 08:49)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24589-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24638"></span>

<div id="answer-container-24638" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24638-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From the Protobuf documentation it looks like "bytes" and "string" are treated almost the same everywhere. Internally they seem to be the same, only when setting or getting the data, there might be differences depending on the language used, because some languages have special types for UTF-8 strings. Using Protobuf from C++ there is no difference between these two types.</p>
<p>I don't know what the original reason was, maybe to optimize away any UTF-8 validity check that the library might do internally. But I don't really see any difficulties. All strings in OSM are always UTF-8, so that's what those are, too. If that's not documented it should be.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '13, 08:01</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-24638" class="comments-container">
&#10;</div>
<div id="comment-tools-24638" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24638-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

