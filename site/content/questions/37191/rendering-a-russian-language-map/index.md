+++
type = "question"
title = "Rendering a Russian-language map"
description = '''I would like to render a map of Ukraine and Moldova that uses [name:ru] instead of the local name where ever name:ru is available and, only when it is not available, use the local name instead. Besides that it should look exactly like the default rendering on openstreetmap.org.  Assuming I have prop...'''
date = "2014-10-01T16:35:00Z"
lastmod = "2015-02-18T13:43:00Z"
weight = 37191
keywords = [ "russian", "lang-ru", "name", "localization" ]
aliases = [ "/questions/37191" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering a Russian-language map](/questions/37191/rendering-a-russian-language-map)

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
<span id="post-37191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37191-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to render a map of Ukraine and Moldova that uses [name:ru] instead of the local name where ever name:ru is available and, only when it is not available, use the local name instead. Besides that it should look exactly like the default rendering on openstreetmap.org.</p>
<p>Assuming I have properly installed mapnik and PostgreSQL/PostGIS on my Linux environment and downloaded the map data, how would I proceed?</p>
<p>Can I just import the map data using osm2pgsql or is this not going to work in my case?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-russian" rel="tag" title="see questions tagged &#39;russian&#39;">russian</span> <span class="post-tag tag-link-lang-ru" rel="tag" title="see questions tagged &#39;lang-ru&#39;">lang-ru</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-localization" rel="tag" title="see questions tagged &#39;localization&#39;">localization</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Oct '14, 16:35</strong></p>
<img src="https://secure.gravatar.com/avatar/9b1b4e90f4146bc02ab2da5df7df202d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maturi0n&#39;s gravatar image" />
<p><span>Maturi0n</span><br />
<span class="score" title="44 reputation points">44</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maturi0n has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37191" class="comments-container">
&#10;</div>
<div id="comment-tools-37191" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37191-form-container" class="comment-form-container">
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

<span id="37201"></span>

<div id="answer-container-37201" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37201-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd load it with osm2pgsql, but use a <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/docs/lua.md">lua tag transformation</a> to move whatever's in "name:ru" to "name", if there is a "name:ru".</p>
<p>I've done that, not for names, but for <a href="https://github.com/SomeoneElseOSM/designation-style">certain other map features</a>. Some brief notes are <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1404_tileserver_load">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '14, 17:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-37201" class="comments-container">
&#10;</div>
<div id="comment-tools-37201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37201-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37195"></span>

<div id="answer-container-37195" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37195-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Starting hints should be found in the OSM wiki about <a href="https://wiki.openstreetmap.org/wiki/Map_internationalization">Map_internationalization</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '14, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-37195" class="comments-container">
&#10;</div>
<div id="comment-tools-37195" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37195-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41115"></span>

<div id="answer-container-41115" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41115-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://mlm.jochentopf.com/?lang=ru%2C_&amp;zoom=6&amp;lat=48.32704&amp;lon=27.55371&amp;layers=0BT">Can this final result you want</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '15, 13:43</strong></p>
<img src="https://secure.gravatar.com/avatar/0148de082bc491462382f8ac188442bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="freeExec&#39;s gravatar image" />
<p><span>freeExec</span><br />
<span class="score" title="116 reputation points">116</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="freeExec has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41115" class="comments-container">
&#10;</div>
<div id="comment-tools-41115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41115-form-container" class="comment-form-container">
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

