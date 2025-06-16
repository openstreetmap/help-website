+++
type = "question"
title = "How to get poi&#x27;s inside bbox in android"
description = '''Hi all, i am developing an android app with which i display my current location and certain poi&#x27;s, like cinema or restaurants around my position (inside a bounding box). i am using osmdroid and i can display my postion in a map, thats fine. but i have not any idea how to display the poi&#x27;s (not in th...'''
date = "2012-12-17T10:27:00Z"
lastmod = "2012-12-19T08:47:00Z"
weight = 18512
keywords = [ "bounding", "map", "android", "data", "box" ]
aliases = [ "/questions/18512" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to get poi's inside bbox in android](/questions/18512/how-to-get-pois-inside-bbox-in-android)

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
<span id="post-18512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18512-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>i am developing an android app with which i display my current location and certain poi's, like cinema or restaurants around my position (inside a bounding box). i am using osmdroid and i can display my postion in a map, thats fine. but i have not any idea how to display the poi's (not in the map, i want the poi data as a sting). so what i want is to display the poi as a string in a textview, e.g. Textview: Cinemaxx. what do I need and how do I proceed? can anyone explain that to me? or gives a simple example code? i heard about a overpass-api, but I have not understood how to use it. should I use a different library e.g. mapsforge? I'm very desperate :( i hope someone can give me a very good hint and help me.</p>
<p>PS: sry for my english</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bounding" rel="tag" title="see questions tagged &#39;bounding&#39;">bounding</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-box" rel="tag" title="see questions tagged &#39;box&#39;">box</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '12, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/971addd249bfcb56dc880fa913ad350f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naruto25&#39;s gravatar image" />
<p><span>naruto25</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naruto25 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18512" class="comments-container">
<span id="18528"></span>
<div id="comment-18528" class="comment">
<div id="post-18528-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When you do a query like Frederik told you, you get an XML file, and that can be read with one of the many XML libraries available for Java/Android. You can easily convert those XML nodes to Java objects, so you can work with those.</p>
</div>
<div id="comment-18528-info" class="comment-info">
<span class="comment-age">(17 Dec '12, 13:33)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-18512" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18512-form-container" class="comment-form-container">
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

<span id="18514"></span>

<div id="answer-container-18514" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18514-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's two sides to your problem: You need a server that delivers the data and you need to display it in your client. I will talk only about the server side in this answer (due to lack of Android skills).</p>
<p>OpenStreetMap does not operate a server that would be suitable to make end-user queries like "what POIs are in this bbox" against. There are some third-party services that could be used, like XAPI or Overpass, however they all have their terms of use and limitations and you should not be using them in an application that you plan to distribute widely! You will have to set up your own server for that.</p>
<p>When queried, Overpass and XAPI will return data in <a href="https://wiki.openstreetmap.org/wiki/Osm_format">OSM format</a>. In the simple case of the POI being mapped as a point in OpenStreetMap, this would be a "node" object with a latitude and longitude, and some tags describing the name etc.; but the POI might also be a way or even relation in cases where it is mapped as an area in OSM.</p>
<p>There's a different, relatively new, third-party API that might suit you even better than Overpass and XAPI - see <a href="http://lists.openstreetmap.org/pipermail/talk-lu/2012-December/000099.html">http://lists.openstreetmap.org/pipermail/talk-lu/2012-December/000099.html</a> for the announcement. This allows you to download data in JSON format, but again, check with the operators before you make wide use of that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '12, 11:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Dec '12, 13:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span></p>
</div>
</div>
<div id="comments-container-18514" class="comments-container">
<span id="18533"></span>
<div id="comment-18533" class="comment">
<div id="post-18533-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank u guys. i will try it. I'll get back if I get stuck :)</p>
</div>
<div id="comment-18533-info" class="comment-info">
<span class="comment-age">(17 Dec '12, 17:00)</span> <span class="comment-user userinfo">naruto25</span>
</div>
</div>
</div>
<div id="comment-tools-18514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18514-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18590"></span>

<div id="answer-container-18590" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18590-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Concerning <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a>, you can boldly try. The relevant values (100'000 queries per day or 10 GB download data per day) have never been surpassed by any app. And the servers protect themselves, so you cannot hurt anybody. Severals apps make successfully use of Overpass API, and they have figures more around 1000 queries per day, 100-300 users, and less than 1 GB of download data.</p>
<p>In particular, there is an example website for mobile devices, <a href="http://overpass-api.de/locate_me.html">http://overpass-api.de/locate_me.html</a> which you can use as a starting point (however, it is written in JavaScript, not Java).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '12, 08:47</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Dec '12, 09:44</strong> </span></p>
</div>
</div>
<div id="comments-container-18590" class="comments-container">
&#10;</div>
<div id="comment-tools-18590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18590-form-container" class="comment-form-container">
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

