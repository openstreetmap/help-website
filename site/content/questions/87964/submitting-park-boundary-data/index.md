+++
type = "question"
title = "Submitting Park Boundary Data"
description = '''I work for a privately owned park which is open to the public. The park is already listed on OSM but the current boundaries are wildly incorrect. I really have no idea how to edit these boundaries. I have access to GIS files of our boundaries in various formats (KMZ, JSON, etc). I am just not sure h...'''
date = "2023-10-30T17:18:00Z"
lastmod = "2023-10-31T07:00:00Z"
weight = 87964
keywords = [ "import", "boundary", "beginner", "parks" ]
aliases = [ "/questions/87964" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Submitting Park Boundary Data](/questions/87964/submitting-park-boundary-data)

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
<span id="post-87964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87964-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I work for a privately owned park which is open to the public. The park is already listed on OSM but the current boundaries are wildly incorrect. I really have no idea how to edit these boundaries. I have access to GIS files of our boundaries in various formats (KMZ, JSON, etc). I am just not sure how to take these files and use them to update or replace the current park boundaries. Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span> <span class="post-tag tag-link-parks" rel="tag" title="see questions tagged &#39;parks&#39;">parks</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '23, 17:18</strong></p>
<img src="https://secure.gravatar.com/avatar/b8f1d1d044e0343250c339c04813f9e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mpintoWHFF&#39;s gravatar image" />
<p><span>mpintoWHFF</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mpintoWHFF has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87964" class="comments-container">
&#10;</div>
<div id="comment-tools-87964" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87964-form-container" class="comment-form-container">
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

<span id="87965"></span>

<div id="answer-container-87965" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87965-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-87965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Editing park boundaries can be a daunting task for a newbie because often what is the outer boundary of the park, is also another boundary - maybe that of a neighbouring residential or agricultural area, a different park, or sometimes also an administrative boundary. In these cases we prefer to have the actual geometry recorded only once (so that, if you change the park boundary, you automatically change the neighbouring boundary, rather than creating an overlap or a no-man's-land in between the two areas).</p>
<p>This is often done using a construct called a "relation" which is made up of several "ways", and different relations can have shared use of the same "way".</p>
<p>It might be easiest if you just made the KMZ or JSON file available somewhere for download and then pinged the community on community.openstreetmap.org asking if someone nearby would mind taking this on. While we're always happy to welcome new mappers, if the first thing you try is edit a park boundary, you're likely to break things ;)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '23, 18:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-87965" class="comments-container">
<span id="87966"></span>
<div id="comment-87966" class="comment">
<div id="post-87966-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This all makes sense - I certainly don't want to break anything.</p>
<p>Is posting in the community similar to leaving a note directly on OSM? I posted a note about a month ago on the current park stating the boundaries are wrong and to contact me for the file. I don't want to overdo it by also creating a post in the community. Thanks!</p>
</div>
<div id="comment-87966-info" class="comment-info">
<span class="comment-age">(30 Oct '23, 19:51)</span> <span class="comment-user userinfo">mpintoWHFF</span>
</div>
</div>
<span id="87967"></span>
<div id="comment-87967" class="comment">
<div id="post-87967-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'll help if you wish, send a message by clicking my name below, and the email address in there.</p>
</div>
<div id="comment-87967-info" class="comment-info">
<span class="comment-age">(31 Oct '23, 07:00)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
</div>
<div id="comment-tools-87965" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87965-form-container" class="comment-form-container">
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

