+++
type = "question"
title = "Cities and villages in area hierarchy"
description = '''Dear developers! I use the features of OSM for a while, mostly for representing geodata related to subareas of my country (Hungary). I see that most countries has the following hierarchy : level 2: country itself level 4: subregion level 5: further division of the subregion level 6: counties level 7...'''
date = "2014-05-11T10:49:00Z"
lastmod = "2014-05-11T11:40:00Z"
weight = 33079
keywords = [ "hierarchy", "city", "subdivision", "batch", "village" ]
aliases = [ "/questions/33079" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cities and villages in area hierarchy](/questions/33079/cities-and-villages-in-area-hierarchy)

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
<span id="post-33079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33079-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear developers!<br />
I use the features of OSM for a while, mostly for representing geodata related to subareas of my country (Hungary).<br />
I see that most countries has the following hierarchy :<br />
level 2: country itself<br />
level 4: subregion<br />
level 5: further division of the subregion<br />
level 6: counties<br />
level 7: part of counties ("járás")<br />
level 8: villages and cities<br />
level 9: districts (of capital)<br />
</p>
<p>The subareas are well linked to each other with "subarea" typed members. But what I miss is to include villages and cities in this hierarchy.<br />
What is the osm policy about extending member declarations of subareas?<br />
I wrote a program which fetches all the villages, and searches for the correspondent level7 area what they are included in. (earlier I modified the map to link missing admin_centre nodes correctly) If you are interested in, i can adopt the method to other countries, it's fast enough to process the whole world if needed. Hovewer, the last step of submitting informations is still missing.<br />
The final result is now a list of village-subarea id pair I calculated which would be posted somehot to the map itself. I guess I should use the API somehow to this, if you have any simple solution to this operation (only want to add a single member as the following):</p>
<pre><code>member type=relation ref=[village_id] role=subarea</code></pre>
<p>Would say thanks for any help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hierarchy" rel="tag" title="see questions tagged &#39;hierarchy&#39;">hierarchy</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-subdivision" rel="tag" title="see questions tagged &#39;subdivision&#39;">subdivision</span> <span class="post-tag tag-link-batch" rel="tag" title="see questions tagged &#39;batch&#39;">batch</span> <span class="post-tag tag-link-village" rel="tag" title="see questions tagged &#39;village&#39;">village</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '14, 10:49</strong></p>
<img src="https://secure.gravatar.com/avatar/b18317f8fea203e9e32c292314d38ead?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cpt%20Balu&#39;s gravatar image" />
<p><span>Cpt Balu</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cpt Balu has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 May '14, 10:53</strong> </span></p>
</div>
</div>
<div id="comments-container-33079" class="comments-container">
&#10;</div>
<div id="comment-tools-33079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33079-form-container" class="comment-form-container">
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

<span id="33081"></span>

<div id="answer-container-33081" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33081-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-33081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "subarea" notation is not established practice in OSM - it is only used in some countries, and generally considered unnecessary or even problematic, much like the <code>is_in</code> tag that we used to have. Whether or not something is a subarea of something else can, and should, be determined by looking at the geometry, not by following some explicit links that someone has added.</p>
<p>Please do not add any subarea tagging to regions where the concept isn't used, and under no circumstances should you automatically generate subarea links and add them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '14, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-33081" class="comments-container">
&#10;</div>
<div id="comment-tools-33081" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33081-form-container" class="comment-form-container">
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

