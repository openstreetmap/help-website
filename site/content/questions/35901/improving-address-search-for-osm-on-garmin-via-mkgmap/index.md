+++
type = "question"
title = "Improving Address Search for OSM on Garmin via mkgmap"
description = '''I noticed that after downloading the California map from http://mapas.alternativaslibres.es/downloads.php#America and putting the IMG file into my Garmin StreetPilot i5, the address search works inconsistently. For example, if I search for the intersection of Coleus Court and Fuchsia Lane in San Die...'''
date = "2014-08-16T21:47:00Z"
lastmod = "2014-08-18T09:47:00Z"
weight = 35901
keywords = [ "mkgmap", "garmin", "addresses" ]
aliases = [ "/questions/35901" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Improving Address Search for OSM on Garmin via mkgmap](/questions/35901/improving-address-search-for-osm-on-garmin-via-mkgmap)

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
<span id="post-35901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35901-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I noticed that after downloading the California map from <a href="http://mapas.alternativaslibres.es/downloads.php#America">http://mapas.alternativaslibres.es/downloads.php#America</a> and putting the IMG file into my Garmin StreetPilot i5, the address search works inconsistently. For example, if I search for the intersection of Coleus Court and Fuchsia Lane in San Diego, California, it works great. However, if I search for 4376 Coleus Ct in San Diego, California, I come up empty. I already checked the address's point with JOSM and the addr:... fields are as follows:</p>
<ul>
<li>country: US</li>
<li>housenumber: 4376</li>
<li>postcode: 92154</li>
<li>street: Coleus Ct</li>
</ul>
<p>The list of streets is also quite incomplete when I search on the Garmin device compared to the streets available on the OSM website.</p>
<p>Is there anything I can do to improve the address search?</p>
<p>In case it matters, it seems that the maps are generated using mkgmap, which should support address searching (see <a href="http://www.mkgmap.org.uk/news/2012/01/28/address-index-for-gps-devices).">http://www.mkgmap.org.uk/news/2012/01/28/address-index-for-gps-devices).</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mkgmap" rel="tag" title="see questions tagged &#39;mkgmap&#39;">mkgmap</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span> <span class="post-tag tag-link-addresses" rel="tag" title="see questions tagged &#39;addresses&#39;">addresses</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '14, 21:47</strong></p>
<img src="https://secure.gravatar.com/avatar/8d4d3618d89915ba9d493fb3da2d9bd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zian&#39;s gravatar image" />
<p><span>Zian</span><br />
<span class="score" title="91 reputation points">91</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zian has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35901" class="comments-container">
&#10;</div>
<div id="comment-tools-35901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35901-form-container" class="comment-form-container">
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

<span id="35921"></span>

<div id="answer-container-35921" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35921-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Zian has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are numerous things that can go wrong in the process of turning OSM data in to a useable Garmin map. For example one thing you should check with the operators of mapas.alternativaslibres.es is if they are actually using a current version of mkgmap and have enabled the address search feature.</p>
<p>Alternatively use one of the <span>other Garmin map providers</span> or grab yourself a current <a href="http://download.geofabrik.de/north-america/us/california.html">extract for California</a> and produce the map yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '14, 14:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '14, 14:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-35921" class="comments-container">
&#10;</div>
<div id="comment-tools-35921" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35921-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35929"></span>

<div id="answer-container-35929" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35929-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should really direct this question to Carlos Davila, the owner of alternativaslibres.es. I believe the site has a forum or contact email, but these may be restricted to people contributing to the development and hosting of the files.</p>
<p>In the past the alternativaslibres.es Garmin maps have been heavily optimised for usage by car drivers and for routing. For instance Spanish roads are shown in the same colours as the standard signage: no trivial matter as each regional government has control over much of the road network. The tiles tend to be large so as to avoid problems with routing across several tiles. In order to achieve large enough tiles some data has to be excluded, which I suspect include addresses.</p>
<p>If address search is an important requirement then follow SimonPoole's advice and use another provider.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '14, 19:25</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-35929" class="comments-container">
&#10;</div>
<div id="comment-tools-35929" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35929-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35937"></span>

<div id="answer-container-35937" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35937-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Mkgmap relies heavily on administrative boundaries, if you search for this street within the city of San Diego and the boundary is not complete or missing in OSM, searching fails (or if addr:city=San Diego is missing here). It might help to leave the city field empty in the search.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '14, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/0f5ffc3756c4662b9dfad80b7665ac6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ligfietser&#39;s gravatar image" />
<p><span>ligfietser</span><br />
<span class="score" title="2894 reputation points"><span>2.9k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="57 badges"><span class="bronze">●</span><span class="badgecount">57</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ligfietser has 8 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Aug '14, 07:41</strong> </span></p>
</div>
</div>
<div id="comments-container-35937" class="comments-container">
<span id="35948"></span>
<div id="comment-35948" class="comment">
<div id="post-35948-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In the past the alternativaslibres maps used is_in tags for building the search index.</p>
</div>
<div id="comment-35948-info" class="comment-info">
<span class="comment-age">(18 Aug '14, 09:47)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-35937" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35937-form-container" class="comment-form-container">
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

