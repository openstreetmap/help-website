+++
type = "question"
title = "Bahn- und Buslinien einzeichnen"
description = '''Hallo! Kann mir jemand sagen, wie ich Bahn- und Buslinien für die OSM ÖPNV-Karte einzeichnen kann, wie ich die Farbe festlege und die Nummer eintragen kann? Ich finde dazu nichts im Menü... Danke! trilex'''
date = "2020-01-06T09:23:00Z"
lastmod = "2020-01-06T10:26:00Z"
weight = 72380
keywords = [ "buslinien", "public-transport", "bahnlinien", "lang-de" ]
aliases = [ "/questions/72380" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bahn- und Buslinien einzeichnen](/questions/72380/bahn-und-buslinien-einzeichnen)

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
<span id="post-72380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72380-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hallo! Kann mir jemand sagen, wie ich Bahn- und Buslinien für die OSM ÖPNV-Karte einzeichnen kann, wie ich die Farbe festlege und die Nummer eintragen kann? Ich finde dazu nichts im Menü... Danke! trilex</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buslinien" rel="tag" title="see questions tagged &#39;buslinien&#39;">buslinien</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-bahnlinien" rel="tag" title="see questions tagged &#39;bahnlinien&#39;">bahnlinien</span> <span class="post-tag tag-link-lang-de" rel="tag" title="see questions tagged &#39;lang-de&#39;">lang-de</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jan '20, 09:23</strong></p>
<img src="https://secure.gravatar.com/avatar/9f0dd5c8815912606633417fbde9ddcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trilex&#39;s gravatar image" />
<p><span>trilex</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trilex has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jan '20, 10:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-72380" class="comments-container">
&#10;</div>
<div id="comment-tools-72380" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72380-form-container" class="comment-form-container">
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

<span id="72381"></span>

<div id="answer-container-72381" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72381-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hallo Trilex,</p>
<p>lies dich am besten im Wiki in das Thema ein:<br />
<a href="https://wiki.openstreetmap.org/wiki/DE:Public_transport">Publich Transport</a><br />
<a href="https://wiki.openstreetmap.org/wiki/DE:Relation:route">Routen-Relation</a></p>
<p>Im Prinzip mappt man zunächst die Haltestelle. Nachdem momentan gültigen Schema ("public transport version 2") markiert man dazu den Ort, wo der Bus hält, als <code>public_transport=stop_position</code> auf dem highway=* und die Stelle, wo die Fahrgäste ein- und aussteigen, als <code>public_transport=platform</code>. Dann fügt man die stops, platforms und Wege einer Richtung in eine Relation ein, die die Linie definiert. Mehrere Richtungen und Alternativwege werden noch in eine Masterroute gepackt. Wie das alles genau geht, ist in den oben verlinkten Seiten beschrieben. Schau dir auch beispielhaft gerne eine existierende Linie an, <a href="https://www.openstreetmap.org/relation/4049168">die ich kürzlich gemappt habe</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '20, 10:26</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span> </br></br></p>
</div>
</div>
<div id="comments-container-72381" class="comments-container">
&#10;</div>
<div id="comment-tools-72381" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72381-form-container" class="comment-form-container">
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

