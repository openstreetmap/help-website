+++
type = "question"
title = "Why are other sites updating Mapnik faster than osm.org?"
description = '''Seems like the local Mapnik layer over at Wikimedia&#x27;s toolserver re-renders map changes faster in various zoom levels than official OSM.org main Mapnik layer. How comes? Does OSM.org deliberately choke the re-rendering speed to save server load?'''
date = "2012-02-24T21:03:00Z"
lastmod = "2012-02-26T11:41:00Z"
weight = 10779
keywords = [ "wikimedia", "server", "toolserver", "mapnik", "rendering" ]
aliases = [ "/questions/10779" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why are other sites updating Mapnik faster than osm.org?](/questions/10779/why-are-other-sites-updating-mapnik-faster-than-osmorg)

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
<span id="post-10779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10779-score" class="post-score" title="current number of votes">
-4
</div>
<span id="post-10779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Seems like the local Mapnik layer over at <a href="http://toolserver.org/~kolossos/openlayers/kml-on-ol.php?lang=de&amp;uselang=de&amp;params=50.416944444444_N_16.163055555556_E_dim%3A10000_region%3ACZ-KR_type%3Acity&amp;zoom=11&amp;lat=50.49847&amp;lon=16.05869&amp;layers=B0000FFFT">Wikimedia's toolserver</a> re-renders map changes faster in various zoom levels than official <a href="http://OSM.org">OSM.org</a> main Mapnik layer. How comes? Does <a href="http://OSM.org">OSM.org</a> deliberately choke the re-rendering speed to save server load?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wikimedia" rel="tag" title="see questions tagged &#39;wikimedia&#39;">wikimedia</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-toolserver" rel="tag" title="see questions tagged &#39;toolserver&#39;">toolserver</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '12, 21:03</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Feb '12, 23:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span></p>
</div>
</div>
<div id="comments-container-10779" class="comments-container">
&#10;</div>
<div id="comment-tools-10779" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10779-form-container" class="comment-form-container">
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

<span id="10793"></span>

<div id="answer-container-10793" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10793-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-10793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally OpenStreetMap aims to have its tiles updated as fast as possible, as one of its main purposes is for it to be useful to mappers. Sparing some caveats, the turn around time from mapping to appearing on the tiles is often only a few minutes. However, the system in place to decide which tiles and when to render things is reasonably complex being a delicate balance between keeping things as up-to-date as possible while not overloading the system. A more detailed response of how the system works can be found at <a href="http://help.openstreetmap.org/questions/178/how-often-does-the-main-mapnik-map-get-updated">http://help.openstreetmap.org/questions/178/how-often-does-the-main-mapnik-map-get-updated</a></p>
<p>Given this balance between load and update frequency, the various tileservers out there, might choose different tradeoffs depending on their hardware characteristics and the load they are serving.</p>
<p>With respect to the toolserver and <a href="http://osm.org">osm.org</a>, I could imagine a couple of reasons for why the toolserver may currently appear faster in some cases than <a href="http://osm.org">osm.org</a>. However, it mostly depends on what zoom levels you are referring to and how much delay you are seeing between when you have edited and when the changes show up. Normally though I would expect the toolserver to be somewhat slower in updating than the <a href="http://osm.org">osm.org</a> server. However, <a href="http://osm.org">osm.org</a> is serving more than an order of magnitude more tiles, so they need to distribute the load over multiple servers, which might cause some of the delays</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '12, 23:54</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Feb '12, 00:31</strong> </span></p>
</div>
</div>
<div id="comments-container-10793" class="comments-container">
&#10;</div>
<div id="comment-tools-10793" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10793-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10780"></span>

<div id="answer-container-10780" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10780-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-10780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is great to see other rendering services catch up in speed and quality. If others do tiles as good as, or even better than we do, then that's the best possible proof that with OSM everyone can have their own tiles.</p>
<p>Re-rendering at OSM's server is certainly not "deliberately choked" but is of course subject to performance, and also follows a different policy than that of the Wikimedia toolserver.</p>
<p>If the toolserver rendering works better for you - use the toolserver. There's no shame in that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '12, 22:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Feb '12, 00:00</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span></p>
</div>
</div>
<div id="comments-container-10780" class="comments-container">
<span id="10797"></span>
<div id="comment-10797" class="comment">
<div id="post-10797-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Seems like several comments were deleted from this answer... I can understand if someone deletes his/her own comment (apmon seems to have converted his comment to an answer) but can not really find a proper reason for deleting comments of others (mine amont others)... Such a behaviour shows weakness of an indivitual who made such thing and only destabilizes the community. I really do not think we need some kind of censorship here...</p>
</div>
<div id="comment-10797-info" class="comment-info">
<span class="comment-age">(26 Feb '12, 10:01)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
<span id="10803"></span>
<div id="comment-10803" class="comment">
<div id="post-10803-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There is a new question for this here: <a href="http://help.openstreetmap.org/questions/10799/why-are-opinions-removed-from-helposmorg">http://help.openstreetmap.org/questions/10799/why-are-opinions-removed-from-helposmorg</a></p>
</div>
<div id="comment-10803-info" class="comment-info">
<span class="comment-age">(26 Feb '12, 11:41)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-10780" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10780-form-container" class="comment-form-container">
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

