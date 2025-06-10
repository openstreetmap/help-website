+++
type = "question"
title = "OSM filter"
description = '''Hey I converted a OSM file to CSV, with: osmconvert64.exe netherlands-latest.osm --max-objects=999999--all-to-nodes --csv=&quot;@lat @lon addr:street addr:housenumber addr:postcode addr:city&quot; -o=streets.csv And I want to import the CSV into MySQL-database, but the file is 3GB. I noticed that in the CSV f...'''
date = "2019-10-04T21:21:00Z"
lastmod = "2019-10-04T21:21:00Z"
weight = 71037
keywords = [ "osmfilter" ]
aliases = [ "/questions/71037" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OSM filter](/questions/71037/osm-filter)

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
<span id="post-71037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71037-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey I converted a OSM file to CSV, with:</p>
<p><code>osmconvert64.exe netherlands-latest.osm --max-objects=999999--all-to-nodes --csv="</code><a href="https://help.openstreetmap.org/users/5110/latroc"></a><a href="https://help.openstreetmap.org/users/5110/latroc"></a><a href="https://help.openstreetmap.org/users/5110/latroc"><code>@lat</code></a></a></a><code> </code><a href="https://help.openstreetmap.org/users/1350/longestaugust"></a><a href="https://help.openstreetmap.org/users/1350/longestaugust"></a><a href="https://help.openstreetmap.org/users/1350/longestaugust"><code>@lon</code></a></a></a><code> addr:street addr:housenumber addr:postcode addr:city" -o=streets.csv</code></p>
<p>And I want to import the CSV into MySQL-database, but the file is 3GB. I noticed that in the CSV file their is sometimes lat/lon, but no addr data. <strong>Is their a way I can filter out records that don't have the addr data? (To reduce filesize CSV, and unwanted data)</strong></p>
<p>I tried: <code>osmfilter.exe netherlands-latest.osm --keep="</code><a href="https://help.openstreetmap.org/users/5110/latroc"></a><a href="https://help.openstreetmap.org/users/5110/latroc"></a><a href="https://help.openstreetmap.org/users/5110/latroc"><code>@lat</code></a></a></a><code>= and </code><a href="https://help.openstreetmap.org/users/1350/longestaugust"></a><a href="https://help.openstreetmap.org/users/1350/longestaugust"></a><a href="https://help.openstreetmap.org/users/1350/longestaugust"><code>@lon</code></a></a></a><code>= and addr:street= and addr:housenumber= and addr:postcode= and addr:city= and </code><a href="https://help.openstreetmap.org/users/5110/latroc"></a><a href="https://help.openstreetmap.org/users/5110/latroc"></a><a href="https://help.openstreetmap.org/users/5110/latroc"><code>@lat</code></a></a></a><code>!=null and </code><a href="https://help.openstreetmap.org/users/1350/longestaugust"></a><a href="https://help.openstreetmap.org/users/1350/longestaugust"></a><a href="https://help.openstreetmap.org/users/1350/longestaugust"><code>@lon</code></a></a></a><code>!=null and addr:street!=null and addr:housenumber!=null and addr:postcode!=null and addr:city!=null" -o=netherlands-filtered.osm</code></p>
<p><code>osmfilter.exe netherlands-latest.osm --keep="addr:street!=null and addr:housenumber!=null and addr:postcode!=null and addr:city!=null" -o=netherlands-filtered.osm</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '19, 21:21</strong></p>
<img src="https://secure.gravatar.com/avatar/430575bf72d15dd9b3052fbdc11ab09e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JSteen&#39;s gravatar image" />
<p><span>JSteen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JSteen has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Oct '19, 21:23</strong> </span></p>
</div>
</div>
<div id="comments-container-71037" class="comments-container">
&#10;</div>
<div id="comment-tools-71037" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71037-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

