+++
type = "question"
title = "Retrieve min and max lon/lat using csv output and bb output"
description = '''Hi, I am trying to output a relation as a CSV along with the bounds of the bbox. My template query comes from this example which retrieves the center lon and lat. [out:csv(::id,name,::lat,::lon; true; &quot;,&quot;)]; (rel[&quot;name&quot;=&quot;Southampton&quot;][&quot;place&quot;=&quot;city&quot;];); out center; But moving to using bb as the out:...'''
date = "2024-01-08T21:07:00Z"
lastmod = "2024-01-08T21:07:00Z"
weight = 88121
keywords = [ "minlat", "csv", "bb" ]
aliases = [ "/questions/88121" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Retrieve min and max lon/lat using csv output and bb output](/questions/88121/retrieve-min-and-max-lonlat-using-csv-output-and-bb-output)

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
<span id="post-88121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88121-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am trying to output a relation as a CSV along with the bounds of the bbox. My template query comes from this example which retrieves the center lon and lat.</p>
<p>[out:csv(::id,name,::lat,::lon; true; ",")];</p>
<p>(rel["name"="Southampton"]["place"="city"];);</p>
<p>out center;</p>
<p>But moving to using bb as the out:</p>
<p>[out:csv(::id,name,::minlat,::minlon,::maxlat,::maxlon; true; ",")];</p>
<p>(rel["name"="Southampton"]["place"="city"];);</p>
<p>out bb;</p>
<p>I get no data returned for the min and max long and lat fields.</p>
<p>Am I doing something wrong or is this simply not supported? Best, Chris</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-minlat" rel="tag" title="see questions tagged &#39;minlat&#39;">minlat</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-bb" rel="tag" title="see questions tagged &#39;bb&#39;">bb</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '24, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a7c7c42b3ace9de1b7d8fd5592ece3ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chessel&#39;s gravatar image" />
<p><span>Chessel</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chessel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88121" class="comments-container">
&#10;</div>
<div id="comment-tools-88121" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88121-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

