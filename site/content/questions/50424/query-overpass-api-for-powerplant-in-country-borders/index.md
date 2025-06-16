+++
type = "question"
title = "query overpass api for power=plant in country borders"
description = '''This excellent post had an example of an overpass query: https://help.openstreetmap.org/questions/19063/get-city-nodes-within-a-country-using-overpass-api Using Python, I can query OSM for all cities in Belgium:  import overpass api = overpass.API(timeout=900)  cities = api.Get(&#x27;area[name=&quot;België - ...'''
date = "2016-06-23T20:16:00Z"
lastmod = "2016-07-05T08:27:00Z"
weight = 50424
keywords = [ "overpassapi", "python", "power_station" ]
aliases = [ "/questions/50424" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [query overpass api for power=plant in country borders](/questions/50424/query-overpass-api-for-powerplant-in-country-borders)

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
<span id="post-50424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50424-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This excellent post had an example of an overpass query: <a href="/questions/19063/get-city-nodes-within-a-country-using-overpass-api">https://help.openstreetmap.org/questions/19063/get-city-nodes-within-a-country-using-overpass-api</a></p>
<p>Using Python, I can query OSM for all cities in Belgium:</p>
<p><code>import overpass api = overpass.API(timeout=900) cities = api.Get('area[name="België - Belgique - Belgien"];(node[place="city"](area););out;') print(cities)</code></p>
<p>but I can't do similar for powerplants. Does anyone know why? Code below returns empty dictionary.</p>
<p><code>api = overpass.API(timeout=900) power = api.Get('area[name="België - Belgique - Belgien"];(node[power="plant"](area););out;') print(power)</code></p>
<p>Thanks again</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-power_station" rel="tag" title="see questions tagged &#39;power_station&#39;">power_station</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jun '16, 20:16</strong></p>
<img src="https://secure.gravatar.com/avatar/51a036c2c2ccd7bf5bcd64e41776e391?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jdills26&#39;s gravatar image" />
<p><span>jdills26</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jdills26 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50424" class="comments-container">
<span id="50431"></span>
<div id="comment-50431" class="comment">
<div id="post-50431-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Duplicate post: <a href="https://github.com/mvexel/overpass-api-python-wrapper/issues/59">https://github.com/mvexel/overpass-api-python-wrapper/issues/59</a></p>
</div>
<div id="comment-50431-info" class="comment-info">
<span class="comment-age">(24 Jun '16, 07:10)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="50627"></span>
<div id="comment-50627" class="comment">
<div id="post-50627-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Exactly the same error message was posted <a href="https://stackoverflow.com/questions/37843782/how-to-get-all-power-plants-from-open-street-map-using-overpass-api-with-python">here</a>. I'm proposing to close this one and continue on stack overflow instead.</p>
</div>
<div id="comment-50627-info" class="comment-info">
<span class="comment-age">(05 Jul '16, 08:27)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-50424" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50424-form-container" class="comment-form-container">
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

<span id="50428"></span>

<div id="answer-container-50428" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50428-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems there simply aren't any power plants modeled as nodes there. There are ways:</p>
<p><a href="http://overpass-turbo.eu/s/gXj">http://overpass-turbo.eu/s/gXj</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jun '16, 22:30</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-50428" class="comments-container">
<span id="50432"></span>
<div id="comment-50432" class="comment">
<div id="post-50432-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Out center may not work with overpass Python wrapper, there are some issues on that topic on github.</p>
</div>
<div id="comment-50432-info" class="comment-info">
<span class="comment-age">(24 Jun '16, 07:12)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="50576"></span>
<div id="comment-50576" class="comment">
<div id="post-50576-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks alot for this! With this code I am still getting an error (below). I'm able to get power plants and power generators when I specify a bounding box, but I'd like a more efficient way to get country data from the API.</p>
<p><code>x=api.Get('area[name="België - Belgique - Belgien"];(way["power"="plant"](area);); out skel;') x</code></p>
<hr />
<p>KeyError Traceback (most recent call last) &lt;ipython-input-96-529c6ed17161&gt; in &lt;module&gt;() 1</p>
<p>C:\Users\julia.dills\AppData\Local\Continuum\Anaconda3\lib\site-packages\overpass\api.py in _asGeoJSON(self, elements) 129 elif elem_type == "way": 130 points = [] --&gt; 131 for coords in elem["geometry"]: 132 points.append((coords["lon"], coords["lat"])) 133 geometry = geojson.LineString(points)</p>
<p>KeyError: 'geometry'</p>
</div>
<div id="comment-50576-info" class="comment-info">
<span class="comment-age">(02 Jul '16, 20:53)</span> <span class="comment-user userinfo">jdills26</span>
</div>
</div>
<span id="50590"></span>
<div id="comment-50590" class="comment">
<div id="post-50590-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've noticed you've changed the output to <code>out skel;</code>. Unfortunately, that's also not going to cut it, as the result doesn't include any coordinates or geometry information. <code>out center;</code> is not supported by the overpass python wrapper, i.e. <a href="https://help.openstreetmap.org/users/10973/maxerickson"></a><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a>'s suggestion is good in general, but does not apply in this particular case.</p>
<p>That leaves us with the question, why you want to stick with overpass-api-python-wrapper. There's plenty of more mature alternatives out there, it all depends on what you're trying to achieve.</p>
</div>
<div id="comment-50590-info" class="comment-info">
<span class="comment-age">(03 Jul '16, 19:31)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-50428" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50428-form-container" class="comment-form-container">
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

