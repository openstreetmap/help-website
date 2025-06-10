+++
type = "question"
title = "Extracting speed limits on a given path"
description = '''Hello everyone! For my Master Thesis work, I need to import in OSM a certain .gpx file with a given path. So far so good. Then I would like extracting for each point of that path the current speed limit for further data analysis. Is there a way to extract such kind of info from OSM? Thank you in adv...'''
date = "2023-05-12T09:05:00Z"
lastmod = "2023-05-12T14:30:00Z"
weight = 87250
keywords = [ "speedlimit", "maxspeed", "data", "data_processing" ]
aliases = [ "/questions/87250" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting speed limits on a given path](/questions/87250/extracting-speed-limits-on-a-given-path)

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
<span id="post-87250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87250-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone! For my Master Thesis work, I need to import in OSM a certain .gpx file with a given path. So far so good. Then I would like extracting for each point of that path the current speed limit for further data analysis. Is there a way to extract such kind of info from OSM? Thank you in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-speedlimit" rel="tag" title="see questions tagged &#39;speedlimit&#39;">speedlimit</span> <span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-data_processing" rel="tag" title="see questions tagged &#39;data_processing&#39;">data_processing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 May '23, 09:05</strong></p>
<img src="https://secure.gravatar.com/avatar/b0ccf92c1a38089c1d9a59e8f9914ec5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lorenzo_m&#39;s gravatar image" />
<p><span>Lorenzo_m</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lorenzo_m has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87250" class="comments-container">
&#10;</div>
<div id="comment-tools-87250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87250-form-container" class="comment-form-container">
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

<span id="87251"></span>

<div id="answer-container-87251" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87251-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM is just the geographic database so on a conceptual level you will need to load (parts of) it and your gpx file into something else rather than the other way around.</p>
<p>OpenStreetMap has well established tags for <a href="https://wiki.openstreetmap.org/wiki/Speed_limits">speed limits</a>, as with other OSM data coverage varies by region. The wiki also has a <a href="https://wiki.openstreetmap.org/wiki/Default_speed_limits">list of "default"</a> speed limits by country that may help fill in gaps.</p>
<p>I think the general keyword for snapping recorded paths to known roads is "map matching", there are a few routing engines for OSM data that do this, <a href="https://wiki.openstreetmap.org/wiki/Open_Source_Routing_Machine">OSRM</a> is one but I not aware of an index of them anywhere. Whether you use an existing engine for this or write your own will probably depend on how it integrates with the rest of your project. Whether you will need way IDs to get back to the input data or can make do with the router's internal representation of the data (assumptions and all) will depend on what you choose to use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '23, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-87251" class="comments-container">
&#10;</div>
<div id="comment-tools-87251" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87251-form-container" class="comment-form-container">
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

