+++
type = "question"
title = "how can I get my OSM tile server to render all my extracts?"
description = '''I created a tile server on an Ubuntu 14.04 system by installing packages according to https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/ and then downloaded and &quot;osm2pgsql&quot;ed the pbf files for Illinois, Missouri and Kentucky. Everything seemed to go smoothly with no errors. W...'''
date = "2017-08-19T14:34:00Z"
lastmod = "2017-08-21T06:28:00Z"
weight = 58403
keywords = [ "gis", "osm2pgsql" ]
aliases = [ "/questions/58403" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how can I get my OSM tile server to render all my extracts?](/questions/58403/how-can-i-get-my-osm-tile-server-to-render-all-my-extracts)

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
<span id="post-58403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58403-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I created a tile server on an Ubuntu 14.04 system by installing packages according to <a href="https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a> and then downloaded and "osm2pgsql"ed the pbf files for Illinois, Missouri and Kentucky. Everything seemed to go smoothly with no errors. When I check with <a href="http://localhost/osm/slippymap.html,">http://localhost/osm/slippymap.html,</a> however, only the Kentucky data seems to be available! I can make detailed maps of Kentucky but not of Illinois or Missouri...</p>
<p>Baffled since I didn't do anything differently between the three pbf files.</p>
<p>I'm willing to wipe everything out and start again, but I don't know how to clear the gis database. Help for this complete newbie would be much appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '17, 14:34</strong></p>
<img src="https://secure.gravatar.com/avatar/090ec71d17f22f1abf9678b6099a0e36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G%20Gyuk&#39;s gravatar image" />
<p><span>G Gyuk</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="G Gyuk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '17, 20:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-58403" class="comments-container">
&#10;</div>
<div id="comment-tools-58403" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58403-form-container" class="comment-form-container">
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

<span id="58405"></span>

<div id="answer-container-58405" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58405-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-58405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can't merge extracts directly with osm2pgsql, you will need to do that pre-import for example with <a href="https://wiki.openstreetmap.org/wiki/Osmosis">osmosis</a>.</p>
<p>Note this is a FAQ and you can find lots of answers on the topic on this site.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '17, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-58405" class="comments-container">
<span id="58418"></span>
<div id="comment-58418" class="comment">
<div id="post-58418-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you!</p>
</div>
<div id="comment-58418-info" class="comment-info">
<span class="comment-age">(21 Aug '17, 06:28)</span> <span class="comment-user userinfo">G Gyuk</span>
</div>
</div>
</div>
<div id="comment-tools-58405" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58405-form-container" class="comment-form-container">
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

