+++
type = "question"
title = "Overpass API: Error for every request"
description = '''I want to run the following request: (area[&quot;name&quot;=&quot;Stuttgart&quot;];)-&amp;gt;.a; (  way.a[&quot;bicycle&quot;=&quot;no&quot;]; ); out geom; I get all the time the error: &quot;Error: runtime error: […] Another request from your IP is still running.&quot; I tried it also with sample requests from the Overpass API wiki page, but no differ...'''
date = "2015-11-06T19:11:00Z"
lastmod = "2015-11-06T21:01:00Z"
weight = 46438
keywords = [ "overpass" ]
aliases = [ "/questions/46438" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: Error for every request](/questions/46438/overpass-api-error-for-every-request)

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
<span id="post-46438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46438-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to run the following request:</p>
<p>(area["name"="Stuttgart"];)-&gt;.a; ( way.a["bicycle"="no"]; ); out geom;</p>
<p>I get all the time the error: "Error: runtime error: […] Another request from your IP is still running."</p>
<p>I tried it also with sample requests from the Overpass API wiki page, but no difference. I have nothing running what uses overpass, so what could be the problem?</p>
<p>Thanks for answer.</p>
<p>Paulest</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Nov '15, 19:11</strong></p>
<img src="https://secure.gravatar.com/avatar/51643a0be1088fbb07f48504489a2600?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paulest&#39;s gravatar image" />
<p><span>Paulest</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paulest has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46438" class="comments-container">
&#10;</div>
<div id="comment-tools-46438" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46438-form-container" class="comment-form-container">
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

<span id="46439"></span>

<div id="answer-container-46439" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46439-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your current query doesn't take the "Stuttgart" area into account. I'd suggest to try this alternative:</p>
<pre><code>area[&quot;name&quot;=&quot;Stuttgart&quot;]-&gt;.a; 
way(area.a)[&quot;bicycle&quot;=&quot;no&quot;];
out geom;</code></pre>
<p>Overpass Turbo link: <a href="http://overpass-turbo.eu/s/cw2">http://overpass-turbo.eu/s/cw2</a></p>
<p>Another option to get to this query is to use overpass turbo wizard and enter <code>bicycle=no in Stuttgart</code> in the wizard popup.</p>
<p>Besides, there are already a few reports out there with the same error message you're seeing:</p>
<ul>
<li><a href="https://github.com/drolbr/Overpass-API/issues/229">https://github.com/drolbr/Overpass-API/issues/229</a></li>
<li><a href="https://github.com/tyrasd/overpass-turbo/issues/213">https://github.com/tyrasd/overpass-turbo/issues/213</a></li>
</ul>
<p>If you're affected by this, please either add a comment to this post or one of the GitHub tickets. It's always worth trying another Overpass API instance, like the rambler.ru instance. That's in overpass turbo -&gt; Settings -&gt; Server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '15, 19:54</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Nov '15, 16:02</strong> </span></p>
</div>
</div>
<div id="comments-container-46439" class="comments-container">
<span id="46440"></span>
<div id="comment-46440" class="comment">
<div id="post-46440-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Same error...</p>
<p>I don't know what is the problem, I think the server has problems with IPv6...</p>
</div>
<div id="comment-46440-info" class="comment-info">
<span class="comment-age">(06 Nov '15, 20:59)</span> <span class="comment-user userinfo">Paulest</span>
</div>
</div>
<span id="46441"></span>
<div id="comment-46441" class="comment">
<div id="post-46441-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Vielleicht funktioniert auch der Tunnel von hier nicht ordentlich, also meine IPv6 wird nicht gut genug in IPv4 umgesetzt?</p>
</div>
<div id="comment-46441-info" class="comment-info">
<span class="comment-age">(06 Nov '15, 21:01)</span> <span class="comment-user userinfo">Paulest</span>
</div>
</div>
</div>
<div id="comment-tools-46439" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46439-form-container" class="comment-form-container">
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

