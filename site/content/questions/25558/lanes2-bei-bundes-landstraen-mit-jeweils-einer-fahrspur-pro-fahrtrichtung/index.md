+++
type = "question"
title = "lanes=2 bei Bundes-/Landstraßen mit jeweils einer Fahrspur pro Fahrtrichtung ?"
description = '''Hallo, ich bin über ITO-Map auf folgende Eintragungen aufmerksam geworden: http://www.itoworld.com/map/179?lon=9.56667&amp;amp;lat=48.15533&amp;amp;zoom=13&amp;amp;fullscreen=true Hier ist die B312 teilweise mit lanes=2 eingetragen, teilweise ohne &quot;lanes&quot;. lanes=2 bedeutet doch 2 Fahrspuren pro Fahrtrichtung, o...'''
date = "2013-08-18T18:38:00Z"
lastmod = "2013-08-19T13:56:00Z"
weight = 25558
keywords = [ "lanes", "highway", "lang-de" ]
aliases = [ "/questions/25558" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [lanes=2 bei Bundes-/Landstraßen mit jeweils einer Fahrspur pro Fahrtrichtung ?](/questions/25558/lanes2-bei-bundes-landstraen-mit-jeweils-einer-fahrspur-pro-fahrtrichtung)

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
<span id="post-25558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25558-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hallo, ich bin über ITO-Map auf folgende Eintragungen aufmerksam geworden: <a href="http://www.itoworld.com/map/179?lon=9.56667&amp;lat=48.15533&amp;zoom=13&amp;fullscreen=true">http://www.itoworld.com/map/179?lon=9.56667&amp;lat=48.15533&amp;zoom=13&amp;fullscreen=true</a> Hier ist die B312 teilweise mit lanes=2 eingetragen, teilweise ohne "lanes". lanes=2 bedeutet doch 2 Fahrspuren pro Fahrtrichtung, oder ? Ist bei Bundes-/Lanstraßen mit nur einer Fahrspur pro Fahrtrichtung "lanes=*" erforderlich ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-lang-de" rel="tag" title="see questions tagged &#39;lang-de&#39;">lang-de</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '13, 18:38</strong></p>
<img src="https://secure.gravatar.com/avatar/070282c59f23d8268813b03dbc535b27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cb650cx&#39;s gravatar image" />
<p><span>cb650cx</span><br />
<span class="score" title="184 reputation points">184</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cb650cx has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25558" class="comments-container">
&#10;</div>
<div id="comment-tools-25558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25558-form-container" class="comment-form-container">
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

<span id="25559"></span>

<div id="answer-container-25559" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25559-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-25559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><span>DE:Key:lanes</span> schreibt: "Der Tag lanes wird zur Angabe der <em>Gesamtanzahl</em> der Fahrstreifen verwendet […]" (Hervorhebung von mir) Wenn eine Straße aber mit geteilten Wegen dargestellt wird, dann gilt das lanes-Tag auch nur für den jeweiligen Weg (also nur für die entsprechende Richtung).</p>
<p>Ob das Tag erforderlich ist? Nein, aber sinnvoll, denn es gibt ja unterschiedliche Anzahlen von Fahrspuren. Wenn lanes nicht bei einer Straße gesetzt ist, dann muss der Datenverwender raten. Einen Standardwert gibt es hier nicht, denke ich (außer vielleicht bei highway=track - da werden die meisten in Deutschland wohl einspurig sein und daher die Annahme sinnvoll und lanes eher nicht nötig). Wie du bei <a href="http://taginfo.openstreetmap.org/keys/?key=lanes">http://taginfo.openstreetmap.org/keys/?key=lanes</a> siehst, gibt es auch durchaus viele Tags mit dem Wert "1".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '13, 18:52</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Aug '13, 19:28</strong> </span></p>
</div>
</div>
<div id="comments-container-25559" class="comments-container">
<span id="25564"></span>
<div id="comment-25564" class="comment">
<div id="post-25564-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Und als Ergänzung: Da lanes die Gesamtzahl der Spuren angibt, erlaubt es nicht immer einen direkten Rückschluss auf die Spuren pro Fahrtrichtung. Daher kann man diese Information bei Bedarf mit lanes:forward=... und lanes:backward=... ergänzen.</p>
</div>
<div id="comment-25564-info" class="comment-info">
<span class="comment-age">(19 Aug '13, 13:56)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-25559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25559-form-container" class="comment-form-container">
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

