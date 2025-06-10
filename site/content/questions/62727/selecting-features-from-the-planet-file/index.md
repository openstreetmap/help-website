+++
type = "question"
title = "Selecting features from the planet file"
description = '''I have dovnloaded &quot;historical&quot; planet file from 2015 year. I need select only some features in the Europe area. As first I used osmosis for this operation: osmosis --read-xml file=&quot;d:&#92;DATA_works&#92;meff2018&#92;planet_2015&#92;planet-151228.osm&quot; --bounding-polygon file=&quot;europe.poly&quot; --tf accept-ways highway= -...'''
date = "2018-03-19T09:30:00Z"
lastmod = "2018-03-19T11:23:00Z"
weight = 62727
keywords = [ "osmconvert", "selection", "osmfilter", "osmosis", "tags" ]
aliases = [ "/questions/62727" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Selecting features from the planet file](/questions/62727/selecting-features-from-the-planet-file)

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
<span id="post-62727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62727-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have dovnloaded "historical" planet file from 2015 year. I need select only some features in the Europe area. As first I used osmosis for this operation:</p>
<p><em>osmosis --read-xml file="d:\DATA_works\meff2018\planet_2015\planet-151228.osm" --bounding-polygon file="europe.poly" --tf accept-ways highway=</em> --write-xml file="d:\DATA_works\meff2018\planet_2015\all_HWs_2015_europe.osm"*</p>
<p>But this command selected only nodes from the planet files, not lines.</p>
<p>So I tried second option - combination of osmfilter and osmconvert commands:</p>
<p>*osmfilter d:\DATA_works\meff2018\planet_2015\planet-151228.osm --keep="highway= motorway =motorway_link =trunk =trunk_link =primary =primary_link =secondary =secondary_link =tertiary= tertiary_link" -o=e:\data\osm2015\accepted_HWs_world.osm</p>
<p>osmconvert e:\data\osm2015\accepted_HWs_world.osm -B=europe.poly -o=e:\data\osm2015\accepted_HWs_europe.osm*</p>
<p>After this, I have file with lines for Europe. But there are ALL highways - not only this, which are mentioned in the --keep option in the osmfilter command. Can you tell me what I'm doing wrong, please?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-selection" rel="tag" title="see questions tagged &#39;selection&#39;">selection</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '18, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/6a954537fae02e15ed5003ded07963ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kope&#39;s gravatar image" />
<p><span>kope</span><br />
<span class="score" title="55 reputation points">55</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kope has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '18, 10:05</strong> </span></p>
</div>
</div>
<div id="comments-container-62727" class="comments-container">
<span id="62728"></span>
<div id="comment-62728" class="comment">
<div id="post-62728-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>at least one problem might be that you have a space between "highway=" and "motorway". This is what I use in a parameter file:</p>
<p>--keep=highway=motorway =motorway_link =trunk =trunk_link =primary =primary_link =secondary =secondary_link =tertiary =residential =unclassified =pedestrian</p>
<p>--drop-relations</p>
</div>
<div id="comment-62728-info" class="comment-info">
<span class="comment-age">(19 Mar '18, 11:23)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62727" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62727-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

