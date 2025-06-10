+++
type = "question"
title = "Umap: Namen eines Markers als Link verwenden"
description = '''Hallo, ich bin noch recht neu in der Nutzung von OSM und Umap. Ich habe jetzt in Umap eine Karte angelegt, in der ich in Hamburg aller Radio und FS-Sender darstellen möchte. Im Grundsatz funktioniert die, d.h. wenn ich auf den Marker clicke, öffnet sich ein Seitenfenster in dem ein Bild und der Link...'''
date = "2021-10-19T09:43:00Z"
lastmod = "2021-10-19T16:30:00Z"
weight = 82239
keywords = [ "umap", "hyperlink", "description", "lang-de" ]
aliases = [ "/questions/82239" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Umap: Namen eines Markers als Link verwenden](/questions/82239/umap-namen-eines-markers-als-link-verwenden)

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
<span id="post-82239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82239-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hallo, ich bin noch recht neu in der Nutzung von OSM und Umap. Ich habe jetzt in Umap eine Karte angelegt, in der ich in Hamburg aller Radio und FS-Sender darstellen möchte. Im Grundsatz funktioniert die, d.h. wenn ich auf den Marker clicke, öffnet sich ein Seitenfenster in dem ein Bild und der Link enthalten ist. Ich habe bei anderen Karten gesehen, dass der Beschreibung selber ein Link hinterlegt ist. D.h. sobald ich auf die Beschriftung "NDR-Hörfunk" clicke, soll sich die Webseite "https://www.ndr.de/radio/" öffnen.</p>
<p>Ich habe schon alles mögliche ausprobiert, habe jetzt aber aber keine Idee mehr, wie ich das hinbekomme. Hat jemand aus der Runde bitte einen Tipp für mich? <a href="https://umap.openstreetmap.de/de/map/radio-und-tv-in-hamburg_18724#13/53.5729/9.9702">link text</a> Danke und liebe Grüße Dieter</p>
<p>Liebe Grüße Dieter</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-hyperlink" rel="tag" title="see questions tagged &#39;hyperlink&#39;">hyperlink</span> <span class="post-tag tag-link-description" rel="tag" title="see questions tagged &#39;description&#39;">description</span> <span class="post-tag tag-link-lang-de" rel="tag" title="see questions tagged &#39;lang-de&#39;">lang-de</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Oct '21, 09:43</strong></p>
<img src="https://secure.gravatar.com/avatar/c89072d2d778e882a9afe39b9418019e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ostfriese-Wedel&#39;s gravatar image" />
<p><span>Ostfriese-Wedel</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ostfriese-Wedel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Oct '21, 16:31</strong> </span></p>
</div>
</div>
<div id="comments-container-82239" class="comments-container">
&#10;</div>
<div id="comment-tools-82239" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82239-form-container" class="comment-form-container">
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

<span id="82247"></span>

<div id="answer-container-82247" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82247-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Tatsächlich funktioniert es, einen Link in den Namen zu setzen. Ich habe es gerade für NDR Fernsehen gemacht. Im Pop-Up siehst du, dass der Name mit einem Link hinterlegt ist. Leider wird das Markup nicht im Label ausgewertet sondern roh angezeigt. Das willst du wohl so nicht.</p>
<p>Man kann allerdings Polygonen einen Link hinterlegen. Ich habe einen Kreis angelegt und mit einem Link hinterlegt. Dafür gib es ein eigenes Feld in Interaktionsoptionen.</p>
<p>Vielleicht kannst du die Seite so gestalten, dass du statt Punktmarkern Formen (z. B. Kreise, Dreiecke oder in Form eines Hauses) verwendest.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '21, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Oct '21, 13:32</strong> </span></p>
</div>
</div>
<div id="comments-container-82247" class="comments-container">
<span id="82251"></span>
<div id="comment-82251" class="comment">
<div id="post-82251-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hallo TZom,</p>
<p>Danke für den Tipp! Das ist für meine Zwecke eine gute Lösung!</p>
</div>
<div id="comment-82251-info" class="comment-info">
<span class="comment-age">(19 Oct '21, 16:30)</span> <span class="comment-user userinfo">Ostfriese-Wedel</span>
</div>
</div>
</div>
<div id="comment-tools-82247" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82247-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82240"></span>

<div id="answer-container-82240" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82240-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Beim Bearbeiten ist beim Textfeld der Marker-Beschreibung ein kleines Fragezeichen. Wenn du dieses anklickst, dann öffnet sich ein Popup mit Hinweisen für spezielle Textformatierungen:</p>
<pre><code>    *Ein Stern für Kursiv*
    **Zwei Sterne für Fett**
    # Eine Raute für große Überschrift
    ## Zwei Rauten für mittlere Überschrift
    ### Drei Rauten für kleine Überschrift
    Einfacher Link: [[http://beispiel.com]]
    Link mit Text: [[http://beispiel.com|Text für den Link]]
    Bild: {{http://bild.url.com}}
    Bild mit benutzerdefinierter Breite (in Pixel): {{http://bild.url.com|Breite}}
    Iframe: {{{http://iframe.url.com}}}
    Iframe mit benutzerdefinierter Höhe (in Pixel): {{{http://iframe.url.com|Höhe}}}
    Iframe mit benutzerdefinierter Höhe und Breite (in Pixel): {{{http://iframe.url.com|Höhe*Breite}}}
    --- Für eine horizontale Linie</code></pre>
<p>Wenn ich deine Frage richtig verstanden habe, dann möchtest du dort einen "Link mit Text" einfügen, also beispielsweise:</p>
<pre><code>[[https://www.ndr.de/radio/|NDR-Hörfunk]]</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '21, 10:07</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Oct '21, 10:08</strong> </span></p>
</div>
</div>
<div id="comments-container-82240" class="comments-container">
<span id="82243"></span>
<div id="comment-82243" class="comment">
<div id="post-82243-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hallo Scai,</p>
<p>ja, für die Beschreibung funktioniert das auch. Ich sehe gerade dass ich mich nicht richtig ausgedrückt habe:</p>
<p>Ich möchte dem Namen (im Feld oberhalb der Beschreibung) einen Link hinterlegen. Das bekomme ich nicht hin.</p>
</div>
<div id="comment-82243-info" class="comment-info">
<span class="comment-age">(19 Oct '21, 10:21)</span> <span class="comment-user userinfo">Ostfriese-Wedel</span>
</div>
</div>
<span id="82244"></span>
<div id="comment-82244" class="comment">
<div id="post-82244-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, verstehe. Ob das möglich ist weiß ich leider nicht. Dort ist auch kein Hinweis auf diese Textformatierungen.</p>
</div>
<div id="comment-82244-info" class="comment-info">
<span class="comment-age">(19 Oct '21, 10:26)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82240" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82240-form-container" class="comment-form-container">
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

