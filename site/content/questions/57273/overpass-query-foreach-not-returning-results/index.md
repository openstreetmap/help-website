+++
type = "question"
title = "overpass query foreach not returning results."
description = '''I have installed overpass api using the docker and german image from geofabrik. I can run queries using the command line and api. However, using foreach and count i get no results but overpass-turbo.eu returns results.  Can anyone help? Here is the my query code. [out:csv(::&quot;type&quot;,::&quot;id&quot;, name, admi...'''
date = "2017-07-25T21:36:00Z"
lastmod = "2017-07-25T21:36:00Z"
weight = 57273
keywords = [ "query", "overpass-api" ]
aliases = [ "/questions/57273" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [overpass query foreach not returning results.](/questions/57273/overpass-query-foreach-not-returning-results)

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
<span id="post-57273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57273-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have installed overpass api using the docker and german image from geofabrik. I can run queries using the command line and api. However, using foreach and count i get no results but overpass-turbo.eu returns results. Can anyone help? Here is the my query code.</p>
<p>[out:csv(::"type",::"id", name, admin_level,::"count")]; area[name="Saarland"][boundary]; rel(area)["boundary"="postal_code"]; map_to_area; foreach-&gt;.d( (.d;);out; (node(area.d)[amenity=pharmacy]; way(area.d)[amenity=pharmacy]; relation(area.d)[amenity=pharmacy];); out count; );</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jul '17, 21:36</strong></p>
<img src="https://secure.gravatar.com/avatar/ac18356019d6ebeea5c9c8e33414ed74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrparadox&#39;s gravatar image" />
<p><span>mrparadox</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrparadox has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57273" class="comments-container">
&#10;</div>
<div id="comment-tools-57273" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57273-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

