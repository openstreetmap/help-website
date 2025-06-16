+++
type = "question"
title = "Town nodes and Polygons that fail to confine the Name within an area"
description = '''If I type a street and town into the search box on the map page the nominatim finds the place on the map correctly but says that the street is in a nearby suburb which is incorrect. To fix this I have drawn a polygon and named it. This should contain it to its own area but it does not always work. S...'''
date = "2011-06-13T22:42:00Z"
lastmod = "2011-06-20T19:22:00Z"
weight = 5745
keywords = [ "boundaries", "nominatim", "polygons" ]
aliases = [ "/questions/5745" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Town nodes and Polygons that fail to confine the Name within an area](/questions/5745/town-nodes-and-polygons-that-fail-to-confine-the-name-within-an-area)

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
<span id="post-5745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5745-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If I type a street and town into the search box on the map page the nominatim finds the place on the map correctly but says that the street is in a nearby suburb which is incorrect.</p>
<p>To fix this I have drawn a polygon and named it. This should contain it to its own area but it does not always work. Some mappers think the single node suburbs are the problem. Please try some address in your area for examples. There is also a delay as the nominatim is not being updated at the present time. What are your solutions or ideas on this problem. Note examples are now fixed</p>
<p><em>Edit (extracted from comments):</em></p>
<p>One example: <a href="https://www.openstreetmap.org/?minlon=-0.171881511807442&amp;minlat=52.3324775695801&amp;maxlon=-0.164698585867882&amp;maxlat=52.335319519043">https://www.openstreetmap.org/?minlon=-0.171881511807442&amp;minlat=52.3324775695801&amp;maxlon=-0.164698585867882&amp;maxlat=52.335319519043</a></p>
<p>This is Hartford Road, Huntingdon, which appears as part of Stukeley Meadows(which is a polygon), whereas Stukeley Meadows is a suburb of Huntingdon. The name also appears in Godmanchester as well.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '11, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jul '12, 11:56</strong> </span></p>
</div>
</div>
<div id="comments-container-5745" class="comments-container">
&#10;</div>
<div id="comment-tools-5745" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5745-form-container" class="comment-form-container">
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

<span id="5909"></span>

<div id="answer-container-5909" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5909-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-5909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="andy mackey has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>To fix this I had to drawn a polygon and name it. This should contain it to its own area but it does not always work.</p>
</blockquote>
<p>This is the key to the problem. Drawing a polygon around a node does not "contain" the node area. Nominatim treats this as two boundaries, one bound by the polygon, and one by the node.</p>
<p>The node area is then estimated, since Nominatim does not have a bounding polygon for it. It makes estimates, and it's often wrong.</p>
<p>If you have a bounding polygon, then you can remove the node. Removing the node should fix your problem once Nominatim comes back online (it's not updating at the moment due to scaling issues discussed in other questions).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '11, 19:18</strong></p>
<img src="https://secure.gravatar.com/avatar/5f2082b86cc50d63c05f33f55166df2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emacsen&#39;s gravatar image" />
<p><span>emacsen</span><br />
<span class="score" title="1191 reputation points"><span>1.2k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emacsen has 4 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Sep '14, 19:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span></p>
</div>
</div>
<div id="comments-container-5909" class="comments-container">
&#10;</div>
<div id="comment-tools-5909" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5909-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5906"></span>

<div id="answer-container-5906" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5906-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-5906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have questions about Nominatim search results, Nominatim lets you see how it reached its conclusions.</p>
<p>To see it, do your search on <a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a> . In the result list, click on "details"; then you'll see exactly how Nominatim reached its conclusions.</p>
<p>In your example, searching for "hartford road, huntingdon" on Nominatim will show you that the OSM DB contains a node called "Stukeley Meadows" ( <a href="https://www.openstreetmap.org/browse/node/280778644">https://www.openstreetmap.org/browse/node/280778644</a> ).</p>
<p>This node is tagged as <code>place = suburb</code>, and Nominatim apparently automatically considers all objects in the vicinity of a <code>place</code> node to be part of that place. This is probably a heuristic for cases where there is no poylgon for a place.</p>
<p>In this case, as a Nominatim search for "stukeley meadows" shows, there are two objects named "Stukeley meadows": A node tagged <code>place=suburb</code> (see above), and a polygon ( <a href="https://www.openstreetmap.org/browse/way/112836767">https://www.openstreetmap.org/browse/way/112836767</a> ). The latter is probably the polygon you made.</p>
<p>In this case, I believe the best solution is to delete the place node (as the polygon you made is more precise). Then Nominatim should no longer consider Hartford Road to be in Stukeley Meadows.</p>
<p>And BTW, please fix the capitalization of the name in the tags of your polygon :-).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '11, 16:43</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-5906" class="comments-container">
<span id="5910"></span>
<div id="comment-5910" class="comment">
<div id="post-5910-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks sleske for nominatim link I've not used that before.I've heard nodes are required to get place names rendered. ponzu as raised this problem <a href="http://trac.openstreetmap.org/ticket/3679">http://trac.openstreetmap.org/ticket/3679</a> . ideally the nominatim would not give a radius for a place of some unknown size (to me) maybe adjacient polygons will shut out other suburbs I try that out</p>
</div>
<div id="comment-5910-info" class="comment-info">
<span class="comment-age">(20 Jun '11, 19:22)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-5906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5906-form-container" class="comment-form-container">
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

