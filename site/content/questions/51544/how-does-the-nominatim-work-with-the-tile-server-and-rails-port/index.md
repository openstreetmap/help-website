+++
type = "question"
title = "how does the nominatim work with the tile server and rails port"
description = '''I have set up the rails port on ubuntu14.04, and then I build my local tile server under the instruction of &quot;Manually building a tile server (14.04)&quot;. And I have changed the OSM map to my local tile server. The nominatim is still use the http://nominatim.openstreetmap.org/ Now I confused that how do...'''
date = "2016-08-19T14:19:00Z"
lastmod = "2016-08-19T14:42:00Z"
weight = 51544
keywords = [ "nominatim", "rubyonrails", "tileserver" ]
aliases = [ "/questions/51544" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how does the nominatim work with the tile server and rails port](/questions/51544/how-does-the-nominatim-work-with-the-tile-server-and-rails-port)

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
<span id="post-51544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51544-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have set up the rails port on ubuntu14.04, and then I build my local tile server under the instruction of "<a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">Manually building a tile server (14.04)</a>". And I have changed the OSM map to my local tile server. The nominatim is still use the <a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a></p>
<p>Now I confused that how does the nominatim work with the tile server and rails port. As I konw there are three database being used in the project: openstreetmap database used in the rails port, gis database used in the tile server and a nominatim database. If I make a search request on the <a href="http://localhost:3000">http://localhost:3000</a> website, first it will ask <a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a> and return several results, and if I click on one of the result, it returns "Sorry, relation #912940 could not be found."</p>
<p><img src="/upfiles/search_msrsPtt.png" alt="alt text" /></p>
<p>From the terminal, I find that it make a request to the openstreetmap database. <img src="/upfiles/wxid_kqsz0bmthrsb22_1471612339340_40.png" alt="alt text" /> I want to know how does the nominatim connect to the openstreetmap database. I also want to know how does the nominatim work with my local tile server. Hope someone can help me, thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-rubyonrails" rel="tag" title="see questions tagged &#39;rubyonrails&#39;">rubyonrails</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '16, 14:19</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</img>
</div>
</div>
<div id="comments-container-51544" class="comments-container">
&#10;</div>
<div id="comment-tools-51544" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51544-form-container" class="comment-form-container">
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

<span id="51545"></span>

<div id="answer-container-51545" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51545-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The server(s) behind <a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a> have loaded the full planet data once and apply minutely updates since them. In theory it finds every (named) OSM feature. The database is completely separate from tiles or the rails port. It runs on the nominatim.openstreetmap.org servers and takes about 700GB-1TB in size.</p>
<p>The rails port sends a HTTP/REST query to Nominatim <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Search">https://wiki.openstreetmap.org/wiki/Nominatim#Search</a> and receives a data structure (JSON? XML?).</p>
<p>You can setup your own Nominatim instance and database of course, it's not part of the tile server instructions. You can then import the pull planet or an extract, e.g. a country. Nominatim can be installed on the same server on a separate server. <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">https://wiki.openstreetmap.org/wiki/Nominatim/Installation</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '16, 14:42</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</img>
</div>
</div>
<div id="comments-container-51545" class="comments-container">
&#10;</div>
<div id="comment-tools-51545" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51545-form-container" class="comment-form-container">
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

