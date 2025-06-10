+++
type = "question"
title = "How to check efficiently if thousands of points are located inside a building polygon using overpass ?"
description = '''Hi, I want to check for thousands of points (lat, lon), if they are located inside a building polygon using the overpass API. I know how to do it for one point (eg: https://help.openstreetmap.org/questions/55529/how-to-detect-if-point-is-inside-a-building-polygon-with-overpass) but I don&#x27;t know how ...'''
date = "2020-04-26T12:59:00Z"
lastmod = "2020-05-02T23:00:00Z"
weight = 74372
keywords = [ "python", "overpass", "buildings", "is_in" ]
aliases = [ "/questions/74372" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to check efficiently if thousands of points are located inside a building polygon using overpass ?](/questions/74372/how-to-check-efficiently-if-thousands-of-points-are-located-inside-a-building-polygon-using-overpass)

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
<span id="post-74372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74372-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I want to check for thousands of points (lat, lon), if they are located inside a building polygon using the overpass API.</p>
<p>I know how to do it for one point (eg: <a href="https://help.openstreetmap.org/questions/55529/how-to-detect-if-point-is-inside-a-building-polygon-with-overpass)">https://help.openstreetmap.org/questions/55529/how-to-detect-if-point-is-inside-a-building-polygon-with-overpass)</a> but I don't know how to do it without sending requests during hours to the overpass API.</p>
<p>I'm currently using this request for one point:</p>
<pre><code>way(around:5, {lat}, {lon})[building];
if(count(ways) &lt; 1) {{
    way(around:10, {lat}, {lon})[building];
  if(count(ways) &lt; 1) {{
       way(around:15, {lat}, {lon})[building];
    if(count(ways) &lt; 1) {{
          way(around:20, {lat}, {lon})[building];
         if(count(ways) &lt; 1) {{
             way(around:25, {lat}, {lon})[building];
         }}}} }}}}
out geom;</code></pre>
<p>where I check gradually up until 25 meters for close buildings. I don't think there is a tool in overpass for checking if the point at lat, lon is located inside any of the close buildings (except creating temporary areas and using is_in?). So, I use the shapely python library for that. The full process for the thousand points takes hours.</p>
<p>How could I do it <strong>efficiently</strong>?</p>
<p>I could query all the close buildings of all the points in one request but I don't know how to keep a reference to the node from which a building is close. Thus, I will be forced to check if a node is inside any buildings that I got, no matter from which node the building is close. In this case, it will also not be efficient.</p>
<p>Does anyone have an idea for the query to use? Or on how to keep the reference?</p>
<p>Thanks!</p>
<p>Vucod</p>
<hr />
<p>The full code:</p>
<pre><code>from OSMPythonTools.overpass import Overpass
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
&#10;def checkIfOnBuilding(lat, lon):
&quot;&quot;&quot;
Check for building in a 25 radius
lat, lon  as string
&quot;&quot;&quot;
point = Point(lat, lon)
&#10;result = overpass.query(f&quot;&quot;&quot;
way(around:5, {lat}, {lon})[building];
if(count(ways) &lt; 1) {{
    way(around:10, {lat}, {lon})[building];
  if(count(ways) &lt; 1) {{
       way(around:15, {lat}, {lon})[building];
    if(count(ways) &lt; 1) {{
          way(around:20, {lat}, {lon})[building];
         if(count(ways) &lt; 1) {{
             way(around:25, {lat}, {lon})[building];
         }}}} }}}}
out geom;
&quot;&quot;&quot;, timeout=500)
&#10;dict_ = result.toJSON()[&#39;elements&#39;]
df = pd.DataFrame(dict_)
&#10;if len(df) &gt; 0:
    for i, row in df.iterrows():
        nodes = [(node[&quot;lat&quot;], node[&quot;lon&quot;]) for node in row.geometry]
        polygon = Polygon(nodes)
        res = polygon.contains(point)
        if res:
            break
else:
    res = False
&#10;return res</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-is_in" rel="tag" title="see questions tagged &#39;is_in&#39;">is_in</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Apr '20, 12:59</strong></p>
<img src="https://secure.gravatar.com/avatar/92cb35f7cbcc794feacd888ba5f60389?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vucod&#39;s gravatar image" />
<p><span>Vucod</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vucod has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '20, 13:01</strong> </span></p>
</div>
</div>
<div id="comments-container-74372" class="comments-container">
<span id="74561"></span>
<div id="comment-74561" class="comment">
<div id="post-74561-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There's not a contains operation in the Overpass-API query language.</p>
<p>You can inject text into the result using the <code>make</code> statement: <a href="https://dev.overpass-api.de/blog/textual_data.html">https://dev.overpass-api.de/blog/textual_data.html</a></p>
</div>
<div id="comment-74561-info" class="comment-info">
<span class="comment-age">(02 May '20, 23:00)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-74372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74372-form-container" class="comment-form-container">
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

<span id="74552"></span>

<div id="answer-container-74552" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74552-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I finally found the way to do it in one request which is a lot faster. I just use my request for every point and I separate each sub request by a <code>out count;</code>. Therefore, as the order of the sets is kept and I have a delimiter between the sets, I can find back for each point the buildings that are close. But there is still maybe a cleaner way to do it using only overpass API?</p>
<p>The full code using python3 :</p>
<pre><code>from OSMPythonTools.overpass import Overpass
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
&#10;def onBuilding(lats: str, lons: str) -&gt; List[bool]:
&quot;&quot;&quot;
Check if coordinates are on a building.
Works only for buildings that have a node
closer than 25 meters from the coordinate.
&quot;&quot;&quot;
&#10;query = &quot;&quot;&quot;    &quot;&quot;&quot;
for lat, lon in zip(lats, lons):
    query += f&quot;&quot;&quot;
    way(around:5, {lat}, {lon})[building];
    if(count(ways) &lt; 1) {{
        way(around:10, {lat}, {lon})[building];
      if(count(ways) &lt; 1) {{
           way(around:15, {lat}, {lon})[building];
        if(count(ways) &lt; 1) {{
              way(around:20, {lat}, {lon})[building];
             if(count(ways) &lt; 1) {{
                 way(around:25, {lat}, {lon})[building];
             }}}} }}}}
    out count;
    out geom;
    &quot;&quot;&quot;
result = overpass.query(query, timeout=15000)
elements = result.toJSON()[&quot;elements&quot;]
&#10;list_ = []
for lat, lon in zip(lats, lons):
    point = Point(lat, lon)
    onBuilding = False
    sizeSet = int(elements[0][&quot;tags&quot;][&#39;total&#39;])
    elements.pop(0)
    for item in range(sizeSet):
        element = elements[item]
        nodes = [(node[&quot;lat&quot;], node[&quot;lon&quot;])
                 for node in element[&quot;geometry&quot;]]
        polygon = Polygon(nodes)
        onBuilding = polygon.contains(point)
        if onBuilding:
            print(&quot;--&gt; the coordinate is inside a building&quot;)
            break
    del elements[:sizeSet]
    list_.append(onBuilding)
return list_</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '20, 19:51</strong></p>
<img src="https://secure.gravatar.com/avatar/92cb35f7cbcc794feacd888ba5f60389?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vucod&#39;s gravatar image" />
<p><span>Vucod</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vucod has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74552" class="comments-container">
&#10;</div>
<div id="comment-tools-74552" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74552-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

