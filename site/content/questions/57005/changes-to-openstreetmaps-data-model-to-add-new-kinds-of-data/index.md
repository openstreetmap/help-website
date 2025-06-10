+++
type = "question"
title = "Changes to OpenStreetMap&#x27;s data model to add new kinds of data"
description = '''How do fundamental changes to OpenStreetMap&#x27;s underlying data model work? How are these proposed, discussed, and decided on? What sort of things are important to consider throughout this process? I am a researcher at a university. My group has a potentially very large grant coming in, with an intere...'''
date = "2017-07-11T00:24:00Z"
lastmod = "2017-07-11T08:15:00Z"
weight = 57005
keywords = [ "openstreetmap", "model", "schema", "data", "database" ]
aliases = [ "/questions/57005" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Changes to OpenStreetMap's data model to add new kinds of data](/questions/57005/changes-to-openstreetmaps-data-model-to-add-new-kinds-of-data)

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
<span id="post-57005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57005-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do fundamental changes to OpenStreetMap's underlying data model work? How are these proposed, discussed, and decided on? What sort of things are important to consider throughout this process?</p>
<p>I am a researcher at a university. My group has a potentially very large grant coming in, with an interest in making housing data publicly available in a consistent way across the US (and ideally, the world). For example, how would we go about discussing with the OpenStreetMap community the possibility of -- and pros and cons of -- creating fields in the OSM database to store data about residential parcels (such as appraised value, last sale date, sale price etc) and buildings (such as number of bedrooms or bathrooms, number of units, rent, etc). We can assume extremely generous funding for this project and ongoing updates to the data on an ongoing basis.</p>
<p>What is the process for this kind of proposal and conversation? What are the key concerns or issues involved? Is this sort of housing data appropriate for the OSM project and mission?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-model" rel="tag" title="see questions tagged &#39;model&#39;">model</span> <span class="post-tag tag-link-schema" rel="tag" title="see questions tagged &#39;schema&#39;">schema</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '17, 00:24</strong></p>
<img src="https://secure.gravatar.com/avatar/8eb28ad933ae655db57b6c6b8563eb67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gboeing&#39;s gravatar image" />
<p><span>gboeing</span><br />
<span class="score" title="136 reputation points">136</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gboeing has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57005" class="comments-container">
&#10;</div>
<div id="comment-tools-57005" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57005-form-container" class="comment-form-container">
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

<span id="57007"></span>

<div id="answer-container-57007" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57007-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-57007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gboeing has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, it looks like you are not asking for a change of the data model, just for some additional tags. The change of the data model would be very difficult, adding some tags is easier. Generally there is no one process to make decisions about new tags. Most tags are simply added, hopefully after some (informal) discussions with knowledgeable mappers who can give advice.</p>
<p>Then there is the question of what belongs in OSM and what doesn't. There are no hard and fast rules here, but some guidelines. An obvious one is "general usability": Is this something that is generally useful (almost everybody drives down roads) or something very specialized only for a very limited audience (I would expect your project to fall somewhere in the middle, but leaning towards specialized). One very important one is "verifyability": Can somebody who stands in the world somewhere verify that the data mapped there is correct. For a road this is obvious. Your project falls through here. You data is coming from somewhere else and no check is possible for the average mapper. This has a flip side: Your data is, I assume, coming from some authoritative source and it makes sense to have the checks and the uniformity of data guaranteed by that source. You don't want any random Joe to change the house prices. But in OSM that is possible. So why do you want this information in OSM when you already have a source that is (probably) updated systematically? This is the most important issue here. What do you expect some bringing this data into OSM where you have to keep it updated in a cumbersome process when you can easily keep the data outside and combining it with the OSM data as needed.</p>
<p>There is always the problem of conflation, of matching your data to OSM data. This process is always messy, but it isn't worse when combining the data every time you use it compared to one on import and then everytime the data source is updated. Find a way to combine the two data sources automatically upon use and everybody will be happier. In developed countries this can usually be done relatively easily using addresses. If OSM is missing address data, help completing that and you have something to match against.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '17, 07:48</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-57007" class="comments-container">
<span id="57008"></span>
<div id="comment-57008" class="comment">
<div id="post-57008-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Just as a further point: adding a number of the details that were mentioned is going to be a non-starter in many many countries for legal reasons (privacy etc), Naturally that applies equally to all possible platfomrs.</p>
</div>
<div id="comment-57008-info" class="comment-info">
<span class="comment-age">(11 Jul '17, 08:15)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-57007" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57007-form-container" class="comment-form-container">
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

