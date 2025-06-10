+++
type = "question"
title = "See only ways edited by both of two users"
description = '''For reasons unknown, a person has changed a load of tracks, bridleways, and cycleways that I previously edited to footways. I doubt that they singled me out - the relevant edits are generally localised around a particular area. Assuming that they either need assistance or don&#x27;t respond to my queries...'''
date = "2017-10-24T20:29:00Z"
lastmod = "2017-12-04T19:12:00Z"
weight = 60287
keywords = [ "revert" ]
aliases = [ "/questions/60287" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [See only ways edited by both of two users](/questions/60287/see-only-ways-edited-by-both-of-two-users)

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
<span id="post-60287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60287-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For reasons unknown, a person has changed a load of tracks, bridleways, and cycleways that I previously edited to footways. I doubt that they singled me out - the relevant edits are generally localised around a particular area.</p>
<p>Assuming that they either need assistance or don't respond to my queries, I'd like an easy way to identify only the subset of ways that I previously edited and which that person has also edited. I suppose I'll then manually edit them, since all that has changed is the highway type.</p>
<p>My alternative is to go through their change history, open each of their changesets, open all footways which have version 2 or above, then check through the change history for each to see if it was one of mine. The number of changesets isn't huge at the moment.</p>
<p>If it makes any difference, I'm still using Potlatch 2.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '17, 20:29</strong></p>
<img src="https://secure.gravatar.com/avatar/cf4d0ea359df782ea8261afa0ad88d1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jpennycook&#39;s gravatar image" />
<p><span>jpennycook</span><br />
<span class="score" title="71 reputation points">71</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jpennycook has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60287" class="comments-container">
<span id="61009"></span>
<div id="comment-61009" class="comment">
<div id="post-61009-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately the person who made the "mistake" originally has repeated the "mistake". I will request a reversion of their edit.</p>
</div>
<div id="comment-61009-info" class="comment-info">
<span class="comment-age">(04 Dec '17, 19:12)</span> <span class="comment-user userinfo">jpennycook</span>
</div>
</div>
</div>
<div id="comment-tools-60287" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60287-form-container" class="comment-form-container">
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

<span id="60289"></span>

<div id="answer-container-60289" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60289-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could use a query like "<code>highway=* and user:maxerickson</code>" in the <a href="http://overpass-turbo.eu/">Overpass Turbo</a> Wizard to visualize the ways they have changed in an area. There's no way to get it to look back a version, but it might be an improvement over going through the changesets.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '17, 23:24</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '17, 23:25</strong> </span></p>
</div>
</div>
<div id="comments-container-60289" class="comments-container">
<span id="60303"></span>
<div id="comment-60303" class="comment">
<div id="post-60303-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks maxerickson. I got that working fairly easily.</p>
</div>
<div id="comment-60303-info" class="comment-info">
<span class="comment-age">(26 Oct '17, 09:03)</span> <span class="comment-user userinfo">jpennycook</span>
</div>
</div>
</div>
<div id="comment-tools-60289" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60289-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60291"></span>

<div id="answer-container-60291" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60291-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you're willing in to dig a little bit more, and if you have programming abilities in more or less any language, you could do this:</p>
<ul>
<li>download the .osh.pbf ("history") file for the are of interest from download.geofabrik.de</li>
<li>(optionally) use the osmium command line utility (github.com/osmcode/osmium-tool or use ready-made Debian/Ubuntu packages) to further reduce the area</li>
<li>convert the file to "opl" format, again using the osmium command line utility (osmium cat myfile.osh.pbf -f opl)</li>
</ul>
<p>The "opl" format is easily parseable; it is an ASCII text file with all versions of every object, using exactly one line for each version. You can process that file with a little code written in the programming language of your choice - for your particular use case, you could even use the command line "grep" utility to find all lines that contain either your or their user name, and then use further text-based Unix utilities like sort and/or comm to determine which object IDs have been touched by both of you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '17, 07:12</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-60291" class="comments-container">
<span id="60304"></span>
<div id="comment-60304" class="comment">
<div id="post-60304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik.</p>
<p>I'm concerned that I might make a mistake and break large parts of the area concerned! I think I'll do this change by hand, and then try your method another time on a small area.</p>
<p>Jon</p>
</div>
<div id="comment-60304-info" class="comment-info">
<span class="comment-age">(26 Oct '17, 09:15)</span> <span class="comment-user userinfo">jpennycook</span>
</div>
</div>
</div>
<div id="comment-tools-60291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60291-form-container" class="comment-form-container">
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

