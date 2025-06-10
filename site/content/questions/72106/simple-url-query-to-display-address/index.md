+++
type = "question"
title = "simple url query to display address"
description = '''Hello everybody, I&#x27;m writing a planning application, witch has a database of place the users may have to go to. This application offer the users the ability the view a place he has to go to on a map website.  Actually my app can do it by showing a link to an map website, for example mith gmap https:...'''
date = "2019-12-14T12:28:00Z"
lastmod = "2019-12-15T12:50:00Z"
weight = 72106
keywords = [ "url", "query", "show", "address", "map" ]
aliases = [ "/questions/72106" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [simple url query to display address](/questions/72106/simple-url-query-to-display-address)

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
<span id="post-72106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72106-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everybody,</p>
<p>I'm writing a planning application, witch has a database of place the users may have to go to. This application offer the users the ability the view a place he has to go to on a map website.</p>
<p>Actually my app can do it by showing a link to an map website, for example mith gmap <a href="https://www.google.com/maps/place/%5BHOUSE_NUMBER%5D%20%5BSTREET_NAME%5D,%5BZIP%5D+%5BCITY%5D">https://www.google.com/maps/place/[HOUSE_NUMBER]%20[STREET_NAME],[ZIP]+[CITY]</a></p>
<p>I don't like to promote GAFAMS and would prefer to promote openstreetmap by directing users to it instead of google.</p>
<p>I searched but didn't found a way to do exactly the same thing with OSM, just by generating an url containing the adresse of the place.</p>
<p>I know that i can build an URL to tell OSM to directly generate a map centred on a given point an a map by giving it it's coordinates. (for exemple: <a href="https://www.openstreetmap.org/?mlat=43.59021&amp;mlon=1.40741#map=17/43.59021/1.40741),">https://www.openstreetmap.org/?mlat=43.59021&amp;mlon=1.40741#map=17/43.59021/1.40741),</a> but i don't know the coordinates, and would like openstreetmap to search it from the adress</p>
<p>I know that i can build an URL telling openstreetmap to search for an adress like <a href="https://www.openstreetmap.org/search?query=%5BHOUSE_NUMBER%5D%20%5BSTREET_NAME%5D%2C%20%5BCITY%5D,">https://www.openstreetmap.org/search?query=[HOUSE_NUMBER]%20[STREET_NAME]%2C%20[CITY],</a> but when i do that, openstreetmap will open a list of results, not show the most relevant one directly on the map.</p>
<p>Is there a way to build on URL to tell him "search for this adress, and show the most relevant result on the map putting a marker on it"?</p>
<p>Or do I need to write some "wrapper" PHP script taking address as argument, search the coordinates on nominatim, and returning a 302(redirect) to an URL telling openstreetmap to show these coordinates?</p>
<p>Thanks for help,</p>
<p>Julien Marin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-show" rel="tag" title="see questions tagged &#39;show&#39;">show</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '19, 12:28</strong></p>
<img src="https://secure.gravatar.com/avatar/55f166a501568c3dec9d73d406c8214c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ptitnuage&#39;s gravatar image" />
<p><span>ptitnuage</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ptitnuage has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Dec '19, 12:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-72106" class="comments-container">
&#10;</div>
<div id="comment-tools-72106" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72106-form-container" class="comment-form-container">
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

<span id="72112"></span>

<div id="answer-container-72112" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72112-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should be using nominatim <a href="https://nominatim.openstreetmap.org/">https://nominatim.openstreetmap.org/</a> to do this (or photon if you need a slightly fuzzy search frontend to it).</p>
<p>The big caveat is that this will only work well when relevant address information is present in our data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '19, 12:36</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-72112" class="comments-container">
<span id="72113"></span>
<div id="comment-72113" class="comment">
<div id="post-72113-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer i didn't knew about photo and fuzzzy, search, it's a big relief...</p>
<p>I will write a script requesting for coordinates then doing</p>
<p>$url="https://www.openstreetmap.org/?mlat=$lat&amp;mlon=$lon#map=$zoom/$lat/$lon"; header("Location: $url");</p>
<p>Have a good day!</p>
<p>julien</p>
</div>
<div id="comment-72113-info" class="comment-info">
<span class="comment-age">(15 Dec '19, 12:50)</span> <span class="comment-user userinfo">ptitnuage</span>
</div>
</div>
</div>
<div id="comment-tools-72112" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72112-form-container" class="comment-form-container">
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

