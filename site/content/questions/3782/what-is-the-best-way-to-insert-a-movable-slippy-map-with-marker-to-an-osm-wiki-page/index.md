+++
type = "question"
title = "what is the best way to insert a (movable) slippy map with marker to an OSM-wiki page?"
description = '''What is the best way to insert a (movable) slippy map with marker to an OSM-wiki page?'''
date = "2011-03-13T19:24:00Z"
lastmod = "2011-03-14T14:48:00Z"
weight = 3782
keywords = [ "marker", "mediawiki", "osm", "extension", "slippymap" ]
aliases = [ "/questions/3782" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [what is the best way to insert a (movable) slippy map with marker to an OSM-wiki page?](/questions/3782/what-is-the-best-way-to-insert-a-movable-slippy-map-with-marker-to-an-osm-wiki-page)

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
<span id="post-3782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3782-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the best way to insert a (movable) slippy map with marker to an OSM-wiki page?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-mediawiki" rel="tag" title="see questions tagged &#39;mediawiki&#39;">mediawiki</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-extension" rel="tag" title="see questions tagged &#39;extension&#39;">extension</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Mar '11, 19:24</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Mar '11, 05:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/bc6d0b055d631830f7891d3f89edb66b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="katpatuka&#39;s gravatar image" />
<p><span>katpatuka</span><br />
<span class="score" title="1041 reputation points"><span>1.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span></p>
</div>
</div>
<div id="comments-container-3782" class="comments-container">
&#10;</div>
<div id="comment-tools-3782" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3782-form-container" class="comment-form-container">
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

<span id="3783"></span>

<div id="answer-container-3783" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3783-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dieterdreist has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm guessing you need to smile at the wiki admins and get them to install the MediaWiki Maps extension</p>
<p><a href="http://mapping.referata.com/wiki/Maps">http://mapping.referata.com/wiki/Maps</a></p>
<p>Alternatively contact the developers of the installed SlippyMap extension and see if they'll address this line of code:</p>
<p><code>if ($marker) $error = 'marker support is disactivated on the OSM wiki pending discussions about wiki syntax';</code></p>
<p>as I can't find any discussions on the wiki (why not just mlat and mlon as optional?). MediaWiki suggests future development of this plugin is unlikely, but not sure where they got that information from.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '11, 20:25</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Mar '11, 20:26</strong> </span></p>
</div>
</div>
<div id="comments-container-3783" class="comments-container">
<span id="3784"></span>
<div id="comment-3784" class="comment">
<div id="post-3784-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>further reference <a href="https://wiki.openstreetmap.org/wiki/Slippy_Map_MediaWiki_Extension">https://wiki.openstreetmap.org/wiki/Slippy_Map_MediaWiki_Extension</a></p>
</div>
<div id="comment-3784-info" class="comment-info">
<span class="comment-age">(14 Mar '11, 05:49)</span> <span class="comment-user userinfo">katpatuka</span>
</div>
</div>
<span id="3796"></span>
<div id="comment-3796" class="comment">
<div id="post-3796-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm the developer of the original MediaWiki extension (including the cited line of code with the "pending discussions" error message) I keep meaning to look into this some more. I used to worry a lot about establishing wiki syntax which we would then not be able to change easily because all the pages would be using it. Worth thinking about, but I was probably worrying more than necessary.</p>
<p>Part of the reason I never got around to tackling this some more, is that I've grown frustrated with use of my own extension. It slows down wiki page loading. I prefer the 'Simple Image' extension.</p>
</div>
<div id="comment-3796-info" class="comment-info">
<span class="comment-age">(14 Mar '11, 14:48)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
</div>
<div id="comment-tools-3783" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3783-form-container" class="comment-form-container">
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

