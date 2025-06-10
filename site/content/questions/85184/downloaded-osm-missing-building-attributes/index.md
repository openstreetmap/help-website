+++
type = "question"
title = "Downloaded OSM missing building attributes"
description = '''I am trying to download OSM for chicago area. From website, I can see that most buildings have building:levels or height attributes. However, none of the downloads from geofabrik contain these attributes. Thus my question is how can I download files with specified attributes.'''
date = "2022-07-21T04:32:00Z"
lastmod = "2022-07-21T09:33:00Z"
weight = 85184
keywords = [ "download", "attributes", "osm", "geofabrik" ]
aliases = [ "/questions/85184" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Downloaded OSM missing building attributes](/questions/85184/downloaded-osm-missing-building-attributes)

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
<span id="post-85184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85184-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to download OSM for chicago area. From website, I can see that most buildings have building:levels or height attributes.</p>
<p>However, none of the downloads from geofabrik contain these attributes. Thus my question is how can I download files with specified attributes.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-attributes" rel="tag" title="see questions tagged &#39;attributes&#39;">attributes</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '22, 04:32</strong></p>
<img src="https://secure.gravatar.com/avatar/0d5ab631d15aec3e6e413c47ad529ac1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hlhl1993&#39;s gravatar image" />
<p><span>hlhl1993</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hlhl1993 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jul '22, 07:34</strong> </span></p>
</div>
</div>
<div id="comments-container-85184" class="comments-container">
<span id="85185"></span>
<div id="comment-85185" class="comment">
<div id="post-85185-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When you say "From website, I can see that most buildings have building:levels or height attributes" do you mean you have queried the OSM data directly to see that the area does actually have levels or have you seen a claim in the wiki?</p>
</div>
<div id="comment-85185-info" class="comment-info">
<span class="comment-age">(21 Jul '22, 07:30)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="85186"></span>
<div id="comment-85186" class="comment">
<div id="post-85186-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>On OSM I can see that most buildings have building:levels attribute. Even on small files downloaded from overpass I can see the attributes. But the file from geofabrik does not have these attributes.</p>
</div>
<div id="comment-85186-info" class="comment-info">
<span class="comment-age">(21 Jul '22, 07:34)</span> <span class="comment-user userinfo">hlhl1993</span>
</div>
</div>
</div>
<div id="comment-tools-85184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85184-form-container" class="comment-form-container">
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

<span id="85187"></span>

<div id="answer-container-85187" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85187-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-85187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The .osm.pbf files you download from Geofabrik have all the attributes present in OpenStreetMap - nothing is removed. Only the free shapefiles that Geofabrik provides have a limited set of attributes. Use the .osm.pbf file if you want to access all the tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '22, 09:33</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-85187" class="comments-container">
&#10;</div>
<div id="comment-tools-85187" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85187-form-container" class="comment-form-container">
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

