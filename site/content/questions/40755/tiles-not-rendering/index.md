+++
type = "question"
title = "Tiles not rendering"
description = '''Since about 2015-01-29 I&#x27;ve seen a problem with tiles not rendering at any zoom level on OpenStreetMap.org. The missing tiles are in diagonal lines from lower left to upper right, touching at the corners. I&#x27;ve tried clearing the Web browser cache and reloading the page, to no avail. It happens at al...'''
date = "2015-02-02T21:23:00Z"
lastmod = "2015-06-21T09:52:00Z"
weight = 40755
keywords = [ "rendering", "tiles", "browser" ]
aliases = [ "/questions/40755" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tiles not rendering](/questions/40755/tiles-not-rendering)

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
<span id="post-40755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40755-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Since about 2015-01-29 I've seen a problem with tiles not rendering <em>at any zoom level</em> on OpenStreetMap.org. The missing tiles are in diagonal lines from lower left to upper right, touching at the corners. I've tried clearing the Web browser cache and reloading the page, to no avail. It happens at all hours of the day and night now, making OpenStreetMap.org essentially useless and very difficult to use when one edits offline with JOSM and would then like to verify results after uploading changes.</p>
<p>Is anyone else seeing this problem? Does anyone know what is causing it?</p>
<p>Update 2015-04-04: Viewing OpenStreetMap.de (the German site) with the same machine and same browser renders correctly, with no missing tiles.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-browser" rel="tag" title="see questions tagged &#39;browser&#39;">browser</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Feb '15, 21:23</strong></p>
<img src="https://secure.gravatar.com/avatar/073c91b59675b4570a152fce196e97f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user8192&#39;s gravatar image" />
<p><span>user8192</span><br />
<span class="score" title="20 reputation points">20</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user8192 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Apr '15, 02:28</strong> </span></p>
</div>
</div>
<div id="comments-container-40755" class="comments-container">
<span id="40756"></span>
<div id="comment-40756" class="comment">
<div id="post-40756-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>tiles are loaded from different tile servers (at least different URLs). Just one of the three (a, b, c) fails, which is the pattern you seeing. I also had this today, but some minutes later those tiles loaded normally again.</p>
<p>It might be useful to know from which country you are accessing. I am from Germany.</p>
<p>Workaroung: use other tiles. E.g. the Humanitarian ones are also updated quite fast (less than ten minutes at my edit now).</p>
</div>
<div id="comment-40756-info" class="comment-info">
<span class="comment-age">(02 Feb '15, 23:00)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="40762"></span>
<div id="comment-40762" class="comment">
<div id="post-40762-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am in California, United States. Per your suggestion, I used the "Layers" menu at the right of the OpenStreetMap.org page to switch from Standard to Humanitarian view. There are no missing tiles in this view, but some features added several days ago, such as gates, service roads and buildings, are not displayed in Cycle Map, Transport Map, MapQuest Open or Humanitarian views.</p>
<p>We can only hope that someone is working on it and will get it fixed soon. How can one tell if it is the a.tile, b.tile or c.tile server with problems, from the latitude and longitude of the missing squares?</p>
</div>
<div id="comment-40762-info" class="comment-info">
<span class="comment-age">(03 Feb '15, 18:46)</span> <span class="comment-user userinfo">user8192</span>
</div>
</div>
<span id="40763"></span>
<div id="comment-40763" class="comment">
<div id="post-40763-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you do a "nslookup a.tile.openstreetmap.org" you'll get the same answer for a, b or c - that's just a cheat to help tiles load faster.</p>
<p>I see:</p>
<p>Name: london.tile.openstreetmap.org Address: 185.73.44.30 Aliases: a.tile.openstreetmap.org tile.geo.openstreetmap.org gb.tile.openstreetmap.org</p>
<p>from the UK which shows me where my tiles are coming from.</p>
</div>
<div id="comment-40763-info" class="comment-info">
<span class="comment-age">(03 Feb '15, 20:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="40765"></span>
<div id="comment-40765" class="comment not_top_scorer">
<div id="post-40765-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>: ah, okay. I get germany.tile.openstreetmap.org (and the same IP) for all three names. However, I do not have the non-loading tiles problem now.</p>
</div>
<div id="comment-40765-info" class="comment-info">
<span class="comment-age">(03 Feb '15, 23:43)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="40772"></span>
<div id="comment-40772" class="comment">
<div id="post-40772-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When I perform "nslookup a.tile.openstreetmap.org", it responds with the result</p>
<p>Name: corvallis.tile.openstreetmap.org</p>
<p>Address: 140.211.167.105</p>
<p>where "corvallis" most likely means Corvallis, Oregon, USA. Same result for "b.tile" and "c.tile". Now we are getting somewhere. It's probably a mirror in the United States that has gone bad. Perhaps it is located at Oregon State University, Corvallis. Does anyone have an idea how to contact the person(s) responsible for that server?</p>
</div>
<div id="comment-40772-info" class="comment-info">
<span class="comment-age">(04 Feb '15, 12:00)</span> <span class="comment-user userinfo">user8192</span>
</div>
</div>
<span id="40773"></span>
<div id="comment-40773" class="comment not_top_scorer">
<div id="post-40773-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you give the URL of a tile (typically via right-click / view image) that does not work for you?</p>
</div>
<div id="comment-40773-info" class="comment-info">
<span class="comment-age">(04 Feb '15, 12:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="40776"></span>
<div id="comment-40776" class="comment not_top_scorer">
<div id="post-40776-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/2397/user8192">@user8192</a>: yes, that's right. Just for info: "<a href="http://dns.openstreetmap.org/tile.openstreetmap.org.html">United States via corvallis</a>"</p>
</div>
<div id="comment-40776-info" class="comment-info">
<span class="comment-age">(04 Feb '15, 13:41)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="43673"></span>
<div id="comment-43673" class="comment not_top_scorer">
<div id="post-43673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I still have this problem and it has been months now, how can it works in Humanitarian layer, but not in Standard layer?</p>
</div>
<div id="comment-43673-info" class="comment-info">
<span class="comment-age">(21 Jun '15, 09:46)</span> <span class="comment-user userinfo">gutenye</span>
</div>
</div>
<span id="43674"></span>
<div id="comment-43674" class="comment">
<div id="post-43674-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11132/gutenye">@gutenye</a> the tiles from the Humanitarian level are not distributed via the tile cache network (IMHO). As pointed out earlier the fastest way to get your problem addressed (if it is actually possible) is to join #osm-dev and give some details.</p>
</div>
<div id="comment-43674-info" class="comment-info">
<span class="comment-age">(21 Jun '15, 09:52)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40755" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-40755-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="40774"></span>

<div id="answer-container-40774" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40774-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The most effective way of communicating with the admins is by mentioning it in the <a href="http://irc://irc.oftc.net/osm-dev">#osm-dev</a> <a href="http://wiki.osm.org/wiki/IRC">IRC</a> channel. Obviously it might take a while for any question to be answered, as the people running the site are volunteers with day jobs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '15, 12:26</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-40774" class="comments-container">
<span id="40775"></span>
<div id="comment-40775" class="comment">
<div id="post-40775-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the tip. It's now 5 a.m. here on the west coast of the U.S., so it's unlikely anyone at OSU Corvallis is online at the moment, but I just posted a question about the tile server status on the channel anyway.</p>
</div>
<div id="comment-40775-info" class="comment-info">
<span class="comment-age">(04 Feb '15, 13:05)</span> <span class="comment-user userinfo">user8192</span>
</div>
</div>
</div>
<div id="comment-tools-40774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40774-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40899"></span>

<div id="answer-container-40899" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40899-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40899-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40899-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>user8192, we, too, have been seeing this issue for several days.</p>
<p>Are you a Time Warner customer? Time Warner's DNS servers (209.18.47.61 and 209.18.47.62) intermittently return no such name when asked to resolve b.tile.openstreetmap.org and c.tile.openstreetmap.org.</p>
<p>I do not see these failures when querying other DNS servers (e.g., Google Public DNS and Amazon DNS as well as OpenStreetMap's DNS servers).</p>
<p>The issue only affects the Standard tiles since other tiles are served from other hostnames.</p>
<p>We are complaining to Time Warner.</p>
<p><em>Update:</em> We complained to Time Warner about their DNS servers and now no longer see the problem, user8192. Let me know if you still see the issue and if you are a Time Warner customer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '15, 20:47</strong></p>
<img src="https://secure.gravatar.com/avatar/3171902d4de6e63728ca4dd1ecf51486?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ccwf&#39;s gravatar image" />
<p><span>ccwf</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ccwf has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Feb '15, 00:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-40899" class="comments-container">
<span id="42124"></span>
<div id="comment-42124" class="comment">
<div id="post-42124-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, I'm a Charter Communications customer, but I don't use Charter's DNS servers since they redirect "404 Not Found" to spammy link farm pages. My primary DNS is set to 8.8.8.8 (Google Public); the secondary DNS is set to 4.2.2.4 (Level 3 Communications). I could try some different name servers to see if it fixes the problem. Interestingly, using the same browser on the same machine, there is no problem seeing www.openstreetmap.de, the German version, although there is a rather big lag between my editing on the west coast of the U.S. and changes appearing on the German site.</p>
</div>
<div id="comment-42124-info" class="comment-info">
<span class="comment-age">(05 Apr '15, 02:25)</span> <span class="comment-user userinfo">user8192</span>
</div>
</div>
</div>
<div id="comment-tools-40899" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40899-form-container" class="comment-form-container">
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

