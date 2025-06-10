+++
type = "question"
title = "Nominatim doesn’t find street numbers for Australia"
description = '''I&#x27;ve started developing a project using OpenStreeMaps and asp.net and I would like to show an address on the map using Nominatim search engine. But &quot;Nominatim&quot; doesn’t find street numbers for Australia when I search for an address in https://nominatim.openstreetmap.org/. The question is:  Does the A...'''
date = "2016-03-29T05:34:00Z"
lastmod = "2016-03-31T22:58:00Z"
weight = 48886
keywords = [ "housenumbers", "australia", "completeness" ]
aliases = [ "/questions/48886" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim doesn’t find street numbers for Australia](/questions/48886/nominatim-doesnt-find-street-numbers-for-australia)

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
<span id="post-48886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48886-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've started developing a project using OpenStreeMaps and asp.net and I would like to show an address on the map using Nominatim search engine. But "Nominatim" doesn’t find street numbers for Australia when I search for an address in <a href="https://nominatim.openstreetmap.org/.">https://nominatim.openstreetmap.org/.</a></p>
<p>The question is: Does the Australia.osm extract include the street numbers? In other words, does nominatim.openstreetmap.org use updated australia.osm extract?</p>
<p>Cheers</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-australia" rel="tag" title="see questions tagged &#39;australia&#39;">australia</span> <span class="post-tag tag-link-completeness" rel="tag" title="see questions tagged &#39;completeness&#39;">completeness</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '16, 05:34</strong></p>
<img src="https://secure.gravatar.com/avatar/ac7e4d574ae83f575da27cda31a87d82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Parya&#39;s gravatar image" />
<p><span>Parya</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Parya has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '16, 10:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-48886" class="comments-container">
<span id="48887"></span>
<div id="comment-48887" class="comment">
<div id="post-48887-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Did you verify on osm.org that there is a house number for the house you are looking for ? Perhaps the house numbers are not (or partially) mapped in the area you need</p>
</div>
<div id="comment-48887-info" class="comment-info">
<span class="comment-age">(29 Mar '16, 06:29)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="48888"></span>
<div id="comment-48888" class="comment">
<div id="post-48888-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>thanks for your reply. yes, I tried and as I mentioned it only finds street name not the house number which I'm looking for. for example, searching for "46 Playfield Street, Chermside" only finds playfield street.</p>
</div>
<div id="comment-48888-info" class="comment-info">
<span class="comment-age">(29 Mar '16, 07:38)</span> <span class="comment-user userinfo">Parya</span>
</div>
</div>
<span id="48892"></span>
<div id="comment-48892" class="comment">
<div id="post-48892-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sorry, it was not clear what I meant with "verify" When you go to the map: <a href="http://osm.org/go/ueGiW0SWR--?m=&amp;way=37675697,">http://osm.org/go/ueGiW0SWR--?m=&amp;way=37675697,</a> you'll see that there are no house numbers visible in Playfield Street. A bit to the south-west, around Hamilton Road x Gympie Road you see a couple of house numbers. When you do not see house numbers displayed on this map, Nominatim will not find the house numbers.</p>
<p>There are a few exceptions to that last rule, when Nominatim has loaded an external database with addresses. But those external addresses do not end up in extracts that you can download yourself from e.g. geofrabrik.</p>
</div>
<div id="comment-48892-info" class="comment-info">
<span class="comment-age">(29 Mar '16, 10:48)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-48886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48886-form-container" class="comment-form-container">
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

<span id="48890"></span>

<div id="answer-container-48890" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48890-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>try <em>19 Hutchins Street, Brisbane</em> or <em>123 Evelyn Street, Brisbane</em>. You will notice that Nominatim works there.</p>
<p>Why is this? Because our data is never fully <a href="https://wiki.openstreetmap.org/wiki/Completeness">complete</a>. The house numbers in that area (and those you were searching for) are just not in our data. That means: just nobody has entered them. We are crowd-sourced.</p>
<p>Please have a look at your city and if there are missing house numbers, get outside, walk through the streets and record the housenumbers (e.g. on a printed out map or with an app like <span>KeypadMapper</span> or <span>OSMtracker</span>). At home, you can enter them into our database using one of our editors.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '16, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '16, 10:46</strong> </span></p>
</div>
</div>
<div id="comments-container-48890" class="comments-container">
<span id="48942"></span>
<div id="comment-48942" class="comment">
<div id="post-48942-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the response.</p>
</div>
<div id="comment-48942-info" class="comment-info">
<span class="comment-age">(30 Mar '16, 05:46)</span> <span class="comment-user userinfo">Parya</span>
</div>
</div>
<span id="48983"></span>
<div id="comment-48983" class="comment">
<div id="post-48983-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Complete agree with aseerel4c26's response. But in the mean time if you need complete addressees you can try using GNAF <a href="https://github.com/minus34/gnaf-loader">https://github.com/minus34/gnaf-loader</a></p>
</div>
<div id="comment-48983-info" class="comment-info">
<span class="comment-age">(31 Mar '16, 22:58)</span> <span class="comment-user userinfo">aharvey</span>
</div>
</div>
</div>
<div id="comment-tools-48890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48890-form-container" class="comment-form-container">
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

