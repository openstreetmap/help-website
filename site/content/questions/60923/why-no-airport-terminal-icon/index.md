+++
type = "question"
title = "Why no airport terminal icon?"
description = '''Why is there no icon for terminals mapped as &quot;aeroway terminal&quot;? This seems to be an important item and the lack of an icon keeps my navigation program from searching the terminal.'''
date = "2017-12-01T20:13:00Z"
lastmod = "2017-12-02T20:52:00Z"
weight = 60923
keywords = [ "feature-request", "icon" ]
aliases = [ "/questions/60923" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why no airport terminal icon?](/questions/60923/why-no-airport-terminal-icon)

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
<span id="post-60923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60923-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Why is there no icon for terminals mapped as "aeroway terminal"? This seems to be an important item and the lack of an icon keeps my navigation program from searching the terminal.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-feature-request" rel="tag" title="see questions tagged &#39;feature-request&#39;">feature-request</span> <span class="post-tag tag-link-icon" rel="tag" title="see questions tagged &#39;icon&#39;">icon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '17, 20:13</strong></p>
<img src="https://secure.gravatar.com/avatar/9871c5f363085817f166ed05a34c45be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdSS&#39;s gravatar image" />
<p><span>EdSS</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdSS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60923" class="comments-container">
<span id="60924"></span>
<div id="comment-60924" class="comment">
<div id="post-60924-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not sure what you mean by "the lack of an icon keeps my navigation program from searching the terminal" - can you give an example of an airport which shows the problem, and how you'd change the data to fix it?</p>
</div>
<div id="comment-60924-info" class="comment-info">
<span class="comment-age">(01 Dec '17, 20:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60927"></span>
<div id="comment-60927" class="comment">
<div id="post-60927-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Albany International Airport in NY shows the problem. "Albany International Airport Main Concourse" across from "Garage" is correctly mapped as "aeroway terminal" but has no icon. The data seems perfect but the lack of the icon is the problem.</p>
<p>An interesting side question is the search "Albany International Airport,NY" shows the parking areas but not the terminal despite both being mapped "operator Albany International Airport" identically.</p>
</div>
<div id="comment-60927-info" class="comment-info">
<span class="comment-age">(01 Dec '17, 21:08)</span> <span class="comment-user userinfo">EdSS</span>
</div>
</div>
</div>
<div id="comment-tools-60923" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60923-form-container" class="comment-form-container">
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

<span id="60928"></span>

<div id="answer-container-60928" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60928-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK, for completeness this is <a href="http://www.openstreetmap.org/way/97882735">here</a> which appears to be mapped as the <a href="https://wiki.openstreetmap.org/wiki/Tag:aeroway=terminal">wiki</a> suggests.</p>
<p>The lack of an icon isn't what's stopping a search at OpenStreetMap.org from returning the terminal in the list, though. The thing that handles the search is <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a>. As <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Bugs_.2F_Error_reporting">mentioned</a>, you can log bugs etc. at the <a href="https://github.com/openstreetmap/Nominatim/issues">issue tracker for it</a> (but search first to see if the problem hasn't already been raised).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '17, 21:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-60928" class="comments-container">
<span id="60968"></span>
<div id="comment-60968" class="comment">
<div id="post-60968-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I notice that there is an icon in the iD editor. Could this icon be also used on the main map?</p>
</div>
<div id="comment-60968-info" class="comment-info">
<span class="comment-age">(02 Dec '17, 19:34)</span> <span class="comment-user userinfo">EdSS</span>
</div>
</div>
<span id="60969"></span>
<div id="comment-60969" class="comment">
<div id="post-60969-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It could (the issue tracker for the "standard style", also known as "OSM Carto", is at <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/">https://github.com/gravitystorm/openstreetmap-carto/issues/</a> ), but it wouldn't affect search in any way.</p>
</div>
<div id="comment-60969-info" class="comment-info">
<span class="comment-age">(02 Dec '17, 20:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-60928" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60928-form-container" class="comment-form-container">
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

