+++
type = "question"
title = "How can I create a map without any names on it?"
description = '''I want to create bitmap maps to use in wikipedia, but I don&#x27;t want any names on itself (otherwise I&#x27;ll have to create different versions for each language). As long as I have searched I didn&#x27;t find a way to export a map like that.'''
date = "2010-12-20T20:31:00Z"
lastmod = "2016-05-20T12:54:00Z"
weight = 1873
keywords = [ "without", "export", "name", "language" ]
aliases = [ "/questions/1873" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How can I create a map without any names on it?](/questions/1873/how-can-i-create-a-map-without-any-names-on-it)

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
<span id="post-1873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1873-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-1873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to create bitmap maps to use in wikipedia, but I don't want any names on itself (otherwise I'll have to create different versions for each language).</p>
<p>As long as I have searched I didn't find a way to export a map like that.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-without" rel="tag" title="see questions tagged &#39;without&#39;">without</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Dec '10, 20:31</strong></p>
<img src="https://secure.gravatar.com/avatar/cb4aa269c844224dbf687bd2eb07fb84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geraki&#39;s gravatar image" />
<p><span>geraki</span><br />
<span class="score" title="171 reputation points">171</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geraki has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '13, 13:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-1873" class="comments-container">
&#10;</div>
<div id="comment-tools-1873" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1873-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="1878"></span>

<div id="answer-container-1878" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1878-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-1878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="geraki has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <em>[old]</em> multilanguage map at <a href="http://tiles.wmflabs.org/osm/slippymap2.html">http://tiles.wmflabs.org/osm/slippymap2.html</a> has tiles without names and many different languages as overlays. I don't think that they have a nice way to export tiles from there but if you need only a couple of them you can fetch them by hand.</p>
<p>The other solution would be to setup a rendering stack (osm2pgsql, mapnik, apache, mod_tile) and modify the stylesheet from openstreetmap to exclude the name labels.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Dec '10, 11:35</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 May '16, 12:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span></p>
</div>
</div>
<div id="comments-container-1878" class="comments-container">
<span id="1880"></span>
<div id="comment-1880" class="comment">
<div id="post-1880-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That's cool. Never knew about that. <a href="http://toolserver.org/~osm/locale/en.html?zoom=12&amp;lat=51.51473&amp;lon=-0.13528&amp;layers=BF">London with no names</a>!</p>
<p>The service I knew about was <a href="http://toolserver.org/~osm/locale/en.html?zoom=12&amp;lat=51.51473&amp;lon=-0.13528&amp;layers=BF">a layer called "captionless" from the tiles@home project</a>, but it's only at zoom level 12, and seems to be not working at the moment (it's showing captions) so that's useless.</p>
</div>
<div id="comment-1880-info" class="comment-info">
<span class="comment-age">(21 Dec '10, 12:43)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
<span id="1883"></span>
<div id="comment-1883" class="comment">
<div id="post-1883-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, fits my purpose.</p>
</div>
<div id="comment-1883-info" class="comment-info">
<span class="comment-age">(21 Dec '10, 14:45)</span> <span class="comment-user userinfo">geraki</span>
</div>
</div>
<span id="21404"></span>
<div id="comment-21404" class="comment">
<div id="post-21404-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>currently also: "osm-no-labels" at <a href="https://toolserver.org/~osm/styles/">https://toolserver.org/~osm/styles/</a> (use the layer switcher on top right)</p>
</div>
<div id="comment-21404-info" class="comment-info">
<span class="comment-age">(11 Apr '13, 13:38)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="37517"></span>
<div id="comment-37517" class="comment">
<div id="post-37517-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I appreciate sharing the information</p>
</div>
<div id="comment-37517-info" class="comment-info">
<span class="comment-age">(11 Oct '14, 09:04)</span> <span class="comment-user userinfo">mmlin</span>
</div>
</div>
<span id="49758"></span>
<div id="comment-49758" class="comment">
<div id="post-49758-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've tweaked the link in this answer, since toolserver.org is no more, but I found this on the new labs servers, which may be the same thing.</p>
<p>But the no-labels layer there is with the old style colours of 'standard' openstreetmap, and I guess its continuity is doubtful because I think wikimedia have revamped their map rendering, which you can read more about here <a href="https://www.mediawiki.org/wiki/Maps">https://www.mediawiki.org/wiki/Maps</a> and see running here: <a href="https://maps.wikimedia.org/">https://maps.wikimedia.org/</a> But I don't know if this new stuff includes a "no labels" layer</p>
</div>
<div id="comment-49758-info" class="comment-info">
<span class="comment-age">(20 May '16, 12:54)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
</div>
<div id="comment-tools-1878" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1878-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1879"></span>

<div id="answer-container-1879" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1879-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another option is to use <a href="http://maperitive.net/">Maperitive</a>, remove any "draw : text" commands in the default rules and you'll end up with no text on your bitmaps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Dec '10, 11:53</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-1879" class="comments-container">
&#10;</div>
<div id="comment-tools-1879" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1879-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1884"></span>

<div id="answer-container-1884" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1884-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a couple different ways, including maperitive.</p>
<p>I have also created maps without text using <a href="https://wiki.openstreetmap.org/wiki/Osmarender">osmarender</a>. You'll have to edit your rules file a bit (make sure to have backups of rule files). There also may be an easier way to do this in the rules file, and I'm not 100% sure if this does it [been a few weeks since I last did it] but I removed each line that began with: <code>&lt;caption k="name"</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Dec '10, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/3f2a3925f19f9684808db864d290682c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorasaurus&#39;s gravatar image" />
<p><span>skorasaurus</span><br />
<span class="score" title="1398 reputation points"><span>1.4k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skorasaurus has 3 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-1884" class="comments-container">
&#10;</div>
<div id="comment-tools-1884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1884-form-container" class="comment-form-container">
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

