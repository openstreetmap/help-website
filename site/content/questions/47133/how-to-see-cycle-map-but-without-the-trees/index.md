+++
type = "question"
title = "how to see cycle map but without the trees?"
description = ''' I am just the most basic simple user. I am browsing https://www.openstreetmap.org/#map=16/24.1612/120.8197&amp;amp;layers=C I can&#x27;t read the map due to the trees blocking the view. If I could remove the trees, then I could see the elevation lines. Those are what I want to see. I just want to look at th...'''
date = "2015-12-13T12:45:00Z"
lastmod = "2015-12-13T22:08:00Z"
weight = 47133
keywords = [ "elevation", "layer", "opencyclemap", "trees" ]
aliases = [ "/questions/47133" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [how to see cycle map but without the trees?](/questions/47133/how-to-see-cycle-map-but-without-the-trees)

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
<span id="post-47133-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47133-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47133-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<ol>
<li>I am just the most basic simple user.</li>
<li>I am browsing <a href="https://www.openstreetmap.org/#map=16/24.1612/120.8197&amp;layers=C">https://www.openstreetmap.org/#map=16/24.1612/120.8197&amp;layers=C</a></li>
<li>I can't read the map due to the trees blocking the view.</li>
<li>If I could remove the trees, then I could see the elevation lines. Those are what I want to see.</li>
<li>I just want to look at this one <a href="https://www.openstreetmap.org/#map=16/24.1612/120.8197&amp;layers=C">https://www.openstreetmap.org/#map=16/24.1612/120.8197&amp;layers=C</a> once, but without those trees.</li>
<li>I don't want to look at a different layer. I want to see this layer, but without the trees.</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-elevation" rel="tag" title="see questions tagged &#39;elevation&#39;">elevation</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-opencyclemap" rel="tag" title="see questions tagged &#39;opencyclemap&#39;">opencyclemap</span> <span class="post-tag tag-link-trees" rel="tag" title="see questions tagged &#39;trees&#39;">trees</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '15, 12:45</strong></p>
<img src="https://secure.gravatar.com/avatar/47edd1ee4d973c50bbe7991bb063d09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jidanni&#39;s gravatar image" />
<p><span>jidanni</span><br />
<span class="score" title="339 reputation points">339</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jidanni has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47133" class="comments-container">
&#10;</div>
<div id="comment-tools-47133" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47133-form-container" class="comment-form-container">
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

<span id="47134"></span>

<div id="answer-container-47134" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47134-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "layers" that you can see on openstreetmap.org are images built from individual bitmaps aka "tiles", there is no simple way to remove features from these bitmaps after they have been generated.</p>
<p>The rules that turn OSM data (typically already processed in one way or another) in to bitmaps are called "styles". So what you want is a style without forests or a style with more visible contours. If you are not happy with one of the many many ready made maps generated from OSM data (see <a href="https://wiki.openstreetmap.org/wiki/List_of_OSM-based_services">https://wiki.openstreetmap.org/wiki/List_of_OSM-based_services</a> for some of them) then you will have to produce one yourself, see for example: <a href="https://switch2osm.org/">https://switch2osm.org/</a> and other similar questions on this site.</p>
<p>For the pundits: yes, vector tiles could address the issue this to a certain point, however would still require a mechanism to change the style on the fly or for the user to provide a custom version.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '15, 13:18</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Dec '15, 22:13</strong> </span></p>
</div>
</div>
<div id="comments-container-47134" class="comments-container">
&#10;</div>
<div id="comment-tools-47134" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47134-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47141"></span>

<div id="answer-container-47141" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47141-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have you tried using Garmin Basecamp (free download). You will also have to download a map see:- OSM on Garmin. Some of these maps may show what you need, The level of detail can be also be varied through 7 levels in Basecamp. If you have a Garmin on your bike they often have map settings that also vari detail. My Garmin Nuvi 1310 car sat nav will also display an OSM .img file but I'd need an extra power supply for more than 2 hours use. It is also possible to build your own Garmin map with Mkg Map and to choose the map style there are type files and editors to style and re-stile them... i haven't tried the latter yet but i hope to soon as i want simple clear map that shows the footpaths clearly on mainly white map that contrasts well and will print without using too much ink.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '15, 21:57</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-47141" class="comments-container">
<span id="47142"></span>
<div id="comment-47142" class="comment">
<div id="post-47142-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://www8.garmin.com/learningcenter/training/basecamp/">http://www8.garmin.com/learningcenter/training/basecamp/</a></p>
</div>
<div id="comment-47142-info" class="comment-info">
<span class="comment-age">(13 Dec '15, 22:01)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="47143"></span>
<div id="comment-47143" class="comment">
<div id="post-47143-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://wiki.openstreetmap.org/wiki/OSM_Map_On_Garmin">https://wiki.openstreetmap.org/wiki/OSM_Map_On_Garmin</a></p>
</div>
<div id="comment-47143-info" class="comment-info">
<span class="comment-age">(13 Dec '15, 22:04)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="47144"></span>
<div id="comment-47144" class="comment">
<div id="post-47144-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://www.openfietsmap.nl/tips-tricks/customize">http://www.openfietsmap.nl/tips-tricks/customize</a></p>
</div>
<div id="comment-47144-info" class="comment-info">
<span class="comment-age">(13 Dec '15, 22:06)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="47145"></span>
<div id="comment-47145" class="comment">
<div id="post-47145-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://wiki.openstreetmap.org/wiki/Mkgmap/help/TYP_files">https://wiki.openstreetmap.org/wiki/Mkgmap/help/TYP_files</a></p>
</div>
<div id="comment-47145-info" class="comment-info">
<span class="comment-age">(13 Dec '15, 22:07)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="47146"></span>
<div id="comment-47146" class="comment">
<div id="post-47146-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://pinns.co.uk/osm/ostyp.html">http://pinns.co.uk/osm/ostyp.html</a></p>
</div>
<div id="comment-47146-info" class="comment-info">
<span class="comment-age">(13 Dec '15, 22:08)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-47141" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47141-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47135"></span>

<div id="answer-container-47135" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47135-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-47135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi did you read these pages, <a href="https://wiki.openstreetmap.org/wiki/Cycle_routes">https://wiki.openstreetmap.org/wiki/Cycle_routes</a> with a lot of links to already made selections. Use the Garmin maps based on OSM or follow this link to <a href="http://www.openfietsmap.nl/">http://www.openfietsmap.nl/</a> Im not shure if it is what your looking for, but other bicyclist use them frequently.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '15, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-47135" class="comments-container">
&#10;</div>
<div id="comment-tools-47135" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47135-form-container" class="comment-form-container">
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

