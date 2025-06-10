+++
type = "question"
title = "Automatic Notification of new data by a specific tag"
description = '''I am working on a long-term project to compile accurate global administrative boundaries in an openly licensed format. I have found OSM boundaries to be particularly useful for this, however, I know that not all administrative boundaries are mapped/tagged on OSM so far. I am trying to figure out a w...'''
date = "2018-03-13T18:41:00Z"
lastmod = "2018-03-15T04:10:00Z"
weight = 62660
keywords = [ "boundaries", "notification" ]
aliases = [ "/questions/62660" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Automatic Notification of new data by a specific tag](/questions/62660/automatic-notification-of-new-data-by-a-specific-tag)

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
<span id="post-62660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62660-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am working on a long-term project to compile accurate global administrative boundaries in an openly licensed format. I have found OSM boundaries to be particularly useful for this, however, I know that not all administrative boundaries are mapped/tagged on OSM so far. I am trying to figure out a way to set up automatic or semi-automatic notification when new features are added and tagged "boundary=administrative", anywhere in the world. I haven't found a tool that notifies by tags yet, only by geographic area or changeset. Does anyone have any advice on a tool that does this or how I could set one up myself? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-notification" rel="tag" title="see questions tagged &#39;notification&#39;">notification</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Mar '18, 18:41</strong></p>
<img src="https://secure.gravatar.com/avatar/c9cd1780b199c901f35c5760d249a5c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lnseitz&#39;s gravatar image" />
<p><span>lnseitz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lnseitz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62660" class="comments-container">
&#10;</div>
<div id="comment-tools-62660" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62660-form-container" class="comment-form-container">
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

<span id="62680"></span>

<div id="answer-container-62680" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62680-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One of the tools that can be used to update a rendering database contains <a href="https://github.com/openstreetmap/mod_tile/blob/master/openstreetmap-tiles-update-expire">this script</a> that creates a file containing OpenStreetMap changes since it was last run. You could use that to detect when new boundaries are <em>added</em> (which is what you asked) but not easily when existing boundaries are <em>deleted</em> (which you didn't, but possibly also want).</p>
<p>Another option would be to setup a local instance of something like <a href="https://github.com/ethan-nelson/osm_hall_monitor">this</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '18, 18:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-62680" class="comments-container">
<span id="62683"></span>
<div id="comment-62683" class="comment">
<div id="post-62683-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>user wambacher runs a service that detects deleted and "critically shrinked" boundary (example <a href="https://twitter.com/wambacher1/status/973857487140130816">tweet</a>) as part of his <a href="https://wambachers-osm.website/index.php/projekte/internationale-administrative-grenzen">website</a> dedicated to boundaries.</p>
</div>
<div id="comment-62683-info" class="comment-info">
<span class="comment-age">(15 Mar '18, 04:10)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-62680" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62680-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62679"></span>

<div id="answer-container-62679" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62679-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could occasionally run overpass queries such as i.e. <a href="https://overpass-turbo.eu/s/x0X">https://overpass-turbo.eu/s/x0X</a> (which will find all administrative boundaries in Denmark), save a list of the relations found and compare results between one query and the next. Internationally you'll probably want to query ways too as well as avoid having nodes returned in the results.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '18, 16:42</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-62679" class="comments-container">
&#10;</div>
<div id="comment-tools-62679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62679-form-container" class="comment-form-container">
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

