+++
type = "question"
title = "Maps werden nicht angezeigt, Javacript-Problem"
description = '''Hallo, Ich habe mehrere Karten in meiner Homepage nach dieser Anleitung eingebunden: https://wiki.openstreetmap.org/wiki/DE:Karte_in_Webseite_einbinden Die Karten wurden bis vor Kurzem immer angezeigt, jetzt aber nicht mehr. Offensichtlich gibt es Probleme mit den JavaScripts OpenLayers.js und OpenS...'''
date = "2020-01-22T15:51:00Z"
lastmod = "2020-01-23T09:19:00Z"
weight = 72614
keywords = [ "embed", "javascript", "lang-de" ]
aliases = [ "/questions/72614" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Maps werden nicht angezeigt, Javacript-Problem](/questions/72614/maps-werden-nicht-angezeigt-javacript-problem)

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
<span id="post-72614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72614-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hallo,</p>
<p>Ich habe mehrere Karten in meiner Homepage nach dieser Anleitung eingebunden: <a href="https://wiki.openstreetmap.org/wiki/DE:Karte_in_Webseite_einbinden">https://wiki.openstreetmap.org/wiki/DE:Karte_in_Webseite_einbinden</a></p>
<p>Die Karten wurden bis vor Kurzem immer angezeigt, jetzt aber nicht mehr. Offensichtlich gibt es Probleme mit den JavaScripts OpenLayers.js und OpenStreetMap.js</p>
<p>Laut meinem Provider können unsichere Elemente nicht geladen werden.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-embed" rel="tag" title="see questions tagged &#39;embed&#39;">embed</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-lang-de" rel="tag" title="see questions tagged &#39;lang-de&#39;">lang-de</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '20, 15:51</strong></p>
<img src="https://secure.gravatar.com/avatar/2a82b0fcb5f34e360bcb6f256eb527f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guenter-pilger&#39;s gravatar image" />
<p><span>guenter-pilger</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guenter-pilger has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '20, 20:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-72614" class="comments-container">
&#10;</div>
<div id="comment-tools-72614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72614-form-container" class="comment-form-container">
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

<span id="72617"></span>

<div id="answer-container-72617" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72617-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Klingt danach, als würde Deine Seite inzwischen über HTTPS laufen.</p>
<p>Dann musst Du nur die Angaben bzgl. der JS Dateien von http in https ändern im HTML Beispiel.</p>
<p>D.h.:</p>
<pre><code>&lt;script type=&quot;text/javascript&quot; src=&quot;http://openlayers.org/api/OpenLayers.js&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/javascript&quot; src=&quot;http://www.openstreetmap.org/openlayers/OpenStreetMap.js&quot;&gt;
&lt;/script&gt;</code></pre>
<p>muss geändert werden in:</p>
<pre><code>&lt;script type=&quot;text/javascript&quot; src=&quot;https://openlayers.org/api/OpenLayers.js&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/javascript&quot; src=&quot;https://www.openstreetmap.org/openlayers/OpenStreetMap.js&quot;&gt;
&lt;/script&gt;</code></pre>
<p>Edit: Das Script von openlayers.org bitte ohne www. referenzieren, weil es sonst durch einen doppelten Redirect (<a href="https://www">https://www</a>. -&gt; http: -&gt; https://) bei der Seite von openlayers.org zu einem Security Fehler (mixed active content) kommt, der das Javascript blockiert.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '20, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '20, 23:01</strong> </span></p>
</div>
</div>
<div id="comments-container-72617" class="comments-container">
<span id="72618"></span>
<div id="comment-72618" class="comment">
<div id="post-72618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Vielen Dank! Stimmt, meine Homepage wurde kürzlich auf https umgestellt. Die Javascripts auf src="https://... zu ändern, hatte ich schon ausprobiert, gerade noch mal. Aber leider kein Erfolg.</p>
</div>
<div id="comment-72618-info" class="comment-info">
<span class="comment-age">(22 Jan '20, 17:02)</span> <span class="comment-user userinfo">guenter-pilger</span>
</div>
</div>
<span id="72619"></span>
<div id="comment-72619" class="comment">
<div id="post-72619-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Im OpenStreetMap.js sind die opencyclemap tiles noch über http referenziert. Du könntest einfach die OpenStreetMap.js in Deinen Webhost kopieren und entsprechend referenzieren und in der Datei die http in https ändern.</p>
</div>
<div id="comment-72619-info" class="comment-info">
<span class="comment-age">(22 Jan '20, 17:08)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="72620"></span>
<div id="comment-72620" class="comment">
<div id="post-72620-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Zudem müsstest Du die Tile-URLs auch anpassen, da sie für https nur über thunderforest laufen (einen API-Key wirst Du dort auch brauchen). Wobei das nur gilt, falls Du die Mapstile OpenCycle oder Transport verwendest. Für den OSM Standard Stil sollte es kein Problem machen.</p>
</div>
<div id="comment-72620-info" class="comment-info">
<span class="comment-age">(22 Jan '20, 17:14)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="72622"></span>
<div id="comment-72622" class="comment">
<div id="post-72622-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Vielen Dank!</p>
<p>In der OpenStreetMap.js (in meinem Webspace) habe ich alles auf https gesetzt und das Script in der Karten.htm entsprechend adressiert. Das funktioniert nicht.</p>
<p>Den letzten Absatz habe ich möglicherweise nicht richtig verstanden. API-Key?</p>
<p>Zudem verhindert das Einstellen des Scripts in meinen Webspace eine Aktualisierung dieser Datei.</p>
</div>
<div id="comment-72622-info" class="comment-info">
<span class="comment-age">(22 Jan '20, 19:04)</span> <span class="comment-user userinfo">guenter-pilger</span>
</div>
</div>
<span id="72624"></span>
<div id="comment-72624" class="comment">
<div id="post-72624-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nutzt Du denn den OpenStreetMap Stil oder den Transport oder Cyclemap Stil aus der OpenStreetMap.js?</p>
<p>Am Hilfreichsten wäre einmal ein Link auf die Seite/Unterseite, wo Du die Karte einbindest, dann kann man da schneller den Fehler finden.</p>
</div>
<div id="comment-72624-info" class="comment-info">
<span class="comment-age">(22 Jan '20, 20:15)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="72625"></span>
<div id="comment-72625" class="comment not_top_scorer">
<div id="post-72625-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Deine Frage kann ich mangels Fachwissen nicht beantworten.</p>
<p>Aber hier gerne die aufrufende Seite. Link auf Button "Landkarte" https://www.guenter-pilger.de/Alpspitze.htm</p>
<p>Die Kartenseite (nicht angepasst) <a href="https://www.guenter-pilger.de/OSM/alpspitze.htm">https://www.guenter-pilger.de/OSM/alpspitze.htm</a></p>
<p>Angepasst die Kartenseite: <a href="https://www.guenter-pilger.de/TEST/alpspitze.htm">https://www.guenter-pilger.de/TEST/alpspitze.htm</a></p>
<p>Die Kartenseiten lassen sich natürlich direkt ohne die Hauptseite aufrufen.</p>
</div>
<div id="comment-72625-info" class="comment-info">
<span class="comment-age">(22 Jan '20, 20:33)</span> <span class="comment-user userinfo">guenter-pilger</span>
</div>
</div>
<span id="72627"></span>
<div id="comment-72627" class="comment not_top_scorer">
<div id="post-72627-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/17747/guenter-pilger">@guenter-pilger</a>: Bitte antworte auf Nachfragen mit Hilfe der Kommentarfunktion, nicht als neue Antwort zu deiner Ursprungsfrage.</p>
</div>
<div id="comment-72627-info" class="comment-info">
<span class="comment-age">(22 Jan '20, 20:42)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="72632"></span>
<div id="comment-72632" class="comment not_top_scorer">
<div id="post-72632-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ich habe die Antwort oben editiert.</p>
<p><a href="https://www.openlayers.org">https://www.openlayers.org</a> darf nicht verwendet werden, stattdessen bitte <a href="https://openlayers.org">https://openlayers.org</a> verwenden.</p>
<p>Da ist bei openlayers.org leider ein suboptimaler Redirect drin.</p>
<p>Allgemein sollte man sowieso am Besten die openlayers.js selbst hosten. (Oder notfalls die bei openlayers.org angegebene cdn URL von jsdelivr.net).</p>
</div>
<div id="comment-72632-info" class="comment-info">
<span class="comment-age">(22 Jan '20, 23:00)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="72634"></span>
<div id="comment-72634" class="comment not_top_scorer">
<div id="post-72634-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Vielen Dank, das funktioniert jetzt so! Nur die Textfelder scheinen mir jetzt viel größer geworden zu sein als vorher oder täusche ich mich da?</p>
</div>
<div id="comment-72634-info" class="comment-info">
<span class="comment-age">(23 Jan '20, 08:34)</span> <span class="comment-user userinfo">guenter-pilger</span>
</div>
</div>
<span id="72635"></span>
<div id="comment-72635" class="comment not_top_scorer">
<div id="post-72635-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In der OSM/tom.js hast Du:</p>
<pre><code>feature.popupClass = OpenLayers.Class(OpenLayers.Popup.FramedCloud, {minSize: new OpenLayers.Size(100,20) } );</code></pre>
<p>In der TEST/tom.js hast Du:</p>
<pre><code>feature.popupClass = OpenLayers.Class(OpenLayers.Popup.FramedCloud, {minSize: new OpenLayers.Size(300,180) } );</code></pre>
<p>D.h.: wenn Du wieder die OSM/tom.js verwendest oder die Zeile in der TEST/tom.js änderst, werden die Textfelder kleiner.</p>
</div>
<div id="comment-72635-info" class="comment-info">
<span class="comment-age">(23 Jan '20, 08:57)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="72637"></span>
<div id="comment-72637" class="comment not_top_scorer">
<div id="post-72637-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In meinem TEST-Ordner war ein falscher Eintrag für die map.css drin. link href="map.css"</p>
<p>Jetzt ist alles in Ordnung. Nochmals vielen Dank für deine Hilfe!</p>
</div>
<div id="comment-72637-info" class="comment-info">
<span class="comment-age">(23 Jan '20, 09:19)</span> <span class="comment-user userinfo">guenter-pilger</span>
</div>
</div>
</div>
<div id="comment-tools-72617" class="comment-tools">
<span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-72617-form-container" class="comment-form-container">
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

