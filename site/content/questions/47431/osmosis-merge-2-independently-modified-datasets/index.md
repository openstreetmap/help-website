+++
type = "question"
title = "Osmosis merge 2 independently modified datasets"
description = '''Hi everyone, I want to use OSM data as a basis for some routing calculations (i want to test something new with special constraints so using existing routing algorithms isn&#x27;t an option). During the calculations I want to add some information into the OSM database (mainly in forms of new relations) t...'''
date = "2016-01-09T13:42:00Z"
lastmod = "2018-07-03T15:53:00Z"
weight = 47431
keywords = [ "diff", "osmosis" ]
aliases = [ "/questions/47431" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis merge 2 independently modified datasets](/questions/47431/osmosis-merge-2-independently-modified-datasets)

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
<span id="post-47431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47431-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>I want to use OSM data as a basis for some routing calculations (i want to test something new with special constraints so using existing routing algorithms isn't an option). During the calculations I want to add some information into the OSM database (mainly in forms of new relations) that my routing algorithm came up with. For this purpose I want to setup a local OSM server (rail ports with postgres database).</p>
<p>As it's a rather long term project i want to update my OSM database from time to time using diffs. At this point I need some help.</p>
<p>Is it possible to apply diffs to a local dataset that was locally changed after importing? I think the issue would be that I have originally two seperate datasets (local and public OSM) that initially are the same (when populating the local database at first) but after that will be modified independently from each other. Is it possible to incorporate changes from the public OSM database into my private OSM data? If yes, what's the best way to do so?</p>
<p>I hope I was able to explain my problem and look foreward to your suggestions.</p>
<p>Thanks a lot!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '16, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/022e1a1d9fe4fec63cbee7340c66fceb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fr0ggynator&#39;s gravatar image" />
<p><span>Fr0ggynator</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fr0ggynator has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47431" class="comments-container">
<span id="47432"></span>
<div id="comment-47432" class="comment">
<div id="post-47432-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Knowing how big approximately is the test area going to be would help.</p>
</div>
<div id="comment-47432-info" class="comment-info">
<span class="comment-age">(09 Jan '16, 21:17)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="47434"></span>
<div id="comment-47434" class="comment">
<div id="post-47434-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For now it's not going to be bigger than southern Germany. The OSM file has roughly 1.3 GB</p>
</div>
<div id="comment-47434-info" class="comment-info">
<span class="comment-age">(09 Jan '16, 22:16)</span> <span class="comment-user userinfo">Fr0ggynator</span>
</div>
</div>
<span id="64502"></span>
<div id="comment-64502" class="comment">
<div id="post-64502-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi! Is there any best practice for this problem? I am having a similar problem now.</p>
</div>
<div id="comment-64502-info" class="comment-info">
<span class="comment-age">(03 Jul '18, 10:30)</span> <span class="comment-user userinfo">Hanson</span>
</div>
</div>
<span id="64505"></span>
<div id="comment-64505" class="comment">
<div id="post-64505-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15335/hanson">@Hanson</a> is your problem "how to merge 2 independently modified datasets with Osmosis" or "how to update a database that has been modified"?</p>
<p>If the former, then <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh">this</a> might be a helpful example to follow - that splits a large .osm.pbf, processes various sections separately and then combines the results.</p>
</div>
<div id="comment-64505-info" class="comment-info">
<span class="comment-age">(03 Jul '18, 13:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="64506"></span>
<div id="comment-64506" class="comment">
<div id="post-64506-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi SomeoneElse. My problem is how to keep a local modified database in sync with osm database.</p>
</div>
<div id="comment-64506-info" class="comment-info">
<span class="comment-age">(03 Jul '18, 15:00)</span> <span class="comment-user userinfo">Hanson</span>
</div>
</div>
<span id="64509"></span>
<div id="comment-64509" class="comment not_top_scorer">
<div id="post-64509-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15335/hanson">@Hanson</a> could you please create a new question, the original one was rather specific.</p>
</div>
<div id="comment-64509-info" class="comment-info">
<span class="comment-age">(03 Jul '18, 15:53)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47431" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-47431-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

