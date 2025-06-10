+++
type = "question"
title = "[closed] generate tiles in WGS84 projection?"
description = '''Hello, I use Maperitive to generate tiles from osm data. Then I use those tiles in my application. The tiles generated are in Mercator projection but my application requires tiles in WGS84. I wonder what options I have: 1. Is there a way to let Maperitive generating tiles in WGS84? 2. If 1 is imposs...'''
date = "2013-09-26T07:12:00Z"
lastmod = "2013-09-30T12:32:00Z"
weight = 26756
keywords = [ "wgs84" ]
aliases = [ "/questions/26756" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] generate tiles in WGS84 projection?](/questions/26756/generate-tiles-in-wgs84-projection)

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
<span id="post-26756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26756-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I use Maperitive to generate tiles from osm data. Then I use those tiles in my application. The tiles generated are in Mercator projection but my application requires tiles in WGS84. I wonder what options I have: 1. Is there a way to let Maperitive generating tiles in WGS84? 2. If 1 is impossible, is MapProxy the only tool I can use to re-project the tiles from Mercator to WGS84?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wgs84" rel="tag" title="see questions tagged &#39;wgs84&#39;">wgs84</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Sep '13, 07:12</strong></p>
<img src="https://secure.gravatar.com/avatar/097099bfea770186a935d80469281663?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hua%20zhang&#39;s gravatar image" />
<p><span>hua zhang</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hua zhang has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>30 Sep '13, 12:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-26756" class="comments-container">
&#10;</div>
<div id="comment-tools-26756" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26756-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason ""Close" was requested by initial questioner; a different question now best reflects what they're asking." by SomeoneElse 30 Sep '13, 12:33

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26789"></span>

<div id="answer-container-26789" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26789-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you may be confusing <a href="http://en.wikipedia.org/wiki/Mercator_projection">Mercator</a> which is a map projection with <a href="http://en.wikipedia.org/wiki/World_Geodetic_System">WGS84</a> which is coordinate frame for the Earth. All location data stored in the OSM database is stored as latitude/longitude positions using the WGS84 standard. WGS84 is a 3-dimentional model of the earth, to create a 2-dimentional map of a part of the earth this data needs to be transformed and scaled to fit. This is what the map projection does for you. Mercator is just one of many hundreds of different possible map transformations, but is the one used by the standard OSM map tiles.</p>
<p>So to answer your question: Your map tiles are created from WGS84 data using the Mercator projection by the Maperitive application. This is probably what your application requires.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '13, 15:40</strong></p>
<img src="https://secure.gravatar.com/avatar/6edb4957e57770118c3b8022cfce68a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srbrook&#39;s gravatar image" />
<p><span>srbrook</span><br />
<span class="score" title="993 reputation points">993</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srbrook has 3 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-26789" class="comments-container">
<span id="26799"></span>
<div id="comment-26799" class="comment">
<div id="post-26799-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hello srbrook, thank you very much for explain WGS84 and projections for me. I think I got better idea now. My application is using tiles from other source. I am trying to use OSM tiles instead. After I put OSM tiles in the application, (I tested on a few places,) the x coordinates looks the same as before, but y coordinates are about a couple of kilometres different between two tile source. My first guess was it is probably to do with osm tiles are using a different projection from what the application requires. After I saw this post <a href="https://help.openstreetmap.org/questions/23934/osm-and-4326-projection,">https://help.openstreetmap.org/questions/23934/osm-and-4326-projection,</a> I am more convinced that this is to do with the different projection.</p>
<p>I will have another look at the application code, and I might need your help again. Thanks.</p>
</div>
<div id="comment-26799-info" class="comment-info">
<span class="comment-age">(27 Sep '13, 04:47)</span> <span class="comment-user userinfo">hua zhang</span>
</div>
</div>
<span id="26861"></span>
<div id="comment-26861" class="comment">
<div id="post-26861-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello srbrook, my application is using osm tiles as the background layer, and features on other layers are created by mapinfo. Because mapinfo is using NAD83 projection. I guess my question became how to generate tiles in NAD83 projection. To remove confusion, I started a new question <a href="https://help.openstreetmap.org/questions/26860/how-to-generate-tiles-in-nad83-projection,">https://help.openstreetmap.org/questions/26860/how-to-generate-tiles-in-nad83-projection,</a> and I will close this question. I look forward to your reply in the new question. Thanks.</p>
</div>
<div id="comment-26861-info" class="comment-info">
<span class="comment-age">(30 Sep '13, 12:29)</span> <span class="comment-user userinfo">hua zhang</span>
</div>
</div>
<span id="26862"></span>
<div id="comment-26862" class="comment">
<div id="post-26862-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know how to close this question. :(</p>
</div>
<div id="comment-26862-info" class="comment-info">
<span class="comment-age">(30 Sep '13, 12:32)</span> <span class="comment-user userinfo">hua zhang</span>
</div>
</div>
</div>
<div id="comment-tools-26789" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26789-form-container" class="comment-form-container">
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

