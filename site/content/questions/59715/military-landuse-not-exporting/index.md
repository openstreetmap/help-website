+++
type = "question"
title = "Military Landuse not exporting"
description = '''I am trying to export all of the landuse tagged military from OSM using Osmosis. It looks like it works successfully but I get an empty OSM file. Any ideas what I am doing wrong? C:&#92;Users&#92;chris&#92;Downloads&amp;gt;osmosis --read-pbf c:&#92;users&#92;chris&#92;downloads&#92;wales-latest.osm.pbf --node-key-value keyValueLis...'''
date = "2017-09-19T19:44:00Z"
lastmod = "2017-09-20T03:50:00Z"
weight = 59715
keywords = [ "osm", "export", "java", "osmosis" ]
aliases = [ "/questions/59715" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Military Landuse not exporting](/questions/59715/military-landuse-not-exporting)

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
<span id="post-59715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59715-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to export all of the landuse tagged military from OSM using Osmosis. It looks like it works successfully but I get an empty OSM file. Any ideas what I am doing wrong?</p>
<p>C:\Users\chris\Downloads&gt;osmosis --read-pbf c:\users\chris\downloads\wales-latest.osm.pbf --node-key-value keyValueList="landuse=military" --write-xml wales_military.osm Sep 19, 2017 7:38:24 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.45 Sep 19, 2017 7:38:24 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. Sep 19, 2017 7:38:24 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Launching pipeline execution. Sep 19, 2017 7:38:24 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline executing, waiting for completion. Sep 19, 2017 7:38:32 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline complete. Sep 19, 2017 7:38:32 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Total execution time: 8536 milliseconds.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Sep '17, 19:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a22748be3d7526cc0e51a11c136cc582?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChristopherSmit702&#39;s gravatar image" />
<p><span>ChristopherS...</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChristopherSmit702 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59715" class="comments-container">
&#10;</div>
<div id="comment-tools-59715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59715-form-container" class="comment-form-container">
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

<span id="59716"></span>

<div id="answer-container-59716" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59716-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-59716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Landuse will mostly be on ways, so you will need a way filter to extract them (you currently have --node-key-value, which is what it sounds like).</p>
<p>If you are just getting started working with OSM data, take a look at <a href="http://wiki.openstreetmap.org/wiki/Elements">http://wiki.openstreetmap.org/wiki/Elements</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '17, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Sep '17, 20:48</strong> </span></p>
</div>
</div>
<div id="comments-container-59716" class="comments-container">
<span id="59717"></span>
<div id="comment-59717" class="comment">
<div id="post-59717-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That was really helpful thanks, I changed it to ways and rejected relations which got the answer I was expecting.</p>
</div>
<div id="comment-59717-info" class="comment-info">
<span class="comment-age">(19 Sep '17, 20:43)</span> <span class="comment-user userinfo">ChristopherS...</span>
</div>
</div>
<span id="59718"></span>
<div id="comment-59718" class="comment">
<div id="post-59718-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>According to tag info, there are 2000 landuse= military tagged on relations, wonder why you reject relations? Compare this with the 31.000 on ways.</p>
</div>
<div id="comment-59718-info" class="comment-info">
<span class="comment-age">(20 Sep '17, 03:50)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-59716" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59716-form-container" class="comment-form-container">
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

