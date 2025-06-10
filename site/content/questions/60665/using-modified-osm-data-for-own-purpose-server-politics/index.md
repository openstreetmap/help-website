+++
type = "question"
title = "using modified OSM data for own-purpose server (politics)"
description = '''In a national OSM forum, there&#x27;s some guys who would like to start their own OSM tile server, starting out with a copy of the current OSM data, but modified to render (internationally disputed) borders in a way they find (politically) correct. In OSM, these borders are - as always - entered accordin...'''
date = "2017-11-17T13:52:00Z"
lastmod = "2017-11-19T12:04:00Z"
weight = 60665
keywords = [ "borders", "political", "copyright", "license" ]
aliases = [ "/questions/60665" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [using modified OSM data for own-purpose server (politics)](/questions/60665/using-modified-osm-data-for-own-purpose-server-politics)

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
<span id="post-60665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60665-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In a national OSM forum, there's some guys who would like to start their own OSM tile server, starting out with a copy of the current OSM data, but modified to render (internationally disputed) borders in a way they find (politically) correct. In OSM, these borders are - as always - entered according to the "on the ground" rule, but some people within one of the adjacent countries are unsatisfied with that and would like to have an own OSM-based map for like-minded people.</p>
<p>Now my question is - is it basically possible to do this with the OSM data, even if copied to an own server and run under "license"? Point being, when people take the work of adding data to OSM upon them, they rely on the idea that nothing will be done with this data that doesn't follow the rules of the OSM community and license, and this is basically what is done here, from my POV. So I'm sceptical about this, but how would you see it?</p>
<p>Aleks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-borders" rel="tag" title="see questions tagged &#39;borders&#39;">borders</span> <span class="post-tag tag-link-political" rel="tag" title="see questions tagged &#39;political&#39;">political</span> <span class="post-tag tag-link-copyright" rel="tag" title="see questions tagged &#39;copyright&#39;">copyright</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Nov '17, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0c0ef6b9ad3a9ec5ff224ccc2d957177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cirko&#39;s gravatar image" />
<p><span>cirko</span><br />
<span class="score" title="106 reputation points">106</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cirko has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60665" class="comments-container">
&#10;</div>
<div id="comment-tools-60665" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60665-form-container" class="comment-form-container">
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

<span id="60666"></span>

<div id="answer-container-60666" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60666-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, there's an example described in some detail for India in <a href="https://www.openstreetmap.org/user/PlaneMad">Planemad</a>'s diary <a href="https://www.openstreetmap.org/user/PlaneMad/diary/38176">here</a>.</p>
<p>What you should be able to do is to download the OSM data you want, remove (using one of the "modify OSM data from the command line" tools such as <a href="https://wiki.openstreetmap.org/wiki/Osmium">osmium</a>) the boundaries that you're not interested in, add in (using a similar tool) data that you have external to OSM that represents the boundaries that you want to show, and also probably manipulate the language of names etc. to match the language you want as the language on the map. An example of a script that I use that among other things does language manipulation is <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh#L121">here</a> - you could probably do something similar for your map.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '17, 14:05</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-60666" class="comments-container">
<span id="60667"></span>
<div id="comment-60667" class="comment">
<div id="post-60667-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I see that it's possible to do it technically, but the question is whether it's a problem regarding licensing and community rules.</p>
</div>
<div id="comment-60667-info" class="comment-info">
<span class="comment-age">(17 Nov '17, 14:22)</span> <span class="comment-user userinfo">cirko</span>
</div>
</div>
<span id="60668"></span>
<div id="comment-60668" class="comment">
<div id="post-60668-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>With regard to licensing, OSM's statement about OSM data is <a href="http://www.openstreetmap.org/copyright">here</a>. OSMF's <a href="http://wiki.osmfoundation.org/w/images/d/d8/DisputedTerritoriesInformation.pdf">policy</a> (PDF) says "We encourage different groups and communities to use our data, collect and contribute data important to you, and to make your own maps that are harmonious with your general usage, culture and legal system", so I'd say you are actually <em>encouraged</em> to make such a map :)</p>
</div>
<div id="comment-60668-info" class="comment-info">
<span class="comment-age">(17 Nov '17, 14:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60694"></span>
<div id="comment-60694" class="comment">
<div id="post-60694-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think what Aleks is looking for, is a statement about the openness of his resulting data, among others. I imagine that for him the situation would be different if his added data was mandatorily with the same legal status as ours in OSM, or not. Bluntly expressed, the issue is "I take open OSM data, I add my own things, then the result is mine/open/must be inserted back in OSM etc." Having not read the OSM reuse statement, I only suspect there'll be some clause imposing a kind of same release as OSM 'own' data...</p>
</div>
<div id="comment-60694-info" class="comment-info">
<span class="comment-age">(19 Nov '17, 12:04)</span> <span class="comment-user userinfo">Hseul</span>
</div>
</div>
</div>
<div id="comment-tools-60666" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60666-form-container" class="comment-form-container">
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

