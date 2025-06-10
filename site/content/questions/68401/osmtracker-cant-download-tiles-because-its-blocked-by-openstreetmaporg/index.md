+++
type = "question"
title = "osmtracker can&#x27;t download tiles because it&#x27;s blocked by openstreetmap.org"
description = '''Around 2 March 2019, OSMtracker for Android stopped displaying background maps, as reported by various users on Github. One user explains that the problem is caused by openstreetmap.org blocking tile download requests with the agent string &quot;osmdroid&quot;. This can be verified as follows: $ wget https://...'''
date = "2019-03-17T12:23:00Z"
lastmod = "2019-04-21T17:35:00Z"
weight = 68401
keywords = [ "osmtracker", "osmdroid", "denied" ]
aliases = [ "/questions/68401" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmtracker can't download tiles because it's blocked by openstreetmap.org](/questions/68401/osmtracker-cant-download-tiles-because-its-blocked-by-openstreetmaporg)

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
<span id="post-68401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68401-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Around 2 March 2019, OSMtracker for Android stopped displaying background maps, as <a href="https://github.com/labexp/osmtracker-android/issues/194">reported by various users on Github</a>.</p>
<p>One user explains that the problem is caused by openstreetmap.org blocking tile download requests with the agent string "osmdroid". This can be verified as follows:</p>
<pre><code>$ wget https://b.tile.openstreetmap.org/12/1206/1539.png
2019-03-17 13:20:31 (7.90 KB/s) - ‘1539.png’ saved [40312/40312]
&#10;$ wget -U zzzzzzzz https://b.tile.openstreetmap.org/12/1206/1540.png
2019-03-17 13:20:58 (7.89 KB/s) - ‘1539.png.1’ saved [40312/40312]
&#10;$ wget -U osmdroid https://b.tile.openstreetmap.org/12/1206/1540.png
2019-03-17 13:21:17 ERROR 403: Forbidden.</code></pre>
<p>Can this be fixed? (Either by unblocking osmdroid on the server, or by changing the user agent string used by OSMtracker)?</p>
<p>EDIT: Ok, SomeoneElse's answer led me to more information. The server <a href="https://github.com/openstreetmap/chef/commit/bb8fbb886ef77d0e23f675966342c10d1d603e00">block was on purpose</a> because the server is overwhelmed by requests naming user-agent "osmdroid". This is contrary to policy. The policy is that apps are supposed to set their own user-agent. However, the policy wasn't enforced for many years, allowing apps like osmtracker to work fine despite violating the policy, until now. More threads about it: <a href="https://github.com/openstreetmap/operations/issues/281">1</a> <a href="https://github.com/osmdroid/osmdroid/issues/1288">2</a> <a href="https://github.com/osmdroid/osmdroid/issues/1286">3</a>. So it looks like we need an OSMtracker app developer to fix it...the remaining question is simply how to make that happen?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmtracker" rel="tag" title="see questions tagged &#39;osmtracker&#39;">osmtracker</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-denied" rel="tag" title="see questions tagged &#39;denied&#39;">denied</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Mar '19, 12:23</strong></p>
<img src="https://secure.gravatar.com/avatar/6ad28c56201340399ec9c944dca247c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Krubo&#39;s gravatar image" />
<p><span>Krubo</span><br />
<span class="score" title="116 reputation points">116</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Krubo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Mar '19, 17:29</strong> </span></p>
</div>
</div>
<div id="comments-container-68401" class="comments-container">
<span id="68870"></span>
<div id="comment-68870" class="comment">
<div id="post-68870-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for this information. I have submitted a <a href="https://github.com/labexp/osmtracker-android/pull/203">Pull Request</a> that fix the problem. I hope this could get into the app soon.</p>
</div>
<div id="comment-68870-info" class="comment-info">
<span class="comment-age">(21 Apr '19, 17:35)</span> <span class="comment-user userinfo">elotrojames</span>
</div>
</div>
</div>
<div id="comment-tools-68401" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68401-form-container" class="comment-form-container">
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

<span id="68402"></span>

<div id="answer-container-68402" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68402-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looks like a bug in the app to me (actually, it looks like they aren't following the tile usage policy). I've commented on the github issue in the osmtracker repository.</p>
<p>Edit following extra info in question:</p>
<blockquote>
<p>So it looks like we need an OSMtracker app developer to fix it...the remaining question is simply how to make that happen?</p>
</blockquote>
<p><a href="https://github.com/osmdroid/osmdroid/issues/1286">This</a> github issue has contributions from an OSM server admin, a developer of the library and the developer of the app. All of these people are likely volunteers. OSMtracker is a free app and Osmdroid is a free library. Why, exactly, should the people involved drop everything to resolve your problem? I'm sure it'll get resolved as soon as the people involved can fit it in to their real-world schedules.</p>
<p>For the avoidance of doubt - OSM data is free (subject to licence), but its servers are not. Neither Osmdroid nor OSMtracker are OSM "products" - both are developed by third parties and are entirely unrelated to OpenStreetMap itself, except that they try and make use of OSM's servers for free.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '19, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Mar '19, 18:40</strong> </span></p>
</div>
</div>
<div id="comments-container-68402" class="comments-container">
<span id="68456"></span>
<div id="comment-68456" class="comment">
<div id="post-68456-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't mean to sound demanding; I'm just a volunteer too, using osmtracker to contribute to the main map. I assume you're a volunteer as well. I appreciate that a lot of skilled volunteer work is going into that <a href="https://github.com/osmdroid/osmdroid/issues/1286">osmdroid issue</a>. I hope the downstream <a href="https://github.com/labexp/osmtracker-android/issues/194">osmtracker issue</a> will get solved afterwards.</p>
</div>
<div id="comment-68456-info" class="comment-info">
<span class="comment-age">(21 Mar '19, 19:25)</span> <span class="comment-user userinfo">Krubo</span>
</div>
</div>
<span id="68457"></span>
<div id="comment-68457" class="comment">
<div id="post-68457-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15871/krubo">@Krubo</a> being a volunteer gives you no additional rights to ask or tell other people how they should spend their spare time. If it is important to you then, then the ways to "make it happen" are: a) do it yourself; or b) pay someone to do it for you.</p>
</div>
<div id="comment-68457-info" class="comment-info">
<span class="comment-age">(22 Mar '19, 11:33)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68402" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68402-form-container" class="comment-form-container">
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

