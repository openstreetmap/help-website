+++
type = "question"
title = "Problem with relation roles"
description = '''I recently added a reservoir to OSM. It is at : https://www.openstreetmap.org/#map=14/18.8371/99.6444&amp;amp;layers=C I went overboard when I traced it from Bing and used about 4,000 nodes, too big to upload as I later learned.(JOSM tells me 2,000 nodes is max per relation). Not wanting to waste any of ...'''
date = "2013-10-11T02:58:00Z"
lastmod = "2013-10-11T12:26:00Z"
weight = 27086
keywords = [ "josm", "relations", "roles" ]
aliases = [ "/questions/27086" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with relation roles](/questions/27086/problem-with-relation-roles)

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
<span id="post-27086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27086-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently added a reservoir to OSM. It is at : <a href="https://www.openstreetmap.org/#map=14/18.8371/99.6444&amp;layers=C">https://www.openstreetmap.org/#map=14/18.8371/99.6444&amp;layers=C</a></p>
<p>I went overboard when I traced it from Bing and used about 4,000 nodes, too big to upload as I later learned.(JOSM tells me 2,000 nodes is max per relation). Not wanting to waste any of my work, I split it into two separate pieces. Both pieces are inner members of a much larger wood multi-polygon. I know I did not do this right because islands in the reservoir (such as <a href="https://www.openstreetmap.org/browse/way/240923279">this one</a>) are also inner members of the same wood polygon and they do not show up in the OSM slippy map.</p>
<p>Relations are tricky and I admit to being a novice with them. Aside from making a commitment to never trace in such detail in the future, how can I fix this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-roles" rel="tag" title="see questions tagged &#39;roles&#39;">roles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Oct '13, 02:58</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '13, 08:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-27086" class="comments-container">
&#10;</div>
<div id="comment-tools-27086" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27086-form-container" class="comment-form-container">
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

<span id="27087"></span>

<div id="answer-container-27087" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27087-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I note at this page <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">see 'Island within a hole'</a> that the islands probably need to be role="outer" You may need to add a landuse= tag to the islands to get them to appear.</p>
<p>In regard to the 2000 node limit: My understanding is that instead of one way with 4000 nodes, you just split up the way into smaller segments &lt; 2000 each and then combine the separate ways in a relation to make one really big polygon. After creating all your polygons, then you would select all your polygons and click create multi-polygon and give them roles. I am still reluctantly learning about these complexities so someone else may need to correct this if necessary.<br />
</p>
<p>I am interested in how you managed to do such a big and detailed trace - 4000 clicks is certainly an effort worthy of a special tag in this forum especially if done one click at a time.</p>
<p>Did you use <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Lakewalker">Lakewalker</a> which seems not active from this note on the page "Lakewalker is no longer actively developed and is considered 'dead' Use Scanaerial instead." or did you use <a href="https://wiki.openstreetmap.org/wiki/Scanaerial">Scanaerial</a></p>
<p>I am not familiar with either but I am thinking of giving them a run with a creek in my area if the images available define the water body well enough.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Oct '13, 06:06</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '13, 07:20</strong> </span></p>
</div>
</div>
<div id="comments-container-27087" class="comments-container">
<span id="27088"></span>
<div id="comment-27088" class="comment">
<div id="post-27088-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I would probably have done it as two multipolygons. One for the large wood, with the reservoir ways as role inner (but untagged), and one for the reservoir (ways as outer, tags on relation) with the islands as inner holes of the reservoir (with tags on the island ways as they are now). So reservoir is a hole in wood, and the islands are holes in the reservoir, if that makes sense?</p>
</div>
<div id="comment-27088-info" class="comment-info">
<span class="comment-age">(11 Oct '13, 09:38)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="27089"></span>
<div id="comment-27089" class="comment">
<div id="post-27089-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm still confused.</p>
<p>Adding some new information, and almost making matters worse, is the fact that a fresh download of a Garmin compatible map from Lambertus does show the one island I mapped as a member of wood polygon with role=inner. So why does it not show in the slippy maps?</p>
<p>nevw, I hand traced the entire damn thing. Don't ask me why. I worked on it for a while, took a dinner break, came back and finished it. Crazy.</p>
<p>Ed, I don't understand the difference between tagging the relation vs tagging the object as regards rendering.</p>
<p>I might fool with the "two separate ways" idea later.</p>
</div>
<div id="comment-27089-info" class="comment-info">
<span class="comment-age">(11 Oct '13, 12:26)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-27087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27087-form-container" class="comment-form-container">
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

