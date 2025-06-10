+++
type = "question"
title = "License requirement for use in a new podcast tag"
description = '''I&#x27;m part of a team working on enhancing the specification used by podcasters across the world to produce open RSS feeds that describe their podcasts. These are used by hundreds of thousands of different publishers as the main syndication format to get their podcasts into podcast apps like Apple Podc...'''
date = "2020-10-14T02:56:00Z"
lastmod = "2020-10-14T11:36:00Z"
weight = 77084
keywords = [ "attribution", "licence" ]
aliases = [ "/questions/77084" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [License requirement for use in a new podcast tag](/questions/77084/license-requirement-for-use-in-a-new-podcast-tag)

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
<span id="post-77084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77084-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm part of a team working on enhancing the specification used by podcasters across the world to produce open RSS feeds that describe their podcasts. These are used by hundreds of thousands of different publishers as the main syndication format to get their podcasts into podcast apps like Apple Podcasts and hundreds of others. The open nature of podcasting means there's nobody really "in charge", and I have no lawyers to ask questions to.</p>
<p>I'm also an active OSM Foundation member, and contribute regularly to the local map of my area.</p>
<p>My proposal for a "podcast:location" specification is to incorporate the type and ID of an OSM object. You'll see the current proposal here: <a href="https://github.com/Podcastindex-org/podcast-namespace">https://github.com/Podcastindex-org/podcast-namespace</a></p>
<p>Recognising that an OSM ID is not permanent, but cities and countries are "permanent enough" for this use, this is to allow podcast apps and search engines to be able to answer the question "where are some good true crime podcasts near me?" or "what shows are about the place I live in"?</p>
<p>An example of the spec being used is:</p>
<pre><code>&lt;podcast:location latlon:&quot;51.49942,-0.12444&quot; osmid=&quot;R1567699&quot;&gt;GB|Houses of Parliament, London&lt;/podcast:location&gt;</code></pre>
<p>... which in this case links to the Relation type, ID 1567699, which is actually marked "Palace of Westminster" in OSM. The "osmid" in this is optional.</p>
<p>Use of any data discovered from OSM in any form would require use of the full OSM database, of course. But my question is:</p>
<p><strong>Will the presence of the ID and type within the open RSS feed - without any other OSM data - require attribution inside the feed itself?</strong></p>
<p>I would hope that this would be appropriate use of OpenStreetMap identifiers, and enable significant publicity for the OSM project as a whole. There are 1.5m podcasts currently available, and this world is growing rapidly.</p>
<p>Guidance on attribution would be very much welcomed.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-attribution" rel="tag" title="see questions tagged &#39;attribution&#39;">attribution</span> <span class="post-tag tag-link-licence" rel="tag" title="see questions tagged &#39;licence&#39;">licence</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Oct '20, 02:56</strong></p>
<img src="https://secure.gravatar.com/avatar/e5c550f1d414e90c3dea32f2630e258e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jamescridland&#39;s gravatar image" />
<p><span>jamescridland</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jamescridland has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77084" class="comments-container">
<span id="77096"></span>
<div id="comment-77096" class="comment">
<div id="post-77096-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not an answer to your question but have you considered referencing a wikidata item? Many OSM objects in turn reference the corresponding wikidata item and you could make the match this way. This could be a way around relying on only fairly stable OSM IDs but not sure current coverage is good enough.</p>
</div>
<div id="comment-77096-info" class="comment-info">
<span class="comment-age">(14 Oct '20, 10:08)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-77084" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77084-form-container" class="comment-form-container">
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

<span id="77100"></span>

<div id="answer-container-77100" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77100-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Having now discovered and read <a href="https://wiki.osmfoundation.org/wiki/Licence/Community_Guidelines/Geocoding_-_Guideline#Examples">this page</a> I think I'm now comfortable that attribution is not required.</p>
<p>Thank you to <a href="https://help.openstreetmap.org/users/10133/tzorn">@Tzorn</a> for the suggestion of Wikidata. Since they suggest that "Relation" type OSM IDs are stable enough for this use, that would be my recommendation too - use of OSM rather than Wikidata seems the most sensible option for our use, since OSM data is considerably more structured and useful. So I've amended the specification to specify that only "Relation" type IDs may be used.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Oct '20, 11:36</strong></p>
<img src="https://secure.gravatar.com/avatar/e5c550f1d414e90c3dea32f2630e258e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jamescridland&#39;s gravatar image" />
<p><span>jamescridland</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jamescridland has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77100" class="comments-container">
&#10;</div>
<div id="comment-tools-77100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77100-form-container" class="comment-form-container">
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

