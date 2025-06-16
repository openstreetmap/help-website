+++
type = "question"
title = "Osm to postgresql import and basemaps problem"
description = '''Hi! I am using imposm to import data downloaded from OpenStreetMap. I am trying to generate map images using MapServer, using the guide from here: https://github.com/mapserver/mapserver/wiki/RenderingOsmDataOnUbuntuv2 When I import the data to my PostgreSql database using imposm, everything goes fin...'''
date = "2013-07-08T11:21:00Z"
lastmod = "2013-07-12T07:20:00Z"
weight = 24079
keywords = [ "openstreetmap", "import", "mapserver", "postgresql" ]
aliases = [ "/questions/24079" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Osm to postgresql import and basemaps problem](/questions/24079/osm-to-postgresql-import-and-basemaps-problem)

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
<span id="post-24079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24079-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I am using imposm to import data downloaded from OpenStreetMap. I am trying to generate map images using MapServer, using the guide from here: <a href="https://github.com/mapserver/mapserver/wiki/RenderingOsmDataOnUbuntuv2">https://github.com/mapserver/mapserver/wiki/RenderingOsmDataOnUbuntuv2</a></p>
<p>When I import the data to my PostgreSql database using imposm, everything goes fine. But in the basemap XML there are a couple of problems. The following tables are not generated:</p>
<pre><code>osm_new_landusages_gen00  
osm_new_waterways_gen0  
osm_new_waterways_gen1</code></pre>
<p>But these tables are referenced in the basemap MapServer XML.</p>
<p>The following pictures show the problem. The first is my result, the second is the expected (from OpenStreetMap website map): <img src="/upfiles/Screen_Shot_2013-07-08_at_10.45.33.png" alt="alt text" /> <img src="/upfiles/Screen_Shot_2013-07-08_at_10.46.36.png" alt="alt text" /></p>
<p>Thanks for any help!</p>
<p><strong>Edit:</strong></p>
<p>Now my maps look better and the tables are generated, still, the water area is not fixed. I found another example for problematic data:</p>
<p><img src="/upfiles/Screen_Shot_2013-07-08_at_14.30.02.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-mapserver" rel="tag" title="see questions tagged &#39;mapserver&#39;">mapserver</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '13, 11:21</strong></p>
<img src="https://secure.gravatar.com/avatar/083145391e68ec47ff73b0670ee42335?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aston&#39;s gravatar image" />
<p><span>Aston</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aston has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jul '13, 14:31</strong> </span></p>
</div>
</div>
<div id="comments-container-24079" class="comments-container">
&#10;</div>
<div id="comment-tools-24079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24079-form-container" class="comment-form-container">
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

<span id="24084"></span>

<div id="answer-container-24084" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24084-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The basemap uses a custom Imposm mapping. See <a href="https://github.com/mapserver/basemaps/blob/master/imposm-mapping.py">imposm-mapping.py</a></p>
<p>You need to import with: <code>imposm --mapping path/to/imposm-mapping.py ...</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '13, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/11b55b18f1f8312c7d917a0fce158162?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="olt&#39;s gravatar image" />
<p><span>olt</span><br />
<span class="score" title="76 reputation points">76</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="olt has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-24084" class="comments-container">
<span id="24085"></span>
<div id="comment-24085" class="comment">
<div id="post-24085-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I am checking it out. The tables are getting generated but the water area is still oddly missing unfortunately. I also had to switch to the basemaps 6-2 branch ...</p>
</div>
<div id="comment-24085-info" class="comment-info">
<span class="comment-age">(08 Jul '13, 13:50)</span> <span class="comment-user userinfo">Aston</span>
</div>
</div>
<span id="24087"></span>
<div id="comment-24087" class="comment">
<div id="post-24087-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The maps look much better now with the mapping file, but still, the odd missing water area problem persists : -(</p>
</div>
<div id="comment-24087-info" class="comment-info">
<span class="comment-age">(08 Jul '13, 14:17)</span> <span class="comment-user userinfo">Aston</span>
</div>
</div>
<span id="24117"></span>
<div id="comment-24117" class="comment">
<div id="post-24117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you see these errors when you zoom in? If not, then you should try a newer version of Imposm (pip install <a href="https://github.com/omniscale/imposm/archive/master.zip)">https://github.com/omniscale/imposm/archive/master.zip)</a> We fixed some issues during generalization.</p>
</div>
<div id="comment-24117-info" class="comment-info">
<span class="comment-age">(09 Jul '13, 07:31)</span> <span class="comment-user userinfo">olt</span>
</div>
</div>
<span id="24122"></span>
<div id="comment-24122" class="comment">
<div id="post-24122-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried with this latest version, but the same problem exists unfortunately. Is there any debug to catch elements that could not be processed? My original problem with the missing water area is like one well defined element that is just clearly missing from all zoom levels. The other problem, as you said, only appears on certain zoom levels.</p>
</div>
<div id="comment-24122-info" class="comment-info">
<span class="comment-age">(09 Jul '13, 12:01)</span> <span class="comment-user userinfo">Aston</span>
</div>
</div>
</div>
<div id="comment-tools-24084" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24084-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24180"></span>

<div id="answer-container-24180" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24180-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should try the latest version from GitHub and not the latest release (in case you didn't). You should also make sure that the geometry is completely included in you OSM extract (where did you get that extract?). Then there is the possibility that the geometry itself is broken. You could tweak <code>imposm.config</code> <a href="https://github.com/mapserver/basemaps/blob/master/imposm-mapping.py#L27..L33">https://github.com/mapserver/basemaps/blob/master/imposm-mapping.py#L27..L33</a> and set import_partial_relations to True and/or change relation_builder to 'union' and see if the geometry gets imported.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '13, 07:20</strong></p>
<img src="https://secure.gravatar.com/avatar/11b55b18f1f8312c7d917a0fce158162?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="olt&#39;s gravatar image" />
<p><span>olt</span><br />
<span class="score" title="76 reputation points">76</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="olt has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-24180" class="comments-container">
&#10;</div>
<div id="comment-tools-24180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24180-form-container" class="comment-form-container">
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

