+++
type = "question"
title = "How to uniquely identify a location from OSM?"
description = '''If I want to store an identifier to a particular location in OSM, what&#x27;s the best way to do this please? For example: If I want to store the link to Hyde Park, I can use this: Way: Hyde Park (372975520) https://www.openstreetmap.org/way/372975520 Whereas if I want to store a link to Wimbledon Common...'''
date = "2020-01-02T11:24:00Z"
lastmod = "2020-01-03T09:25:00Z"
weight = 72330
keywords = [ "uid" ]
aliases = [ "/questions/72330" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to uniquely identify a location from OSM?](/questions/72330/how-to-uniquely-identify-a-location-from-osm)

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
<span id="post-72330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72330-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If I want to store an identifier to a particular location in OSM, what's the best way to do this please?</p>
<p>For example:</p>
<p>If I want to store the link to Hyde Park, I can use this: Way: Hyde Park (<strong>372975520</strong>) <a href="https://www.openstreetmap.org/way/372975520">https://www.openstreetmap.org/way/372975520</a></p>
<p>Whereas if I want to store a link to Wimbledon Common, it's listed as this: Relation: Wimbledon Common (<strong>4285108</strong>) <a href="https://www.openstreetmap.org/relation/4285108">https://www.openstreetmap.org/relation/4285108</a></p>
<p>Note that one is a <em>Way</em> and the other is a <em>Relation</em>. Are these numbers still useful as UIDs? Or should I be storing the ID and the type (Way/Relation etc)?</p>
<p>Any guidance appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-uid" rel="tag" title="see questions tagged &#39;uid&#39;">uid</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jan '20, 11:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a46552eca5ac633d307cf48128c76950?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ab76555&#39;s gravatar image" />
<p><span>ab76555</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ab76555 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72330" class="comments-container">
<span id="72331"></span>
<div id="comment-72331" class="comment">
<div id="post-72331-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For completeness, if you just want to store a link to a location, you can store what's in the browser URL (for Hyde Park at zoom 15 that's <a href="https://www.openstreetmap.org/#map=15/51.5070/-0.1729">https://www.openstreetmap.org/#map=15/51.5070/-0.1729</a> ). That's not linking to a particular object in OSM but is linking to a location.</p>
</div>
<div id="comment-72331-info" class="comment-info">
<span class="comment-age">(02 Jan '20, 11:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="72332"></span>
<div id="comment-72332" class="comment">
<div id="post-72332-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the quick reply! What if I do want access to OSM object too? For example, if I've got a database that stores locations alongside ratings (which I'm accessing through my API), and I occasionally want to access the OSM object (for example, I might query my_location_id/osm_object_coordinates).</p>
</div>
<div id="comment-72332-info" class="comment-info">
<span class="comment-age">(02 Jan '20, 11:47)</span> <span class="comment-user userinfo">ab76555</span>
</div>
</div>
<span id="72338"></span>
<div id="comment-72338" class="comment">
<div id="post-72338-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>escada's answer covers the aspect of permanent linking. Regarding your question about the way and relation IDs, each object type has its own numbering. That is, there's a node #1, way #1, and relation #1, all representing different things. So, to identify an object using its ID, you'd also need to record its object type.</p>
</div>
<div id="comment-72338-info" class="comment-info">
<span class="comment-age">(02 Jan '20, 17:22)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="72347"></span>
<div id="comment-72347" class="comment">
<div id="post-72347-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Brilliant - thanks all for your help. That's great to know about the node/way numbering!</p>
</div>
<div id="comment-72347-info" class="comment-info">
<span class="comment-age">(03 Jan '20, 09:25)</span> <span class="comment-user userinfo">ab76555</span>
</div>
</div>
</div>
<div id="comment-tools-72330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72330-form-container" class="comment-form-container">
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

<span id="72333"></span>

<div id="answer-container-72333" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72333-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-72333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ab76555 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Since IDs can change, there is no definite solution. There are some workarounds (e.g. using Wikidata) listed on the wiki page <a href="https://wiki.openstreetmap.org/wiki/Permanent_ID">Permanent ID</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '20, 13:44</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jan '20, 13:45</strong> </span></p>
</div>
</div>
<div id="comments-container-72333" class="comments-container">
&#10;</div>
<div id="comment-tools-72333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72333-form-container" class="comment-form-container">
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

