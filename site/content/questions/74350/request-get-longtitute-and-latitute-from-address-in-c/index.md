+++
type = "question"
title = "Request: Get longtitute and latitute from address in c#"
description = '''Hi!  How can i get the geodata from adress (country,city,street) in c# ? Greetings'''
date = "2020-04-23T21:25:00Z"
lastmod = "2020-04-23T23:36:00Z"
weight = 74350
keywords = [ "request" ]
aliases = [ "/questions/74350" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Request: Get longtitute and latitute from address in c#](/questions/74350/request-get-longtitute-and-latitute-from-address-in-c)

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
<span id="post-74350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74350-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>How can i get the geodata from adress (country,city,street) in c# ?</p>
<p>Greetings</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '20, 21:25</strong></p>
<img src="https://secure.gravatar.com/avatar/ba5907481ccbca707a04af680c99105e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hermetes&#39;s gravatar image" />
<p><span>Hermetes</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hermetes has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '20, 12:00</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-74350" class="comments-container">
&#10;</div>
<div id="comment-tools-74350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74350-form-container" class="comment-form-container">
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

<span id="74351"></span>

<div id="answer-container-74351" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74351-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to do this with OpenStreetMap data,</p>
<ol>
<li>Install your own Nominatim server, loading data for the region of the world you are interested in (<a href="https://github.com/osm-search/Nominatim">https://github.com/osm-search/Nominatim</a> has all you need)</li>
<li>Use the C# HttpClient to access your server's API which is described on <a href="https://nominatim.org/release-docs/develop/api/Overview/">https://nominatim.org/release-docs/develop/api/Overview/</a></li>
<li>The response can either be in XML or in JSON, and can be parsed with appropriate libraries (see <a href="https://stackoverflow.com/questions/6620165/how-can-i-parse-json-with-c">https://stackoverflow.com/questions/6620165/how-can-i-parse-json-with-c</a> )</li>
</ol>
<p>If you only want to make a few requests (instead of making thousands of requests or shipping a software that depends on the server), you can also access the public, donation-funded Nominatim server and skip step 1 above; be sure to adhere to <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> if you do that to avoid the risk of the service being cut off.</p>
<p>Another alternative to step 1 above is buying services from a commercial provider; see <a href="https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services</a> for an inofficial list maintained by the providers themselves.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '20, 21:33</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Apr '20, 21:34</strong> </span></p>
</div>
</div>
<div id="comments-container-74351" class="comments-container">
<span id="74352"></span>
<div id="comment-74352" class="comment">
<div id="post-74352-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hallo Frederik!</p>
<p>Du bist ja aus Karlsruhe, dann spreche ich lieber Deutsch mit Dir! :) Vielen Dank schon mal für die schnelle Antwort. Arbeitest du direkt bei OSM ?</p>
<p>Ich arbeite an einem Anwendungsprogramm in Unity (GameEngine). Dabei benutze ich einen Globus der auf eure Karten läuft. <a href="https://assetstore.unity.com/packages/tools/gui/world-map-globe-edition-2-150643">https://assetstore.unity.com/packages/tools/gui/world-map-globe-edition-2-150643</a> User können eine Kontaktliste erstellen, diese Kontakte möchte ich als Marker auf den Globus zeigen lassen.</p>
<p>Es gibt bei Google ein Webrequest mit der Methode GetGeoDataFromAddress(country,city,street) (oder so ähnlich) Möchte Google aber schon allein aus ideologischen Gründen nicht nutzen.</p>
<p>Du weißt nun was ich vor habe, könntest du mir etwas empfehlen? Das Programm werde ich zwar kostenlos zur Verfügung stellen, wäre aber auch bereit bei euch eine Kommerzielle Lösung anzunehmen.</p>
<p>Grüße Paulo</p>
</div>
<div id="comment-74352-info" class="comment-info">
<span class="comment-age">(23 Apr '20, 22:19)</span> <span class="comment-user userinfo">Hermetes</span>
</div>
</div>
<span id="74353"></span>
<div id="comment-74353" class="comment">
<div id="post-74353-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So ähnlich wie dieser Google-Aufruf funktioniert auch der öffentliche Nominatim-Server. Wenn Du Dein Programm frei zur Verfügung stellst und nicht weisst, wer es wie massiv einsetzt, ist es vielleicht am besten, wenn Du in Deinem Programm grundsätzlich die Nominatim-API implementierst, aber den URL einstellbar machst. Dann können "Klein-Anwender" den spendenfinanzierten OSMF-Nominatim nutzen, und Groß-Anwender sich was eigenes aufsetzen.</p>
</div>
<div id="comment-74353-info" class="comment-info">
<span class="comment-age">(23 Apr '20, 23:36)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74351" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74351-form-container" class="comment-form-container">
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

