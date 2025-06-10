+++
type = "question"
title = "using data from open streetmap"
description = '''I work for a municipal council in Belgium. We have our own GIS software which we use to create maps for our employees but also for citizens. We are currently using OSM as a substrate for our citizen geo-windows. Since we create certain layers ourselves with benches, for example, we wondered whether ...'''
date = "2021-03-12T09:32:00Z"
lastmod = "2021-03-12T12:51:00Z"
weight = 79235
keywords = [ "geodata" ]
aliases = [ "/questions/79235" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [using data from open streetmap](/questions/79235/using-data-from-open-streetmap)

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
<span id="post-79235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79235-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I work for a municipal council in Belgium. We have our own GIS software which we use to create maps for our employees but also for citizens. We are currently using OSM as a substrate for our citizen geo-windows. Since we create certain layers ourselves with benches, for example, we wondered whether the data of the points in OSM (e.g. benches, play areas, etc.) could also be obtained as a shp.-file or something like that, so that we no longer have to register the data ourselves.</p>
<p>Kind regards, Griet</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geodata" rel="tag" title="see questions tagged &#39;geodata&#39;">geodata</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '21, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/70eed023c40aaddf87517c0440862f68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Griet&#39;s gravatar image" />
<p><span>Griet</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Griet has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79235" class="comments-container">
&#10;</div>
<div id="comment-tools-79235" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79235-form-container" class="comment-form-container">
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

<span id="79238"></span>

<div id="answer-container-79238" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79238-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-79238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a fairly standard practice, and the tool you probably need is Overpass Turbo which can be used to query specific types of features on OSM and export them as geojson (or indeed other formats).</p>
<p>Overpass Turbo is a front-end to the Overpass API, but it does a few extra useful things such as assembling areas (which you'd need to do yourselves if using Overpass direct).</p>
<p>As an <a href="https://overpass-turbo.eu/s/14Y4">example here</a> are the benches in a Belgian municipality, Leuven. Simply change the name of the municipality in the query. Note some benches are mapped as lines (ways in OSM speak) but it is possible to alter the query just to return the centre of objects. The overpass query language is very powerful and there are quite reasonable resources with example queries on-line.</p>
<p>Lastly, there is a strong OSM community in Belgium, and I believe at least some work for or closely with municipalities, so further advice may be available from the OSM Belgium chapter.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '21, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Mar '21, 13:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-79238" class="comments-container">
&#10;</div>
<div id="comment-tools-79238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79238-form-container" class="comment-form-container">
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

