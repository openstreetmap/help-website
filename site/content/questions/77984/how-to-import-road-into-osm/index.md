+++
type = "question"
title = "How to import road into OSM ?"
description = '''Hi, is there anyway we can import roads into OSM ? Cos the area i&#x27;m currently looking at in OSM is an empty land. Can i overlay with roads and if so, what format(s) are accepted by OSM ? Thanks in advance. '''
date = "2020-12-18T09:23:00Z"
lastmod = "2020-12-19T00:35:00Z"
weight = 77984
keywords = [ "roads" ]
aliases = [ "/questions/77984" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to import road into OSM ?](/questions/77984/how-to-import-road-into-osm)

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
<span id="post-77984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77984-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, is there anyway we can import roads into OSM ? Cos the area i'm currently looking at in OSM is an empty land. Can i overlay with roads and if so, what format(s) are accepted by OSM ? Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '20, 09:23</strong></p>
<img src="https://secure.gravatar.com/avatar/da5e015424a1d22ec13eb6f63cb92536?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AvonTay&#39;s gravatar image" />
<p><span>AvonTay</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AvonTay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77984" class="comments-container">
<span id="77987"></span>
<div id="comment-77987" class="comment">
<div id="post-77987-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you paste the osm url of this empty land so we can best evaluate how to proceed with the road mapping.</p>
</div>
<div id="comment-77987-info" class="comment-info">
<span class="comment-age">(18 Dec '20, 11:17)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="77988"></span>
<div id="comment-77988" class="comment">
<div id="post-77988-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, not sure if you can see this ? The bottom part is a beige patch of land.. <a href="https://www.openstreetmap.org/way/795855457#map=12/1.2769/103.6386">https://www.openstreetmap.org/way/795855457#map=12/1.2769/103.6386</a></p>
</div>
<div id="comment-77988-info" class="comment-info">
<span class="comment-age">(18 Dec '20, 11:29)</span> <span class="comment-user userinfo">AvonTay</span>
</div>
</div>
</div>
<div id="comment-tools-77984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77984-form-container" class="comment-form-container">
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

<span id="77997"></span>

<div id="answer-container-77997" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77997-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you zoom in further you will notice that the area is well mapped. A different amount of detail is rendered on the tiles at different zoom levels.</p>
<p>If you have detailed plans for roadworks you would likely need explicit permission from the copyright holders for use in OSM and comply with the import guidelines. See <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">https://wiki.openstreetmap.org/wiki/Import/Guidelines</a></p>
<p>Then you would need to process the plans into a form to add the OSM, including using the correct projection coordinate system. If using an image you would need to warp/georeference to match osm. There are many varied way of processing data into a form suitable for osm and I will leave that for you to investigate as it can be very complex and time consuming and if not done correctly with help from local mappers can be a disaster to rectify. Proceed cautiously. <a href="https://wiki.openstreetmap.org/wiki/Import/Software">https://wiki.openstreetmap.org/wiki/Import/Software</a></p>
<p>If already in a form that JOSM can open you could merge sections that are suitable for OSM and tag with usual tags used in OSM or you could use the plans as a background and draw the roads (edit) in to the OSM directly.</p>
<p>After getting this far through my reply I think you will agree that this small area you are wanting to update is more easily accomplished by doing more simply using one of the main editors like iD, JOSM or the new Potlatch 3 when released and using the aerial imagery and gps traces that are available. You can also use a gps receiver and camera to walk/ride/drive the new streets and add to the editor if they are not yet on imagery.<br />
<a href="https://learnosm.org/en/">https://learnosm.org/en/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '20, 00:35</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Dec '20, 01:38</strong> </span></p>
</div>
</div>
<div id="comments-container-77997" class="comments-container">
&#10;</div>
<div id="comment-tools-77997" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77997-form-container" class="comment-form-container">
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

