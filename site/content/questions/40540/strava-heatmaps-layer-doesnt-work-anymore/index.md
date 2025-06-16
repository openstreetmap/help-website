+++
type = "question"
title = "Strava Heatmaps layer doesn&#x27;t work anymore"
description = '''Hi all, I tried to activate the Strava layer just now in iD without success. I tried to use the url provided in this link https://wiki.openstreetmap.org/wiki/Strava without success. No problems whatsoever in the past. Any ideas what&#x27;s wrong there? Thanks René'''
date = "2015-01-22T21:05:00Z"
lastmod = "2015-01-22T22:00:00Z"
weight = 40540
keywords = [ "layer", "strava", "heatmap" ]
aliases = [ "/questions/40540" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Strava Heatmaps layer doesn't work anymore](/questions/40540/strava-heatmaps-layer-doesnt-work-anymore)

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
<span id="post-40540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40540-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I tried to activate the Strava layer just now in iD without success. I tried to use the url provided in this link <a href="https://wiki.openstreetmap.org/wiki/Strava">https://wiki.openstreetmap.org/wiki/Strava</a> without success. No problems whatsoever in the past. Any ideas what's wrong there?</p>
<p>Thanks René</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-strava" rel="tag" title="see questions tagged &#39;strava&#39;">strava</span> <span class="post-tag tag-link-heatmap" rel="tag" title="see questions tagged &#39;heatmap&#39;">heatmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '15, 21:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a6e2839b04b99e35e45d64fe66b9a500?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rene78&#39;s gravatar image" />
<p><span>rene78</span><br />
<span class="score" title="700 reputation points">700</span><span title="29 badges"><span class="badge1">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rene78 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40540" class="comments-container">
<span id="40543"></span>
<div id="comment-40543" class="comment">
<div id="post-40543-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>just to confirm: I had configured their heatmap layer in JOSM, it stopped working too (since some days - maybe a week already).</p>
</div>
<div id="comment-40543-info" class="comment-info">
<span class="comment-age">(22 Jan '15, 21:42)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40540" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40540-form-container" class="comment-form-container">
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

<span id="40545"></span>

<div id="answer-container-40545" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40545-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-40545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rene78 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For JOSM (at least the cycling heat layer) the URL was fixed <a href="https://josm.openstreetmap.de/wiki/Maps?sfp_email=&amp;sfph_mail=&amp;action=diff&amp;version=349&amp;old_version=348&amp;sfp_email=&amp;sfph_mail=">23h ago</a>. It seems strava simply changed servers (the second time). If you would use JOSM: update your imagery list in the settings, maybe you need to re-activate those entries afterwards.</p>
<p>Apparently the strava software engineer Paul Mach <a href="https://josm.openstreetmap.de/wiki/Maps?sfp_email=&amp;sfph_mail=&amp;action=diff&amp;version=346&amp;old_version=345&amp;sfp_email=&amp;sfph_mail=">changed</a> the servers in our josm config before. So I guess it is fine that we also use the new servers. But I will ask to be sure.</p>
<p>Now, <a href="https://josm.openstreetmap.de/wiki/Maps?sfp_email=&amp;sfph_mail=&amp;action=diff&amp;version=350&amp;old_version=349&amp;sfp_email=&amp;sfph_mail=">I have changed the running tiles for JOSM too</a>. And updated <span>our wiki page</span>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '15, 22:00</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '15, 22:34</strong> </span></p>
</div>
</div>
<div id="comments-container-40545" class="comments-container">
&#10;</div>
<div id="comment-tools-40545" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40545-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40542"></span>

<div id="answer-container-40542" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40542-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd contact Strava, not OSM. My recollection was that a lot of what Strava were doing were "labs projects" - essentially finding out what worked well and what didn't. They may have moved, or they may be looking to do things in a different way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '15, 21:10</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-40542" class="comments-container">
<span id="40544"></span>
<div id="comment-40544" class="comment">
<div id="post-40544-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I am asking the mapper who asked for permission originally, if he knows more info or can ask again (via twitter).</p>
</div>
<div id="comment-40544-info" class="comment-info">
<span class="comment-age">(22 Jan '15, 21:55)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40542" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40542-form-container" class="comment-form-container">
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

