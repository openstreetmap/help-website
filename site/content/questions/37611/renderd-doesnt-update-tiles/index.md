+++
type = "question"
title = "Renderd doesn&#x27;t update tiles"
description = '''I am running a tile server on an Ubuntu-based virtual machine and configured it using the guide the guide on switch2osm.org. It&#x27;s just for private purposes, so it&#x27;s not public. In the beginning, everything was just fine and I could import large amounts of map data without problems. Changes became vi...'''
date = "2014-10-14T17:27:00Z"
lastmod = "2014-10-16T13:05:00Z"
weight = 37611
keywords = [ "tiles", "renderd", "updating", "mapnik", "tileserver" ]
aliases = [ "/questions/37611" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Renderd doesn't update tiles](/questions/37611/renderd-doesnt-update-tiles)

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
<span id="post-37611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37611-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am running a tile server on an Ubuntu-based virtual machine and configured it using the guide the guide on switch2osm.org. It's just for private purposes, so it's not public. In the beginning, everything was just fine and I could import large amounts of map data without problems. Changes became visible soon after. I have done some minor edits to Mapnik's osm.xml file since then, changing things such as water color or label font size. Since a couple of days, my tiles don't seem to get updated anymore.</p>
<p>When I use</p>
<pre><code>render_list -f -a</code></pre>
<p>this <em>normally</em> gives me no errors. Well, actually that means it goes until</p>
<pre><code>Rendering all tiles for zoom 6 from (0,0) to (63,63)</code></pre>
<p>and then it gets stuck forever. Sometimes it doesn't get that far and gives me an error message saying</p>
<pre><code>rendering failed with command 4, pausing</code></pre>
<p>I can restart Renderd just fine and get no errors. I also often use</p>
<pre><code>touch /var/lib/mod_tile/planet-import-complete</code></pre>
<p>to notify it of any change.</p>
<p>Why are my tiles not getting updated anymore? I have my machine switched on for more than 12 hours and yet I see no changes on my slippymap.</p>
<p>Did my edits to Mapnik's osm.xml maybe corrupt the file and therefore make updating tiles impossible for renderd? Is my machine too slow and it takes weeks to render the whole planet? (I have 16 GB RAM and an 8 core CPU) What else could be the reason?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-updating" rel="tag" title="see questions tagged &#39;updating&#39;">updating</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Oct '14, 17:27</strong></p>
<img src="https://secure.gravatar.com/avatar/9b1b4e90f4146bc02ab2da5df7df202d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maturi0n&#39;s gravatar image" />
<p><span>Maturi0n</span><br />
<span class="score" title="44 reputation points">44</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maturi0n has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Oct '14, 18:01</strong> </span></p>
</div>
</div>
<div id="comments-container-37611" class="comments-container">
<span id="37650"></span>
<div id="comment-37650" class="comment">
<div id="post-37650-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Rendering the planet requires a lot of resources, especially if you want to speed-up the first import. But if you say that your problem is only coming after a style change, I would suggest you to report your change on the mapnik forum (Search google) or mailing list dev@openstreetmap.org</p>
</div>
<div id="comment-37650-info" class="comment-info">
<span class="comment-age">(16 Oct '14, 13:05)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-37611" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37611-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

