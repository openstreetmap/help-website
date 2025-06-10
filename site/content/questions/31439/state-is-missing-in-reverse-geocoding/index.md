+++
type = "question"
title = "state is missing in reverse geocoding"
description = '''Hi, I installed a local Nominatim server, including TIGER data. In some reverse-geocoding queries for locations in the US, I&#x27;m not getting back the state.  For example, for the following query, I get a similar result on my local server, minus the state: http://nominatim.openstreetmap.org/reverse?lat...'''
date = "2014-03-11T09:45:00Z"
lastmod = "2019-04-02T10:05:00Z"
weight = 31439
keywords = [ "reversegeocoding", "reversegeolocation", "nominatim", "state" ]
aliases = [ "/questions/31439" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [state is missing in reverse geocoding](/questions/31439/state-is-missing-in-reverse-geocoding)

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
<span id="post-31439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31439-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I installed a local Nominatim server, including TIGER data.</p>
<p>In some reverse-geocoding queries for locations in the US, I'm not getting back the state.</p>
<p>For example, for the following query, I get a similar result on my local server, minus the state:</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?lat=25.760901249584499&amp;lon=-80.145328467942463">http://nominatim.openstreetmap.org/reverse?lat=25.760901249584499&amp;lon=-80.145328467942463</a></p>
<p>Does anyone know what could be the reason for this?</p>
<p>Thanks, Raz</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-reversegeolocation" rel="tag" title="see questions tagged &#39;reversegeolocation&#39;">reversegeolocation</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-state" rel="tag" title="see questions tagged &#39;state&#39;">state</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Mar '14, 09:45</strong></p>
<img src="https://secure.gravatar.com/avatar/84ebb95a07dd884e34f0170b07b1d652?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RazAlon&#39;s gravatar image" />
<p><span>RazAlon</span><br />
<span class="score" title="61 reputation points">61</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RazAlon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31439" class="comments-container">
<span id="31443"></span>
<div id="comment-31443" class="comment">
<div id="post-31443-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Did you import the entire planet or a US extract only?</p>
</div>
<div id="comment-31443-info" class="comment-info">
<span class="comment-age">(11 Mar '14, 12:48)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="31444"></span>
<div id="comment-31444" class="comment">
<div id="post-31444-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>the entire planet, the file is from early January 2014</p>
</div>
<div id="comment-31444-info" class="comment-info">
<span class="comment-age">(11 Mar '14, 13:46)</span> <span class="comment-user userinfo">RazAlon</span>
</div>
</div>
<span id="68604"></span>
<div id="comment-68604" class="comment">
<div id="post-68604-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2921/lonvia">@lonvia</a> does it matter whether one import the whole planet or only a particular country please? I'm struggling with same problem</p>
</div>
<div id="comment-68604-info" class="comment-info">
<span class="comment-age">(02 Apr '19, 10:05)</span> <span class="comment-user userinfo">Yura</span>
</div>
</div>
</div>
<div id="comment-tools-31439" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31439-form-container" class="comment-form-container">
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

<span id="31462"></span>

<div id="answer-container-31462" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31462-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-31462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RazAlon has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Florida relation was broken in early January. It has been fixed in the meantime but you still caught the bad version with your import, so the boundary for Florida is missing. Here is a way to update your database for such broken objects without a reimport:</p>
<ol>
<li><p>Import the latest version of the object in question. You need to find the OSM type and id of the object, for example by searching on osm.org. Florida is <a href="http://www.openstreetmap.org/relation/162050">here</a>. For the import, the update script can be used, i.e</p>
<pre><code>./utils/update.php --import-relation 162050 --index</code></pre></li>
<li><p>Check that the import worked by searching for the object in your local instance. If it didn't work, the object might still be broken and you have to fix it in OSM first. Find out the place_id of the object by looking up details in your instance. For example, Florida on the osm.org instance is <a href="http://nominatim.openstreetmap.org/details.php?place_id=97976186">here</a>, so the place_id is 97976186. The ids are different for every instance.</p></li>
<li><p>Update any places in your database that depend on the object, e.g. for Florida again:</p>
<pre><code> psql -d nominatim -c &#39;select place_force_update(97976186)&#39;
 ./utils/update.php --index --index-instances 2</code></pre>
<p>Be warned that this may take a long time for an area as large as Florida.</p></li>
</ol>
<p>If you run updates on your database, (1) will happen automatically. Dependent places, however, will not be updated for larger areas for performance reasons, so you may still want to do (2) and (3).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '14, 22:50</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-31462" class="comments-container">
<span id="31472"></span>
<div id="comment-31472" class="comment">
<div id="post-31472-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you, that explains about 93% of my missing states. I do see the same problem in other states too, for example Kansas:</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?lat=39.062966597302903&amp;lon=-94.608148997737700">http://nominatim.openstreetmap.org/reverse?lat=39.062966597302903&amp;lon=-94.608148997737700</a></p>
<p>Are there any other general known problems? Thanks, Raz</p>
</div>
<div id="comment-31472-info" class="comment-info">
<span class="comment-age">(12 Mar '14, 09:19)</span> <span class="comment-user userinfo">RazAlon</span>
</div>
</div>
<span id="31474"></span>
<div id="comment-31474" class="comment">
<div id="post-31474-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The Kansas example is a road that goes over the state boundary and clearly has a problem with that (after reindexing, it's visible on osm.org, too). That is a bug worth reporting.</p>
</div>
<div id="comment-31474-info" class="comment-info">
<span class="comment-age">(12 Mar '14, 09:44)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="31775"></span>
<div id="comment-31775" class="comment">
<div id="post-31775-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks, I reported it on github</p>
</div>
<div id="comment-31775-info" class="comment-info">
<span class="comment-age">(23 Mar '14, 10:52)</span> <span class="comment-user userinfo">RazAlon</span>
</div>
</div>
</div>
<div id="comment-tools-31462" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31462-form-container" class="comment-form-container">
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

