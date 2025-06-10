+++
type = "question"
title = "Set longitude and latitude of a node"
description = '''I&#x27;m looking for an easy way to directly set the longitude and latitude of a node. The best would be a &quot;copy-paste&quot; of both longitude and latitude. The editor doesn&#x27;t matter. I thought this would be a build-in feature in JOSM but seems not (I may be blind though). So at this moment, all I have found ...'''
date = "2020-07-10T11:01:00Z"
lastmod = "2020-07-10T13:23:00Z"
weight = 75633
keywords = [ "latitude", "josm", "nodes", "longitude" ]
aliases = [ "/questions/75633" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Set longitude and latitude of a node](/questions/75633/set-longitude-and-latitude-of-a-node)

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
<span id="post-75633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75633-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for an easy way to directly set the longitude and latitude of a node. The best would be a "copy-paste" of both longitude and latitude. The editor doesn't matter. I thought this would be a build-in feature in JOSM but seems not (I may be blind though).</p>
<p>So at this moment, all I have found to set the position of a node using JOSM is:</p>
<ol>
<li>Download the node. Download as few as possible data to make your life easier !</li>
<li>Move the node somewhere, position doesn't matter,</li>
<li>Save the data layer as "my_file.osm",</li>
<li>Open "my_file.osm" with a text editor and find your node there (e.g. by ID). If you're flooded by text you downloaded too much data :3</li>
<li>Change the "lat" and "lon" values of the node and save the file,</li>
<li>Open "my_file.osm" on JOSM. Now you can publish your changes. This just took you 1 hour :D</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '20, 11:01</strong></p>
<img src="https://secure.gravatar.com/avatar/c0172bdf1daad257d68989757bcfa6a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zatiranyk&#39;s gravatar image" />
<p><span>zatiranyk</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zatiranyk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jul '20, 11:35</strong> </span></p>
</div>
</div>
<div id="comments-container-75633" class="comments-container">
<span id="75640"></span>
<div id="comment-75640" class="comment">
<div id="post-75640-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>FWIW if you're overwhelmed by reams of xml you can also create another layer and selectively merge across only the elements that interest you. If you are modifying existing nodes you may also need to manually set <code>action='modify'</code> if you haven't edited any tags.</p>
</div>
<div id="comment-75640-info" class="comment-info">
<span class="comment-age">(10 Jul '20, 13:23)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-75633" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75633-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="75634"></span>

<div id="answer-container-75634" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75634-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-75634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="zatiranyk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For new nodes in JOSM:</p>
<ul>
<li>Tools -&gt; Add Node (<em>Shift</em>+*D)</li>
</ul>
<p>To move an existing node:</p>
<ul>
<li>Tools -&gt; Move Node</li>
</ul>
<p>Both of these require expert mode.</p>
<p>Alternately, if you add a new node then merge an existing node to it it should keep the history of the old node.</p>
<p>This should also be fairly trivial in the <a href="https://wiki.openstreetmap.org/wiki/Level0">Level0</a> editor.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '20, 12:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jul '20, 12:17</strong> </span></p>
</div>
</div>
<div id="comments-container-75634" class="comments-container">
<span id="75638"></span>
<div id="comment-75638" class="comment">
<div id="post-75638-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So it's confirmed, I'm blind. Thank you :)</p>
</div>
<div id="comment-75638-info" class="comment-info">
<span class="comment-age">(10 Jul '20, 12:52)</span> <span class="comment-user userinfo">zatiranyk</span>
</div>
</div>
<span id="75639"></span>
<div id="comment-75639" class="comment">
<div id="post-75639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Needles in a haystack.</p>
</div>
<div id="comment-75639-info" class="comment-info">
<span class="comment-age">(10 Jul '20, 13:17)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-75634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75634-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75635"></span>

<div id="answer-container-75635" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75635-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another way (still not simple):</p>
<ol>
<li>Tools / Add Node - place a new node at the exact Lat and Lon values</li>
<li>Select the node to be positioned, then shift-select the new node (the order is important)</li>
<li>Select M (or Tools / Merge nodes)</li>
</ol>
<p>The old node will be moved to the new node position and the new node deleted in the merge.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '20, 12:25</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jul '20, 12:25</strong> </span></p>
</div>
</div>
<div id="comments-container-75635" class="comments-container">
&#10;</div>
<div id="comment-tools-75635" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75635-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75636"></span>

<div id="answer-container-75636" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75636-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have just tried dragging a waymark.gpx into the iD window and that works. I have also displayed waymarks with Potlatch2 ..Backgrounds at the botton choose vector file .. browse to waypoint file and load and select it. That mark displays. Potlatch2 can display the cursor co-ords Lat/long just select the feature from the toolbox.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '20, 12:25</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jul '20, 13:07</strong> </span></p>
</div>
</div>
<div id="comments-container-75636" class="comments-container">
&#10;</div>
<div id="comment-tools-75636" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75636-form-container" class="comment-form-container">
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

