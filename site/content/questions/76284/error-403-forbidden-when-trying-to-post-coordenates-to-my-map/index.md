+++
type = "question"
title = "Error 403 - Forbidden when trying to post coordenates to my map"
description = '''Hello everyone, I&#x27;m new to map making, so I&#x27;m learning how to do some stuffs. I&#x27;m trying to create a custom map using uMap. I would like to load some latitude and longitude coordenates using a python script because they are too many. I have tried to use a post request and using this url &quot;https://uma...'''
date = "2020-08-25T03:33:00Z"
lastmod = "2020-08-25T17:05:00Z"
weight = 76284
keywords = [ "python", "umap", "osm", "geojson" ]
aliases = [ "/questions/76284" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error 403 - Forbidden when trying to post coordenates to my map](/questions/76284/error-403-forbidden-when-trying-to-post-coordenates-to-my-map)

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
<span id="post-76284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76284-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>I'm new to map making, so I'm learning how to do some stuffs. I'm trying to create a custom map using uMap. I would like to load some latitude and longitude coordenates using a python script because they are too many. I have tried to use a post request and using this url</p>
<p>"<a href="https://umap.openstreetmap.fr/es/map/%3Cmap_id%3E/datalayer/update/%3Clayer_id%3E/"><code>https://umap.openstreetmap.fr/es/map/&lt;map_id&gt;/datalayer/update/&lt;layer_id&gt;/</code></a>"</p>
<p>And also provided sessionid and csrftoken cookies (I copied the values using the inspect feature).</p>
<p>To test the post request, I'm trying to add only 1 single point to a map using this:</p>
<pre><code>from geojson.geometry import GeoJSON
&#10;d={
  &quot;type&quot;: &quot;Feature&quot;,
  &quot;geometry&quot;: {
    &quot;type&quot;: &quot;Point&quot;,
    &quot;coordinates&quot;: [125.6, 10.1]
  },
  &quot;properties&quot;: {
    &quot;name&quot;: &quot;Dinagat Islands&quot;
  }
}</code></pre>
<p>Using all this, I'm just getting "Error 403-Forbidden". Why is this and how can I solve it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '20, 03:33</strong></p>
<img src="https://secure.gravatar.com/avatar/ca97a96e358ce694cc8cdda51e81fe99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppsev&#39;s gravatar image" />
<p><span>ppsev</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppsev has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76284" class="comments-container">
&#10;</div>
<div id="comment-tools-76284" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76284-form-container" class="comment-form-container">
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

<span id="76293"></span>

<div id="answer-container-76293" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76293-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If your aim is just to avoid manual data entry you may be better off either:</p>
<ol>
<li>Generating the data locally and using the "<a href="https://wiki.openstreetmap.org/wiki/UMap/Guide/Import_data_files">import data</a>" option to upload the file. This is the fist button on the second panel of buttons on the right.</li>
<li>Uploading your file to somewhere you can update as necessary and editing the layer properties to point at that location using the "Remote Data" options.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '20, 14:00</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-76293" class="comments-container">
<span id="76294"></span>
<div id="comment-76294" class="comment">
<div id="post-76294-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello <a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a>. Yes, I want to avoid manual data entry but mostly avoid the usual import option. I'm aware of the "import data" available in OSM, but the thing is that I have actually lots of points to upload (more than 300k). Last time I tried to upload around 50k points in csv format, the website froze :(.</p>
</div>
<div id="comment-76294-info" class="comment-info">
<span class="comment-age">(25 Aug '20, 14:07)</span> <span class="comment-user userinfo">ppsev</span>
</div>
</div>
<span id="76298"></span>
<div id="comment-76298" class="comment">
<div id="post-76298-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Where is your data from originally? Is it OSM based?</p>
</div>
<div id="comment-76298-info" class="comment-info">
<span class="comment-age">(25 Aug '20, 16:40)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="76300"></span>
<div id="comment-76300" class="comment">
<div id="post-76300-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmmm kinda. Its from a map based on osm and probably umap, but I'm not sure about the second one. I extracted the latitude and longitude based on that map because its way more accurate than consulting the string direction directly in osm (or even google maps).</p>
</div>
<div id="comment-76300-info" class="comment-info">
<span class="comment-age">(25 Aug '20, 17:05)</span> <span class="comment-user userinfo">ppsev</span>
</div>
</div>
</div>
<div id="comment-tools-76293" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76293-form-container" class="comment-form-container">
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

