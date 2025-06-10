+++
type = "question"
title = "My is Overpass server is running slowly after re-populating the database"
description = '''Hi all,  I have just populated the full planet file into my database (on top of an existing UK database install) and I&#x27;m now having some problems:  Calling an is_in area query does not return any results for any new areas my database should now cover. It still returns the old UK areas however, but t...'''
date = "2014-08-25T14:31:00Z"
lastmod = "2015-03-31T20:42:00Z"
weight = 36152
keywords = [ "overpassapi", "overpass", "private_server", "slow", "error" ]
aliases = [ "/questions/36152" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [My is Overpass server is running slowly after re-populating the database](/questions/36152/my-is-overpass-server-is-running-slowly-after-re-populating-the-database)

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
<span id="post-36152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36152-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I have just populated the full planet file into my database (on top of an existing UK database install) and I'm now having some problems:</p>
<ol>
<li>Calling an <code>is_in</code> area query does not return any results for any new areas my database should now cover. It still returns the old UK areas however, but this leads me onto my second problem (possibly the same problem!)</li>
<li>An <code>is_in</code> area call (in the UK or otherwise) does not return any admin_level 1 or 2 information, like it does on the Overpass API public server. This didn't happen pre-full planet installation but I assumed this was due to only having the UK installed, not multiple countries.</li>
<li>The server now runs really slow! When it was just the UK, the server would process requests in a matter of milliseconds, now, since installing the planet, it takes 4-5 SECONDS to process a request! The RAM usage has escalated from ~75% while idle to ~99%. This happened before to me from populating a full UK install on top of an England only install on a different server. Restarting the server does not help.</li>
</ol>
<p>The planet file I used is <a href="http://ftp.heanet.ie/mirrors/openstreetmap.org/planet/planet-latest.osm.bz2">http://ftp.heanet.ie/mirrors/openstreetmap.org/planet/planet-latest.osm.bz2</a></p>
<p>I am baffled on this one and have no idea how to overcome it besides completely reinstalling the planet database. Is there a better way to solve this? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-private_server" rel="tag" title="see questions tagged &#39;private_server&#39;">private_server</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '14, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/5abb2932327bb97ee8a2abc3c14caa8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmeister4&#39;s gravatar image" />
<p><span>gmeister4</span><br />
<span class="score" title="60 reputation points">60</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmeister4 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Mar '15, 20:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-36152" class="comments-container">
<span id="36153"></span>
<div id="comment-36153" class="comment">
<div id="post-36153-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You didn't mention the Overpass API version you're using and how you're importing the data. Did you see any kind of warning/error message during the import?</p>
<p>Anyway, I'd recommend a fresh start, i.e. dump the current db or use a different db directory for the new import.</p>
</div>
<div id="comment-36153-info" class="comment-info">
<span class="comment-age">(25 Aug '14, 14:50)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="36154"></span>
<div id="comment-36154" class="comment">
<div id="post-36154-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh sorry about that, I'm running version 0.7.4. I downloaded the planet .bz2 then executed the <code>init_osm3s.sh</code> script to build into the same directory of the original database. There were no error messages. I read on the wiki that you should be able to update the DB this way. Was it wrong to merge the database directory into an existing one? I guess this means that this method for updating part of the database is not recommended. All other queries I tested worked apart from the area search. Thanks for the advice!</p>
</div>
<div id="comment-36154-info" class="comment-info">
<span class="comment-age">(25 Aug '14, 15:52)</span> <span class="comment-user userinfo">gmeister4</span>
</div>
</div>
<span id="42084"></span>
<div id="comment-42084" class="comment">
<div id="post-42084-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>judging from the question text of <a href="/questions/36464/">overpass-api-area-query-does-not-recognise-all-areas</a> this particular "slow" problem may be solved. <a href="http://help.openstreetmap.org/users/8446/gmeister4"></a><a href="http://help.openstreetmap.org/users/8446/gmeister4">@gmeister4</a>: Is it? How exactly?</p>
<p>If possible, please focus on one problem per question here on this help site (for more usefulness to other users with similar problems), unless you think that the problems may be due to the same reason, of course.</p>
</div>
<div id="comment-42084-info" class="comment-info">
<span class="comment-age">(31 Mar '15, 20:42)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-36152" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36152-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

