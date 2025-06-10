+++
type = "question"
title = "How do I install Nominatim with local tiles"
description = '''I&#x27;ve edited the local.php settings file in Nominatim/settings and add the following line: @define(&#x27;CONST_Website_BaseURL&#x27;, &#x27;http://localhost/nominatim/&#x27;); Now the map is rendered on my page. However, it&#x27;s loading tiles from OSM server. I tried to change http://b.tile.openstreetmap.org/${z}/${x}/${y}...'''
date = "2013-06-12T14:26:00Z"
lastmod = "2014-07-18T15:40:00Z"
weight = 23272
keywords = [ "nominatim" ]
aliases = [ "/questions/23272" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I install Nominatim with local tiles](/questions/23272/how-do-i-install-nominatim-with-local-tiles)

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
<span id="post-23272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23272-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've edited the local.php settings file in Nominatim/settings and add the following line: @define('CONST_Website_BaseURL', 'http://localhost/nominatim/');</p>
<p>Now the map is rendered on my page. However, it's loading tiles from OSM server. I tried to change <a href="http://b.tile.openstreetmap.org/$%7Bz%7D/$%7Bx%7D/$%7By%7D.png">http://b.tile.openstreetmap.org/${z}/${x}/${y}.png</a> by <a href="http://localhost/nominatim/$%7Bz%7D/$%7Bx%7D/$%7By%7D.png">http://localhost/nominatim/${z}/${x}/${y}.png</a> in tiles.js but it's not working. Indeed, I checked in the localhost/nominatim folder and there's no tiles in it...</p>
<p>In other words, where can I find them?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '13, 14:26</strong></p>
<img src="https://secure.gravatar.com/avatar/4015aaa7dcb688fc988901e4caaac771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kalu06&#39;s gravatar image" />
<p><span>Kalu06</span><br />
<span class="score" title="140 reputation points">140</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kalu06 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jun '13, 16:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span></p>
</div>
</div>
<div id="comments-container-23272" class="comments-container">
<span id="23281"></span>
<div id="comment-23281" class="comment">
<div id="post-23281-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The details I suspect are here:</p>
<p><a href="https://help.openstreetmap.org/questions/23250/osm2pgsql-import-for-geo-coding">https://help.openstreetmap.org/questions/23250/osm2pgsql-import-for-geo-coding</a></p>
</div>
<div id="comment-23281-info" class="comment-info">
<span class="comment-age">(12 Jun '13, 15:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23272" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23272-form-container" class="comment-form-container">
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

<span id="23345"></span>

<div id="answer-container-23345" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23345-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-23345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kalu06 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim provides search functionality only, it does not provide a rendered map. For details on setting up tile rendering you may want to have a look at these help topics (there are probably others if you search)</p>
<p><a href="https://help.openstreetmap.org/questions/136/how-do-i-render-my-own-maps-for-my-website">https://help.openstreetmap.org/questions/136/how-do-i-render-my-own-maps-for-my-website</a></p>
<p><a href="https://help.openstreetmap.org/questions/8371/how-to-serve-tiles-from-my-own-server">https://help.openstreetmap.org/questions/8371/how-to-serve-tiles-from-my-own-server</a></p>
<p>There is also a virtual machine image setup to do both nominatim and tiles - although it currently has problems with more recent osm data in nominatim:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Virtual_machine_image">http://wiki.openstreetmap.org/wiki/Virtual_machine_image</a></p>
<p>By default Nominatim is setup to use OSM tiles, but there are other providers of pre-rendered tiles available, for instance MapQuest. Alternatively you can render your own and provide a custom url - but this requires additional software and another copy of the OSM database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '13, 16:35</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-23345" class="comments-container">
<span id="23347"></span>
<div id="comment-23347" class="comment">
<div id="post-23347-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you very much for this really comprehensive answer. It's very helpful. I'm thinking using Gisgraphy (<a href="http://stevenyue.com/2013/04/24/install-gisgraphy-on-ubuntu-12-04-from-scratch/">http://stevenyue.com/2013/04/24/install-gisgraphy-on-ubuntu-12-04-from-scratch/</a>) instead of Nominatim (which is really hard to set up...) for search functionality .</p>
<p>Lucas</p>
</div>
<div id="comment-23347-info" class="comment-info">
<span class="comment-age">(13 Jun '13, 17:00)</span> <span class="comment-user userinfo">Kalu06</span>
</div>
</div>
<span id="23348"></span>
<div id="comment-23348" class="comment">
<div id="post-23348-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Gisgraphy is easier and quicker to setup but less complete. It depends on your usage as to which one is more suitable. You Probably want to compare the results from their demo system <a href="http://services.gisgraphy.com/public/geocoding.html">http://services.gisgraphy.com/public/geocoding.html</a> and <a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a> and see which best meets your needs.</p>
</div>
<div id="comment-23348-info" class="comment-info">
<span class="comment-age">(13 Jun '13, 17:29)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
<span id="23363"></span>
<div id="comment-23363" class="comment">
<div id="post-23363-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Indeed Nominatim seems to be much more complete and more appropriate to my needs. Thanks for your advices twain.</p>
</div>
<div id="comment-23363-info" class="comment-info">
<span class="comment-age">(14 Jun '13, 09:31)</span> <span class="comment-user userinfo">Kalu06</span>
</div>
</div>
<span id="34964"></span>
<div id="comment-34964" class="comment">
<div id="post-34964-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Kalu06</span> The link should be <a href="http://stevenyue.com/2013/04/24/install-gisgraphy-on-ubuntu-12-04-from-scratch/">http://stevenyue.com/2013/04/24/install-gisgraphy-on-ubuntu-12-04-from-scratch/</a></p>
<p>You happened to include an extra ')' in the link' href, which will lead to a 404 page, and the google webmaster tool keeps telling me the error, so I have to comment it here to clear it. Sorry for any inconvenience :)</p>
</div>
<div id="comment-34964-info" class="comment-info">
<span class="comment-age">(18 Jul '14, 15:36)</span> <span class="comment-user userinfo">steven_yue</span>
</div>
</div>
<span id="34965"></span>
<div id="comment-34965" class="comment">
<div id="post-34965-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@steven_yue</span> I'm not Kalu06 but have fixed it :)</p>
</div>
<div id="comment-34965-info" class="comment-info">
<span class="comment-age">(18 Jul '14, 15:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23345-form-container" class="comment-form-container">
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

