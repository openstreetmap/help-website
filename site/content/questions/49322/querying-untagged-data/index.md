+++
type = "question"
title = "Querying untagged data?"
description = '''Is it possible to query data by attributes that are not tagged? For example if I wanted to find all roads with access:bicycle=yes or bike lanes=both - I end up missing some roads with those attributes simply because those attributes haven&#x27;t been &quot;tagged&quot; yet. I realize I could manually find and tag ...'''
date = "2016-04-21T01:46:00Z"
lastmod = "2016-04-21T13:11:00Z"
weight = 49322
keywords = [ "untagged", "tag", "query", "tagging", "tags" ]
aliases = [ "/questions/49322" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Querying untagged data?](/questions/49322/querying-untagged-data)

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
<span id="post-49322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49322-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to query data by attributes that are not tagged? For example if I wanted to find all roads with access:bicycle=yes or bike lanes=both - I end up missing some roads with those attributes simply because those attributes haven't been "tagged" yet.</p>
<p>I realize I could manually find and tag them all, but I'm searching a rather large area. Any thoughts?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-untagged" rel="tag" title="see questions tagged &#39;untagged&#39;">untagged</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Apr '16, 01:46</strong></p>
<img src="https://secure.gravatar.com/avatar/874c5126a98d733f9bd02366e8ab38f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tordor&#39;s gravatar image" />
<p><span>tordor</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tordor has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49322" class="comments-container">
<span id="49324"></span>
<div id="comment-49324" class="comment">
<div id="post-49324-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>which query language do you use ? OverPass ?</p>
<p>Also, shouldn't access:bicycle=yes be bicycle=yes ?</p>
</div>
<div id="comment-49324-info" class="comment-info">
<span class="comment-age">(21 Apr '16, 06:11)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-49322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49322-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="49325"></span>

<div id="answer-container-49325" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49325-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think there's a misunderstanding here. In OSM parlance, "tagging" means to apply an attribute to a feature. So by this very definition, there cannot be roads "with certain attributes" in OSM that "have not been tagged as such" - if they have not been tagged then they do not have the attributes.</p>
<p>Of course you can run a query that gives you all roads that don't have a certain attribute, but without going out and surveying the road (or checking on aerial imagery at least) you won't know whether those roads rightly don't have the attribute, or should have it but lack it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '16, 06:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-49325" class="comments-container">
&#10;</div>
<div id="comment-tools-49325" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49325-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49334"></span>

<div id="answer-container-49334" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49334-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Keeping Frederik's cautioning words in mind, you can use an <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">overpass</a> query to find <a href="http://overpass-turbo.eu/s/fNN">osm ways tagged with <em>highway</em> but not tagged with <em>any variant of bicycle</em></a>. Remember that the absence of a tag on an osm object doesn't mean that that tag is missing : it might just not be necessary. Also, highways are not the only objects that may have <em>bicycle</em> tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '16, 12:01</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-49334" class="comments-container">
<span id="49337"></span>
<div id="comment-49337" class="comment">
<div id="post-49337-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your responses - they helped clarify some things. I guess what I am confused about is why I can select a road feature in editor, see that the field -allowed access- is bicycle=yes, but no wizard query I run for bicycles ever returns the road.</p>
</div>
<div id="comment-49337-info" class="comment-info">
<span class="comment-age">(21 Apr '16, 13:03)</span> <span class="comment-user userinfo">tordor</span>
</div>
</div>
<span id="49339"></span>
<div id="comment-49339" class="comment">
<div id="post-49339-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Be sure to open the "all tags" tab in your editor or find another way to see the actual tags the object has; perhaps you're just making wrong assumptions about what tags the editor converts your form input to.</p>
</div>
<div id="comment-49339-info" class="comment-info">
<span class="comment-age">(21 Apr '16, 13:11)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-49334" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49334-form-container" class="comment-form-container">
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

