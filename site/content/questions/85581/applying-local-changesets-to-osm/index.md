+++
type = "question"
title = "Applying local changesets to OSM"
description = '''Context: I have a local version of the openstreetmap-website on a server for routing purposes. Every ~30min I go through a process of generating a changeset with osmosis, applying that changeset to an osm file, and updating the data for the router.  Question: What I&#x27;d like to do is automatically app...'''
date = "2022-09-07T18:48:00Z"
lastmod = "2022-09-09T19:43:00Z"
weight = 85581
keywords = [ "openstreetmap", "changeset", "osm", "routing", "osmosis" ]
aliases = [ "/questions/85581" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Applying local changesets to OSM](/questions/85581/applying-local-changesets-to-osm)

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
<span id="post-85581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85581-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Context:</strong> I have a local version of the openstreetmap-website on a server for routing purposes. Every ~30min I go through a process of generating a changeset with osmosis, applying that changeset to an osm file, and updating the data for the router.</p>
<p><strong>Question:</strong> What I'd like to do is automatically apply changes made on the server to the public version of OSM as well, is this possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Sep '22, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/1a5c982dc8825ee7594f38a8876576b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeorgeValleyeats&#39;s gravatar image" />
<p><span>GeorgeValley...</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeorgeValleyeats has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Sep '22, 18:50</strong> </span></p>
</div>
</div>
<div id="comments-container-85581" class="comments-container">
&#10;</div>
<div id="comment-tools-85581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85581-form-container" class="comment-form-container">
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

<span id="85589"></span>

<div id="answer-container-85589" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85589-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-85589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GeorgeValleyeats has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Technically the problem is that both object ids and versions will have diverged between your data and OSM proper and will be out of sync.</p>
<p>There is not really a good way to work around this even if you use the original diff uploads (from the editor you are using) to update your data. There have been attempts to do things along such lines in the "humanitarian" space, but a) these typically have been used in low-density data areas, and b) involve throwing away local data and replacing it with fresh data from osm.org after syncing. See <a href="https://github.com/posm/posm">https://github.com/posm/posm</a></p>
<p>Legally if these are only changes made by you there wouldn't be an issue, if the data is added and changed by multiple legal entities it is highly problematic.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '22, 07:35</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Sep '22, 07:36</strong> </span></p>
</div>
</div>
<div id="comments-container-85589" class="comments-container">
<span id="85590"></span>
<div id="comment-85590" class="comment">
<div id="post-85590-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was afraid that would be the answer, I did come across POSM in my research but I don't believe it will work for my purposes. Thanks for the answer.</p>
</div>
<div id="comment-85590-info" class="comment-info">
<span class="comment-age">(09 Sep '22, 13:28)</span> <span class="comment-user userinfo">GeorgeValley...</span>
</div>
</div>
<span id="85592"></span>
<div id="comment-85592" class="comment">
<div id="post-85592-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there any reason that the edits can't be made to OSM directly?</p>
</div>
<div id="comment-85592-info" class="comment-info">
<span class="comment-age">(09 Sep '22, 15:24)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="85594"></span>
<div id="comment-85594" class="comment">
<div id="post-85594-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The goal was to setup a local version of both OSM and OSRM. Make changes locally which can be easily turned into change files with osmosis from the local postgres database. Nothing would prevent me doing the changes to both local and proper, I just wanted to automate that process. As for why not use data directly from OSM, simply because I could not find a way to automatically get updated data every ~30 min.</p>
</div>
<div id="comment-85594-info" class="comment-info">
<span class="comment-age">(09 Sep '22, 17:15)</span> <span class="comment-user userinfo">GeorgeValley...</span>
</div>
</div>
<span id="85595"></span>
<div id="comment-85595" class="comment">
<div id="post-85595-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That shouldn't really be an issue, though I have to say I've never kept an API database up to date from diffs (only osm2pgsql schema), but I would be slightly amazed if that isn't possible.</p>
</div>
<div id="comment-85595-info" class="comment-info">
<span class="comment-age">(09 Sep '22, 17:39)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="85596"></span>
<div id="comment-85596" class="comment not_top_scorer">
<div id="post-85596-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I really don't care about the database being up to date, what I really want is the osm.pbf file to stay updated and receive changes ASAP. It might be possible to do with osmupdate with the two regions polylines I care about. But I think I tried that and there was some compatibility issue with OSRM but maybe I'm just miss remembering.</p>
</div>
<div id="comment-85596-info" class="comment-info">
<span class="comment-age">(09 Sep '22, 18:11)</span> <span class="comment-user userinfo">GeorgeValley...</span>
</div>
</div>
<span id="85597"></span>
<div id="comment-85597" class="comment">
<div id="post-85597-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Keeping a local planet file up to date is really simple see <a href="https://docs.osmcode.org/pyosmium/latest/tools_uptodate.html">https://docs.osmcode.org/pyosmium/latest/tools_uptodate.html</a></p>
</div>
<div id="comment-85597-info" class="comment-info">
<span class="comment-age">(09 Sep '22, 19:00)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="85598"></span>
<div id="comment-85598" class="comment not_top_scorer">
<div id="post-85598-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for all your input, it's given me a lot of help. I'm pretty sure I know what to do now to get the result I was going for.</p>
</div>
<div id="comment-85598-info" class="comment-info">
<span class="comment-age">(09 Sep '22, 19:43)</span> <span class="comment-user userinfo">GeorgeValley...</span>
</div>
</div>
</div>
<div id="comment-tools-85589" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-85589-form-container" class="comment-form-container">
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

