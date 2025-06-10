+++
type = "question"
title = "Why won&#x27;t object show on map layer but does on data layer?"
description = '''I have recently added some new footpaths to OSM and 3 archeological features (2 x ruined churches and 1 x wayside cross). One of the churches and the wayside cross (plus all footpath additions) are showing on the map but the 2nd church isn&#x27;t showing. It is there on the data layer but not on the map....'''
date = "2017-01-09T13:34:00Z"
lastmod = "2017-01-09T19:05:00Z"
weight = 53948
keywords = [ "datadisplay" ]
aliases = [ "/questions/53948" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why won't object show on map layer but does on data layer?](/questions/53948/why-wont-object-show-on-map-layer-but-does-on-data-layer)

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
<span id="post-53948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53948-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have recently added some new footpaths to OSM and 3 archeological features (2 x ruined churches and 1 x wayside cross). One of the churches and the wayside cross (plus all footpath additions) are showing on the map but the 2nd church isn't showing. It is there on the data layer but not on the map. I've tried replacing it, copying the "good" church into the required location (then changing the tags) but I'm missing something here. I've tried editing the data using the OSM website and JOSM.</p>
<p>Can someone have a look at 50.3658353, -5.1341847 (Perran Sands, Perranporth, Cornwall UK) to see what I'm doing wrong?</p>
<p>Thanks</p>
<p>XG</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-datadisplay" rel="tag" title="see questions tagged &#39;datadisplay&#39;">datadisplay</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '17, 13:34</strong></p>
<img src="https://secure.gravatar.com/avatar/3a9a0c918f8ce5994e08a3958895e9b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xgraphica&#39;s gravatar image" />
<p><span>xgraphica</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xgraphica has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53948" class="comments-container">
<span id="53954"></span>
<div id="comment-53954" class="comment">
<div id="post-53954-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just a note: an easier way to point to an ares is to just copy this bit from the map view. <a href="http://www.openstreetmap.org/search?query=50.3658353%2C%20-5.1341847#map=16/50.3808/-5.1512">http://www.openstreetmap.org/search?query=50.3658353%2C%20-5.1341847#map=16/50.3808/-5.1512</a></p>
</div>
<div id="comment-53954-info" class="comment-info">
<span class="comment-age">(09 Jan '17, 17:17)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-53948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53948-form-container" class="comment-form-container">
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

<span id="53949"></span>

<div id="answer-container-53949" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53949-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-53949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Esentially, because the standard map style chooses not to render the things that you have mapped. Using the map style that I normally use I can see <a href="http://www.openstreetmap.org/node/4579545504">these</a> <a href="http://www.openstreetmap.org/node/4580945263">three</a> <a href="http://www.openstreetmap.org/node/4598030093">nodes</a>. Something more tailored to showing historical information may work for you.</p>
<p>My first thought for a public site that might show these was the <a href="http://gk.historic.place/historische_objekte/translate/en/index-en.html?zoom=17&amp;lat=50.3656&amp;lon=-5.13522&amp;pid=KmHaSaHe">historical objects map</a>, but that doesn't seem to.</p>
<p>For info I'm seeing your 3 nodes on a map <a href="https://github.com/SomeoneElseOSM/openstreetmap-carto-AJT">forked from what the "standard style" was several years ago</a>, but there are no public tiles for that I'm afraid.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '17, 13:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-53949" class="comments-container">
<span id="53950"></span>
<div id="comment-53950" class="comment">
<div id="post-53950-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your explanation - If understand correctly, I need to find a symbol/reference that is acceptable to the standard rendering style.</p>
</div>
<div id="comment-53950-info" class="comment-info">
<span class="comment-age">(09 Jan '17, 14:12)</span> <span class="comment-user userinfo">xgraphica</span>
</div>
</div>
<span id="53951"></span>
<div id="comment-53951" class="comment">
<div id="post-53951-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not really - the "standard" map style is designed as a general map style and some things won't show up on there by design (many of the things that I map regularly, such as public footpaths, offices and stiles, don't). Just use the best tags you can to describe what it is.</p>
<p>One other thought - if you can draw it as an area rather than just a node it'd be better, since that gives a better "real world picture" of the object.</p>
</div>
<div id="comment-53951-info" class="comment-info">
<span class="comment-age">(09 Jan '17, 14:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53957"></span>
<div id="comment-53957" class="comment">
<div id="post-53957-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, the data contained on the three nodes is mostly duplicated, it could all be contained on one node. Or if you decide to draw an area for the ruins all data could be contained on the polygon.</p>
</div>
<div id="comment-53957-info" class="comment-info">
<span class="comment-age">(09 Jan '17, 19:05)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
</div>
<div id="comment-tools-53949" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53949-form-container" class="comment-form-container">
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

