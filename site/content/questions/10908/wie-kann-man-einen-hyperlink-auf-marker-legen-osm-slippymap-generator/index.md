+++
type = "question"
title = "Wie kann man einen Hyperlink auf Marker legen (OSM SlippyMap Generator)"
description = '''Hallo, Mit dem OSM SlippyMap Generator habe ich eine Karte erstellt und mehrere Marker eingefügt - jeweils:  addMarker(layer_markes, lon,lat ,“&amp;lt;b&amp;gt;Text&amp;lt;/b&amp;gt;&amp;lt; /p&amp;gt;“, false,0);  Wie kann man erreichen, dass beim Anklicken des jeweiligen Markers jeweils eine spezielle html-Seite aufgeruf...'''
date = "2012-03-01T16:45:00Z"
lastmod = "2012-03-21T21:04:00Z"
weight = 10908
keywords = [ "marker", "lang-de", "slippymap", "hyperlink" ]
aliases = [ "/questions/10908" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wie kann man einen Hyperlink auf Marker legen (OSM SlippyMap Generator)](/questions/10908/wie-kann-man-einen-hyperlink-auf-marker-legen-osm-slippymap-generator)

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
<span id="post-10908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10908-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hallo, Mit dem OSM SlippyMap Generator habe ich eine Karte erstellt und mehrere Marker eingefügt - jeweils:<br />
</p>
<pre><code>addMarker(layer_markes, lon,lat ,“&lt;b&gt;Text&lt;/b&gt;&lt; /p&gt;“, false,0);</code></pre>
<p>Wie kann man erreichen, dass beim Anklicken des jeweiligen Markers jeweils eine spezielle html-Seite aufgerufen wird? Danke</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-lang-de" rel="tag" title="see questions tagged &#39;lang-de&#39;">lang-de</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span> <span class="post-tag tag-link-hyperlink" rel="tag" title="see questions tagged &#39;hyperlink&#39;">hyperlink</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Mar '12, 16:45</strong></p>
<img src="https://secure.gravatar.com/avatar/65f0a2466c00020807fedac43a91bfdc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoeJohn&#39;s gravatar image" />
<p><span>JoeJohn</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoeJohn has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '13, 03:08</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-10908" class="comments-container">
&#10;</div>
<div id="comment-tools-10908" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10908-form-container" class="comment-form-container">
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

<span id="11400"></span>

<div id="answer-container-11400" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11400-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Du kannst einen HTML-Link in die Markerbeschreibung einfügen:</p>
<pre><code>&lt;a href=&quot;http://example.com/&quot;&gt;Link-Beschreibung&lt;/a&gt;</code></pre>
<p>Der Link wird dann im Popup angezeigt, der erscheint, wenn man auf den Marker klickt.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Mar '12, 21:04</strong></p>
<img src="https://secure.gravatar.com/avatar/97f754e0356a74acc666550948b48bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hfs&#39;s gravatar image" />
<p><span>hfs</span><br />
<span class="score" title="851 reputation points">851</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hfs has 3 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-11400" class="comments-container">
&#10;</div>
<div id="comment-tools-11400" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11400-form-container" class="comment-form-container">
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

