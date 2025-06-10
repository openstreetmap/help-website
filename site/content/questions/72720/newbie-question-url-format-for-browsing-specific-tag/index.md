+++
type = "question"
title = "Newbie question: URL format for browsing specific tag"
description = '''I am new to OSM map, specially URL parameters. I have this tag:amenity=toilets How can I format URL to display all public toilets in one city (eg New York ) ? Tried with https://www.openstreetmap.org/relation/175905/?key=amenity&amp;amp;value=toilets But its wrong'''
date = "2020-01-27T16:59:00Z"
lastmod = "2020-01-27T23:42:00Z"
weight = 72720
keywords = [ "url", "tagging" ]
aliases = [ "/questions/72720" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Newbie question: URL format for browsing specific tag](/questions/72720/newbie-question-url-format-for-browsing-specific-tag)

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
<span id="post-72720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72720-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new to OSM map, specially URL parameters. I have this tag:amenity=toilets How can I format URL to display all public toilets in one city (eg New York ) ?</p>
<p>Tried with <a href="https://www.openstreetmap.org/relation/175905/?key=amenity&amp;value=toilets">https://www.openstreetmap.org/relation/175905/?key=amenity&amp;value=toilets</a></p>
<p>But its wrong</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jan '20, 16:59</strong></p>
<img src="https://secure.gravatar.com/avatar/48c5456713a1b3f88b34bc8cbf469914?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jalle&#39;s gravatar image" />
<p><span>Jalle</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jalle has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> reverted <strong>27 Jan '20, 17:07</strong> </span></p>
</div>
</div>
<div id="comments-container-72720" class="comments-container">
&#10;</div>
<div id="comment-tools-72720" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72720-form-container" class="comment-form-container">
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

<span id="72727"></span>

<div id="answer-container-72727" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72727-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jalle has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>You can't use <a href="https://www.openstreetmap.org">https://www.openstreetmap.org</a> for this purpose.</p>
<p>But you can do it with Overpass API, for example through <a href="http://overpass-turbo.eu/">OverPass Turbo website</a></p>
<p>Here is the request for your need: <a href="http://overpass-turbo.eu/s/Q9I">http://overpass-turbo.eu/s/Q9I</a>. It has been generated throug the <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo/Wizard">OverPass Turbo Wizard</a>, using the expression <code>amenity=toilets in "New York"</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '20, 22:08</strong></p>
<img src="https://secure.gravatar.com/avatar/e8872726c57a506c351071fc1b7b3aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustind&#39;s gravatar image" />
<p><span>augustind</span><br />
<span class="score" title="166 reputation points">166</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustind has one accepted answer">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jan '20, 22:12</strong> </span></p>
</div>
</div>
<div id="comments-container-72727" class="comments-container">
<span id="72728"></span>
<div id="comment-72728" class="comment">
<div id="post-72728-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot !! thats exactly what I wanted</p>
</div>
<div id="comment-72728-info" class="comment-info">
<span class="comment-age">(27 Jan '20, 23:42)</span> <span class="comment-user userinfo">Jalle</span>
</div>
</div>
</div>
<div id="comment-tools-72727" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72727-form-container" class="comment-form-container">
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

