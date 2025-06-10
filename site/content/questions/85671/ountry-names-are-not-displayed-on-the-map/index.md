+++
type = "question"
title = "Сountry names are not displayed on the map"
description = '''I`m trying to create map which has several layers. One of them consist of country borders (admin_level = 2,3), country name and region names. I use data of coordinates of Armenia and China from https://download.geofabrik.de/asia.html. I succesfully consolidated these countries with Osmosis 0.40.1.: ...'''
date = "2022-09-21T08:56:00Z"
lastmod = "2022-09-21T08:56:00Z"
weight = 85671
keywords = [ "countryname", "osmosis" ]
aliases = [ "/questions/85671" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Сountry names are not displayed on the map](/questions/85671/ountry-names-are-not-displayed-on-the-map)

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
<span id="post-85671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85671-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I`m trying to create map which has several layers. One of them consist of country borders (admin_level = 2,3), country name and region names. I use data of coordinates of Armenia and China from <a href="https://download.geofabrik.de/asia.html.">https://download.geofabrik.de/asia.html.</a> I succesfully consolidated these countries with Osmosis 0.40.1.:</p>
<pre><code>osmosis --read-pbf armenia-latest.osm.pbf --read-pbf china-latest.osm.pbf --merge --write-pbf ArChina.osm.pbf</code></pre>
<p>And extracted border with admin_level = 2,3:</p>
<pre><code>osmosis --read-pbf ArChina.osm.pbf --tf accept-relation boundary=administrative admin_level=2,3 --tf reject-ways admin_level=5,6,7,8,9 --used-way idTrackerType=Dynamic --tf reject-nodes admin_level=4,5,6,7,8,9 --tf reject-nodes place=village,town,suburb,city --used-node idTrackerType=Dynamic --write-xml ArChinaBord1.osm</code></pre>
<p>Then I converted it to .osm.pbf with Osmosis.</p>
<p>I understand that I didn't remove all the nodes such as bus stops, natural objects, etc. That`s not the problem.</p>
<p>The problem is - when I`ve launched this map on Ubuntu server - I saw the borders of 2 countries, region names of both of them and only 1 country name (Armenia). I was trying to zoom in and zoom out, but it didn't help. Сhina name is not showing at all.</p>
<p>I checked ArChinaBord1.osm (consolidated file with Armenia and China borders, names). The xml structure of Armenia and China names (node with place=country) is the same, but only one name is shown.</p>
<p>Could you give me some advice, how it could be fixed?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-countryname" rel="tag" title="see questions tagged &#39;countryname&#39;">countryname</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '22, 08:56</strong></p>
<img src="https://secure.gravatar.com/avatar/9c50686cfab696ad0f304e44256c319d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ives111&#39;s gravatar image" />
<p><span>Ives111</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ives111 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85671" class="comments-container">
&#10;</div>
<div id="comment-tools-85671" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85671-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

