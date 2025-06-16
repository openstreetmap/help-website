+++
type = "question"
title = "Using external ID"
description = '''Hello, Due to the current situation of coronavirus. We (me and some friends, from Tunisia) were asked by the government to create a map with all the pharmacies. All they could provide us with were different lists of pharmacies with lat/lng from different sources. We decided we&#x27;ll use OSM for that pu...'''
date = "2020-03-20T12:36:00Z"
lastmod = "2020-03-20T15:09:00Z"
weight = 73643
keywords = [ "ref", "corona_virus", "tagging", "pharmacy" ]
aliases = [ "/questions/73643" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Using external ID](/questions/73643/using-external-id)

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
<span id="post-73643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73643-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>Due to the current situation of coronavirus. We (me and some friends, from Tunisia) were asked by the government to create a map with all the pharmacies.</p>
<p>All they could provide us with were different lists of pharmacies with lat/lng from different sources.</p>
<p>We decided we'll use OSM for that purpose and <strong>the question is</strong> : Is it ok to add tags like "ref:med.tn = 3233" which means the source is www.med.tn and the pharmacy id in their database is 3233 ? <strong>Is there any chance a script might remove them ?</strong></p>
<p>We have a few sources and that would allow us to synchronise everything with what' already available in OSM.</p>
<p>Or should we use a different tag/technique for that matter ? I would like to avoid the node/way Ids as there are a lot of duplicates already in the actual map.</p>
<p>Thank you</p>
<p>PS: We already started ... those tags would be removed in a few months, it's just temporary.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ref" rel="tag" title="see questions tagged &#39;ref&#39;">ref</span> <span class="post-tag tag-link-corona_virus" rel="tag" title="see questions tagged &#39;corona_virus&#39;">corona_virus</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-pharmacy" rel="tag" title="see questions tagged &#39;pharmacy&#39;">pharmacy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Mar '20, 12:36</strong></p>
<img src="https://secure.gravatar.com/avatar/2627913548c0e0d2dc3d7be90a3a6bd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="selimachour&#39;s gravatar image" />
<p><span>selimachour</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="selimachour has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73643" class="comments-container">
&#10;</div>
<div id="comment-tools-73643" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73643-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="73644"></span>

<div id="answer-container-73644" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73644-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-73644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The fastest and easiest way to create a map like you say is umap.openstreetmap.fr - just create a JSON file with the pharamacies, open it on umap, and you're done!</p>
<p>In order to import data into OpenStreetMap, you need to follow the import guidelines (<a href="https://wiki.openstreetmap.org/wiki/Import).">https://wiki.openstreetmap.org/wiki/Import).</a> Please pause any activities adding data to OSM until you have read and understood these guidelines.</p>
<p>Among other things, we need to establish:</p>
<ol>
<li><p>Are the sources that you want to use cleared from a copyright point of view? You say that you have "a few sources" and it is unclear what the license is on those; just because someone in the government has given you a few lists doesn't necessarily mean anything.</p></li>
<li><p>What is the data quality like? Do you have the local knowledge (or additional sources) to verify the data? More often than not, such data sets have had their lat/lon created by throwing an address into a geocoder which can lead to copyright issues (see 1) but also to locations that are hundreds of metres away from the correct spot (occasionally even in a different city).</p></li>
<li><p>What exactly is your procedure to "synchronize" with what is already in OSM?</p></li>
</ol>
<p>Using an "umap" for your project is quick way of getting something done that you can show to the government; we can then take the necessary time to vet the dataset for import in OpenStreetMap proper and ultimately have the data in OSM, but you cannot import questionable data just like that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '20, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-73644" class="comments-container">
<span id="73648"></span>
<div id="comment-73648" class="comment">
<div id="post-73648-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>As pointed out in a <a href="/questions/73633/difference-between-osm-and-overpass-turbo">recent question</a>, different types of element <em>can</em> have the same id, but they are unique within each type.</p>
</div>
<div id="comment-73648-info" class="comment-info">
<span class="comment-age">(20 Mar '20, 15:09)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-73644" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73644-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73645"></span>

<div id="answer-container-73645" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73645-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Frederik,</p>
<p>I did start with umap (which I oftern use) this morning but quickly gave up. The idea was to use overpass to query all the pharmacies but lots of "name:en" with no "name" etc ... I thought I might as well fix those in OSM.</p>
<p>I will take the time to read the <a href="https://wiki.openstreetmap.org/wiki/Import">https://wiki.openstreetmap.org/wiki/Import</a></p>
<ol>
<li>The second I read the word "source", I decided to stop :) Thank you for pointing this out. It completely slipped my mind</li>
<li>The quality is actually good but maybe not complete. We're verifying by doing searches on google for the pharmacies and looking at the infos they provided (address, phone numbers, opening hours ...)</li>
<li>The procedure is just manually checking with JOSM, importing from OSM and checking the around which already shows that sometimes up to 3 nodes or closed ways exist for the same pharmacy</li>
</ol>
<p>I will revert to creating an extra table in my postgres database (which is updated every night from geofabric) which will hold a merge of osm + the extra sources.</p>
<p><strong>Last Question</strong>: In the OSM database, there are node Ids, way Ids, and relation Ids. Are they all unique within each other ? Is it possible to have the same Id for a node and a way ?</p>
<p>Thanks again</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '20, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/2627913548c0e0d2dc3d7be90a3a6bd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="selimachour&#39;s gravatar image" />
<p><span>selimachour</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="selimachour has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Mar '20, 13:13</strong> </span></p>
</div>
</div>
<div id="comments-container-73645" class="comments-container">
&#10;</div>
<div id="comment-tools-73645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73645-form-container" class="comment-form-container">
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

