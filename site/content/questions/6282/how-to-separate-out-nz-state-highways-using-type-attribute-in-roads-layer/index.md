+++
type = "question"
title = "How to separate out NZ state highways using type attribute in roads layer?"
description = '''After posting this I realised I had forgotten to mention that I am working off downloaded NZ road shapefile from http://download.geofabrik.de/osm/australia-oceania/ - so perhaps this download does not include all road attributes. I also noted a New Zealand discussion on highway attribution - http://...'''
date = "2011-07-12T05:26:00Z"
lastmod = "2011-07-12T09:39:00Z"
weight = 6282
keywords = [ "type", "road" ]
aliases = [ "/questions/6282" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to separate out NZ state highways using type attribute in roads layer?](/questions/6282/how-to-separate-out-nz-state-highways-using-type-attribute-in-roads-layer)

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
<span id="post-6282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6282-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After posting this I realised I had forgotten to mention that I am working off downloaded NZ road shapefile from <a href="http://download.geofabrik.de/osm/australia-oceania/">http://download.geofabrik.de/osm/australia-oceania/</a> - so perhaps this download does not include all road attributes. I also noted a New Zealand discussion on highway attribution - <a href="https://wiki.openstreetmap.org/wiki/Talk:WikiProject_New_Zealand">https://wiki.openstreetmap.org/wiki/Talk:WikiProject_New_Zealand</a> so I will follow up with the New Zealand OSM group.</p>
<p>In New Zealand there is a clear distinction between roads that are state highways and roads that are not. They are managed and signposted separately. Although open street map data has a variety of entries in the 'name', 'ref' and 'type' fields, it is not possible to create a valid query just for state highways. This is primarily a problem of consistency in attribute usage.</p>
<p>I would like a simple query to be able to select all New Zealand state highways and think that many users of the data would find this useful. I am aware that different countries have very different hierarchies for roads and different administrative and management classification systems.</p>
<p>My simple suggestion would be to add a new type to the roads layer = 'NZ State Highway', and apply this to all state highway road sections in New Zealand. Is this a reasonable approach? How could this be done better? How could this be made more generic to be useful to the wider community? Should another attribute be added to roads? Should the new type just be 'Highway' - even though this means different things in different countries?</p>
<p><strong>Examples of state highway attribute data existing currently.</strong><br />
1. where 'name' like "SH" "State Highway" "SH36" "Highway"<br />
2. where 'ref' like "SH" - in practise either "SH2" or just "2" has been used<br />
3. where 'type" in ('motorway', 'primary','trunk') - although this usage is not consistent - some state highways are classified as 'secondary' and not all 'primary' roads are state highways</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-type" rel="tag" title="see questions tagged &#39;type&#39;">type</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '11, 05:26</strong></p>
<img src="https://secure.gravatar.com/avatar/da35d2937e9b5bc22ed18232848c36b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Filby&#39;s gravatar image" />
<p><span>Filby</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Filby has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jul '11, 06:35</strong> </span></p>
</div>
</div>
<div id="comments-container-6282" class="comments-container">
&#10;</div>
<div id="comment-tools-6282" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6282-form-container" class="comment-form-container">
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

<span id="6283"></span>

<div id="answer-container-6283" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6283-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In OpenStreetMap, the <code>highway</code> (<em>not</em> <code>type</code>) tag is used to indicate a road's prominence in the country's road system.</p>
<p>There are certain internationally agreed values for this tag: <code>highway=motorway, highway=trunk, highway=primary, highway=secondary, highway=tertiary, highway=unclassified</code>, and <code>highway=residential</code>.</p>
<p>Different countries have their own rules for what type of road gets what value, and often (though not always) these coincide with administrative classifications. In the UK, for example, "primary A roads" with green signs are tagged <code>highway=trunk</code>; other A roads with black-and-white signs are tagged <code>highway=primary</code>; and B roads are tagged <code>highway=secondary</code>. You can read a country-by-country list of these rules <a href="https://wiki.openstreetmap.org/wiki/Key:highway#International_equivalence">on the wiki</a>.</p>
<p>New Zealand doesn't appear to have settled on a consistent set of rules yet. It would be good if it did. You can discuss this on <a href="http://groups.google.com/group/nzopengis">the local mailing list</a>, but you should be aiming to agree on a rule whereby "all state highways are classed as <code>highway=trunk</code>, and the <code>ref</code> tag just contains the number" or something like that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '11, 08:10</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jul '11, 10:35</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-6283" class="comments-container">
<span id="6284"></span>
<div id="comment-6284" class="comment">
<div id="post-6284-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Additionally you may want to set operator="NZ state highway agency" or similar. But again that has to be decided by the New Zealand community and this help site is the wrong forum to do so.</p>
</div>
<div id="comment-6284-info" class="comment-info">
<span class="comment-age">(12 Jul '11, 09:39)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
</div>
<div id="comment-tools-6283" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6283-form-container" class="comment-form-container">
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

