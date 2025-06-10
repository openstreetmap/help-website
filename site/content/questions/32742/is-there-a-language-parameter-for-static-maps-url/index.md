+++
type = "question"
title = "Is there a language parameter for static maps URL?"
description = '''Hey together, I have been wondering whether it is possible to include some kind of &quot;language parameter&quot; in the URL of a static map.  http://staticmap.openstreetmap.de/staticmap.php?center=48.1351253,11.5819806&amp;amp;zoom=14&amp;amp;size=1024x768&amp;amp;markers=48.1351253,11.5819806,ol-marker e.g. Munich inst...'''
date = "2014-04-29T15:10:00Z"
lastmod = "2014-04-29T16:05:00Z"
weight = 32742
keywords = [ "url", "static", "parameters", "language" ]
aliases = [ "/questions/32742" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a language parameter for static maps URL?](/questions/32742/is-there-a-language-parameter-for-static-maps-url)

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
<span id="post-32742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32742-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey together,</p>
<p>I have been wondering whether it is possible to include some kind of "language parameter" in the URL of a static map. <a href="http://staticmap.openstreetmap.de/staticmap.php?center=48.1351253,11.5819806&amp;zoom=14&amp;size=1024x768&amp;markers=48.1351253,11.5819806,ol-marker">http://staticmap.openstreetmap.de/staticmap.php?center=48.1351253,11.5819806&amp;zoom=14&amp;size=1024x768&amp;markers=48.1351253,11.5819806,ol-marker</a> e.g. Munich instead of "München".</p>
<p>Is there maybe even a page where I find all the parameters that can be included in the URL? For instance I have also looked for for different marker icons but didn't come any further than here: <a href="http://staticmap.openstreetmap.de/wizzard/">http://staticmap.openstreetmap.de/wizzard/</a></p>
<p>Best, Emanuel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-static" rel="tag" title="see questions tagged &#39;static&#39;">static</span> <span class="post-tag tag-link-parameters" rel="tag" title="see questions tagged &#39;parameters&#39;">parameters</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '14, 15:10</strong></p>
<img src="https://secure.gravatar.com/avatar/6c7e5c2e70ceb4182b4fbb3c7b537446?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Emu1000&#39;s gravatar image" />
<p><span>Emu1000</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Emu1000 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32742" class="comments-container">
&#10;</div>
<div id="comment-tools-32742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32742-form-container" class="comment-form-container">
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

<span id="32743"></span>

<div id="answer-container-32743" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32743-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No there isn't a language parameter. This would require that the static map script uses tiles made with labels in different languages but it always simply uses the standard OSM map.</p>
<p>See <a href="http://sourceforge.net/projects/staticmaplite/">http://sourceforge.net/projects/staticmaplite/</a> for the original source code of the Static Map script; the instance on staticmap.openstreetmap.de is not 100% identical but similar. You can set up your own instance of the script and even point it to other servers for downloading tiles, however make sure you respect the servers' usage policies.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '14, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-32743" class="comments-container">
<span id="32745"></span>
<div id="comment-32745" class="comment">
<div id="post-32745-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, thank you for your quick and accurate response, Frederik.</p>
</div>
<div id="comment-32745-info" class="comment-info">
<span class="comment-age">(29 Apr '14, 16:05)</span> <span class="comment-user userinfo">Emu1000</span>
</div>
</div>
</div>
<div id="comment-tools-32743" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32743-form-container" class="comment-form-container">
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

