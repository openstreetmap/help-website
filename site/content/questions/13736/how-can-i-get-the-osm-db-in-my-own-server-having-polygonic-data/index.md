+++
type = "question"
title = "How can I get the OSM DB in my own server having polygonic data?"
description = '''I want OSM DB as I need to use some map polygon (GEO cordinates) data of nodes as read only purpose in my current application. As I can see Nominatim is little bit tough and too large to install. SO please suggest me another way so I can just mirror the existing mysql / postgresql DB.  I have alread...'''
date = "2012-06-23T07:37:00Z"
lastmod = "2012-06-25T19:43:00Z"
weight = 13736
keywords = [ "private_server", "own", "osm", "polygon", "nominatim" ]
aliases = [ "/questions/13736" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I get the OSM DB in my own server having polygonic data?](/questions/13736/how-can-i-get-the-osm-db-in-my-own-server-having-polygonic-data)

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
<span id="post-13736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13736-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want OSM DB as I need to use some map polygon (GEO cordinates) data of nodes as read only purpose in my current application. As I can see Nominatim is little bit tough and too large to install. SO please suggest me another way so I can just mirror the existing mysql / postgresql DB.</p>
<p>I have already tried the way as defined below as I could read from the openstreetmap book: -&gt; Ruby and rails installation with the basic gems -&gt; Installation of required gems for the OSM db migration -&gt; rake db:migrate</p>
<p>And I could see few tables and could run the osm search website on my 3000 port. But I can not see the polygon data in that DB and I found that it is fetching the polygon data from the Nominatim API at the run time.</p>
<p>If anyone has already done this installation and he has already this OSM DB with polygonic data in his server then please let me know so I can mirror it on my server.</p>
<p>Or let me know the easier way to get the data in my server.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-private_server" rel="tag" title="see questions tagged &#39;private_server&#39;">private_server</span> <span class="post-tag tag-link-own" rel="tag" title="see questions tagged &#39;own&#39;">own</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jun '12, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/b3013a84207a32bed7ddfad7004100f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ravi%20Kotwani&#39;s gravatar image" />
<p><span>Ravi Kotwani</span><br />
<span class="score" title="136 reputation points">136</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ravi Kotwani has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13736" class="comments-container">
&#10;</div>
<div id="comment-tools-13736" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13736-form-container" class="comment-form-container">
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

<span id="13739"></span>

<div id="answer-container-13739" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13739-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-13739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ravi Kotwani has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a> to get data into database. You can then modify stylefile default.style to get only the polygons you want into database.</p>
<p>You can find all necessary steps on <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server/">switch to osm page</a>. As you do not need the rendering part just read the parts that describe db setup and data import. In case you need to keep this db up to date also take a look at <a href="https://wiki.openstreetmap.org/wiki/Osmosis">osmosis</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jun '12, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RM87 has 20 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jun '12, 11:59</strong> </span></p>
</div>
</div>
<div id="comments-container-13739" class="comments-container">
<span id="13754"></span>
<div id="comment-13754" class="comment">
<div id="post-13754-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have already tried all these steps, but getting 2 much errors while importing planet file. So now I don't want to do all this as I need the DB for read only purpose. So I would request you to give me export of your complete DB if you have this DB on your server. I am ready to pay for this also. Please give me your contact details so I can contact you personally.</p>
</div>
<div id="comment-13754-info" class="comment-info">
<span class="comment-age">(25 Jun '12, 08:16)</span> <span class="comment-user userinfo">Ravi Kotwani</span>
</div>
</div>
<span id="13757"></span>
<div id="comment-13757" class="comment">
<div id="post-13757-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Unfortunately the only export format provided for osm in the planet.osm file. DB dumps are not provided.</p>
<p>There are various companies that provide OSM services who may be able to assist on a commercial basis - you can find a list here: <a href="http://switch2osm.org/providers/">http://switch2osm.org/providers/</a></p>
</div>
<div id="comment-13757-info" class="comment-info">
<span class="comment-age">(25 Jun '12, 10:06)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
<span id="13773"></span>
<div id="comment-13773" class="comment">
<div id="post-13773-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You may begin with some smaller extracts from <a href="http://download.geofabrik.de/osm/">geofabrik</a>, so reaching those errors and retrying won't take long (some minutes for extra tiny area compared to some days for full planet). If everything goes well with small extract then everything should also go well with planet file.</p>
<p>If you reach an error you could not figure out (even after refreshing break) then post it here, to the <a href="http://forum.openstreetmap.org/">forum</a> (better place for discussions) or ask on the <a href="https://wiki.openstreetmap.org/wiki/IRC">irc</a>.</p>
</div>
<div id="comment-13773-info" class="comment-info">
<span class="comment-age">(25 Jun '12, 19:43)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
</div>
<div id="comment-tools-13739" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13739-form-container" class="comment-form-container">
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

