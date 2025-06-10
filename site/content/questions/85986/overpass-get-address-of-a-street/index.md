+++
type = "question"
title = "Overpass: get address of a street"
description = '''Hi, I need to get all the addresses (buildings) of a street. I currently have a query that gets me all the streets in an area: [out:json][timeout:2500]; {{geocodeArea:Rome}}-&amp;gt;.searchArea; (  way[&quot;highway&quot;]&quot;name&quot;; ); for (t[&quot;name&quot;]) {  make street name=_.val;  out; }. But I can&#x27;t get the data for ...'''
date = "2022-10-25T10:51:00Z"
lastmod = "2022-10-25T11:05:00Z"
weight = 85986
keywords = [ "overpass-turbo", "address" ]
aliases = [ "/questions/85986" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass: get address of a street](/questions/85986/overpass-get-address-of-a-street)

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
<span id="post-85986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85986-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I need to get all the addresses (buildings) of a street.</p>
<p>I currently have a query that gets me all the streets in an area:</p>
<p>[out:json][timeout:2500]; {{geocodeArea:Rome}}-&gt;.searchArea; ( way["highway"]<a href="area.searchArea">"name"</a>; ); for (t["name"]) { make street name=_.val; out; }.</p>
<p>But I can't get the data for each building on those streets.</p>
<p>Can you help me?</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '22, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a21354b1e350f21c55949d93e8bf0f9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pelioro&#39;s gravatar image" />
<p><span>Pelioro</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pelioro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85986" class="comments-container">
<span id="85987"></span>
<div id="comment-85987" class="comment">
<div id="post-85987-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please don't duplicate posts. Publish a routine that you've used &amp; works.</p>
</div>
<div id="comment-85987-info" class="comment-info">
<span class="comment-age">(25 Oct '22, 11:05)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-85986" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85986-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

