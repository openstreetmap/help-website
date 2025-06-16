+++
type = "question"
title = "How to get the lat long polygon for a given airport"
description = '''What I need to do is to get the bounding box polygon for all airports worldwide. The only way I&#x27;m aware of do this, is by using esy.osm.pbf. I&#x27;ve written the following code: osm = esy.osm.pbf.File(file_path) lat_lons = OrderedDict() index = 0 print(&quot;There are &quot; + str(len(airport.refs)) + &quot; nodes to ...'''
date = "2021-05-20T17:52:00Z"
lastmod = "2021-05-25T09:11:00Z"
weight = 80243
keywords = [ "python", "polygon" ]
aliases = [ "/questions/80243" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get the lat long polygon for a given airport](/questions/80243/how-to-get-the-lat-long-polygon-for-a-given-airport)

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
<span id="post-80243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80243-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What I need to do is to get the bounding box polygon for all airports worldwide. The only way I'm aware of do this, is by using esy.osm.pbf. I've written the following code:</p>
<pre><code>osm = esy.osm.pbf.File(file_path)
lat_lons = OrderedDict()
index = 0
print(&quot;There are &quot; + str(len(airport.refs)) + &quot; nodes to go through.&quot;)
for ref in airport.refs:
    print(str(index))
    index = index + 1
    nodes = [entry for entry in osm if entry.id == ref]
    lonlat = nodes[0].lonlat
    print(lonlat)
    print(type(lonlat[1]))
    print(type(lonlat[0]))
    lat_lons[ref] = ([lonlat[1], lonlat[0]])
return lat_lons</code></pre>
<p>But it takes much too long to do this, that's just for a single airport, and I need to do it for all airports worldwide. Is there a better way of fetching the latitudes and longitudes for the polygons for all airports worldwide?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '21, 17:52</strong></p>
<img src="https://secure.gravatar.com/avatar/dccb738f23c5eabe357863e07f5111ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="michaelnares&#39;s gravatar image" />
<p><span>michaelnares</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="michaelnares has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80243" class="comments-container">
&#10;</div>
<div id="comment-tools-80243" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80243-form-container" class="comment-form-container">
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

<span id="80284"></span>

<div id="answer-container-80284" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80284-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim can fetch bboxes. <a href="/questions/25634/is-there-a-way-to-automatically-obtain-a-bbox-for-something-from-osm-or-other-api">Old thread</a>. You can test some limited areas and then build a batch or requests.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '21, 09:11</strong></p>
<img src="https://secure.gravatar.com/avatar/d33efa30f05d8f3604e7210c48b24a8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cascafico&#39;s gravatar image" />
<p><span>Cascafico</span><br />
<span class="score" title="283 reputation points">283</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cascafico has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80284" class="comments-container">
&#10;</div>
<div id="comment-tools-80284" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80284-form-container" class="comment-form-container">
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

