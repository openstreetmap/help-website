+++
type = "question"
title = "how can i filter the duplicated shapes (small shapes inside a big shape)?"
description = '''Hello every one,  I am new to opensreetmap but i found it is a great project. I am trying to statisc the green space in a city (i got the geojson,then i treat it by geopandas of python)  So i use overpass to get all the elements of natural. But the pb is that the geometry sharpes is covered and mixt...'''
date = "2018-03-23T12:08:00Z"
lastmod = "2018-03-26T13:00:00Z"
weight = 62792
keywords = [ "greenfield" ]
aliases = [ "/questions/62792" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how can i filter the duplicated shapes (small shapes inside a big shape)?](/questions/62792/how-can-i-filter-the-duplicated-shapes-small-shapes-inside-a-big-shape)

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
<span id="post-62792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62792-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello every one, I am new to opensreetmap but i found it is a great project.</p>
<p>I am trying to statisc the green space in a city (i got the geojson,then i treat it by geopandas of python) So i use overpass to get all the elements of natural.</p>
<p>But the pb is that the geometry sharpes is covered and mixted. for example:</p>
<pre><code>          - parks in parks, 
          - garden in parks</code></pre>
<p>` - etc</p>
<p>I just want all the indepent shapes (filter the samll shapes inside if exsits), i readed the wiki,but i did not find a specific solution, do you have any advice?</p>
<p>Thanks in advance</p>
<p><img src="https://help.openstreetmap.org/upfiles/Capture_4Gz6XFj.JPG" alt="alt text" /></p>
<p>QL code [out:json][timeout:25]; // gather results ( // query part</p>
<pre><code>  way[&quot;leisure&quot;=&quot;garden&quot;]({{bbox}});
  relation[&quot;leisure&quot;=&quot;garden&quot;]({{bbox}});
&#10;  way[&quot;leisure&quot;=&quot;golf_course&quot;]({{bbox}});
  relation[&quot;leisure&quot;=&quot;golf_course&quot;]({{bbox}});
&#10;  way[&quot;leisure&quot;=&quot;park&quot;]({{bbox}});
  relation[&quot;leisure&quot;=&quot;park&quot;]({{bbox}});
&#10;  way[&quot;leisure&quot;=&quot;dog_park&quot;]({{bbox}});
  relation[&quot;leisure&quot;=&quot;dog_park&quot;]({{bbox}});
&#10;  way[&quot;leisure&quot;=&quot;pitch&quot;]({{bbox}});
  relation[&quot;leisure&quot;=&quot;pitch&quot;]({{bbox}});
&#10; way[&quot;landuse&quot;=&quot;village_green&quot;]({{bbox}});
 way[&quot;landuse&quot;=&quot;meadow&quot;]({{bbox}});
 way[&quot;landuse&quot;=&quot;forest&quot;]({{bbox}});
 relation[&quot;landuse&quot;=&quot;forest&quot;]({{bbox}});
&#10;);
// print results
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-greenfield" rel="tag" title="see questions tagged &#39;greenfield&#39;">greenfield</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '18, 12:08</strong></p>
<img src="https://secure.gravatar.com/avatar/86dbc9d54763a2b084bea768e71f0df6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xiaoyuan1998&#39;s gravatar image" />
<p><span>xiaoyuan1998</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xiaoyuan1998 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '18, 12:12</strong> </span></p>
</div>
</div>
<div id="comments-container-62792" class="comments-container">
&#10;</div>
<div id="comment-tools-62792" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62792-form-container" class="comment-form-container">
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

<span id="62795"></span>

<div id="answer-container-62795" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62795-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62795-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62795-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should be able to do a single union across all the data, providing you ignore the relevant landuse tags. This looks to describe the relevant operations in geopandas: <a href="http://geopandas.org/set_operations.html">http://geopandas.org/set_operations.html</a>. You can do equivalent operations in QGIS and PostGis.</p>
<p>Note that if you are trying to do something more than just determine the area of green space: for instance creating a coherent dataset of green space the problem becomes considerably more complicated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '18, 13:00</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-62795" class="comments-container">
<span id="62830"></span>
<div id="comment-62830" class="comment">
<div id="post-62830-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks your answer, i i have tried geopanda, the one pb is that geopadans can not read all the geo shape, the antoher pb is that when there are more than 40 small shapes for a city.. it is very long to do the union of the set of shapes.</p>
</div>
<div id="comment-62830-info" class="comment-info">
<span class="comment-age">(26 Mar '18, 13:00)</span> <span class="comment-user userinfo">xiaoyuan1998</span>
</div>
</div>
</div>
<div id="comment-tools-62795" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62795-form-container" class="comment-form-container">
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

