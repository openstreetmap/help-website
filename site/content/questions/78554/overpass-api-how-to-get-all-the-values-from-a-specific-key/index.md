+++
type = "question"
title = "Overpass API: how to get all the values from a specific key"
description = '''Hello, I want to get all the shops in London. I tried the query below, but it didn&#x27;t work. Any help please? [out:json]; area[name=&quot;London&quot;]; node&quot;shop&quot;=*; out center; Thank you, Catherine '''
date = "2021-01-27T21:54:00Z"
lastmod = "2021-01-30T23:02:00Z"
weight = 78554
keywords = [ "overpass" ]
aliases = [ "/questions/78554" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: how to get all the values from a specific key](/questions/78554/overpass-api-how-to-get-all-the-values-from-a-specific-key)

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
<span id="post-78554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78554-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I want to get all the shops in London. I tried the query below, but it didn't work. Any help please?</p>
<p>[out:json]; area[name="London"]; node<a href="area">"shop"=*</a>; out center;</p>
<p>Thank you, Catherine</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jan '21, 21:54</strong></p>
<img src="https://secure.gravatar.com/avatar/78ca4faede71449fd93c1790b87d816d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Katerina_Kourou&#39;s gravatar image" />
<p><span>Katerina_Kourou</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Katerina_Kourou has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78554" class="comments-container">
&#10;</div>
<div id="comment-tools-78554" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78554-form-container" class="comment-form-container">
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

<span id="78556"></span>

<div id="answer-container-78556" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78556-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a few ways to do this, but behind the scenes they do essentially the same job. Note 'node' won't return all shops so I used 'nwr' (nodes/ways/relations) I use:</p>
<pre><code>rel[boundary][name=&quot;Greater London&quot;];
map_to_area;
nwr(area)[shop=car];
out meta center;</code></pre>
<p>shop on its own returns 20mb of data so I restricted it to car shops in this example.</p>
<p>If you want to display the boundary use this:</p>
<pre><code>rel[boundary][name=&quot;Greater London&quot;]-&gt;.LDN;
.LDN map_to_area;
nwr(area)[shop=car];
out meta center;
way(r.LDN);
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '21, 23:27</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jan '21, 23:28</strong> </span></p>
</div>
</div>
<div id="comments-container-78556" class="comments-container">
<span id="78560"></span>
<div id="comment-78560" class="comment">
<div id="post-78560-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Dave. I want though a way to get not only the category "car", but all the categories that are included in the shop. E.g. Supermarket+car+clothes etc..Eveything! Any way to do that please?</p>
</div>
<div id="comment-78560-info" class="comment-info">
<span class="comment-age">(28 Jan '21, 08:05)</span> <span class="comment-user userinfo">Katerina_Kourou</span>
</div>
</div>
<span id="78603"></span>
<div id="comment-78603" class="comment">
<div id="post-78603-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Remove '=car' There's a fair bit of info on the wiki such as this page: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example</a></p>
</div>
<div id="comment-78603-info" class="comment-info">
<span class="comment-age">(30 Jan '21, 23:02)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-78556" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78556-form-container" class="comment-form-container">
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

