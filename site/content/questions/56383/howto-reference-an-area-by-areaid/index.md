+++
type = "question"
title = "howto reference an area by area:id"
description = '''I have a query for administrative regions within a bbox which looks like this: [out:json]; rel[&quot;boundary&quot;=&quot;administrative&quot;] (48.64136, 9.22671, 48.74122, 9.41370); out; ... and it works like expected. Now, at a later time I want to get a street-map for one of the administrative areas with another qu...'''
date = "2017-05-30T15:05:00Z"
lastmod = "2017-05-31T11:45:00Z"
weight = 56383
keywords = [ "overpass", "query", "id", "area" ]
aliases = [ "/questions/56383" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [howto reference an area by area:id](/questions/56383/howto-reference-an-area-by-areaid)

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
<span id="post-56383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56383-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a query for administrative regions within a bbox which looks like this:</p>
<p><strong>[out:json]; rel["boundary"="administrative"] (48.64136, 9.22671, 48.74122, 9.41370); out;</strong></p>
<p>... and it works like expected. Now, <strong>at a later time</strong> I want to get a street-map for one of the administrative areas with <strong>another</strong> query:</p>
<p><strong>[out:json][timeout:60]; way(area:3605732220)["highway"]["highway"!~"motorway"]["name"]; out;</strong></p>
<p>... where in e.g. the id returned for the boundary relation was "5732220" ("Berkheim" part of "Esslingen am Neckar") and I added 3600000000. However this does not seem to work and the query just times out. What am I doing wrong ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '17, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/f9e61182ebcd9d06405e298a8057c945?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cssdata&#39;s gravatar image" />
<p><span>cssdata</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cssdata has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56383" class="comments-container">
<span id="56384"></span>
<div id="comment-56384" class="comment">
<div id="post-56384-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you try to increase the timeout?</p>
</div>
<div id="comment-56384-info" class="comment-info">
<span class="comment-age">(30 May '17, 15:51)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="56385"></span>
<div id="comment-56385" class="comment">
<div id="post-56385-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I did.</p>
</div>
<div id="comment-56385-info" class="comment-info">
<span class="comment-age">(30 May '17, 17:31)</span> <span class="comment-user userinfo">cssdata</span>
</div>
</div>
<span id="56389"></span>
<div id="comment-56389" class="comment">
<div id="post-56389-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Really? Increasing the timeout works for me and the query returns after around 90 seconds.</p>
</div>
<div id="comment-56389-info" class="comment-info">
<span class="comment-age">(31 May '17, 09:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="56391"></span>
<div id="comment-56391" class="comment">
<div id="post-56391-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Upps, in fact I increased to 240 and the query returned with the expected result! Thank you! Any idea why it takes so long? I don't wana put unneccessary load on the servers. Is there a faster way to do this?</p>
</div>
<div id="comment-56391-info" class="comment-info">
<span class="comment-age">(31 May '17, 11:38)</span> <span class="comment-user userinfo">cssdata</span>
</div>
</div>
<span id="56392"></span>
<div id="comment-56392" class="comment">
<div id="post-56392-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What I forgot to mention: In desperate attempt to get something to work I executed the following:</p>
<p>area["boundary"="administrative"][name="Berkheim"]((48.64136, 9.22671, 48.74122, 9.41370)-&gt;.a;</p>
<p>way(area.a)["highway"]["highway"!~"motorway"]["name"];</p>
<p>( ._; &gt;; );</p>
<p>out;</p>
<p>And this returned a lot faster! However, it also returned ways form all "Berkheim(s)" even those outside the bbox. ... Very confusing! Again, thanks!</p>
</div>
<div id="comment-56392-info" class="comment-info">
<span class="comment-age">(31 May '17, 11:45)</span> <span class="comment-user userinfo">cssdata</span>
</div>
</div>
</div>
<div id="comment-tools-56383" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56383-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

